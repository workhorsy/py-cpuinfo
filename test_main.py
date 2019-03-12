

if __name__ == '__main__':
	from multiprocessing import freeze_support
	from cpuinfo import get_cpu_info

	freeze_support()
	get_cpu_info()
	print('This should only be printed once per test')
