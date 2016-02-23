

import unittest
import cpuinfo
import helpers


class DataSource(object):
	bits = '32bit'
	cpu_count = 1
	is_windows = False
	raw_arch_string = 'unknown_cpu'


class TestInvalidCPU(unittest.TestCase):
	def test_arch_parse_unknown(self):
		# If the arch is unknown, the result should be null
		arch, bits = cpuinfo.parse_arch(DataSource.raw_arch_string)
		self.assertEqual(None, arch)
		self.assertEqual(None, bits)

	def test_check_arch_exception(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)

		# If the arch is unknown, it should raise and exception
		try:
			cpuinfo.cpuinfo._check_arch()
			self.fail('Failed to raise Exception')
		except Exception as err:
			self.assertEqual('py-cpuinfo currently only works on X86 and some ARM CPUs.', err.args[0])
