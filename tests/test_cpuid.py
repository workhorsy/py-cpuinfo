

import unittest
from cpuinfo import *
import helpers



class MockDataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	raw_arch_string = 'INVALID'


class TestCPUID(unittest.TestCase):
	def setUp(self):
		helpers.restore_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	# Make sure this returns {} on an invalid arch
	def test_return_empty(self):
		self.assertEqual({}, cpuinfo.get_cpu_info_from_cpuid())
