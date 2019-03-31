

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 8
	is_windows = False
	raw_arch_string = 'i86pc'
	raw_uname_string = 'x86_32'
	can_cpuid = False

	@staticmethod
	def has_isainfo():
		return True

	@staticmethod
	def has_kstat():
		return True

	@staticmethod
	def isainfo_vb():
		returncode = 0
		output = '''
64-bit amd64 applications
	rdseed avx2 rdrand avx xsave pclmulqdq aes movbe sse4.2 sse4.1
	ssse3 amd_lzcnt popcnt amd_sse4a tscp ahf cx16 sse3 sse2 sse fxsr
amd_mmx mmx cmov amd_sysc cx8 tsc fpu

'''
		return returncode, output

	@staticmethod
	def kstat_m_cpu_info():
		returncode = 0
		output = '''
module: cpu_info                        instance: 0
name:   cpu_info0                       class:    misc
	brand                           AMD Ryzen 7 2700X Eight-Core Processor
	cache_id                        0
	chip_id                         0
	clock_MHz                       3693
	clog_id                         0
	core_id                         0
	cpu_type                        i386
	crtime                          22.539390752
	current_clock_Hz                3692643590
	current_cstate                  1
	family                          23
	fpu_type                        i387 compatible
	implementation                  x86 (chipid 0x0 AuthenticAMD 800F82 family 23 model 8 step 2 clock 3693 MHz)
	model                           8
	ncore_per_chip                  8
	ncpu_per_chip                   8
	pg_id                           1
	pkg_core_id                     0
	snaptime                        120.971135132
	socket_type                     Unknown
	state                           on-line
	state_begin                     1553482276
	stepping                        2
	supported_frequencies_Hz        3692643590
	supported_max_cstates           0
vendor_id AuthenticAMD

'''
		return returncode, output



class TestOpenIndiana_5_11_Ryzen_7(unittest.TestCase):
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
		self.assertEqual(10, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(16, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_kstat(self):
		info = cpuinfo._get_cpu_info_from_kstat()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(r) Core(tm) i7 CPU         870  @ 2.93GHz', info['brand'])
		self.assertEqual('2.9310 GHz', info['hz_advertised'])
		self.assertEqual('2.9305 GHz', info['hz_actual'])
		self.assertEqual((2931000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2930505167, 0), info['hz_actual_raw'])

		self.assertEqual(5, info['stepping'])
		self.assertEqual(30, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['ahf', 'amd_sysc', 'cmov', 'cx8', 'fpu', 'fxsr', 'mmx', 'sse', 'sse2', 'sse3', 'ssse3', 'tsc', 'tscp']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(r) Core(tm) i7 CPU         870  @ 2.93GHz', info['brand'])
		self.assertEqual('2.9310 GHz', info['hz_advertised'])
		self.assertEqual('2.9305 GHz', info['hz_actual'])
		self.assertEqual((2931000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2930505167, 0), info['hz_actual_raw'])
		self.assertEqual('X86_32', info['arch'])
		self.assertEqual(32, info['bits'])
		self.assertEqual(4, info['count'])

		self.assertEqual('i86pc', info['raw_arch_string'])

		self.assertEqual(5, info['stepping'])
		self.assertEqual(30, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['ahf', 'amd_sysc', 'cmov', 'cx8', 'fpu', 'fxsr', 'mmx', 'sse', 'sse2', 'sse3', 'ssse3', 'tsc', 'tscp']
			,
			info['flags']
		)
