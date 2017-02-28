

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
	def cat_var_run_dmesg_boot():
		retcode = 0
		output = '''
VT(vga): text 80x25
CPU: Intel(R) Pentium(R) CPU G640 @ 2.80GHz (2793.73-MHz K8-class CPU)
  Origin="GenuineIntel" Id=0x206a7 Family=0x6 Model=02a Stepping=7
  Features=0x1783fbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,MMX,FXSR,SSE,SSE2,HTT>
  Features2=0xc982203<SSE3,PCLMULQDQ,SSSE3,CX16,SSE4.1,SSE4.2,POPCNT,XSAVE,OSXSAVE>
  AMD Features=0x28100800<SYSCALL,NX,RDTSCP,LM>
  AMD Features2=0x1<LAHF>
  TSC: P-state invariant
 '''
		return retcode, output



class TestFreeBSD_11_X86_64(unittest.TestCase):
	def setUp(self):
		helpers.restore_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	'''
	Make sure calls that should work return something,
	and calls that should NOT work return None.
	'''
	def test_returns(self):
		info = cpuinfo._get_cpu_info_from_registry()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_sysctl()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_kstat()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_dmesg()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()
		self.assertIsNotNone(info)

		info = cpuinfo._get_cpu_info_from_sysinfo()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_cpuid()
		self.assertIsNone(info)

	def test_all(self):
		info = cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('', info['hardware'])
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand'])
		self.assertEqual('2.8000 GHz', info['hz_advertised'])
		self.assertEqual('2.7937 GHz', info['hz_actual'])
		self.assertEqual((2800000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2793730000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(1, info['count'])

		self.assertEqual('amd64', info['raw_arch_string'])

		self.assertEqual(0, info['l2_cache_size'])
		self.assertEqual(0, info['l2_cache_line_size'])
		self.assertEqual(0, info['l2_cache_associativity'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(0, info['processor_type'])
		self.assertEqual(0, info['extended_model'])
		self.assertEqual(0, info['extended_family'])
		self.assertEqual(
			['apic', 'cmov', 'cx16', 'cx8', 'de', 'fpu', 'fxsr', 'htt',
			'lahf', 'lm', 'mca', 'mce', 'mmx', 'msr', 'mtrr', 'nx',
			'osxsave', 'pae', 'pat', 'pclmulqdq', 'pge', 'popcnt', 'pse',
			'pse36', 'rdtscp', 'sep', 'sse', 'sse2', 'sse3', 'sse4.1',
			'sse4.2', 'ssse3', 'syscall', 'tsc', 'vme', 'xsave']
			,
			info['flags']
		)
