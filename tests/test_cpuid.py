

import unittest
import cpuinfo
import helpers



class DataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	raw_arch_string = 'INVALID'


class TestCPUID(unittest.TestCase):
	# Make sure this returns {} on an invalid arch
	def test_return_empty(self):
		helpers.monkey_patch_data_source(cpuinfo, DataSource)
		self.assertEqual({}, cpuinfo.get_cpu_info_from_cpuid())
