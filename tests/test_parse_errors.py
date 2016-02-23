

import unittest
import cpuinfo
import helpers


class DataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = True
	raw_arch_string = 'x86_64'

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def has_dmesg():
		return True

	@staticmethod
	def has_cpufreq_info():
		return True

	@staticmethod
	def has_sestatus():
		return True

	@staticmethod
	def has_sysctl():
		return True

	@staticmethod
	def has_isainfo():
		return True

	@staticmethod
	def has_kstat():
		return True

	@staticmethod
	def has_sysinfo():
		return True

	@staticmethod
	def cat_proc_cpuinfo():
		return 0, ""

	@staticmethod
	def cpufreq_info():
		return 0, ""

	@staticmethod
	def sestatus_allow_execheap():
		return True

	@staticmethod
	def sestatus_allow_execmem():
		return True

	@staticmethod
	def dmesg_a():
		return 0, ""

	@staticmethod
	def sysctl_machdep_cpu_hw_cpufrequency():
		return 0, ""

	@staticmethod
	def isainfo_vb():
		return 0, ""

	@staticmethod
	def kstat_m_cpu_info():
		return 0, ""

	@staticmethod
	def sysinfo_cpu():
		return 0, ""

	@staticmethod
	def winreg_processor_brand():
		return None

	@staticmethod
	def winreg_vendor_id():
		return None

	@staticmethod
	def winreg_raw_arch_string():
		return None

	@staticmethod
	def winreg_hz_actual():
		return None

	@staticmethod
	def winreg_feature_bits():
		return None


class TestParseErrors(unittest.TestCase):
	def test_all(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)

		self.assertEqual(None, cpuinfo.get_cpu_info_from_registry())

		self.assertEqual(None, cpuinfo.get_cpu_info_from_proc_cpuinfo())

		self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())

		self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())

		self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())

		self.assertEqual(None, cpuinfo.get_cpu_info_from_sysinfo())

		#self.assertEqual(None, cpuinfo.get_cpu_info_from_cpuid())

		#self.assertEqual(None, cpuinfo.get_cpu_info())
