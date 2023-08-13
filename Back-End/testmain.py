import Test
import time
import sys
import tensorflow as tf
import os as os


def time_stamp():
    temp = r"%Y-%m-%d %H:%M:%S"
    tmp = f"{time.strftime(temp, time.localtime(time.time()))}: [{os.path.basename(__file__)}]:"
    return tmp

def version_all():
    print(f"{time_stamp()}Python 버전 {sys.version_info}")
    print(f"{time_stamp()}Test.file 은 {Test.__file__}")
    print(f"{time_stamp()}Tensorflow 버전 {tf.__version__}")


version_all()