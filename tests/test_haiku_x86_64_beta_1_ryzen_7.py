

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '32bit'
	cpu_count = 2
	is_windows = False
	arch_string_raw = 'BePC'
	uname_string_raw = 'x86_32'
	can_cpuid = False

	@staticmethod
	def has_sysinfo():
		return True

	@staticmethod
	def sysinfo_cpu():
		returncode = 0
		output = '''
2 AMD Ryzen 7, revision 800f82 running at 3693MHz

CPU #0: "AMD Ryzen 7 2700X Eight-Core Processor         "
	Signature: 0x800f82; Type 0, family 23, model 8, stepping 2
	Features: 0x178bfbff
		FPU VME DE PSE TSC MSR PAE MCE CX8 APIC SEP MTRR PGE MCA CMOV PAT
		PSE36 CFLUSH MMX FXSTR SSE SSE2 HTT
	Extended Features (0x00000001): 0x56d82203
		SSE3 PCLMULDQ SSSE3 CX16 SSE4.1 SSE4.2 MOVEB POPCNT AES XSAVE AVX RDRND
	Extended Features (0x80000001): 0x2bd3fb7f
		SCE NX AMD-MMX FXSR FFXSR RDTSCP 64
	Extended Features (0x80000007): 0x00000100
		ITSC
	Extended Features (0x80000008): 0x00000000

	Inst TLB: 2M/4M-byte pages, 64 entries, fully associative
	Data TLB: 2M/4M-byte pages, 64 entries, fully associative
	Inst TLB: 4K-byte pages, 64 entries, fully associative
	Data TLB: 4K-byte pages, 64 entries, fully associative
	L1 inst cache: 32 KB, 8-way set associative, 1 lines/tag, 64 bytes/line
	L1 data cache: 64 KB, 4-way set associative, 1 lines/tag, 64 bytes/line
	L2 cache: 512 KB, 8-way set associative, 1 lines/tag, 64 bytes/line

'''
		return returncode, output




class TestHaiku_x86_64_Beta_1_Ryzen7(unittest.TestCase):
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

		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('3.6930 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6930 GHz', info['hz_actual_friendly'])
		self.assertEqual((3693000000, 0), info['hz_advertised'])
		self.assertEqual((3693000000, 0), info['hz_actual'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])
		self.assertEqual(
			['64', 'aes', 'amd-mmx', 'apic', 'avx', 'cflush', 'cmov', 'cx16',
			'cx8', 'de', 'ffxsr', 'fpu', 'fxsr', 'fxstr', 'htt', 'mca', 'mce',
			'mmx', 'moveb', 'msr', 'mtrr', 'nx', 'pae', 'pat', 'pclmuldq',
			'pge', 'popcnt', 'pse', 'pse36', 'rdrnd', 'rdtscp', 'sce', 'sep',
			'sse', 'sse2', 'sse3', 'sse4.1', 'sse4.2', 'ssse3', 'tsc', 'vme',
			'xsave']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('3.6930 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6930 GHz', info['hz_actual_friendly'])
		self.assertEqual((3693000000, 0), info['hz_advertised'])
		self.assertEqual((3693000000, 0), info['hz_actual'])
		self.assertEqual('X86_32', info['arch'])
		self.assertEqual(32, info['bits'])
		self.assertEqual(2, info['count'])

		self.assertEqual('BePC', info['arch_string_raw'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])
		self.assertEqual(
			['64', 'aes', 'amd-mmx', 'apic', 'avx', 'cflush', 'cmov', 'cx16',
			'cx8', 'de', 'ffxsr', 'fpu', 'fxsr', 'fxstr', 'htt', 'mca', 'mce',
			'mmx', 'moveb', 'msr', 'mtrr', 'nx', 'pae', 'pat', 'pclmuldq',
			'pge', 'popcnt', 'pse', 'pse36', 'rdrnd', 'rdtscp', 'sce', 'sep',
			'sse', 'sse2', 'sse3', 'sse4.1', 'sse4.2', 'ssse3', 'tsc', 'vme',
			'xsave']
			,
			info['flags']
		)
