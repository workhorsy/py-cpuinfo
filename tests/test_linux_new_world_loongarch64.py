

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 4
	is_windows = False
	arch_string_raw = 'loongarch64'
	uname_string_raw = 'loongarch64'
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
CPU Family		: Loongson-64bit
Model Name		: Loongson-3A5000
CPU Revision		: 0x10
FPU Revision		: 0x00
CPU MHz			: 2500.00
BogoMIPS		: 5000.00
TLB Entries		: 2112
Address Sizes		: 48 bits physical, 48 bits virtual
ISA			: loongarch32 loongarch64
Features		: cpucfg lam ual fpu complex crypto lvz
Hardware Watchpoint	: yes, iwatch count: 0, dwatch count: 0

processor		: 1
package			: 0
core			: 1
CPU Family		: Loongson-64bit
Model Name		: Loongson-3A5000
CPU Revision		: 0x10
FPU Revision		: 0x00
CPU MHz			: 2500.00
BogoMIPS		: 5000.00
TLB Entries		: 2112
Address Sizes		: 48 bits physical, 48 bits virtual
ISA			: loongarch32 loongarch64
Features		: cpucfg lam ual fpu complex crypto lvz
Hardware Watchpoint	: yes, iwatch count: 0, dwatch count: 0

processor		: 2
package			: 0
core			: 2
CPU Family		: Loongson-64bit
Model Name		: Loongson-3A5000
CPU Revision		: 0x10
FPU Revision		: 0x00
CPU MHz			: 2500.00
BogoMIPS		: 5000.00
TLB Entries		: 2112
Address Sizes		: 48 bits physical, 48 bits virtual
ISA			: loongarch32 loongarch64
Features		: cpucfg lam ual fpu complex crypto lvz
Hardware Watchpoint	: yes, iwatch count: 0, dwatch count: 0

processor		: 3
package			: 0
core			: 3
CPU Family		: Loongson-64bit
Model Name		: Loongson-3A5000
CPU Revision		: 0x10
FPU Revision		: 0x00
CPU MHz			: 2500.00
BogoMIPS		: 5000.00
TLB Entries		: 2112
Address Sizes		: 48 bits physical, 48 bits virtual
ISA			: loongarch32 loongarch64
Features		: cpucfg lam ual fpu complex crypto lvz
Hardware Watchpoint	: yes, iwatch count: 0, dwatch count: 0

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
Model name:          -
Thread(s) per core:  1
Core(s) per socket:  4
Socket(s):           1
BogoMIPS:            5000.00
Flags:               cpucfg lam ual fpu complex crypto lvz
L1d cache:           256 KiB (4 instances)
L1i cache:           256 KiB (4 instances)
L2 cache:            1 MiB (4 instances)
L3 cache:            16 MiB (1 instance)
NUMA node(s):        1
NUMA node0 CPU(s):   0-3
'''
		return returncode, output


class TestLinux_NewWorld_loongarch64(unittest.TestCase):

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
		self.assertEqual(6, len(cpuinfo._get_cpu_info_from_lscpu()))
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

		self.assertEqual('-', info['brand_raw'])
		self.assertEqual(262144, info['l1_data_cache_size'])
		self.assertEqual(262144, info['l1_instruction_cache_size'])
		self.assertEqual(1048576, info['l2_cache_size'])
		self.assertEqual(16777216, info['l3_cache_size'])
		self.assertEqual(['complex', 'cpucfg', 'crypto', 'fpu', 'lam', 'lvz', 'ual'], info['flags'])

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('Loongson-3A5000', info['brand_raw'])
		self.assertEqual('2.5000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.5000 GHz', info['hz_actual_friendly'])
		self.assertEqual((2500000000, 0), info['hz_advertised'])
		self.assertEqual((2500000000, 0), info['hz_actual'])
		self.assertEqual(['complex', 'cpucfg', 'crypto', 'fpu', 'lam', 'lvz', 'ual'], info['flags'])

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('Loongson-3A5000', info['brand_raw'])
		self.assertEqual('Loong_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])
		self.assertEqual('loongarch64', info['arch_string_raw'])
		self.assertEqual(['complex', 'cpucfg', 'crypto', 'fpu', 'lam', 'lvz', 'ual'], info['flags'])
