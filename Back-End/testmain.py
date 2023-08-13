import Test
import time
temp = r"%Y-%m-%d %H:%M:%S"
print(f"{time.strftime(temp, time.localtime(time.time()))}:Test.file 은 {Test.__file__}")