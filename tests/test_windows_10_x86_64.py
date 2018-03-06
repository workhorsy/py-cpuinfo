

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
	def has_wmic():
		return True

	@staticmethod
	def wmic_cpu():
		returncode = 0
		output = '''
Caption=Intel64 Family 6 Model 69 Stepping 1
CurrentClockSpeed=2494
Description=Intel64 Family 6 Model 69 Stepping 1
L2CacheSize=512
L3CacheSize=3072
Manufacturer=GenuineIntel
Name=Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz

'''
		return returncode, output

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
		self.assertEqual(11, len(cpuinfo._get_cpu_info_from_wmic()));
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
		self.assertEqual(18, len(cpuinfo.get_cpu_info()))

	def test_get_cpu_info_from_wmic(self):
		info = cpuinfo._get_cpu_info_from_wmic()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz', info['brand'])
		self.assertEqual('1.9000 GHz', info['hz_advertised'])
		self.assertEqual('2.4940 GHz', info['hz_actual'])
		self.assertEqual((1900000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2494000000, 0), info['hz_actual_raw'])

		self.assertEqual(1, info['stepping'])
		self.assertEqual(69, info['model'])
		self.assertEqual(6, info['family'])

		self.assertEqual('512 KB', info['l2_cache_size'])
		self.assertEqual('3072 KB', info['l3_cache_size'])

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

		self.assertEqual(1, info['stepping'])
		self.assertEqual(69, info['model'])
		self.assertEqual(6, info['family'])

		self.assertEqual('512 KB', info['l2_cache_size'])
		self.assertEqual('3072 KB', info['l3_cache_size'])

		if "logger" in dir(unittest): unittest.logger("FIXME: Missing flags such as sse3 and sse4")

		self.assertEqual(
			['3dnow', 'acpi', 'clflush', 'cmov', 'de', 'dts', 'fxsr',
			'ia64', 'mca', 'mce', 'mmx', 'msr', 'mtrr', 'pse', 'sep',
			'serial', 'ss', 'sse', 'sse2', 'tm', 'tsc']
			,
			info['flags']
		)
