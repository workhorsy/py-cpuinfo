

import unittest
from cpuinfo import cpuinfo


class DataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	raw_arch_string = 'amd64'

	@staticmethod
	def has_dmesg():
		return True

	@staticmethod
	def dmesg_a_grep_cpu():
		retcode = 0
		output = "CPU: Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz (2993.39-MHz K8-class CPU)"
		return retcode, output

	@staticmethod
	def dmesg_a_grep_origin():
		retcode = 0
		output = '  Origin = "GenuineIntel"  Id = 0x306c3  Family = 0x6  Model = 0x3c  Stepping = 3'
		return retcode, output

	@staticmethod
	def dmesg_a_grep_features():
		retcode = 0
		output = '  Features=0x78bfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,MMX,FXSR,SSE,SSE2>'
		return retcode, output




class TestPCBSD(unittest.TestCase):
	def test_all(self):
		cpuinfo.DataSource = DataSource

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
			['apic', 'clflush', 'cmov', 'cx8', 'de', 'fpu', 'fxsr', 'mca', 
			'mce', 'mmx', 'msr', 'mtrr', 'pae', 'pat', 'pge', 'pse', 'pse36', 
			'sep', 'sse', 'sse2', 'tsc', 'vme']
			,
			info['flags']
		)




