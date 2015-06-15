

from cpuinfo import cpuinfo


class DataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	raw_arch_string = 'x86_64'

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def cat_proc_cpuinfo():
		return 1, None

	@staticmethod
	def cpufreq_info():
		return 1, None

	@staticmethod
	def sestatus_allow_execheap():
		return False

	@staticmethod
	def sestatus_allow_execmem():
		return False

	@staticmethod
	def dmesg_a_grep_cpu():
		return 1, None

	@staticmethod
	def dmesg_a_grep_origin():
		return 1, None

	@staticmethod
	def dmesg_a_grep_features():
		return 1, None

	@staticmethod
	def sysctl_machdep_cpu_hw_cpufrequency():
		return 1, None

	@staticmethod
	def isainfo_vb():
		return 1, None

	@staticmethod
	def kstat_m_cpu_info():
		return 1, None

cpuinfo.DataSource = DataSource


print(cpuinfo.get_cpu_info())

