

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 4
	is_windows = False
	arch_string_raw = 'BePC'
	uname_string_raw = 'x86_64'
	can_cpuid = False

	@staticmethod
	def has_sysinfo():
		return True

	@staticmethod
	def sysinfo_cpu():
		returncode = 0
		output = '''
1 Intel Core i7, revision 106e5 running at 2933MHz

CPU #0: "Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz"
        Signature: 0x0106e5; Type 0, family 6, model 30, stepping 5
        Features: 0x078bfbff
                FPU VME DE PSE TSC MSR PAE MCE CX8 APIC SEP MTRR PGE MCA CMOV PAT
                PSE36 CFLUSH MMX FXSTR SSE SSE2
        Extended Features (0x00000001): 0x00180209
                SSE3 MONITOR SSSE3 SSE4.1 SSE4.2
        Extended Features (0x80000001): 0x28100800
                SCE NX RDTSCP 64

        L2 Data cache fully associative, 1 lines/tag, 64 bytes/line
        L2 cache: 0 KB, 1-way set associative, 0 lines/tag, 63 bytes/line

        L0 Data TLB: 2M/4M-bytes pages, 4-way set associative, 32 entries
        Data TLB: 4k-byte pages, 4-way set associative, 64 entries
        Inst TLB: 2M/4M-bytes pages, fully associative, 7 entries
        L3 cache: 8192 KB, 16-way set associative, 64-bytes/line
        Inst TLB: 4K-bytes pages, 4-way set associative, 128 entries
        64-byte Prefetching
        L1 data cache: 32 KB, 8-way set associative, 64 bytes/line
        L2 cache: 256 KB (MLC), 8-way set associative, 64-bytes/line
        Shared 2nd-level TLB: 4K, 4-way set associative, 512 entries
        Unknown cache descriptor 0x09
'''
		return returncode, output




class TestHaiku_x86_64(unittest.TestCase):
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
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(9, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(16, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_sysinfo(self):
		info = cpuinfo._get_cpu_info_from_sysinfo()

		self.assertEqual('Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz', info['brand_raw'])
		self.assertEqual('2.9330 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.9330 GHz', info['hz_actual_friendly'])
		self.assertEqual((2933000000, 0), info['hz_advertised'])
		self.assertEqual((2933000000, 0), info['hz_actual'])

		self.assertEqual(5, info['stepping'])
		self.assertEqual(30, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['64', 'apic', 'cflush', 'cmov', 'cx8', 'de', 'fpu', 'fxstr',
			'mca', 'mce', 'mmx', 'monitor', 'msr', 'mtrr', 'nx', 'pae',
			'pat', 'pge', 'pse', 'pse36', 'rdtscp', 'sce', 'sep', 'sse',
			'sse2', 'sse3', 'sse4.1', 'sse4.2', 'ssse3', 'tsc', 'vme']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz', info['brand_raw'])
		self.assertEqual('2.9330 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.9330 GHz', info['hz_actual_friendly'])
		self.assertEqual((2933000000, 0), info['hz_advertised'])
		self.assertEqual((2933000000, 0), info['hz_actual'])
		self.assertEqual('X86_32', info['arch'])
		self.assertEqual(32, info['bits'])
		self.assertEqual(4, info['count'])

		self.assertEqual('BePC', info['arch_string_raw'])

		self.assertEqual(5, info['stepping'])
		self.assertEqual(30, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['64', 'apic', 'cflush', 'cmov', 'cx8', 'de', 'fpu', 'fxstr',
			'mca', 'mce', 'mmx', 'monitor', 'msr', 'mtrr', 'nx', 'pae',
			'pat', 'pge', 'pse', 'pse36', 'rdtscp', 'sce', 'sep', 'sse',
			'sse2', 'sse3', 'sse4.1', 'sse4.2', 'ssse3', 'tsc', 'vme']
			,
			info['flags']
		)
