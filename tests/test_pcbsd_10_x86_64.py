

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	arch_string_raw = 'amd64'
	uname_string_raw = 'x86_64'
	can_cpuid = False

	@staticmethod
	def has_dmesg():
		return True

	@staticmethod
	def dmesg_a():
		retcode = 0
		output = '''Copyright (c) 1992-2014 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
    The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 10.0-RELEASE-p17 #0: Tue Sep 16 14:33:46 UTC 2014
    root@amd64-builder.pcbsd.org:/usr/obj/usr/src/sys/GENERIC amd64
FreeBSD clang version 3.3 (tags/RELEASE_33/final 183502) 20130610
CPU: Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz (2993.39-MHz K8-class CPU)
  Origin = "GenuineIntel"  Id = 0x306c3  Family = 0x6  Model = 0x3c  Stepping = 3
  Features=0x78bfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,MMX,FXSR,SSE,SSE2>
  Features2=0x209<SSE3,MON,SSSE3>
  AMD Features=0x28100800<SYSCALL,NX,RDTSCP,LM>
  AMD Features2=0x1<LAHF>
  TSC: P-state invariant

 '''
		return retcode, output



class TestPCBSD(unittest.TestCase):
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
		self.assertEqual(6, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(13, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_dmesg(self):
		info = cpuinfo._get_cpu_info_from_dmesg()

		self.assertEqual('Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz', info['brand_raw'])
		self.assertEqual('3.1000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.1000 GHz', info['hz_actual_friendly'])
		self.assertEqual((3100000000, 0), info['hz_advertised'])
		self.assertEqual((3100000000, 0), info['hz_actual'])

		self.assertEqual(
			['apic', 'clflush', 'cmov', 'cx8', 'de', 'fpu', 'fxsr', 'lahf',
			'lm', 'mca', 'mce', 'mmx', 'mon', 'msr', 'mtrr', 'nx', 'pae',
			'pat', 'pge', 'pse', 'pse36', 'rdtscp', 'sep', 'sse', 'sse2',
			'sse3', 'ssse3', 'syscall', 'tsc', 'vme']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz', info['brand_raw'])
		self.assertEqual('3.1000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.1000 GHz', info['hz_actual_friendly'])
		self.assertEqual((3100000000, 0), info['hz_advertised'])
		self.assertEqual((3100000000, 0), info['hz_actual'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(1, info['count'])

		self.assertEqual('amd64', info['arch_string_raw'])

		self.assertEqual(
			['apic', 'clflush', 'cmov', 'cx8', 'de', 'fpu', 'fxsr', 'lahf',
			'lm', 'mca', 'mce', 'mmx', 'mon', 'msr', 'mtrr', 'nx', 'pae',
			'pat', 'pge', 'pse', 'pse36', 'rdtscp', 'sep', 'sse', 'sse2',
			'sse3', 'ssse3', 'syscall', 'tsc', 'vme']
			,
			info['flags']
		)
