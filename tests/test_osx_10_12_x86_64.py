
# OS X 10.12 Sierra
# Darwin version 16

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 4
	is_windows = False
	arch_string_raw = 'x86_64'
	uname_string_raw = 'x86_64'
	can_cpuid = False

	@staticmethod
	def has_sysctl():
		return True

	@staticmethod
	def sysctl_machdep_cpu_hw_cpufrequency():
		returncode = 0
		output = r'''
machdep.cpu.tsc_ccc.denominator: 0
machdep.cpu.tsc_ccc.numerator: 0
machdep.cpu.thread_count: 4
machdep.cpu.core_count: 2
machdep.cpu.address_bits.virtual: 48
machdep.cpu.address_bits.physical: 36
machdep.cpu.tlb.shared: 512
machdep.cpu.tlb.data.large: 32
machdep.cpu.tlb.data.small: 64
machdep.cpu.tlb.inst.large: 8
machdep.cpu.tlb.inst.small: 64
machdep.cpu.cache.size: 256
machdep.cpu.cache.L2_associativity: 8
machdep.cpu.cache.linesize: 64
machdep.cpu.arch_perf.fixed_width: 48
machdep.cpu.arch_perf.fixed_number: 3
machdep.cpu.arch_perf.events: 0
machdep.cpu.arch_perf.events_number: 7
machdep.cpu.arch_perf.width: 48
machdep.cpu.arch_perf.number: 4
machdep.cpu.arch_perf.version: 3
machdep.cpu.xsave.extended_state1: 1 0 0 0
machdep.cpu.xsave.extended_state: 7 832 832 0
machdep.cpu.thermal.energy_policy: 1
machdep.cpu.thermal.hardware_feedback: 0
machdep.cpu.thermal.package_thermal_intr: 1
machdep.cpu.thermal.fine_grain_clock_mod: 1
machdep.cpu.thermal.core_power_limits: 1
machdep.cpu.thermal.ACNT_MCNT: 1
machdep.cpu.thermal.thresholds: 2
machdep.cpu.thermal.invariant_APIC_timer: 1
machdep.cpu.thermal.dynamic_acceleration: 1
machdep.cpu.thermal.sensor: 1
machdep.cpu.mwait.sub_Cstates: 135456
machdep.cpu.mwait.extensions: 3
machdep.cpu.mwait.linesize_max: 64
machdep.cpu.mwait.linesize_min: 64
machdep.cpu.processor_flag: 4
machdep.cpu.microcode_version: 40
machdep.cpu.cores_per_package: 8
machdep.cpu.logical_per_package: 16
machdep.cpu.extfeatures: SYSCALL XD EM64T LAHF RDTSCP TSCI
machdep.cpu.features: FPU VME DE PSE TSC MSR PAE MCE CX8 APIC SEP MTRR PGE MCA CMOV PAT PSE36 CLFSH DS ACPI MMX FXSR SSE SSE2 SS HTT TM PBE SSE3 PCLMULQDQ DTES64 MON DSCPL VMX SMX EST TM2 SSSE3 CX16 TPR PDCM SSE4.1 SSE4.2 x2APIC POPCNT AES PCID XSAVE OSXSAVE TSCTMR AVX1.0
machdep.cpu.brand: 0
machdep.cpu.signature: 132775
machdep.cpu.extfeature_bits: 4967106816
machdep.cpu.feature_bits: 2286390448420027391
machdep.cpu.stepping: 7
machdep.cpu.extfamily: 0
machdep.cpu.extmodel: 2
machdep.cpu.model: 42
machdep.cpu.family: 6
machdep.cpu.brand_string: Intel(R) Core(TM) i5-2557M CPU @ 1.70GHz
machdep.cpu.vendor: GenuineIntel
machdep.cpu.max_ext: 2147483656
machdep.cpu.max_basic: 13
hw.cpufrequency: 1700000000
'''
		return returncode, output




class TestOSX_10_12(unittest.TestCase):
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
		self.assertEqual(11, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(18, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_sysctl(self):
		info = cpuinfo._get_cpu_info_from_sysctl()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Core(TM) i5-2557M CPU @ 1.70GHz', info['brand_raw'])
		self.assertEqual('1.7000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('1.7000 GHz', info['hz_actual_friendly'])
		self.assertEqual((1700000000, 0), info['hz_advertised'])
		self.assertEqual((1700000000, 0), info['hz_actual'])

		self.assertEqual(256 * 1024, info['l2_cache_size'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])

		self.assertEqual(
			['acpi', 'aes', 'apic', 'avx1.0', 'clfsh', 'cmov', 'cx16', 'cx8',
			'de', 'ds', 'dscpl', 'dtes64', 'em64t', 'est', 'fpu', 'fxsr',
			'htt', 'lahf', 'mca', 'mce', 'mmx', 'mon', 'msr', 'mtrr',
			'osxsave', 'pae', 'pat', 'pbe', 'pcid', 'pclmulqdq', 'pdcm',
			'pge', 'popcnt', 'pse', 'pse36', 'rdtscp', 'sep', 'smx', 'ss',
			'sse', 'sse2', 'sse3', 'sse4.1', 'sse4.2', 'ssse3', 'syscall',
			'tm', 'tm2', 'tpr', 'tsc', 'tsci', 'tsctmr', 'vme', 'vmx',
			'x2apic', 'xd', 'xsave']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Core(TM) i5-2557M CPU @ 1.70GHz', info['brand_raw'])
		self.assertEqual('1.7000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('1.7000 GHz', info['hz_actual_friendly'])
		self.assertEqual((1700000000, 0), info['hz_advertised'])
		self.assertEqual((1700000000, 0), info['hz_actual'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])

		self.assertEqual('x86_64', info['arch_string_raw'])

		self.assertEqual(256 * 1024, info['l2_cache_size'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])

		self.assertEqual(
			['acpi', 'aes', 'apic', 'avx1.0', 'clfsh', 'cmov', 'cx16', 'cx8',
			'de', 'ds', 'dscpl', 'dtes64', 'em64t', 'est', 'fpu', 'fxsr',
			'htt', 'lahf', 'mca', 'mce', 'mmx', 'mon', 'msr', 'mtrr',
			'osxsave', 'pae', 'pat', 'pbe', 'pcid', 'pclmulqdq', 'pdcm',
			'pge', 'popcnt', 'pse', 'pse36', 'rdtscp', 'sep', 'smx', 'ss',
			'sse', 'sse2', 'sse3', 'sse4.1', 'sse4.2', 'ssse3', 'syscall',
			'tm', 'tm2', 'tpr', 'tsc', 'tsci', 'tsctmr', 'vme', 'vmx',
			'x2apic', 'xd', 'xsave']
			,
			info['flags']
		)
