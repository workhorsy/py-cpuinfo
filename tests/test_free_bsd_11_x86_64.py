

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
	def has_var_run_dmesg_boot():
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
VT(vga): text 80x25
CPU: Intel(R) Pentium(R) CPU G640 @ 2.80GHz (2793.73-MHz K8-class CPU)
  Origin="GenuineIntel"  Id=0x206a7  Family=0x6  Model=02a  Stepping=7
  Features=0x1783fbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,MMX,FXSR,SSE,SSE2,HTT>
  Features2=0xc982203<SSE3,PCLMULQDQ,SSSE3,CX16,SSE4.1,SSE4.2,POPCNT,XSAVE,OSXSAVE>
  AMD Features=0x28100800<SYSCALL,NX,RDTSCP,LM>
  AMD Features2=0x1<LAHF>
  TSC: P-state invariant
 '''
		return retcode, output

	@staticmethod
	def cat_var_run_dmesg_boot():
		retcode = 0
		output = '''
VT(vga): text 80x25
CPU: Intel(R) Pentium(R) CPU G640 @ 2.80GHz (2793.73-MHz K8-class CPU)
  Origin="GenuineIntel"  Id=0x206a7  Family=0x6  Model=02a  Stepping=7
  Features=0x1783fbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,MMX,FXSR,SSE,SSE2,HTT>
  Features2=0xc982203<SSE3,PCLMULQDQ,SSSE3,CX16,SSE4.1,SSE4.2,POPCNT,XSAVE,OSXSAVE>
  AMD Features=0x28100800<SYSCALL,NX,RDTSCP,LM>
  AMD Features2=0x1<LAHF>
  TSC: P-state invariant
 '''
		return retcode, output



class TestFreeBSD_11_X86_64(unittest.TestCase):
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
		self.assertEqual(10, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(15, len(cpuinfo.get_cpu_info()))

	def test_get_cpu_info_from_dmesg(self):
		info = cpuinfo._get_cpu_info_from_dmesg()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand'])
		self.assertEqual('2.8000 GHz', info['hz_advertised'])
		self.assertEqual('2.8000 GHz', info['hz_actual'])
		self.assertEqual((2800000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2800000000, 0), info['hz_actual_raw'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['apic', 'cmov', 'cx16', 'cx8', 'de', 'fpu', 'fxsr', 'htt',
			'lahf', 'lm', 'mca', 'mce', 'mmx', 'msr', 'mtrr', 'nx',
			'osxsave', 'pae', 'pat', 'pclmulqdq', 'pge', 'popcnt', 'pse',
			'pse36', 'rdtscp', 'sep', 'sse', 'sse2', 'sse3', 'sse4.1',
			'sse4.2', 'ssse3', 'syscall', 'tsc', 'vme', 'xsave']
			,
			info['flags']
		)

	def test_get_cpu_info_from_cat_var_run_dmesg_boot(self):
		info = cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand'])
		self.assertEqual('2.8000 GHz', info['hz_advertised'])
		self.assertEqual('2.8000 GHz', info['hz_actual'])
		self.assertEqual((2800000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2800000000, 0), info['hz_actual_raw'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['apic', 'cmov', 'cx16', 'cx8', 'de', 'fpu', 'fxsr', 'htt',
			'lahf', 'lm', 'mca', 'mce', 'mmx', 'msr', 'mtrr', 'nx',
			'osxsave', 'pae', 'pat', 'pclmulqdq', 'pge', 'popcnt', 'pse',
			'pse36', 'rdtscp', 'sep', 'sse', 'sse2', 'sse3', 'sse4.1',
			'sse4.2', 'ssse3', 'syscall', 'tsc', 'vme', 'xsave']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo.get_cpu_info()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand'])
		self.assertEqual('2.8000 GHz', info['hz_advertised'])
		self.assertEqual('2.8000 GHz', info['hz_actual'])
		self.assertEqual((2800000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2800000000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(1, info['count'])

		self.assertEqual('amd64', info['raw_arch_string'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['apic', 'cmov', 'cx16', 'cx8', 'de', 'fpu', 'fxsr', 'htt',
			'lahf', 'lm', 'mca', 'mce', 'mmx', 'msr', 'mtrr', 'nx',
			'osxsave', 'pae', 'pat', 'pclmulqdq', 'pge', 'popcnt', 'pse',
			'pse36', 'rdtscp', 'sep', 'sse', 'sse2', 'sse3', 'sse4.1',
			'sse4.2', 'ssse3', 'syscall', 'tsc', 'vme', 'xsave']
			,
			info['flags']
		)
