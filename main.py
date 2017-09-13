
print("!!!!!!!!!! main.py")
# main.py
# Put everything in a main guard or it may execute twice when the process forks
if __name__ == '__main__':
	import multiprocessing
	import cpuinfo

	# Call freeze_support or Pyinstaller will recursively fork infinite processes forever
	multiprocessing.freeze_support()
	print("!!! called multiprocessing.freeze_support()")
	print(cpuinfo.get_cpu_info())
