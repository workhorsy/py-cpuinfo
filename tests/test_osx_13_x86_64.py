

import unittest
import cpuinfo
import helpers


class DataSource(object):
	bits = '64bit'
	cpu_count = 4
	is_windows = False
	raw_arch_string = 'x86_64'

	@staticmethod
	def has_sysctl():
		return True

	@staticmethod
	def sysctl_machdep_cpu_hw_cpufrequency():
		returncode = 0
		output = '''
machdep.cpu.max_basic: 5
machdep.cpu.max_ext: 2147483656
machdep.cpu.vendor: GenuineIntel
machdep.cpu.brand_string: Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz
machdep.cpu.family: 6
machdep.cpu.model: 58
machdep.cpu.extmodel: 3
machdep.cpu.extfamily: 0
machdep.cpu.stepping: 9
machdep.cpu.feature_bits: 395049983 2147484161
machdep.cpu.leaf7_feature_bits: 832
machdep.cpu.extfeature_bits: 672139264 1
machdep.cpu.signature: 198313
machdep.cpu.brand: 0
machdep.cpu.features: FPU VME DE PSE TSC MSR PAE MCE CX8 APIC SEP MTRR PGE MCA CMOV PAT PSE36 CLFSH MMX FXSR SSE SSE2 HTT SSE3 SSSE3 VMM
machdep.cpu.leaf7_features: ENFSTRG BMI2
machdep.cpu.extfeatures: SYSCALL XD EM64T LAHF RDTSCP
machdep.cpu.logical_per_package: 4
machdep.cpu.cores_per_package: 4
machdep.cpu.microcode_version: 25
machdep.cpu.processor_flag: 1
machdep.cpu.mwait.linesize_min: 0
machdep.cpu.mwait.linesize_max: 0
machdep.cpu.mwait.extensions: 3
machdep.cpu.mwait.sub_Cstates: 0
machdep.cpu.cache.linesize: 64
machdep.cpu.cache.L2_associativity: 8
machdep.cpu.cache.size: 256
machdep.cpu.tlb.inst.large: 8
machdep.cpu.tlb.data.small: 64
machdep.cpu.tlb.data.small_level1: 128
machdep.cpu.tlb.shared: 1024
machdep.cpu.address_bits.physical: 39
machdep.cpu.address_bits.virtual: 48
machdep.cpu.core_count: 4
machdep.cpu.thread_count: 4
hw.cpufrequency: 2890000000
'''
		return returncode, output




class TestOSX(unittest.TestCase):
	def test_all(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)

		info = cpuinfo.get_cpu_info_from_sysctl()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('', info['hardware'])
		self.assertEqual('Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz', info['brand'])
		self.assertEqual('3.1000 GHz', info['hz_advertised'])
		self.assertEqual('2.8900 GHz', info['hz_actual'])
		self.assertEqual((3100000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2890000000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])

		self.assertEqual('x86_64', info['raw_arch_string'])

		self.assertEqual('256', info['l2_cache_size'])
		self.assertEqual(0, info['l2_cache_line_size'])
		self.assertEqual(0, info['l2_cache_associativity'])

		self.assertEqual(9, info['stepping'])
		self.assertEqual(58, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(0, info['processor_type'])
		self.assertEqual(0, info['extended_model'])
		self.assertEqual(0, info['extended_family'])
		self.assertEqual(
			['apic', 'bmi2', 'clfsh', 'cmov', 'cx8', 'de', 'em64t', 'enfstrg', 'fpu', 'fxsr', 'htt',
			'lahf', 'mca', 'mce', 'mmx', 'msr', 'mtrr', 'pae', 'pat', 'pge', 'pse',
			'pse36', 'rdtscp', 'sep', 'sse', 'sse2', 'sse3', 'ssse3', 'syscall', 'tsc', 'vme',
			'vmm', 'xd', ]
			,
			info['flags']
		)
