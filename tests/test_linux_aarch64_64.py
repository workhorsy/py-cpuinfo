

import unittest
from cpuinfo import *
import helpers


class DataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	raw_arch_string = 'aarch64'

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


class TestLinuxAarch64(unittest.TestCase):
	'''
	Make sure calls that should work return something,
	and calls that should NOT work return None.
	'''
	def test_returns(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)

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

		info = cpuinfo._get_cpu_info_from_sysinfo()
		self.assertIsNone(info)

		info = cpuinfo._get_cpu_info_from_cpuid()
		self.assertIsNone(info)

	'''
	This should return None on ARM, because /proc/cpuinfo returns
	useless info on ARM. It only returns good info on X86.
	'''
	def test_get_cpu_info_from_proc_cpuinfo(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)

		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertIsNone(info)

	def test_get_cpu_info(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)

		info = cpuinfo.get_cpu_info()

		#FIXME: Make sure a valid result is returned
