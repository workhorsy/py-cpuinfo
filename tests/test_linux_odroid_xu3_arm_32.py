

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '32bit'
	cpu_count = 8
	is_windows = False
	raw_arch_string = 'armv7l'
	can_cpuid = False

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def has_lscpu():
		return True

	@staticmethod
	def has_cpufreq_info():
		return True

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = '''
processor	: 0
model name	: ARMv7 Processor rev 3 (v7l)
BogoMIPS	: 84.00
Features	: swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xc07
CPU revision	: 3

processor	: 1
model name	: ARMv7 Processor rev 3 (v7l)
BogoMIPS	: 84.00
Features	: swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xc07
CPU revision	: 3

processor	: 2
model name	: ARMv7 Processor rev 3 (v7l)
BogoMIPS	: 84.00
Features	: swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xc07
CPU revision	: 3

processor	: 3
model name	: ARMv7 Processor rev 3 (v7l)
BogoMIPS	: 84.00
Features	: swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xc07
CPU revision	: 3

processor	: 4
model name	: ARMv7 Processor rev 3 (v7l)
BogoMIPS	: 36.00
Features	: swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x2
CPU part	: 0xc0f
CPU revision	: 3

processor	: 5
model name	: ARMv7 Processor rev 3 (v7l)
BogoMIPS	: 36.00
Features	: swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x2
CPU part	: 0xc0f
CPU revision	: 3

processor	: 6
model name	: ARMv7 Processor rev 3 (v7l)
BogoMIPS	: 36.00
Features	: swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x2
CPU part	: 0xc0f
CPU revision	: 3

processor	: 7
model name	: ARMv7 Processor rev 3 (v7l)
BogoMIPS	: 36.00
Features	: swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x2
CPU part	: 0xc0f
CPU revision	: 3

Hardware	: ODROID-XU3
Revision	: 0100
Serial		: 0000000000000000


'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = '''
Architecture:          armv7l
Byte Order:            Little Endian
CPU(s):                8
On-line CPU(s) list:   0-7
Thread(s) per core:    1
Core(s) per socket:    4
Socket(s):             2
Model name:            ARMv7 Processor rev 3 (v7l)
CPU max MHz:           1400.0000
CPU min MHz:           200.0000

'''
		return returncode, output

	@staticmethod
	def cpufreq_info():
		returncode = 0
		output = '''
cpufrequtils 008: cpufreq-info (C) Dominik Brodowski 2004-2009
Report errors and bugs to cpufreq@vger.kernel.org, please.
analyzing CPU 0:
  driver: exynos_cpufreq
  CPUs which run at the same hardware frequency: 0 1 2 3
  CPUs which need to have their frequency coordinated by software: 0 1 2 3
  maximum transition latency: 100.0 us.
  hardware limits: 200 MHz - 1.40 GHz
  available cpufreq governors: interactive, conservative, ondemand, powersave, performance
  current policy: frequency should be within 200 MHz and 1.40 GHz.
                  The governor "interactive" may decide which speed to use
                  within this range.
  current CPU frequency is 1.40 GHz (asserted by call to hardware).
  cpufreq stats: 1.40 GHz:33.77%, 1.30 GHz:0.04%, 1.20 GHz:0.03%, 1.10 GHz:0.02%, 1000 MHz:0.03%, 900 MHz:0.04%, 800 MHz:0.06%, 700 MHz:0.10%, 600 MHz:0.13%, 500 MHz:0.19%, 400 MHz:0.31%, 300 MHz:2.09%, 200 MHz:63.20%  (880901)
analyzing CPU 1:
  driver: exynos_cpufreq
  CPUs which run at the same hardware frequency: 0 1 2 3
  CPUs which need to have their frequency coordinated by software: 0 1 2 3
  maximum transition latency: 100.0 us.
  hardware limits: 200 MHz - 1.40 GHz
  available cpufreq governors: interactive, conservative, ondemand, powersave, performance
  current policy: frequency should be within 200 MHz and 1.40 GHz.
                  The governor "interactive" may decide which speed to use
                  within this range.
  current CPU frequency is 1.40 GHz (asserted by call to hardware).
  cpufreq stats: 1.40 GHz:33.77%, 1.30 GHz:0.04%, 1.20 GHz:0.03%, 1.10 GHz:0.02%, 1000 MHz:0.03%, 900 MHz:0.04%, 800 MHz:0.06%, 700 MHz:0.10%, 600 MHz:0.13%, 500 MHz:0.19%, 400 MHz:0.31%, 300 MHz:2.09%, 200 MHz:63.20%  (880901)
analyzing CPU 2:
  driver: exynos_cpufreq
  CPUs which run at the same hardware frequency: 0 1 2 3
  CPUs which need to have their frequency coordinated by software: 0 1 2 3
  maximum transition latency: 100.0 us.
  hardware limits: 200 MHz - 1.40 GHz
  available cpufreq governors: interactive, conservative, ondemand, powersave, performance
  current policy: frequency should be within 200 MHz and 1.40 GHz.
                  The governor "interactive" may decide which speed to use
                  within this range.
  current CPU frequency is 1.40 GHz (asserted by call to hardware).
  cpufreq stats: 1.40 GHz:33.77%, 1.30 GHz:0.04%, 1.20 GHz:0.03%, 1.10 GHz:0.02%, 1000 MHz:0.03%, 900 MHz:0.04%, 800 MHz:0.06%, 700 MHz:0.10%, 600 MHz:0.13%, 500 MHz:0.19%, 400 MHz:0.31%, 300 MHz:2.09%, 200 MHz:63.20%  (880901)
analyzing CPU 3:
  driver: exynos_cpufreq
  CPUs which run at the same hardware frequency: 0 1 2 3
  CPUs which need to have their frequency coordinated by software: 0 1 2 3
  maximum transition latency: 100.0 us.
  hardware limits: 200 MHz - 1.40 GHz
  available cpufreq governors: interactive, conservative, ondemand, powersave, performance
  current policy: frequency should be within 200 MHz and 1.40 GHz.
                  The governor "interactive" may decide which speed to use
                  within this range.
  current CPU frequency is 1.40 GHz (asserted by call to hardware).
  cpufreq stats: 1.40 GHz:33.77%, 1.30 GHz:0.04%, 1.20 GHz:0.03%, 1.10 GHz:0.02%, 1000 MHz:0.03%, 900 MHz:0.04%, 800 MHz:0.06%, 700 MHz:0.10%, 600 MHz:0.13%, 500 MHz:0.19%, 400 MHz:0.31%, 300 MHz:2.09%, 200 MHz:63.20%  (880901)
analyzing CPU 4:
  driver: exynos_cpufreq
  CPUs which run at the same hardware frequency: 4 5 6 7
  CPUs which need to have their frequency coordinated by software: 4 5 6 7
  maximum transition latency: 100.0 us.
  hardware limits: 200 MHz - 2.00 GHz
  available cpufreq governors: interactive, conservative, ondemand, powersave, performance
  current policy: frequency should be within 200 MHz and 2.00 GHz.
                  The governor "interactive" may decide which speed to use
                  within this range.
  current CPU frequency is 2.00 GHz (asserted by call to hardware).
  cpufreq stats: 2.00 GHz:22.57%, 1.90 GHz:0.02%, 1.80 GHz:0.01%, 1.70 GHz:0.02%, 1.60 GHz:0.09%, 1.50 GHz:0.11%, 1.40 GHz:0.01%, 1.30 GHz:0.00%, 1.20 GHz:0.01%, 1.10 GHz:0.00%, 1000 MHz:0.00%, 900 MHz:0.13%, 800 MHz:0.00%, 700 MHz:0.01%, 600 MHz:0.01%, 500 MHz:0.03%, 400 MHz:0.14%, 300 MHz:0.18%, 200 MHz:76.65%  (316653)
analyzing CPU 5:
  driver: exynos_cpufreq
  CPUs which run at the same hardware frequency: 4 5 6 7
  CPUs which need to have their frequency coordinated by software: 4 5 6 7
  maximum transition latency: 100.0 us.
  hardware limits: 200 MHz - 2.00 GHz
  available cpufreq governors: interactive, conservative, ondemand, powersave, performance
  current policy: frequency should be within 200 MHz and 2.00 GHz.
                  The governor "interactive" may decide which speed to use
                  within this range.
  current CPU frequency is 2.00 GHz (asserted by call to hardware).
  cpufreq stats: 2.00 GHz:22.57%, 1.90 GHz:0.02%, 1.80 GHz:0.01%, 1.70 GHz:0.02%, 1.60 GHz:0.09%, 1.50 GHz:0.11%, 1.40 GHz:0.01%, 1.30 GHz:0.00%, 1.20 GHz:0.01%, 1.10 GHz:0.00%, 1000 MHz:0.00%, 900 MHz:0.13%, 800 MHz:0.00%, 700 MHz:0.01%, 600 MHz:0.01%, 500 MHz:0.03%, 400 MHz:0.14%, 300 MHz:0.18%, 200 MHz:76.65%  (316653)
analyzing CPU 6:
  driver: exynos_cpufreq
  CPUs which run at the same hardware frequency: 4 5 6 7
  CPUs which need to have their frequency coordinated by software: 4 5 6 7
  maximum transition latency: 100.0 us.
  hardware limits: 200 MHz - 2.00 GHz
  available cpufreq governors: interactive, conservative, ondemand, powersave, performance
  current policy: frequency should be within 200 MHz and 2.00 GHz.
                  The governor "interactive" may decide which speed to use
                  within this range.
  current CPU frequency is 2.00 GHz (asserted by call to hardware).
  cpufreq stats: 2.00 GHz:22.57%, 1.90 GHz:0.02%, 1.80 GHz:0.01%, 1.70 GHz:0.02%, 1.60 GHz:0.09%, 1.50 GHz:0.11%, 1.40 GHz:0.01%, 1.30 GHz:0.00%, 1.20 GHz:0.01%, 1.10 GHz:0.00%, 1000 MHz:0.00%, 900 MHz:0.13%, 800 MHz:0.00%, 700 MHz:0.01%, 600 MHz:0.01%, 500 MHz:0.03%, 400 MHz:0.14%, 300 MHz:0.18%, 200 MHz:76.65%  (316653)
analyzing CPU 7:
  driver: exynos_cpufreq
  CPUs which run at the same hardware frequency: 4 5 6 7
  CPUs which need to have their frequency coordinated by software: 4 5 6 7
  maximum transition latency: 100.0 us.
  hardware limits: 200 MHz - 2.00 GHz
  available cpufreq governors: interactive, conservative, ondemand, powersave, performance
  current policy: frequency should be within 200 MHz and 2.00 GHz.
                  The governor "interactive" may decide which speed to use
                  within this range.
  current CPU frequency is 2.00 GHz (asserted by call to hardware).
  cpufreq stats: 2.00 GHz:22.57%, 1.90 GHz:0.02%, 1.80 GHz:0.01%, 1.70 GHz:0.02%, 1.60 GHz:0.09%, 1.50 GHz:0.11%, 1.40 GHz:0.01%, 1.30 GHz:0.00%, 1.20 GHz:0.01%, 1.10 GHz:0.00%, 1000 MHz:0.00%, 900 MHz:0.13%, 800 MHz:0.00%, 700 MHz:0.01%, 600 MHz:0.01%, 500 MHz:0.03%, 400 MHz:0.14%, 300 MHz:0.18%, 200 MHz:76.65%  (316653)

'''
		return returncode, output


class TestLinux_Odroid_XU3_arm_32(unittest.TestCase):
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
		self.assertEqual(4, len(cpuinfo._get_cpu_info_from_cpufreq_info()))
		self.assertEqual(5, len(cpuinfo._get_cpu_info_from_lscpu()))
		self.assertEqual(3, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(12, len(cpuinfo.get_cpu_info()))

	def test_get_cpu_info_from_cpufreq_info(self):
		info = cpuinfo._get_cpu_info_from_cpufreq_info()

		self.assertEqual('1.4000 GHz', info['hz_advertised'])
		self.assertEqual('1.4000 GHz', info['hz_actual'])
		self.assertEqual((1400000000, 0), info['hz_advertised_raw'])
		self.assertEqual((1400000000, 0), info['hz_actual_raw'])

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()

		self.assertEqual('ARMv7 Processor rev 3 (v7l)', info['brand'])
		self.assertEqual('1.4000 GHz', info['hz_advertised'])
		self.assertEqual('1.4000 GHz', info['hz_actual'])
		self.assertEqual((1400000000, 0), info['hz_advertised_raw'])
		self.assertEqual((1400000000, 0), info['hz_actual_raw'])

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('ARMv7 Processor rev 3 (v7l)', info['brand'])
		self.assertEqual('ODROID-XU3', info['hardware'])

		self.assertEqual(
			['edsp', 'fastmult', 'half', 'idiva', 'idivt', 'neon', 'swp',
			'thumb', 'tls', 'vfp', 'vfpv3', 'vfpv4' ],
			info['flags']
		)

	def test_all(self):
		info = cpuinfo.get_cpu_info()

		self.assertEqual('ARMv7 Processor rev 3 (v7l)', info['brand'])
		self.assertEqual('ODROID-XU3', info['hardware'])
		self.assertEqual('1.4000 GHz', info['hz_advertised'])
		self.assertEqual('1.4000 GHz', info['hz_actual'])
		self.assertEqual((1400000000, 0), info['hz_advertised_raw'])
		self.assertEqual((1400000000, 0), info['hz_actual_raw'])
		self.assertEqual('ARM_7', info['arch'])
		self.assertEqual(32, info['bits'])
		self.assertEqual(8, info['count'])

		self.assertEqual('armv7l', info['raw_arch_string'])

		self.assertEqual(
			['edsp', 'fastmult', 'half', 'idiva', 'idivt', 'neon', 'swp',
			'thumb', 'tls', 'vfp', 'vfpv3', 'vfpv4' ],
			info['flags']
		)
