import sys
import time
import os as os


def time_stamp():
    temp = r"%Y-%m-%d %H:%M:%S"
    tmp = f"{time.strftime(temp, time.localtime(time.time()))}: [{os.path.basename(__file__)}]:"
    return tmp

print(f"{time_stamp()}: [Back-End/Test/__init__.py]: {sys.path}")