

import unittest
import cpuinfo
import helpers


class DataSource(object):
	bits = '32bit'
	cpu_count = 4
	is_windows = False
	raw_arch_string = 'BePC'

	@staticmethod
	def has_sysinfo():
		return True

	@staticmethod
	def sysinfo_cpu():
		returncode = 0
		output = '''
4 Intel Core i7, revision 46e5 running at 2928MHz (ID: 0x00000000 0x00000000)

CPU #0: "Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz"
	Type 0, family 6, model 30, stepping 5, features 0x178bfbbf
		FPU VME DE PSE TSC MSR MCE CX8 APIC SEP MTRR PGE MCA CMOV PAT PSE36
		CFLUSH MMX FXSTR SSE SSE2 HTT
	Extended Intel: 0x00000201
		SSE3 SSSE3
	Extended AMD: type 0, family 0, model 0, stepping 0, features 0x08000000
		RDTSCP
	Power Management Features:

	L2 Data cache 8-way set associative, 1 lines/tag, 64 bytes/line
	L2 cache: 0 KB, 1-way set associative, 0 lines/tag, 63 bytes/line

	Data TLB: 2M/4M-bytes pages, 4-way set associative, 32 entries
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




class TestHaiku(unittest.TestCase):
	def test_all(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)

		info = cpuinfo.get_cpu_info_from_sysinfo()

		# FIXME: Add vendor id
		#self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('', info['hardware'])
		self.assertEqual('Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz', info['brand'])
		self.assertEqual('2.9300 GHz', info['hz_advertised'])
		self.assertEqual('2.9300 GHz', info['hz_actual'])
		self.assertEqual((2930000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2930000000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_32', info['arch'])
		self.assertEqual(32, info['bits'])
		self.assertEqual(4, info['count'])

		self.assertEqual('BePC', info['raw_arch_string'])

		self.assertEqual('', info['l2_cache_size'])
		self.assertEqual(0, info['l2_cache_line_size'])
		self.assertEqual(0, info['l2_cache_associativity'])

		self.assertEqual(5, info['stepping'])
		self.assertEqual(30, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(0, info['processor_type'])
		self.assertEqual(0, info['extended_model'])
		self.assertEqual(0, info['extended_family'])
		self.assertEqual(
			['apic', 'cflush', 'cmov', 'cx8', 'de', 'fpu', 'fxstr', 'htt',
			'mca', 'mce', 'mmx', 'msr', 'mtrr', 'pat', 'pge', 'pse', 'pse36',
			'rdtscp', 'sep', 'sse', 'sse2', 'sse3', 'ssse3', 'tsc', 'vme']
			,
			info['flags']
		)
