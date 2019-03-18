
import sys

# Import cpuinfo.py from up one directory
sys.path.append('../cpuinfo')

# NOTE: Pyinstaller may spawn infinite processes if __main__ is not used
if __name__ == '__main__':
	from multiprocessing import freeze_support
	from cpuinfo import get_cpu_info

	# NOTE: Pyinstaller also requires freeze_support
	freeze_support()
	print(get_cpu_info())
