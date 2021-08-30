

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '32bit'
	cpu_count = 1
	is_windows = False
	arch_string_raw = 'unknown_cpu'
	uname_string_raw = 'unknown_cpu'


class TestInvalidCPU(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	def test_arch_parse_unknown(self):
		# If the arch is unknown, the result should be null
		arch, bits = cpuinfo._parse_arch(DataSource.arch_string_raw)
		self.assertIsNone(arch)
		self.assertIsNone(bits)

	def test_check_arch_exception(self):
		# If the arch is unknown, it should raise and exception
		try:
			cpuinfo._check_arch()
			self.fail('Failed to raise Exception')
		except Exception as err:
			self.assertEqual('py-cpuinfo currently only works on X86 and some ARM/PPC/S390X/MIPS/RISCV CPUs.', err.args[0])
