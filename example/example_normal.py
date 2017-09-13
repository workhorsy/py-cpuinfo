
import sys

# Import cpuinfo.py from up one directory
sys.path.append('../cpuinfo')

if __name__ == '__main__':
	from cpuinfo import get_cpu_info

	print(get_cpu_info())
