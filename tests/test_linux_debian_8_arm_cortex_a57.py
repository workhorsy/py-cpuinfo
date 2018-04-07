
# FIXME: This is just a test branch to work on tests for more ARM CPUs

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '32bit'
	cpu_count = 4
	is_windows = False
	raw_arch_string = 'armv7l'
	can_cpuid = False

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = '''
processor : 7
BogoMIPS : 500.00
Features : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
CPU implementer : 0x41
CPU architecture: 8
CPU variant : 0x1
CPU part : 0xd07
CPU revision : 2


'''
		return returncode, output



class TestLinuxDebian_8_arm_cortex_a57(unittest.TestCase):
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
		self.assertEqual(11, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(17, len(cpuinfo.get_cpu_info()))

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

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
			['aes', 'asimd', 'cpuid', 'crc32', 'evtstrm', 'fp',
			'pmull', 'sha1', 'sha2'],
			info['flags']
		)

	def test_all(self):
		info = cpuinfo.get_cpu_info()

		if "logger" in dir(unittest): unittest.logger("FIXME: Add other data sources")

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
			['aes', 'asimd', 'cpuid', 'crc32', 'evtstrm', 'fp',
			'pmull', 'sha1', 'sha2'],
			info['flags']
		)
