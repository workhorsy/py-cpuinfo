

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 6
	is_windows = False
	raw_arch_string = 'aarch64'
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
processor       : 90
BogoMIPS        : 200.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics
CPU implementer : 0x43
CPU architecture: 8
CPU variant     : 0x1
CPU part        : 0x0a1
CPU revision    : 0

processor       : 91
BogoMIPS        : 200.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics
CPU implementer : 0x43
CPU architecture: 8
CPU variant     : 0x1
CPU part        : 0x0a1
CPU revision    : 0

processor       : 92
BogoMIPS        : 200.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics
CPU implementer : 0x43
CPU architecture: 8
CPU variant     : 0x1
CPU part        : 0x0a1
CPU revision    : 0

processor       : 93
BogoMIPS        : 200.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics
CPU implementer : 0x43
CPU architecture: 8
CPU variant     : 0x1
CPU part        : 0x0a1
CPU revision    : 0

processor       : 94
BogoMIPS        : 200.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics
CPU implementer : 0x43
CPU architecture: 8
CPU variant     : 0x1
CPU part        : 0x0a1
CPU revision    : 0

processor       : 95
BogoMIPS        : 200.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics
CPU implementer : 0x43
CPU architecture: 8
CPU variant     : 0x1
CPU part        : 0x0a1
CPU revision    : 0


'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = '''
Architecture:          aarch64
Byte Order:            Little Endian
CPU(s):                96
On-line CPU(s) list:   0-95
Thread(s) per core:    1
Core(s) per socket:    48
Socket(s):             2
NUMA node(s):          2
L1d cache:             32K
L1i cache:             78K
L2 cache:              16384K
NUMA node0 CPU(s):     0-47
NUMA node1 CPU(s):     48-95
'''
		return returncode, output


class TestLinux_Aarch_64(unittest.TestCase):
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
		self.assertEqual(1, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(6, len(cpuinfo.get_cpu_info()))

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()

		self.assertEqual(0, len(info))

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual(
			['aes', 'asimd', 'atomics', 'crc32', 'evtstrm',
			'fp', 'pmull', 'sha1', 'sha2']
			,
			info['flags']
		)

	@unittest.skip("FIXME: This fails because it does not have a way to get CPU brand string and Hz.")
	def test_all(self):
		info = cpuinfo.get_cpu_info()

		self.assertEqual('', info['vendor_id'])
		self.assertEqual('FIXME', info['hardware'])
		self.assertEqual('FIXME', info['brand'])
		self.assertEqual('FIXME', info['hz_advertised'])
		self.assertEqual('FIXME', info['hz_actual'])
		self.assertEqual((1000000000, 0), info['hz_advertised_raw'])
		self.assertEqual((1000000000, 0), info['hz_actual_raw'])
		self.assertEqual('ARM_8', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(6, info['count'])

		self.assertEqual('aarch64', info['raw_arch_string'])

		self.assertEqual('', info['l2_cache_size'])
		self.assertEqual(0, info['l2_cache_line_size'])
		self.assertEqual(0, info['l2_cache_associativity'])

		self.assertEqual(0, info['stepping'])
		self.assertEqual(0, info['model'])
		self.assertEqual(0, info['family'])
		self.assertEqual(0, info['processor_type'])
		self.assertEqual(0, info['extended_model'])
		self.assertEqual(0, info['extended_family'])
		self.assertEqual(
			['aes', 'asimd', 'atomics', 'crc32', 'evtstrm',
			'fp', 'pmull', 'sha1', 'sha2']
			,
			info['flags']
		)
