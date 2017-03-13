

import unittest
from cpuinfo import *
import helpers


class TestActual(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)
		#helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	def test_all(self):
		os_type = helpers.get_os_type()

		if os_type == 'BeOS':
			self.assertEqual(None, cpuinfo.get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())
			self.assertNotEqual({}, cpuinfo.get_cpu_info_from_sysinfo())
			#self.assertNotEqual({}, cpuinfo.get_cpu_info_from_cpuid())
			self.assertNotEqual({}, cpuinfo.get_cpu_info())
		elif os_type == 'BSD':
			self.assertEqual(None, cpuinfo.get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())
			self.assertNotEqual({}, cpuinfo.get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysinfo())
			# FIXME: This fails by segfaulting for some reason
			#self.assertEqual(None, cpuinfo.get_cpu_info_from_cpuid())
			self.assertNotEqual({}, cpuinfo.get_cpu_info())
		elif os_type == 'Cygwin':
			self.assertEqual(None, cpuinfo.get_cpu_info_from_registry())
			self.assertNotEqual({}, cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysinfo())
			# FIXME: This fails by segfaulting for some reason
			#self.assertEqual(None, cpuinfo.get_cpu_info_from_cpuid())
			self.assertNotEqual({}, cpuinfo.get_cpu_info())
		elif os_type == 'MacOS':
			self.assertEqual(None, cpuinfo.get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertNotEqual({}, cpuinfo.get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysinfo())
			# FIXME: This fails by segfaulting for some reason
			#self.assertEqual(None, cpuinfo.get_cpu_info_from_cpuid())
			self.assertNotEqual({}, cpuinfo.get_cpu_info())
		elif os_type == 'Linux':
			self.assertEqual(None, cpuinfo.get_cpu_info_from_registry())
			self.assertNotEqual({}, cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysinfo())
			#self.assertNotEqual({}, cpuinfo.get_cpu_info_from_cpuid())
			self.assertNotEqual({}, cpuinfo.get_cpu_info())
		elif os_type == 'Solaris':
			self.assertEqual(None, cpuinfo.get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())
			self.assertNotEqual({}, cpuinfo.get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysinfo())
			# FIXME: This fails by segfaulting for some reason
			#self.assertEqual(None, cpuinfo.get_cpu_info_from_cpuid())
			self.assertNotEqual({}, cpuinfo.get_cpu_info())
		elif os_type == 'Windows':
			self.assertNotEqual({}, cpuinfo.get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysinfo())
			#self.assertNotEqual({}, cpuinfo.get_cpu_info_from_cpuid())
			self.assertNotEqual({}, cpuinfo.get_cpu_info())
		else:
			raise AssertionError('Unexpected OS type "{0}".'.format(os_type))

		self.assertEqual(True, True)
