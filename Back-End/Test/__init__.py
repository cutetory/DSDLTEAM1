import sys
import time
temp = r"%Y-%m-%d %H:%M:%S"
print(f"{time.strftime(temp, time.localtime(time.time()))}: [Back-End/Test/__init__.py]")
print(f"Test패키지 기본 sys.pah: {sys.path}")