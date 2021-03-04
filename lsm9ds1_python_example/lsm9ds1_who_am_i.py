import lsm9ds1_python
import time
import sys

lsm9ds1 = lsm9ds1_python.lsm9ds1()

try:

	while True:
		print("hello_world")
		time.sleep(0.5)
except KeyboardInterrupt:
	sys.exit()
