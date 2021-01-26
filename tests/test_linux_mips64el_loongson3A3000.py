

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 4
	is_windows = False
	arch_string_raw = 'mips64'
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
system type             : generic-loongson-machine
machine                 : Unknown
processor               : 0
cpu model               : ICT Loongson-3 V0.13  FPU V0.1
model name              : ICT Loongson-3A R3 (Loongson-3A3000) @ 1449MHz
BogoMIPS                : 2887.52
wait instruction        : yes
microsecond timers      : yes
tlb_entries             : 1088
extra interrupt vector  : no
hardware watchpoint     : yes, count: 0, address/irw mask: []
isa                     : mips1 mips2 mips3 mips4 mips5 mips32r1 mips32r2 mips64r1 mips64r2
ASEs implemented        : vz
shadow register sets    : 1
kscratch registers      : 6
package                 : 0
core                    : 0
VCED exceptions         : not available
VCEI exceptions         : not available

processor               : 1
cpu model               : ICT Loongson-3 V0.13  FPU V0.1
model name              : ICT Loongson-3A R3 (Loongson-3A3000) @ 1449MHz
BogoMIPS                : 2902.61
wait instruction        : yes
microsecond timers      : yes
tlb_entries             : 1088
extra interrupt vector  : no
hardware watchpoint     : yes, count: 0, address/irw mask: []
isa                     : mips1 mips2 mips3 mips4 mips5 mips32r1 mips32r2 mips64r1 mips64r2
ASEs implemented        : vz
shadow register sets    : 1
kscratch registers      : 6
package                 : 0
core                    : 1
VCED exceptions         : not available
VCEI exceptions         : not available

processor               : 2
cpu model               : ICT Loongson-3 V0.13  FPU V0.1
model name              : ICT Loongson-3A R3 (Loongson-3A3000) @ 1449MHz
BogoMIPS                : 2902.61
wait instruction        : yes
microsecond timers      : yes
tlb_entries             : 1088
extra interrupt vector  : no
hardware watchpoint     : yes, count: 0, address/irw mask: []
isa                     : mips1 mips2 mips3 mips4 mips5 mips32r1 mips32r2 mips64r1 mips64r2
ASEs implemented        : vz
shadow register sets    : 1
kscratch registers      : 6
package                 : 0
core                    : 2
VCED exceptions         : not available
VCEI exceptions         : not available

processor               : 3
cpu model               : ICT Loongson-3 V0.13  FPU V0.1
model name              : ICT Loongson-3A R3 (Loongson-3A3000) @ 1449MHz
BogoMIPS                : 2887.52
wait instruction        : yes
microsecond timers      : yes
tlb_entries             : 1088
extra interrupt vector  : no
hardware watchpoint     : yes, count: 0, address/irw mask: []
isa                     : mips1 mips2 mips3 mips4 mips5 mips32r1 mips32r2 mips64r1 mips64r2
ASEs implemented        : vz
shadow register sets    : 1
kscratch registers      : 6
package                 : 0
core                    : 3
VCED exceptions         : not available
VCEI exceptions         : not available
'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = r'''
Architecture:          mips64
Byte Order:            Little Endian
CPU(s):                4
On-line CPU(s) list:   0-3
Thread(s) per core:    1
Core(s) per socket:    4
Socket(s):             1
NUMA node(s):          1
Model name:            ICT Loongson-3A R3 (Loongson-3A3000) @ 1449MHz
BogoMIPS:              2887.52
L1d cache:             64K
L1i cache:             64K
L2 cache:              256K
L3 cache:              2048K
NUMA node0 CPU(s):     0-3
'''
		return returncode, output


class TestLinux_mips64el_Loongson3A3000(unittest.TestCase):

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
		self.assertEqual(5, len(cpuinfo._get_cpu_info_from_lscpu()))
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

		self.assertEqual('ICT Loongson-3A R3 (Loongson-3A3000) @ 1449MHz', info['brand_raw'])
		self.assertEqual(65536, info['l1_data_cache_size'])
		self.assertEqual(65536, info['l1_instruction_cache_size'])
		self.assertEqual(262144, info['l2_cache_size'])
		self.assertEqual(2097152, info['l3_cache_size'])

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('ICT Loongson-3A R3 (Loongson-3A3000) @ 1449MHz', info['brand_raw'])
		self.assertEqual('1.4490 GHz', info['hz_advertised_friendly'])
		self.assertEqual('1.4490 GHz', info['hz_actual_friendly'])
		self.assertEqual((1449000000, 0), info['hz_advertised'])
		self.assertEqual((1449000000, 0), info['hz_actual'])
		self.assertEqual(['vz'], info['flags'])

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('ICT Loongson-3A R3 (Loongson-3A3000) @ 1449MHz', info['brand_raw'])
		self.assertEqual('MIPS_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])
		self.assertEqual('mips64', info['arch_string_raw'])
		self.assertEqual(['vz'], info['flags'])
