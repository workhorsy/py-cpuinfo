

import unittest
import cpuinfo
import helpers


class DataSource(object):
	bits = '32bit'
	cpu_count = 1
	is_windows = False
	raw_arch_string = 'armv6l'

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def has_cpufreq_info():
		return False

	@staticmethod
	def has_lscpu():
		return True

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = '''
Processor	: ARMv6-compatible processor rev 7 (v6l)
BogoMIPS	: 697.95
Features	: swp half thumb fastmult vfp edsp java tls
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xb76
CPU revision	: 7

Hardware	: BCM2708
Revision	: 000d
Serial		: 0000000066564a8f


'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = '''
Architecture:          armv6l
Byte Order:            Little Endian
CPU(s):                1
On-line CPU(s) list:   0
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             1
CPU max MHz:           700.0000
CPU min MHz:           700.0000


'''
		return returncode, output

class TestRaspberryPiModelB(unittest.TestCase):
	def test_all(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)

		info = cpuinfo.get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('', info['vendor_id'])
		self.assertEqual('BCM2708', info['hardware'])
		self.assertEqual('ARMv6-compatible processor rev 7 (v6l)', info['brand'])
		self.assertEqual('700.0000 MHz', info['hz_advertised'])
		self.assertEqual('700.0000 MHz', info['hz_actual'])
		self.assertEqual((700000000, 0), info['hz_advertised_raw'])
		self.assertEqual((700000000, 0), info['hz_actual_raw'])
		self.assertEqual('ARM_7', info['arch'])
		self.assertEqual(32, info['bits'])
		self.assertEqual(1, info['count'])

		self.assertEqual('armv6l', info['raw_arch_string'])

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
			['edsp', 'fastmult', 'half', 'java', 'swp', 'thumb', 'tls', 'vfp']
			,
			info['flags']
		)
