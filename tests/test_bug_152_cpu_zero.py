

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 1
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
		output = r'''
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 0
model		: 0
model name	: Intel(R) Pentium(R) CPU G640 @ 2.80GHz
stepping	: 0
microcode	: 0x29
cpu MHz		: 1901.375
cache size	: 3072 KB
physical id	: 0
siblings	: 2
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave lahf_lm epb tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm arat pln pts
bugs		:
bogomips	: 5587.32
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:


'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = r'''
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                2
On-line CPU(s) list:   0,1
Thread(s) per core:    1
Core(s) per socket:    2
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            0
Model:                 0
Model name:            Intel(R) Pentium(R) CPU G640 @ 2.80GHz
Stepping:              0
CPU MHz:               2070.796
CPU max MHz:           2800.0000
CPU min MHz:           1600.0000
BogoMIPS:              5587.32
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              3072K
NUMA node0 CPU(s):     0,1
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave lahf_lm epb tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm arat pln pts


'''
		return returncode, output

# Confirms fix for: https://github.com/workhorsy/py-cpuinfo/issues/152
# CPU stepping, model, and family values are blank if 0
class TestBug152(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()

		# Make sure fields with 0 are not filtered out
		self.assertIn('stepping', info.keys())
		self.assertIn('model', info.keys())
		self.assertIn('family', info.keys())

		self.assertEqual(0, info['stepping'])
		self.assertEqual(0, info['model'])
		self.assertEqual(0, info['family'])

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		# Make sure fields with 0 are not filtered out
		self.assertIn('stepping', info.keys())
		self.assertIn('model', info.keys())
		self.assertIn('family', info.keys())

		self.assertEqual(0, info['stepping'])
		self.assertEqual(0, info['model'])
		self.assertEqual(0, info['family'])

