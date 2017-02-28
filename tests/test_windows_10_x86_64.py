

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
		helpers.restore_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	'''
	Make sure calls that should work return something,
	and calls that should NOT work return None.
	'''
	def test_returns(self):
		info = cpuinfo._get_cpu_info_from_registry()
		self.assertIsNotNone(info)

		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_sysctl()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_kstat()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_dmesg()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_sysinfo()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_cpuid()
		self.assertIsNone(info)

	def test_all(self):
		info = cpuinfo._get_cpu_info_from_registry()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('', info['hardware'])
		self.assertEqual('Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz', info['brand'])
		self.assertEqual('1.9000 GHz', info['hz_advertised'])
		self.assertEqual('2.4940 GHz', info['hz_actual'])
		self.assertEqual((1900000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2494000000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])

		self.assertEqual('AMD64', info['raw_arch_string'])

		self.assertEqual(0, info['l2_cache_size']) # FIXME
		self.assertEqual(0, info['l2_cache_line_size'])
		self.assertEqual(0, info['l2_cache_associativity'])

		self.assertEqual(0, info['stepping']) # FIXME
		self.assertEqual(0, info['model']) # FIXME
		self.assertEqual(0, info['family']) # FIXME
		self.assertEqual(0, info['processor_type'])
		self.assertEqual(0, info['extended_model'])
		self.assertEqual(0, info['extended_family'])
		 # FIXME: Missing flags such as sse3 and sse4
		self.assertEqual(
			['3dnow', 'acpi', 'clflush', 'cmov', 'de', 'dts', 'fxsr',
			'ia64', 'mca', 'mce', 'mmx', 'msr', 'mtrr', 'pse', 'sep',
			'serial', 'ss', 'sse', 'sse2', 'tm', 'tsc']
			,
			info['flags']
		)
