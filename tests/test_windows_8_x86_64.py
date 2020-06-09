

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 4
	is_windows = True
	arch_string_raw = 'AMD64'
	uname_string_raw = 'AMD64 Family 6 Model 30 Stepping 5, GenuineIntel'
	can_cpuid = True

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
	def winreg_vendor_id_raw():
		return 'GenuineIntel'

	@staticmethod
	def winreg_arch_string_raw():
		return 'AMD64'

	@staticmethod
	def winreg_hz_actual():
		return 2933

	@staticmethod
	def winreg_feature_bits():
		return 756629502




class TestWindows_8_X86_64(unittest.TestCase):
	def setUp(self):
		cpuinfo.CAN_CALL_CPUID_IN_SUBPROCESS = False
		helpers.backup_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

		helpers.backup_cpuid(cpuinfo)
		helpers.monkey_patch_cpuid(cpuinfo, 2930000000, [
			# max_extension_support
			0x80000008,
			# get_cache
			0x1006040,
			# get_info
			0x106e5,
			# get_processor_brand
			0x65746e49, 0x2952286c, 0x726f4320,
			0x4d542865, 0x37692029, 0x55504320,
			0x20202020, 0x20202020, 0x30373820,
			0x20402020, 0x33392e32, 0x7a4847,
			# get_vendor_id
			0x756e6547, 0x6c65746e, 0x49656e69,
			# get_flags
			0xbfebfbff, 0x98e3fd, 0x0,
			0x0, 0x0, 0x1,
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
		self.assertEqual(14, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(3, len(cpuinfo._get_cpu_info_from_platform_uname()))
		self.assertEqual(22, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_cpuid(self):
		info = cpuinfo._get_cpu_info_from_cpuid()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz', info['brand_raw'])
		#self.assertEqual('2.9300 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.9300 GHz', info['hz_actual_friendly'])
		#self.assertEqual((2930000000, 0), info['hz_advertised'])
		self.assertEqual((2930000000, 0), info['hz_actual'])

		self.assertEqual(5, info['stepping'])
		self.assertEqual(14, info['model'])
		self.assertEqual(6, info['family'])
		#self.assertEqual(8, info['extended_family'])

		# FIXME: These cache fields are in the wrong format
		self.assertEqual('64', info['l2_cache_size'])
		self.assertEqual(256, info['l2_cache_line_size'])
		self.assertEqual('0x6', info['l2_cache_associativity'])

		self.assertEqual(
			['acpi', 'apic', 'clflush', 'cmov', 'cx16', 'cx8', 'de', 'ds_cpl',
			'dtes64', 'dts', 'est', 'fpu', 'fxsr', 'ht', 'lahf_lm', 'mca',
			'mce', 'mmx', 'monitor', 'msr', 'mtrr', 'pae', 'pat', 'pbe',
			'pdcm', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'sep', 'smx',
			'ss', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'ssse3', 'tm', 'tm2',
			'tsc', 'vme', 'vmx', 'xtpr']
			,
			info['flags']
		)

	def test_get_cpu_info_from_platform_uname(self):
		info = cpuinfo._get_cpu_info_from_platform_uname()

		self.assertEqual(5, info['stepping'])
		self.assertEqual(30, info['model'])
		self.assertEqual(6, info['family'])

	def test_get_cpu_info_from_wmic(self):
		info = cpuinfo._get_cpu_info_from_wmic()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz', info['brand_raw'])
		self.assertEqual('2.9300 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.9330 GHz', info['hz_actual_friendly'])
		self.assertEqual((2930000000, 0), info['hz_advertised'])
		self.assertEqual((2933000000, 0), info['hz_actual'])

		self.assertEqual(5, info['stepping'])
		self.assertEqual(30, info['model'])
		self.assertEqual(6, info['family'])

		self.assertEqual('256 KB', info['l2_cache_size'])
		self.assertEqual('8192 KB', info['l3_cache_size'])

	def test_get_cpu_info_from_registry(self):
		info = cpuinfo._get_cpu_info_from_registry()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz', info['brand_raw'])
		self.assertEqual('2.9300 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.9330 GHz', info['hz_actual_friendly'])
		self.assertEqual((2930000000, 0), info['hz_advertised'])
		self.assertEqual((2933000000, 0), info['hz_actual'])

		self.assertEqual(
			['acpi', 'clflush', 'cmov', 'de', 'dts', 'fxsr', 'ia64',
			'mce', 'mmx', 'msr', 'mtrr', 'sep', 'serial', 'ss',
			'sse', 'sse2', 'tm', 'tsc']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz', info['brand_raw'])
		self.assertEqual('2.9300 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.9330 GHz', info['hz_actual_friendly'])
		self.assertEqual((2930000000, 0), info['hz_advertised'])
		self.assertEqual((2933000000, 0), info['hz_actual'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])

		self.assertEqual('AMD64', info['arch_string_raw'])

		# FIXME: These cache fields are in the wrong format
		self.assertEqual(5, info['stepping'])
		self.assertEqual(30, info['model'])
		self.assertEqual(6, info['family'])

		self.assertEqual('256 KB', info['l2_cache_size'])
		self.assertEqual('8192 KB', info['l3_cache_size'])

		self.assertEqual(
			['acpi', 'apic', 'clflush', 'cmov', 'cx16', 'cx8', 'de', 'ds_cpl',
			'dtes64', 'dts', 'est', 'fpu', 'fxsr', 'ht', 'ia64', 'lahf_lm',
			'mca', 'mce', 'mmx', 'monitor', 'msr', 'mtrr', 'pae', 'pat',
			'pbe', 'pdcm', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'sep',
			'serial', 'smx', 'ss', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'ssse3',
			'tm', 'tm2', 'tsc', 'vme', 'vmx', 'xtpr']
			,
			info['flags']
		)
