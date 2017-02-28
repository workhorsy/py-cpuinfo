

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	raw_arch_string = 'amd64'
	can_cpuid = False

	@staticmethod
	def has_dmesg():
		return True

	@staticmethod
	def dmesg_a():
		retcode = 0
		output = '''
 '''
		return retcode, output



class TestFreeBSD_X86_64(unittest.TestCase):
	def setUp(self):
		helpers.restore_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	'''
	Make sure calls that should work return something,
	and calls that should NOT work return None.
	'''
	def test_returns(self):
		info = cpuinfo._get_cpu_info_from_registry()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_sysctl()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_kstat()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_dmesg()
		self.assertIsNotNone(info)

		info = cpuinfo._get_cpu_info_from_sysinfo()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_cpuid()
		self.assertIsNone(info)

	def test_all(self):
		info = cpuinfo._get_cpu_info_from_dmesg()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('', info['hardware'])
		self.assertEqual('Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz', info['brand'])
		self.assertEqual('3.1000 GHz', info['hz_advertised'])
		self.assertEqual('2.9934 GHz', info['hz_actual'])
		self.assertEqual((3100000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2993390000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(1, info['count'])

		self.assertEqual('amd64', info['raw_arch_string'])

		self.assertEqual(0, info['l2_cache_size'])
		self.assertEqual(0, info['l2_cache_line_size'])
		self.assertEqual(0, info['l2_cache_associativity'])

		self.assertEqual(3, info['stepping'])
		self.assertEqual(60, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(0, info['processor_type'])
		self.assertEqual(0, info['extended_model'])
		self.assertEqual(0, info['extended_family'])
		self.assertEqual(
			['apic', 'clflush', 'cmov', 'cx8', 'de', 'fpu', 'fxsr', 'lahf',
			'lm', 'mca', 'mce', 'mmx', 'mon', 'msr', 'mtrr', 'nx', 'pae',
			'pat', 'pge', 'pse', 'pse36', 'rdtscp', 'sep', 'sse', 'sse2',
			'sse3', 'ssse3', 'syscall', 'tsc', 'vme']
			,
			info['flags']
		)
