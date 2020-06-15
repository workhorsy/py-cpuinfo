

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 4
	is_windows = True
	arch_string_raw = 'AMD64'
	uname_string_raw = 'Intel64 Family 6 Model 69 Stepping 1, GenuineIntel'
	can_cpuid = True

	@staticmethod
	def has_wmic():
		return True

	@staticmethod
	def wmic_cpu():
		returncode = 0
		output = r'''
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
	def winreg_vendor_id_raw():
		return 'GenuineIntel'

	@staticmethod
	def winreg_arch_string_raw():
		return 'AMD64'

	@staticmethod
	def winreg_hz_actual():
		return 2494

	@staticmethod
	def winreg_feature_bits():
		return 1025196031




class TestWindows_10_X86_64(unittest.TestCase):
	def setUp(self):
		cpuinfo.CAN_CALL_CPUID_IN_SUBPROCESS = False
		helpers.backup_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

		helpers.backup_cpuid(cpuinfo)
		helpers.monkey_patch_cpuid(cpuinfo, 2494000000, [
			# max_extension_support
			0x80000008,
			# get_cache
			0x1006040,
			# get_info
			0x40651,
			# get_processor_brand
			0x65746e49, 0x2952286c, 0x726f4320,
			0x4d542865, 0x35692029, 0x3033342d,
			0x43205530, 0x40205550, 0x392e3120,
			0x7a484730, 0x0, 0x0,
			# get_vendor_id
			0x756e6547, 0x6c65746e, 0x49656e69,
			# get_flags
			0xbfebfbff, 0x7ffafbff, 0x27ab,
			0x0, 0x0, 0x21,
		])

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)
		helpers.restore_cpuid(cpuinfo)
		cpuinfo.CAN_CALL_CPUID_IN_SUBPROCESS = True

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
		self.assertEqual(13, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(3, len(cpuinfo._get_cpu_info_from_platform_uname()))
		self.assertEqual(21, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_cpuid(self):
		info = cpuinfo._get_cpu_info_from_cpuid()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz', info['brand_raw'])
		#self.assertEqual('2.4940 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.4940 GHz', info['hz_actual_friendly'])
		#self.assertEqual((2494000000, 0), info['hz_advertised'])
		self.assertEqual((2494000000, 0), info['hz_actual'])

		self.assertEqual(1, info['stepping'])
		self.assertEqual(69, info['model'])
		self.assertEqual(6, info['family'])

		self.assertEqual(64 * 1024, info['l2_cache_size'])
		self.assertEqual(256, info['l2_cache_line_size'])
		self.assertEqual(6, info['l2_cache_associativity'])

		self.assertEqual(
			['abm', 'acpi', 'aes', 'apic', 'avx', 'avx2', 'bmi1', 'bmi2',
			'clflush', 'cmov', 'cx16', 'cx8', 'de', 'ds_cpl', 'dtes64',
			'dts', 'erms', 'est', 'f16c', 'fma', 'fpu', 'fxsr', 'ht',
			'invpcid', 'lahf_lm', 'mca', 'mce', 'mmx', 'monitor', 'movbe',
			'msr', 'mtrr', 'osxsave', 'pae', 'pat', 'pbe', 'pcid',
			'pclmulqdq', 'pdcm', 'pge', 'pni', 'popcnt', 'pse', 'pse36',
			'rdrnd', 'sep', 'smep', 'smx', 'ss', 'sse', 'sse2', 'sse4_1',
			'sse4_2', 'ssse3', 'tm', 'tm2', 'tsc', 'tscdeadline', 'vme',
			'vmx', 'x2apic', 'xsave', 'xtpr']
			,
			info['flags']
		)

	def test_get_cpu_info_from_platform_uname(self):
		info = cpuinfo._get_cpu_info_from_platform_uname()

		self.assertEqual(1, info['stepping'])
		self.assertEqual(69, info['model'])
		self.assertEqual(6, info['family'])

	def test_get_cpu_info_from_wmic(self):
		info = cpuinfo._get_cpu_info_from_wmic()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz', info['brand_raw'])
		self.assertEqual('1.9000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.4940 GHz', info['hz_actual_friendly'])
		self.assertEqual((1900000000, 0), info['hz_advertised'])
		self.assertEqual((2494000000, 0), info['hz_actual'])

		self.assertEqual(1, info['stepping'])
		self.assertEqual(69, info['model'])
		self.assertEqual(6, info['family'])

		self.assertEqual(512 * 1024, info['l2_cache_size'])
		self.assertEqual(3072 * 1024, info['l3_cache_size'])

	def test_get_cpu_info_from_registry(self):
		info = cpuinfo._get_cpu_info_from_registry()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz', info['brand_raw'])
		self.assertEqual('1.9000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.4940 GHz', info['hz_actual_friendly'])
		self.assertEqual((1900000000, 0), info['hz_advertised'])
		self.assertEqual((2494000000, 0), info['hz_actual'])

		self.assertEqual(
			['3dnow', 'acpi', 'clflush', 'cmov', 'de', 'dts', 'fxsr',
			'ia64', 'mca', 'mce', 'mmx', 'msr', 'mtrr', 'pse', 'sep',
			'serial', 'ss', 'sse', 'sse2', 'tm', 'tsc']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Core(TM) i5-4300U CPU @ 1.90GHz', info['brand_raw'])
		self.assertEqual('1.9000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.4940 GHz', info['hz_actual_friendly'])
		self.assertEqual((1900000000, 0), info['hz_advertised'])
		self.assertEqual((2494000000, 0), info['hz_actual'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])

		self.assertEqual('AMD64', info['arch_string_raw'])

		self.assertEqual(1, info['stepping'])
		self.assertEqual(69, info['model'])
		self.assertEqual(6, info['family'])

		self.assertEqual(512 * 1024, info['l2_cache_size'])
		self.assertEqual(3072 * 1024, info['l3_cache_size'])
		self.assertEqual(6, info['l2_cache_associativity'])
		self.assertEqual(256, info['l2_cache_line_size'])

		self.assertEqual(
			['3dnow', 'abm', 'acpi', 'aes', 'apic', 'avx', 'avx2', 'bmi1',
			'bmi2', 'clflush', 'cmov', 'cx16', 'cx8', 'de', 'ds_cpl',
			'dtes64', 'dts', 'erms', 'est', 'f16c', 'fma', 'fpu', 'fxsr',
			'ht', 'ia64', 'invpcid', 'lahf_lm', 'mca', 'mce', 'mmx',
			'monitor', 'movbe', 'msr', 'mtrr', 'osxsave', 'pae', 'pat',
			'pbe', 'pcid', 'pclmulqdq', 'pdcm', 'pge', 'pni', 'popcnt',
			'pse', 'pse36', 'rdrnd', 'sep', 'serial', 'smep', 'smx', 'ss',
			'sse', 'sse2', 'sse4_1', 'sse4_2', 'ssse3', 'tm', 'tm2', 'tsc',
			'tscdeadline', 'vme', 'vmx', 'x2apic', 'xsave', 'xtpr']
			,
			info['flags']
		)
