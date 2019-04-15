

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 4
	is_windows = False
	arch_string_raw = 'aarch64'
	uname_string_raw = 'x86_64'
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
BogoMIPS	: 2.00
Features	: fp asimd crc32
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 4

processor	: 1
BogoMIPS	: 2.00
Features	: fp asimd crc32
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 4

processor	: 2
BogoMIPS	: 2.00
Features	: fp asimd crc32
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 4

processor	: 3
BogoMIPS	: 2.00
Features	: fp asimd crc32
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 4

Hardware	: ODROID-C2
Revision	: 020c


'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = '''
Architecture:          aarch64
Byte Order:            Little Endian
CPU(s):                4
On-line CPU(s) list:   0-3
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             4
CPU max MHz:           1536.0000
CPU min MHz:           100.0000
'''
		return returncode, output

	@staticmethod
	def cpufreq_info():
		returncode = 0
		output = '''
cpufrequtils 008: cpufreq-info (C) Dominik Brodowski 2004-2009
Report errors and bugs to cpufreq@vger.kernel.org, please.
analyzing CPU 0:
  driver: meson_cpufreq
  CPUs which run at the same hardware frequency: 0 1 2 3
  CPUs which need to have their frequency coordinated by software: 0 1 2 3
  maximum transition latency: 200 us.
  hardware limits: 100.0 MHz - 1.54 GHz
  available frequency steps: 100.0 MHz, 250 MHz, 500 MHz, 1000 MHz, 1.30 GHz, 1.54 GHz
  available cpufreq governors: hotplug, interactive, conservative, ondemand, userspace, powersave, performance
  current policy: frequency should be within 100.0 MHz and 1.54 GHz.
                  The governor "interactive" may decide which speed to use
                  within this range.
  current CPU frequency is 1.54 GHz.
  cpufreq stats: 100.0 MHz:0.00%, 250 MHz:0.00%, 500 MHz:0.00%, 1000 MHz:0.00%, 1.30 GHz:0.00%, 1.54 GHz:100.00%  (439)
analyzing CPU 1:
  driver: meson_cpufreq
  CPUs which run at the same hardware frequency: 0 1 2 3
  CPUs which need to have their frequency coordinated by software: 0 1 2 3
  maximum transition latency: 200 us.
  hardware limits: 100.0 MHz - 1.54 GHz
  available frequency steps: 100.0 MHz, 250 MHz, 500 MHz, 1000 MHz, 1.30 GHz, 1.54 GHz
  available cpufreq governors: hotplug, interactive, conservative, ondemand, userspace, powersave, performance
  current policy: frequency should be within 100.0 MHz and 1.54 GHz.
                  The governor "interactive" may decide which speed to use
                  within this range.
  current CPU frequency is 1.54 GHz.
  cpufreq stats: 100.0 MHz:0.00%, 250 MHz:0.00%, 500 MHz:0.00%, 1000 MHz:0.00%, 1.30 GHz:0.00%, 1.54 GHz:100.00%  (439)
analyzing CPU 2:
  driver: meson_cpufreq
  CPUs which run at the same hardware frequency: 0 1 2 3
  CPUs which need to have their frequency coordinated by software: 0 1 2 3
  maximum transition latency: 200 us.
  hardware limits: 100.0 MHz - 1.54 GHz
  available frequency steps: 100.0 MHz, 250 MHz, 500 MHz, 1000 MHz, 1.30 GHz, 1.54 GHz
  available cpufreq governors: hotplug, interactive, conservative, ondemand, userspace, powersave, performance
  current policy: frequency should be within 100.0 MHz and 1.54 GHz.
                  The governor "interactive" may decide which speed to use
                  within this range.
  current CPU frequency is 1.54 GHz.
  cpufreq stats: 100.0 MHz:0.00%, 250 MHz:0.00%, 500 MHz:0.00%, 1000 MHz:0.00%, 1.30 GHz:0.00%, 1.54 GHz:100.00%  (439)
analyzing CPU 3:
  driver: meson_cpufreq
  CPUs which run at the same hardware frequency: 0 1 2 3
  CPUs which need to have their frequency coordinated by software: 0 1 2 3
  maximum transition latency: 200 us.
  hardware limits: 100.0 MHz - 1.54 GHz
  available frequency steps: 100.0 MHz, 250 MHz, 500 MHz, 1000 MHz, 1.30 GHz, 1.54 GHz
  available cpufreq governors: hotplug, interactive, conservative, ondemand, userspace, powersave, performance
  current policy: frequency should be within 100.0 MHz and 1.54 GHz.
                  The governor "interactive" may decide which speed to use
                  within this range.
  current CPU frequency is 1.54 GHz.
  cpufreq stats: 100.0 MHz:0.00%, 250 MHz:0.00%, 500 MHz:0.00%, 1000 MHz:0.00%, 1.30 GHz:0.00%, 1.54 GHz:100.00%  (439)

'''
		return returncode, output


class TestLinux_Odroid_C2_Aarch_64(unittest.TestCase):
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
		self.assertEqual(4, len(cpuinfo._get_cpu_info_from_lscpu()))
		self.assertEqual(2, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(13, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_cpufreq_info(self):
		info = cpuinfo._get_cpu_info_from_cpufreq_info()

		self.assertEqual('1.5400 GHz', info['hz_advertised_friendly'])
		self.assertEqual('1.5400 GHz', info['hz_actual_friendly'])
		self.assertEqual((1540000000, 0), info['hz_advertised'])
		self.assertEqual((1540000000, 0), info['hz_actual'])

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()

		self.assertEqual('1.5360 GHz', info['hz_advertised_friendly'])
		self.assertEqual('1.5360 GHz', info['hz_actual_friendly'])
		self.assertEqual((1536000000, 0), info['hz_advertised'])
		self.assertEqual((1536000000, 0), info['hz_actual'])

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('ODROID-C2', info['hardware_raw'])

		self.assertEqual(
			['asimd', 'crc32', 'fp'],
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('ODROID-C2', info['hardware_raw'])
		self.assertEqual('1.5400 GHz', info['hz_advertised_friendly'])
		self.assertEqual('1.5400 GHz', info['hz_actual_friendly'])
		self.assertEqual((1540000000, 0), info['hz_advertised'])
		self.assertEqual((1540000000, 0), info['hz_actual'])
		self.assertEqual('ARM_8', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])

		self.assertEqual('aarch64', info['arch_string_raw'])

		self.assertEqual(
			['asimd', 'crc32', 'fp'],
			info['flags']
		)
