

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '32bit'
	cpu_count = 2
	is_windows = False
	arch_string_raw = 'mips'
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
system type		: Baikal-T Generic SoC
machine			: Baikal-T1 BFK3 evaluation board
processor		: 0
cpu model		: MIPS P5600 V3.0  FPU V2.0
BogoMIPS		: 1196.85
wait instruction	: yes
microsecond timers	: yes
tlb_entries		: 576
extra interrupt vector	: yes
hardware watchpoint	: yes, count: 4, address/irw mask: [0x0ffc, 0x0ffc, 0x0ffb, 0x0ffb]
isa			: mips1 mips2 mips32r1 mips32r2
ASEs implemented	: vz msa eva xpa
shadow register sets	: 1
kscratch registers	: 3
package			: 0
core			: 0
VCED exceptions		: not available
VCEI exceptions		: not available

processor		: 1
cpu model		: MIPS P5600 V3.0  FPU V2.0
BogoMIPS		: 1202.58
wait instruction	: yes
microsecond timers	: yes
tlb_entries		: 576
extra interrupt vector	: yes
hardware watchpoint	: yes, count: 4, address/irw mask: [0x0ffc, 0x0ffc, 0x0ffb, 0x0ffb]
isa			: mips1 mips2 mips32r1 mips32r2
ASEs implemented	: vz msa eva xpa
shadow register sets	: 1
kscratch registers	: 3
package			: 0
core			: 1
VCED exceptions		: not available
VCEI exceptions		: not available
'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = r'''
Architecture:        mips
Byte Order:          Little Endian
CPU(s):              2
On-line CPU(s) list: 0,1
Thread(s) per core:  1
Core(s) per socket:  2
Socket(s):           1
Model:               MIPS P5600 V3.0  FPU V2.0
CPU max MHz:         1200,0000
CPU min MHz:         200,0000
BogoMIPS:            1196.85
Flags:               vz msa eva xpa
'''
		return returncode, output


class TestLinuxAlt_p9_mipsel_bfk3(unittest.TestCase):

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
		self.assertEqual(1, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(13, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()

		self.assertEqual('MIPS P5600 V3.0  FPU V2.0', info['brand_raw'])
		self.assertEqual('1.2000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('1.2000 GHz', info['hz_actual_friendly'])
		self.assertEqual((1200000000, 0), info['hz_advertised'])
		self.assertEqual((1200000000, 0), info['hz_actual'])
		self.assertEqual(['eva', 'msa', 'vz', 'xpa'], info['flags'])

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual(['eva', 'msa', 'vz', 'xpa'], info['flags'])

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('MIPS P5600 V3.0  FPU V2.0', info['brand_raw'])
		self.assertEqual('MIPS_32', info['arch'])
		self.assertEqual(32, info['bits'])
		self.assertEqual(2, info['count'])
		self.assertEqual('mips', info['arch_string_raw'])
		self.assertEqual(['eva', 'msa', 'vz', 'xpa'], info['flags'])
