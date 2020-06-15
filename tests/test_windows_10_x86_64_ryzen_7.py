

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 16
	is_windows = True
	arch_string_raw = 'AMD64'
	uname_string_raw = 'AMD64 Family 23 Model 8 Stepping 2, AuthenticAMD'
	can_cpuid = True

	@staticmethod
	def winreg_processor_brand():
		return 'AMD Ryzen 7 2700X Eight-Core Processor         '

	@staticmethod
	def winreg_vendor_id_raw():
		return 'AuthenticAMD'

	@staticmethod
	def winreg_arch_string_raw():
		return 'AMD64'

	@staticmethod
	def winreg_hz_actual():
		return 3693

	@staticmethod
	def winreg_feature_bits():
		return 1010515455




class TestWindows_10_X86_64_Ryzen7(unittest.TestCase):
	def setUp(self):
		cpuinfo.CAN_CALL_CPUID_IN_SUBPROCESS = False
		helpers.backup_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

		helpers.backup_cpuid(cpuinfo)
		helpers.monkey_patch_cpuid(cpuinfo, 3693000000, [
			# get_max_extension_support
			0x8000001f,
			# get_cache
			0x2006140,
			# get_info
			0x800f82,
			# get_processor_brand
			0x20444d41, 0x657a7952, 0x2037206e,
			0x30303732, 0x69452058, 0x2d746867,
			0x65726f43, 0x6f725020, 0x73736563,
			0x2020726f, 0x20202020, 0x202020,
			# get_vendor_id
			0x68747541, 0x444d4163, 0x69746e65,
			# get_flags
			0x178bfbff, 0x7ed8320b, 0x209c01a9,
			0x0, 0x20000000, 0x35c233ff,
		])

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)
		helpers.restore_cpuid(cpuinfo)
		cpuinfo.CAN_CALL_CPUID_IN_SUBPROCESS = True

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
		self.assertEqual(11, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(3, len(cpuinfo._get_cpu_info_from_platform_uname()))
		self.assertEqual(20, len(cpuinfo._get_cpu_info_internal()))


	def test_get_cpu_info_from_cpuid(self):
		info = cpuinfo._get_cpu_info_from_cpuid()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		#self.assertEqual('3.6930 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6930 GHz', info['hz_actual_friendly'])
		#self.assertEqual((3693000000, 0), info['hz_advertised'])
		self.assertEqual((3693000000, 0), info['hz_actual'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])

		self.assertEqual(64 * 1024, info['l2_cache_size'])
		self.assertEqual(512, info['l2_cache_line_size'])
		self.assertEqual(6, info['l2_cache_associativity'])

		self.assertEqual(
			['3dnowprefetch', 'abm', 'adx', 'aes', 'apic', 'avx', 'avx2',
			'bmi1', 'bmi2', 'clflush', 'clflushopt', 'cmov', 'cmp_legacy',
			'cr8_legacy', 'cx16', 'cx8', 'dbx', 'de', 'extapic', 'f16c',
			'fma', 'fpu', 'fxsr', 'ht', 'lahf_lm', 'lm', 'mca', 'mce',
			'misalignsse', 'mmx', 'monitor', 'movbe', 'msr', 'mtrr', 'osvw',
			'osxsave', 'pae', 'pat', 'pci_l2i', 'pclmulqdq', 'perfctr_core',
			'perfctr_nb', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'rdrnd',
			'rdseed', 'sep', 'sha', 'skinit', 'smap', 'smep', 'sse', 'sse2',
			'sse4_1', 'sse4_2', 'sse4a', 'ssse3', 'svm', 'tce', 'topoext',
			'tsc', 'vme', 'wdt', 'xsave']
			,
			info['flags']
		)

	def test_get_cpu_info_from_platform_uname(self):
		info = cpuinfo._get_cpu_info_from_platform_uname()

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])

	def test_get_cpu_info_from_registry(self):
		info = cpuinfo._get_cpu_info_from_registry()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('3.6930 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6930 GHz', info['hz_actual_friendly'])
		self.assertEqual((3693000000, 0), info['hz_advertised'])
		self.assertEqual((3693000000, 0), info['hz_actual'])

		self.assertEqual(
			['3dnow', 'clflush', 'cmov', 'de', 'dts', 'fxsr', 'ia64', 'mca',
			'mmx', 'msr', 'mtrr', 'pse', 'sep', 'sepamd', 'serial', 'ss',
			'sse', 'sse2', 'tm', 'tsc']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('3.6930 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6930 GHz', info['hz_actual_friendly'])
		self.assertEqual((3693000000, 0), info['hz_advertised'])
		self.assertEqual((3693000000, 0), info['hz_actual'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(16, info['count'])

		self.assertEqual('AMD64', info['arch_string_raw'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])

		self.assertEqual(64 * 1024, info['l2_cache_size'])
		self.assertEqual(6, info['l2_cache_associativity'])
		self.assertEqual(512, info['l2_cache_line_size'])

		self.assertEqual(
			['3dnow', '3dnowprefetch', 'abm', 'adx', 'aes', 'apic', 'avx',
			'avx2', 'bmi1', 'bmi2', 'clflush', 'clflushopt', 'cmov',
			'cmp_legacy', 'cr8_legacy', 'cx16', 'cx8', 'dbx', 'de', 'dts',
			'extapic', 'f16c', 'fma', 'fpu', 'fxsr', 'ht', 'ia64', 'lahf_lm',
			'lm', 'mca', 'mce', 'misalignsse', 'mmx', 'monitor', 'movbe',
			'msr', 'mtrr', 'osvw', 'osxsave', 'pae', 'pat', 'pci_l2i',
			'pclmulqdq', 'perfctr_core', 'perfctr_nb', 'pge', 'pni',
			'popcnt', 'pse', 'pse36', 'rdrnd', 'rdseed', 'sep', 'sepamd',
			'serial', 'sha', 'skinit', 'smap', 'smep', 'ss', 'sse', 'sse2',
			'sse4_1', 'sse4_2', 'sse4a', 'ssse3', 'svm', 'tce', 'tm',
			'topoext', 'tsc', 'vme', 'wdt', 'xsave']
			,
			info['flags']
		)
