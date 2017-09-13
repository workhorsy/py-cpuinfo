
import sys

# Import cpuinfo.py from up one directory
sys.path.append('../cpuinfo')

if __name__ == '__main__':
	from multiprocessing import freeze_support
	from cpuinfo import get_cpu_info

	# NOTE: Make sure to call freeze_support or Pyinstaller will break
	freeze_support()
	print(get_cpu_info())
