

import unittest
from cpuinfo import *
import helpers



class MockDataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	raw_arch_string = 'INVALID'
	can_cpuid = True


class TestCPUID(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	# Make sure this returns {} on an invalid arch
	def test_return_empty(self):
		self.assertEqual({}, cpuinfo._get_cpu_info_from_cpuid())
