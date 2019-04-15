

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	arch_string_raw = 'x86_64'
	uname_string_raw = 'x86_64'

	@staticmethod
	def has_proc_cpuinfo():
		return False

	@staticmethod
	def has_dmesg():
		return False

	@staticmethod
	def has_var_run_dmesg_boot():
		return False

	@staticmethod
	def has_cpufreq_info():
		return False

	@staticmethod
	def has_sestatus():
		return False

	@staticmethod
	def has_sysctl():
		return False

	@staticmethod
	def has_isainfo():
		return False

	@staticmethod
	def has_kstat():
		return False

	@staticmethod
	def has_sysinfo():
		return False

	@staticmethod
	def has_lscpu():
		return False

	@staticmethod
	def cat_proc_cpuinfo():
		return 1, None

	@staticmethod
	def cpufreq_info():
		return 1, None

	@staticmethod
	def sestatus_b():
		return 1, None

	@staticmethod
	def dmesg_a():
		return 1, None

	@staticmethod
	def cat_var_run_dmesg_boot():
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

	@staticmethod
	def lscpu():
		return 1, None

	@staticmethod
	def sysinfo_cpu():
		return 1, None

	@staticmethod
	def winreg_processor_brand():
		return None

	@staticmethod
	def winreg_vendor_id_raw():
		return None

	@staticmethod
	def winreg_arch_string_raw():
		return None

	@staticmethod
	def winreg_hz_actual():
		return None

	@staticmethod
	def winreg_feature_bits():
		return None


class TestExample(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	def test_all(self):
		self.assertEqual({}, cpuinfo._get_cpu_info_from_registry())

		self.assertEqual({}, cpuinfo._get_cpu_info_from_proc_cpuinfo())

		self.assertEqual({}, cpuinfo._get_cpu_info_from_sysctl())

		self.assertEqual({}, cpuinfo._get_cpu_info_from_kstat())

		self.assertEqual({}, cpuinfo._get_cpu_info_from_dmesg())

		self.assertEqual({}, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())

		self.assertEqual({}, cpuinfo._get_cpu_info_from_sysinfo())

		#self.assertEqual({}, cpuinfo._get_cpu_info_from_cpuid())

		#self.assertEqual({}, cpuinfo._get_cpu_info_internal())
