

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 8
	is_windows = False
	arch_string_raw = 'amd64'
	uname_string_raw = 'amd64'
	can_cpuid = False

	@staticmethod
	def has_dmesg():
		return True

	@staticmethod
	def dmesg_a():
		retcode = 0
		output = '''Copyright (c) 1992-2018 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
	The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 12.0-CURRENT #26 fa797a5a3(trueos-stable-18.03): Mon Mar 26 00:24:47 UTC 2018
    root@chimera:/usr/obj/usr/src/amd64.amd64/sys/GENERIC amd64
FreeBSD clang version 6.0.0 (branches/release_60 324090) (based on LLVM 6.0.0)
VT(vga): text 80x25
CPU: AMD Ryzen 7 2700X Eight-Core Processor          (3693.15-MHz K8-class CPU)
  Origin="AuthenticAMD"  Id=0x800f82  Family=0x17  Model=0x8  Stepping=2
  Features=0x1783fbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,MMX,FXSR,SSE,SSE2,HTT>
  Features2=0x5ed82203<SSE3,PCLMULQDQ,SSSE3,CX16,SSE4.1,SSE4.2,MOVBE,POPCNT,AESNI,XSAVE,OSXSAVE,AVX,RDRAND>
  AMD Features=0x2a500800<SYSCALL,NX,MMX+,FFXSR,RDTSCP,LM>
  AMD Features2=0x1f3<LAHF,CMP,CR8,ABM,SSE4A,MAS,Prefetch>
  Structured Extended Features=0x40021<FSGSBASE,AVX2,RDSEED>
  TSC: P-state invariant

 '''
		return retcode, output

class TestTrueOS_18_X86_64_Ryzen7(unittest.TestCase):
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
		self.assertEqual(10, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(17, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_dmesg(self):
		info = cpuinfo._get_cpu_info_from_dmesg()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('3.6932 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6932 GHz', info['hz_actual_friendly'])
		self.assertEqual((3693150000, 0), info['hz_advertised'])
		self.assertEqual((3693150000, 0), info['hz_actual'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])

		self.assertEqual(
			['abm', 'aesni', 'apic', 'avx', 'cmov', 'cmp', 'cr8', 'cx16',
			'cx8', 'de', 'ffxsr', 'fpu', 'fxsr', 'htt', 'lahf', 'lm', 'mas',
			'mca', 'mce', 'mmx', 'mmx+', 'movbe', 'msr', 'mtrr', 'nx',
			'osxsave', 'pae', 'pat', 'pclmulqdq', 'pge', 'popcnt', 'prefetch',
			'pse', 'pse36', 'rdrand', 'rdtscp', 'sep', 'sse', 'sse2', 'sse3',
			'sse4.1', 'sse4.2', 'sse4a', 'ssse3', 'syscall', 'tsc', 'vme',
			'xsave']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('3.6932 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6932 GHz', info['hz_actual_friendly'])
		self.assertEqual((3693150000, 0), info['hz_advertised'])
		self.assertEqual((3693150000, 0), info['hz_actual'])

		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(8, info['count'])
		self.assertEqual('amd64', info['arch_string_raw'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])

		self.assertEqual(
			['abm', 'aesni', 'apic', 'avx', 'cmov', 'cmp', 'cr8', 'cx16',
			'cx8', 'de', 'ffxsr', 'fpu', 'fxsr', 'htt', 'lahf', 'lm', 'mas',
			'mca', 'mce', 'mmx', 'mmx+', 'movbe', 'msr', 'mtrr', 'nx',
			'osxsave', 'pae', 'pat', 'pclmulqdq', 'pge', 'popcnt', 'prefetch',
			'pse', 'pse36', 'rdrand', 'rdtscp', 'sep', 'sse', 'sse2', 'sse3',
			'sse4.1', 'sse4.2', 'sse4a', 'ssse3', 'syscall', 'tsc', 'vme',
			'xsave']
			,
			info['flags']
		)
