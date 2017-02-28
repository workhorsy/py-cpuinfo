

import unittest
from cpuinfo import *
import helpers



class TestActual(unittest.TestCase):
	def setUp(self):
		helpers.restore_data_source(cpuinfo)

	def test_all(self):
		os_type = helpers.get_os_type()

		if os_type == 'BeOS':
			self.assertEqual(None, cpuinfo._get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertIsNotNone(cpuinfo._get_cpu_info_from_sysinfo())
			self.assertIsNotNone(cpuinfo._get_cpu_info_from_cpuid())
			self.assertIsNotNone(cpuinfo.get_cpu_info())
		elif os_type == 'BSD':
			self.assertEqual(None, cpuinfo._get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_kstat())
			self.assertIsNotNone(cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_sysinfo())
			# FIXME: This fails by segfaulting for some reason
			self.assertEqual(None, cpuinfo._get_cpu_info_from_cpuid())
			self.assertIsNotNone(cpuinfo.get_cpu_info())
		elif os_type == 'Cygwin':
			self.assertEqual(None, cpuinfo._get_cpu_info_from_registry())
			self.assertIsNotNone(cpuinfo._get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_sysinfo())
			# FIXME: This fails by segfaulting for some reason
			self.assertEqual(None, cpuinfo._get_cpu_info_from_cpuid())
			self.assertIsNotNone(cpuinfo.get_cpu_info())
		elif os_type == 'MacOS':
			self.assertEqual(None, cpuinfo._get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_proc_cpuinfo())
			self.assertIsNotNone(cpuinfo._get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_sysinfo())
			# FIXME: This fails by segfaulting for some reason
			self.assertEqual(None, cpuinfo._get_cpu_info_from_cpuid())
			self.assertIsNotNone(cpuinfo.get_cpu_info())
		elif os_type == 'Linux':
			self.assertEqual(None, cpuinfo._get_cpu_info_from_registry())
			self.assertIsNotNone(cpuinfo._get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_sysinfo())
			self.assertIsNotNone(cpuinfo._get_cpu_info_from_cpuid())
			self.assertIsNotNone(cpuinfo.get_cpu_info())
		elif os_type == 'Solaris':
			self.assertEqual(None, cpuinfo._get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_sysctl())
			self.assertIsNotNone(cpuinfo._get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_sysinfo())
			# FIXME: This fails by segfaulting for some reason
			self.assertEqual(None, cpuinfo._get_cpu_info_from_cpuid())
			self.assertIsNotNone(cpuinfo.get_cpu_info())
		elif os_type == 'Windows':
			self.assertIsNotNone(cpuinfo._get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertEqual(None, cpuinfo._get_cpu_info_from_sysinfo())
			self.assertIsNotNone(cpuinfo._get_cpu_info_from_cpuid())
			self.assertIsNotNone(cpuinfo.get_cpu_info())
		else:
			raise AssertionError('Unexpected OS type "{0}".'.format(os_type))
