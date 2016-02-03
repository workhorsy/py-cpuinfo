

import unittest
import cpuinfo
import helpers


class DataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	raw_arch_string = 'amd64'

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
	def test_all(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)

		info = cpuinfo.get_cpu_info_from_dmesg()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('', info['hardware'])
		self.assertEqual('Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz', info['brand'])
		self.assertEqual('3.1000 GHz', info['hz_advertised'])
		self.assertEqual('2.9934 GHz', info['hz_actual'])
		self.assertEqual((3100000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2993390000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(1, info['count'])

		self.assertEqual('amd64', info['raw_arch_string'])

		self.assertEqual(0, info['l2_cache_size'])
		self.assertEqual(0, info['l2_cache_line_size'])
		self.assertEqual(0, info['l2_cache_associativity'])

		self.assertEqual(3, info['stepping'])
		self.assertEqual(60, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(0, info['processor_type'])
		self.assertEqual(0, info['extended_model'])
		self.assertEqual(0, info['extended_family'])
		self.assertEqual(
			['apic', 'clflush', 'cmov', 'cx8', 'de', 'fpu', 'fxsr', 'lahf',
			'lm', 'mca', 'mce', 'mmx', 'mon', 'msr', 'mtrr', 'nx', 'pae',
			'pat', 'pge', 'pse', 'pse36', 'rdtscp', 'sep', 'sse', 'sse2',
			'sse3', 'ssse3', 'syscall', 'tsc', 'vme']
			,
			info['flags']
		)
