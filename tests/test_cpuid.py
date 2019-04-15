

import unittest
from cpuinfo import *
import helpers



class MockDataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	arch_string_raw = 'INVALID'
	uname_string_raw = 'INVALID'
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

	def test_normal(self):
		cpuid = CPUID()
		#if cpuid.is_selinux_enforcing:
		#	queue.put(_obj_to_b64({}))
		#	return

		# Get the cpu info from the CPUID register
		max_extension_support = cpuid.get_max_extension_support()
		print('max_extension_support', max_extension_support)

		cache_info = cpuid.get_cache(max_extension_support)
		print('cache_info', cache_info)

		info = cpuid.get_info()
		print('info', info)

		processor_brand = cpuid.get_processor_brand(max_extension_support)
		print('processor_brand', processor_brand)

		hz_actual = cpuid.get_raw_hz()
		print('hz_actual', hz_actual)

		vendor_id = cpuid.get_vendor_id()
		print('vendor_id', vendor_id)

		flags = cpuid.get_flags(max_extension_support)
		print('flags', flags)
