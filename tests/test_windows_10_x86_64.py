

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 4
	is_windows = True
	raw_arch_string = 'AMD64'
	can_cpuid = False

	@staticmethod
	def winreg_processor_brand():
		return 'Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz'

	@staticmethod
	def winreg_vendor_id():
		return 'GenuineIntel'

	@staticmethod
	def winreg_raw_arch_string():
		return 'AMD64'

	@staticmethod
	def winreg_hz_actual():
		return 2494

	@staticmethod
	def winreg_feature_bits():
		return 1025196031




class TestWindows_10_X86_64(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	'''
	Make sure calls return the expected number of fields.
	'''
	def test_returns(self):
		self.assertEqual(7, len(cpuinfo._get_cpu_info_from_registry()))
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
		self.assertEqual(12, len(cpuinfo.get_cpu_info()))

	def test_get_cpu_info_from_registry(self):
		info = cpuinfo._get_cpu_info_from_registry()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz', info['brand'])
		self.assertEqual('1.9000 GHz', info['hz_advertised'])
		self.assertEqual('2.4940 GHz', info['hz_actual'])
		self.assertEqual((1900000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2494000000, 0), info['hz_actual_raw'])

		if "logger" in dir(unittest): unittest.logger("FIXME: Missing flags such as sse3 and sse4")

		self.assertEqual(
			['3dnow', 'acpi', 'clflush', 'cmov', 'de', 'dts', 'fxsr',
			'ia64', 'mca', 'mce', 'mmx', 'msr', 'mtrr', 'pse', 'sep',
			'serial', 'ss', 'sse', 'sse2', 'tm', 'tsc']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo.get_cpu_info()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz', info['brand'])
		self.assertEqual('1.9000 GHz', info['hz_advertised'])
		self.assertEqual('2.4940 GHz', info['hz_actual'])
		self.assertEqual((1900000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2494000000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])

		self.assertEqual('AMD64', info['raw_arch_string'])

		if "logger" in dir(unittest): unittest.logger("FIXME: Missing flags such as sse3 and sse4")

		self.assertEqual(
			['3dnow', 'acpi', 'clflush', 'cmov', 'de', 'dts', 'fxsr',
			'ia64', 'mca', 'mce', 'mmx', 'msr', 'mtrr', 'pse', 'sep',
			'serial', 'ss', 'sse', 'sse2', 'tm', 'tsc']
			,
			info['flags']
		)
