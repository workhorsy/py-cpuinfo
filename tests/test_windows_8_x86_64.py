

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
Caption=Intel64 Family 6 Model 30 Stepping 5
CurrentClockSpeed=2933
Description=Intel64 Family 6 Model 30 Stepping 5
L2CacheSize=256
L3CacheSize=8192
Manufacturer=GenuineIntel
Name=Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz

'''
		return returncode, output

	@staticmethod
	def winreg_processor_brand():
		return 'Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz'

	@staticmethod
	def winreg_vendor_id():
		return 'GenuineIntel'

	@staticmethod
	def winreg_raw_arch_string():
		return 'AMD64'

	@staticmethod
	def winreg_hz_actual():
		return 2933

	@staticmethod
	def winreg_feature_bits():
		return 756629502




class TestWindows_8_X86_64(unittest.TestCase):
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
		self.assertEqual('Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz', info['brand'])
		self.assertEqual('2.9300 GHz', info['hz_advertised'])
		self.assertEqual('2.9330 GHz', info['hz_actual'])
		self.assertEqual((2930000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2933000000, 0), info['hz_actual_raw'])

		self.assertEqual(5, info['stepping'])
		self.assertEqual(30, info['model'])
		self.assertEqual(6, info['family'])

		self.assertEqual('256 KB', info['l2_cache_size'])
		self.assertEqual('8192 KB', info['l3_cache_size'])

	def test_get_cpu_info_from_registry(self):
		info = cpuinfo._get_cpu_info_from_registry()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz', info['brand'])
		self.assertEqual('2.9300 GHz', info['hz_advertised'])
		self.assertEqual('2.9330 GHz', info['hz_actual'])
		self.assertEqual((2930000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2933000000, 0), info['hz_actual_raw'])

		if "logger" in dir(unittest): unittest.logger("FIXME: Missing flags such as sse3 and sse4")

		self.assertEqual(
			['acpi', 'clflush', 'cmov', 'de', 'dts', 'fxsr', 'ia64',
			'mce', 'mmx', 'msr', 'mtrr', 'sep', 'serial', 'ss',
			'sse', 'sse2', 'tm', 'tsc']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo.get_cpu_info()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz', info['brand'])
		self.assertEqual('2.9300 GHz', info['hz_advertised'])
		self.assertEqual('2.9330 GHz', info['hz_actual'])
		self.assertEqual((2930000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2933000000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])

		self.assertEqual('AMD64', info['raw_arch_string'])

		self.assertEqual(5, info['stepping'])
		self.assertEqual(30, info['model'])
		self.assertEqual(6, info['family'])

		self.assertEqual('256 KB', info['l2_cache_size'])
		self.assertEqual('8192 KB', info['l3_cache_size'])

		if "logger" in dir(unittest): unittest.logger("FIXME: Missing flags such as sse3 and sse4")

		self.assertEqual(
			['acpi', 'clflush', 'cmov', 'de', 'dts', 'fxsr', 'ia64',
			'mce', 'mmx', 'msr', 'mtrr', 'sep', 'serial', 'ss',
			'sse', 'sse2', 'tm', 'tsc']
			,
			info['flags']
		)
