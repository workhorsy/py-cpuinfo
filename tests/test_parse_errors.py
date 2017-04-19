

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = True
	raw_arch_string = 'x86_64'
	can_cpuid = False

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def has_dmesg():
		return True

	@staticmethod
	def has_var_run_dmesg_boot():
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
	def cat_var_run_dmesg_boot():
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
		return {}

	@staticmethod
	def winreg_vendor_id():
		return {}

	@staticmethod
	def winreg_raw_arch_string():
		return {}

	@staticmethod
	def winreg_hz_actual():
		return {}

	@staticmethod
	def winreg_feature_bits():
		return {}


class TestParseErrors(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	'''
	Make sure calls return the expected number of fields.
	'''
	def test_returns(self):
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_registry()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpufreq_info()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_lscpu()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))

	def test_all(self):
		self.assertEqual({}, cpuinfo._get_cpu_info_from_registry())

		self.assertEqual({}, cpuinfo._get_cpu_info_from_proc_cpuinfo())

		self.assertEqual({}, cpuinfo._get_cpu_info_from_sysctl())

		self.assertEqual({}, cpuinfo._get_cpu_info_from_kstat())

		self.assertEqual({}, cpuinfo._get_cpu_info_from_dmesg())

		self.assertEqual({}, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())

		self.assertEqual({}, cpuinfo._get_cpu_info_from_sysinfo())

		#self.assertEqual({}, cpuinfo._get_cpu_info_from_cpuid())

		#self.assertEqual({}, cpuinfo.get_cpu_info())
