

import unittest
from cpuinfo import *
import helpers


class MockDataSource_enforcing(object):
	@staticmethod
	def has_sestatus():
		return True

	@staticmethod
	def sestatus_b():
		returncode = 0
		output = '''
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      31
'''
		return returncode, output

class MockDataSource_not_enforcing(object):
	@staticmethod
	def has_sestatus():
		return True

	@staticmethod
	def sestatus_b():
		returncode = 0
		output = '''
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   eating
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      31
'''
		return returncode, output

class MockDataSource_exec_mem_and_heap(object):
	@staticmethod
	def has_sestatus():
		return True

	@staticmethod
	def sestatus_b():
		returncode = 0
		output = '''
allow_execheap                  on
allow_execmem                   on
'''
		return returncode, output

class MockDataSource_no_exec_mem_and_heap(object):
	@staticmethod
	def has_sestatus():
		return True

	@staticmethod
	def sestatus_b():
		returncode = 0
		output = '''
allow_execheap                  off
allow_execmem                   off
'''
		return returncode, output


class TestSELinux(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	def test_enforcing(self):
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource_enforcing)
		self.assertEqual(True, cpuinfo._is_selinux_enforcing())

	def test_not_enforcing(self):
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource_not_enforcing)
		self.assertEqual(False, cpuinfo._is_selinux_enforcing())

	def test_exec_mem_and_heap(self):
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource_exec_mem_and_heap)
		self.assertEqual(False, cpuinfo._is_selinux_enforcing())

	def test_no_exec_mem_and_heap(self):
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource_no_exec_mem_and_heap)
		self.assertEqual(True, cpuinfo._is_selinux_enforcing())
