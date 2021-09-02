

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 4
	is_windows = False
	arch_string_raw = 'riscv64'
	uname_string_raw = 'riscv64'
	can_cpuid = False

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def has_dmesg():
		return True

	@staticmethod
	def has_lscpu():
		return True

	@staticmethod
	def has_ibm_pa_features():
		return False

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = r'''
processor       : 0
hart            : 2
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 1
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

'''
		return returncode, output

	@staticmethod
	def dmesg_a():
		returncode = 1
		output = r'''
dmesg: read kernel buffer failed: Operation not permitted

'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = r'''
Architecture:        riscv64
Byte Order:          Little Endian
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  4
Core(s) per socket:  1
Socket(s):           1
L1d cache:           32 KiB
L1i cache:           32 KiB
L2 cache:            2 MiB


'''
		return returncode, output


class TestLinuxUbuntu_21_04_riscv64(unittest.TestCase):
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
		self.assertEqual(3, len(cpuinfo._get_cpu_info_from_lscpu()))
		self.assertEqual(1, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(11, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()
		self.assertEqual(32 * 1024, info['l1_instruction_cache_size'])
		self.assertEqual(32 * 1024, info['l1_data_cache_size'])
		self.assertEqual(2 * 1024 * 1024, info['l2_cache_size'])
		self.assertEqual(3, len(info))

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()
		self.assertEqual('sifive,u74-mc', info['brand_raw'])
		self.assertEqual(1, len(info))

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('sifive,u74-mc', info['brand_raw'])
		self.assertEqual('RISCV_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])
		self.assertEqual(32 * 1024, info['l1_instruction_cache_size'])
		self.assertEqual(32 * 1024, info['l1_data_cache_size'])
		self.assertEqual(2 * 1024 * 1024, info['l2_cache_size'])
		self.assertEqual('riscv64', info['arch_string_raw'])
