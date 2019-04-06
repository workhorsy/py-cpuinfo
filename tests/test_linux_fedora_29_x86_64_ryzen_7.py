

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 8
	is_windows = False
	arch_string_raw = 'x86_64'
	uname_string_raw = 'x86_64'
	can_cpuid = False

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def has_lscpu():
		return True

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = '''
processor	: 0
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x6000626
cpu MHz		: 3693.060
cache size	: 512 KB
physical id	: 0
siblings	: 8
core id		: 0
cpu cores	: 8
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid tsc_known_freq pni pclmulqdq ssse3 cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx rdrand hypervisor lahf_lm cmp_legacy cr8_legacy abm sse4a misalignsse 3dnowprefetch cpb ssbd vmmcall fsgsbase avx2 rdseed clflushopt arat
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
bogomips	: 7386.12
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management:


'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = '''
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              8
On-line CPU(s) list: 0-7
Thread(s) per core:  1
Core(s) per socket:  8
Socket(s):           1
NUMA node(s):        1
Vendor ID:           AuthenticAMD
CPU family:          23
Model:               8
Model name:          AMD Ryzen 7 2700X Eight-Core Processor
Stepping:            2
CPU MHz:             3693.060
BogoMIPS:            7386.12
Hypervisor vendor:   KVM
Virtualization type: full
L1d cache:           32K
L1i cache:           64K
L2 cache:            512K
L3 cache:            16384K
NUMA node0 CPU(s):   0-7
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid tsc_known_freq pni pclmulqdq ssse3 cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx rdrand hypervisor lahf_lm cmp_legacy cr8_legacy abm sse4a misalignsse 3dnowprefetch cpb ssbd vmmcall fsgsbase avx2 rdseed clflushopt arat


'''
		return returncode, output


class Test_Linux_Fedora_29_X86_64_Ryzen_7(unittest.TestCase):
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
		self.assertEqual(14, len(cpuinfo._get_cpu_info_from_lscpu()))
		self.assertEqual(11, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(20, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('3.6931 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6931 GHz', info['hz_actual'])
		self.assertEqual((3693060000, 0), info['hz_advertised_raw'])
		self.assertEqual((3693060000, 0), info['hz_actual_raw'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])

		self.assertEqual('64 KB', info['l1_instruction_cache_size'])
		self.assertEqual('32 KB', info['l1_data_cache_size'])
		self.assertEqual('512 KB', info['l2_cache_size'])
		self.assertEqual('16384 KB', info['l3_cache_size'])

		self.assertEqual(
			['3dnowprefetch', 'abm', 'aes', 'apic', 'arat', 'avx', 'avx2',
			'clflush', 'clflushopt', 'cmov', 'cmp_legacy', 'constant_tsc',
			'cpb', 'cpuid', 'cr8_legacy', 'cx16', 'cx8', 'de', 'extd_apicid',
			'fpu', 'fsgsbase', 'fxsr', 'fxsr_opt', 'ht', 'hypervisor',
			'lahf_lm', 'lm', 'mca', 'mce', 'misalignsse', 'mmx', 'mmxext',
			'movbe', 'msr', 'mtrr', 'nonstop_tsc', 'nopl', 'nx', 'pae', 'pat',
			'pclmulqdq', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'rdrand',
			'rdseed', 'rdtscp', 'rep_good', 'sep', 'ssbd', 'sse', 'sse2',
			'sse4_1', 'sse4_2', 'sse4a', 'ssse3', 'syscall', 'tsc',
			'tsc_known_freq', 'vme', 'vmmcall', 'x2apic', 'xsave']
			,
			info['flags']
		)

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('3.6931 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6931 GHz', info['hz_actual'])
		self.assertEqual((3693060000, 0), info['hz_advertised_raw'])
		self.assertEqual((3693060000, 0), info['hz_actual_raw'])

		# FIXME: This is l2 cache size not l3 cache size
		self.assertEqual('512 KB', info['l3_cache_size'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])
		self.assertEqual(
			['3dnowprefetch', 'abm', 'aes', 'apic', 'arat', 'avx', 'avx2',
			'clflush', 'clflushopt', 'cmov', 'cmp_legacy', 'constant_tsc',
			'cpb', 'cpuid', 'cr8_legacy', 'cx16', 'cx8', 'de', 'extd_apicid',
			'fpu', 'fsgsbase', 'fxsr', 'fxsr_opt', 'ht', 'hypervisor',
			'lahf_lm', 'lm', 'mca', 'mce', 'misalignsse', 'mmx', 'mmxext',
			'movbe', 'msr', 'mtrr', 'nonstop_tsc', 'nopl', 'nx', 'pae',
			'pat', 'pclmulqdq', 'pge', 'pni', 'popcnt', 'pse', 'pse36',
			'rdrand', 'rdseed', 'rdtscp', 'rep_good', 'sep', 'ssbd', 'sse',
			'sse2', 'sse4_1', 'sse4_2', 'sse4a', 'ssse3', 'syscall', 'tsc',
			'tsc_known_freq', 'vme', 'vmmcall', 'x2apic', 'xsave']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('3.6931 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6931 GHz', info['hz_actual'])
		self.assertEqual((3693060000, 0), info['hz_advertised_raw'])
		self.assertEqual((3693060000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(8, info['count'])

		self.assertEqual('x86_64', info['arch_string_raw'])

		self.assertEqual('64 KB', info['l1_instruction_cache_size'])
		self.assertEqual('32 KB', info['l1_data_cache_size'])

		self.assertEqual('512 KB', info['l2_cache_size'])
		# FIXME: This is l2 cache size not l3 cache size
		# it is wrong in /proc/cpuinfo
		self.assertEqual('512 KB', info['l3_cache_size'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])
		self.assertEqual(
			['3dnowprefetch', 'abm', 'aes', 'apic', 'arat', 'avx', 'avx2',
			'clflush', 'clflushopt', 'cmov', 'cmp_legacy', 'constant_tsc',
			'cpb', 'cpuid', 'cr8_legacy', 'cx16', 'cx8', 'de', 'extd_apicid',
			'fpu', 'fsgsbase', 'fxsr', 'fxsr_opt', 'ht', 'hypervisor',
			'lahf_lm', 'lm', 'mca', 'mce', 'misalignsse', 'mmx', 'mmxext',
			'movbe', 'msr', 'mtrr', 'nonstop_tsc', 'nopl', 'nx', 'pae', 'pat',
			'pclmulqdq', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'rdrand',
			'rdseed', 'rdtscp', 'rep_good', 'sep', 'ssbd', 'sse', 'sse2',
			'sse4_1', 'sse4_2', 'sse4a', 'ssse3', 'syscall', 'tsc',
			'tsc_known_freq', 'vme', 'vmmcall', 'x2apic', 'xsave']
			,
			info['flags']
		)
