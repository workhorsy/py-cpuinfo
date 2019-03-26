

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 16
	is_windows = True
	raw_arch_string = 'AMD64'
	can_cpuid = False

	@staticmethod
	def winreg_processor_brand():
		return 'AMD Ryzen 7 2700X Eight-Core Processor         '

	@staticmethod
	def winreg_vendor_id():
		return 'AuthenticAMD'

	@staticmethod
	def winreg_raw_arch_string():
		return 'AMD64'

	@staticmethod
	def winreg_hz_actual():
		return 3693

	@staticmethod
	def winreg_feature_bits():
		return 1010515455




class TestWindows_10_X86_64_Ryzen7(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	'''
	Make sure calls return the expected number of fields.
	'''
	def test_returns(self):
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_wmic()));
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
		self.assertEqual(13, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_registry(self):
		info = cpuinfo._get_cpu_info_from_registry()

		self.assertEqual('AuthenticAMD', info['vendor_id'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor         ', info['brand'])
		#FIXME self.assertEqual('1.9000 GHz', info['hz_advertised'])
		self.assertEqual('3.6930 GHz', info['hz_actual'])
		#FIXME self.assertEqual((1900000000, 0), info['hz_advertised_raw'])
		self.assertEqual((3693000000, 0), info['hz_actual_raw'])

		if "logger" in dir(unittest): unittest.logger("FIXME: Missing flags such as sse3 and sse4")

		self.assertEqual(
			['3dnow', 'clflush', 'cmov', 'de', 'dts', 'fxsr', 'ia64', 'mca',
			'mmx', 'msr', 'mtrr', 'pse', 'sep', 'sepamd', 'serial', 'ss',
			'sse', 'sse2', 'tm', 'tsc']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('AuthenticAMD', info['vendor_id'])
		#FIXME self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor         ', info['brand'])
		#FIXME self.assertEqual('1.9000 GHz', info['hz_advertised'])
		self.assertEqual('3.6930 GHz', info['hz_actual'])
		#FIXME self.assertEqual((1900000000, 0), info['hz_advertised_raw'])
		self.assertEqual((3693000000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(16, info['count'])

		self.assertEqual('AMD64', info['raw_arch_string'])

		#FIXME self.assertEqual(1, info['stepping'])
		#FIXME self.assertEqual(69, info['model'])
		#FIXME self.assertEqual(6, info['family'])

		#FIXME self.assertEqual('512 KB', info['l2_cache_size'])
		#FIXME self.assertEqual('3072 KB', info['l3_cache_size'])

		if "logger" in dir(unittest): unittest.logger("FIXME: Missing flags such as sse3 and sse4")

		self.assertEqual(
			['3dnow', 'clflush', 'cmov', 'de', 'dts', 'fxsr', 'ia64', 'mca', 'mmx', 'msr',
			'mtrr', 'pse', 'sep', 'sepamd', 'serial', 'ss', 'sse', 'sse2', 'tm', 'tsc']
			,
			info['flags']
		)
