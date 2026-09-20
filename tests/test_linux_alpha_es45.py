

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 2
	is_windows = False
	arch_string_raw = 'alpha'
	uname_string_raw = 'alpha'
	can_cpuid = False

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = r'''
cpu			: Alpha
cpu model		: EV68CB
cpu variation		: 7
cpu revision		: 0
cpu serial number	: JA31800791
system type		: Titan
system variation	: Privateer
system revision		: 0
system serial number	: AY32202587
cycle frequency [Hz]	: 1250000000 
timer frequency [Hz]	: 1024.00
page size [bytes]	: 8192
phys. address bits	: 44
max. addr. space #	: 255
BogoMIPS		: 2480.92
kernel unaligned acc	: 0 (pc=0,va=0)
user unaligned acc	: 92 (pc=1202a56d8,va=20009a80013)
platform string		: AlphaServer ES45 Model 1
cpus detected		: 2
cpus active		: 2
cpu active mask		: 0000000000000003
L1 Icache		: 64K, 2-way, 64b line
L1 Dcache		: 64K, 2-way, 64b line
L2 cache		: n/a
L3 cache		: n/a
'''
		return returncode, output


class TestLinux_Alpha_ES45(unittest.TestCase):

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
		self.assertEqual(6, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(13, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('EV68CB', info['brand_raw'])
		self.assertEqual('AlphaServer ES45 Model 1', info['hardware_raw'])
		self.assertEqual('1.2500 GHz', info['hz_advertised_friendly'])
		self.assertEqual('1.2500 GHz', info['hz_actual_friendly'])
		self.assertEqual((1250000000, 0), info['hz_advertised'])
		self.assertEqual((1250000000, 0), info['hz_actual'])

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('EV68CB', info['brand_raw'])
		self.assertEqual('AlphaServer ES45 Model 1', info['hardware_raw'])
		self.assertEqual('ALPHA', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(2, info['count'])
		self.assertEqual('alpha', info['arch_string_raw'])
		self.assertEqual('1.2500 GHz', info['hz_advertised_friendly'])
		self.assertEqual((1250000000, 0), info['hz_advertised'])
