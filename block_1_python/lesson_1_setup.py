import sys
import platform

def show_environment_info():
    print(f"Версия Python: {platform.python_version()}")
    print(f"Платформа: {platform.system()} {platform.release()}")
    print(f"Путь к интерпретатору: {sys.executable}")

if __name__ == "__main__":
    show_environment_info()