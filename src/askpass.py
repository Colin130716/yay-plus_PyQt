#!/usr/bin/env python3
import os
import sys
import argparse
from getpass import getpass
from cryptography.fernet import Fernet

# 安全配置
KEY_FILE = os.path.expanduser("~/.askpass_key")
PASS_FILE = os.path.expanduser("~/.askpass_encrypted")
FAIL_LOCK_FILE = os.path.expanduser("~/.askpass_fails")
MAX_ATTEMPTS = 3  # 最大允许失败次数

def secure_cleanup():
    """安全擦除凭证文件"""
    print("\n[安全清理] 正在安全擦除敏感数据...")
    files_to_clean = [KEY_FILE, PASS_FILE, FAIL_LOCK_FILE]

    for file_path in files_to_clean:
        if os.path.exists(file_path):
            try:
                # 用随机数据覆盖原文件
                with open(file_path, "wb") as f:
                    f.write(os.urandom(512))
                # 重命名文件增加混淆
                temp_name = f"{file_path}.del.{os.urandom(4).hex()}"
                os.rename(file_path, temp_name)
                # 再次覆盖后删除
                with open(temp_name, "wb") as f:
                    f.write(os.urandom(512))
                os.remove(temp_name)
            except Exception as e:
                print(f"清理失败 {file_path}: {str(e)}", file=sys.stderr)

def check_attempts():
    """检查失败计数器"""
    try:
        if os.path.exists(FAIL_LOCK_FILE):
            with open(FAIL_LOCK_FILE, "r") as f:
                return int(f.read().strip())
        return 0
    except:
        return 0

def record_failure():
    """记录失败尝试"""
    try:
        count = check_attempts() + 1
        with open(FAIL_LOCK_FILE, "w") as f:
            f.write(str(count))

        # 超过阈值触发清理
        if count >= MAX_ATTEMPTS:
            secure_cleanup()
            print("安全警报：凭证已销毁，请重新初始化！")
            sys.exit(99)
    except Exception as e:
        print(f"记录失败: {str(e)}", file=sys.stderr)

def initialize_password():
    """初始化加密存储"""
    if not sys.stdin.isatty():
        print("错误：必须在交互终端初始化", file=sys.stderr)
        return 1

    password = getpass("请输入sudo密码: ")
    confirm = getpass("确认密码: ")

    if password != confirm:
        print("错误：密码不匹配", file=sys.stderr)
        return 1

    try:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        os.chmod(KEY_FILE, 0o600)

        fernet = Fernet(key)
        encrypted = fernet.encrypt(password.encode())

        with open(PASS_FILE, "wb") as f:
            f.write(encrypted)
        os.chmod(PASS_FILE, 0o600)

        print("初始化成功！")
        return 0
    except Exception as e:
        print(f"初始化失败: {e}", file=sys.stderr)
        for f in [KEY_FILE, PASS_FILE]:
            if os.path.exists(f):
                os.remove(f)
        return 1

def get_password():
    # 在get_password()开头添加
    if check_attempts():
        print("安全锁定：超过最大尝试次数")
        sys.exit(99)

    """安全获取密码"""
    if not is_sudo_call():
        print("拒绝非sudo请求", file=sys.stderr)
        return 1

    try:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
        with open(PASS_FILE, "rb") as f:
            encrypted = f.read()

        return Fernet(key).decrypt(encrypted).decode()
    except FileNotFoundError as e:
        print(f"错误：{e.filename} 不存在", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"解密失败: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        record_failure()  # 记录解密失败
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--init", action="store_true", help="初始化密码存储")
    parser.add_argument("--cleanup", action="store_true",
                       help="安全擦除所有凭证数据")

    args, _ = parser.parse_known_args()

    if args.cleanup:
        secure_cleanup()
        print("清理完成，所有凭证数据已安全删除")
        sys.exit(0)

    if args.init:
        sys.exit(initialize_password())
    else:
        try:
            result = get_password()
            # 解密成功时重置计数器
            if os.path.exists(FAIL_LOCK_FILE):
                os.remove(FAIL_LOCK_FILE)

            if isinstance(result, str):
                print(result)
                sys.exit(0)
            sys.exit(result if isinstance(result, int) else 1)
        except:
            sys.exit(1)
