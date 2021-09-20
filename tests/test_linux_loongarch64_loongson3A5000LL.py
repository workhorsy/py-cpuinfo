

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 4
	is_windows = False
	arch_string_raw = 'loongarch64'
	uname_string_raw = ''
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
		output = r'''
system type		: generic-loongson-machine
processor		: 0
package			: 0
core			: 0
cpu family		: Loongson-64bit
model name		: Loongson-3A5000LL
CPU Revision		: 0x10
FPU Revision		: 0x00
CPU MHz			: 2300.00
BogoMIPS		: 4600.00
TLB entries		: 2112
Address sizes		: 48 bits physical, 48 bits virtual
isa			: loongarch32 loongarch64
features		: cpucfg lam ual fpu lsx lasx complex crypto lvz
hardware watchpoint	: yes, iwatch count: 8, dwatch count: 8
'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = r'''
Architecture:        loongarch64
Byte Order:          Little Endian
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  1
Core(s) per socket:  4
Socket(s):           1
NUMA node(s):        1
CPU family:          Loongson-64bit
Model name:          Loongson-3A5000LL
CPU max MHz:         2300.0000
CPU min MHz:         225.0000
BogoMIPS:            4600.00
L1d cache:           64K
L1i cache:           64K
L2 cache:            256K
L3 cache:            16384K
NUMA node0 CPU(s):   0-3
Flags:               cpucfg lam ual fpu lsx lasx complex crypto lvz
'''
		return returncode, output


class TestLinux_loongarch64_Loongson3A5000LL(unittest.TestCase):

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
		self.assertEqual(10, len(cpuinfo._get_cpu_info_from_lscpu()))
		self.assertEqual(6, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(17, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()

		self.assertEqual('Loongson-3A5000LL', info['brand_raw'])
		self.assertEqual(65536, info['l1_data_cache_size'])
		self.assertEqual(65536, info['l1_instruction_cache_size'])
		self.assertEqual(262144, info['l2_cache_size'])
		self.assertEqual(16777216, info['l3_cache_size'])

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('Loongson-3A5000LL', info['brand_raw'])
		self.assertEqual('2.3000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.3000 GHz', info['hz_actual_friendly'])
		self.assertEqual((2300000000, 0), info['hz_advertised'])
		self.assertEqual((2300000000, 0), info['hz_actual'])
		self.assertEqual(['complex', 'cpucfg', 'crypto', 'fpu', 'lam', 'lasx', 'lsx', 'lvz', 'ual'], info['flags'])

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('Loongson-3A5000LL', info['brand_raw'])
		self.assertEqual('LOONG_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])
		self.assertEqual('loongarch64', info['arch_string_raw'])
		self.assertEqual(['complex', 'cpucfg', 'crypto', 'fpu', 'lam', 'lasx', 'lsx', 'lvz', 'ual'], info['flags'])
