

import unittest
from cpuinfo import *
import helpers



class TestActual(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	def test_all(self):
		os_type = helpers.get_os_type()

		if os_type == 'BeOS':
			self.assertEqual({}, cpuinfo._get_cpu_info_from_registry())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cpufreq_info())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_lscpu())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_proc_cpuinfo())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_sysctl())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_kstat())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertTrue(len(cpuinfo._get_cpu_info_from_sysinfo()) > 0)
			#self.assertTrue(len(cpuinfo._get_cpu_info_from_cpuid()) > 0)
			self.assertTrue(len(cpuinfo.get_cpu_info()) > 0)
		elif os_type == 'BSD':
			self.assertEqual({}, cpuinfo._get_cpu_info_from_registry())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cpufreq_info())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_lscpu())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_proc_cpuinfo())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_sysctl())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_kstat())
			self.assertTrue(len(cpuinfo._get_cpu_info_from_dmesg()) > 0)
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_sysinfo())
			# FIXME: This fails by segfaulting for some reason
			#self.assertEqual({}, cpuinfo._get_cpu_info_from_cpuid())
			self.assertTrue(len(cpuinfo.get_cpu_info()) > 0)
		elif os_type == 'Cygwin':
			self.assertEqual({}, cpuinfo._get_cpu_info_from_registry())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cpufreq_info())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_lscpu())
			self.assertTrue(len(cpuinfo._get_cpu_info_from_proc_cpuinfo()) > 0)
			self.assertEqual({}, cpuinfo._get_cpu_info_from_sysctl())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_kstat())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_sysinfo())
			# FIXME: This fails by segfaulting for some reason
			#self.assertEqual({}, cpuinfo._get_cpu_info_from_cpuid())
			self.assertTrue(len(cpuinfo.get_cpu_info()) > 0)
		elif os_type == 'MacOS':
			self.assertEqual({}, cpuinfo._get_cpu_info_from_registry())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cpufreq_info())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_lscpu())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_proc_cpuinfo())
			self.assertTrue(len(cpuinfo._get_cpu_info_from_sysctl()) > 0)
			self.assertEqual({}, cpuinfo._get_cpu_info_from_kstat())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_sysinfo())
			# FIXME: This fails by segfaulting for some reason
			#self.assertEqual({}, cpuinfo._get_cpu_info_from_cpuid())
			self.assertTrue(len(cpuinfo.get_cpu_info()) > 0)
		elif os_type == 'Linux':
			self.assertEqual({}, cpuinfo._get_cpu_info_from_registry())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cpufreq_info())
			#self.assertTrue(len(cpuinfo._get_cpu_info_from_lscpu()) > 0)
			self.assertTrue(len(cpuinfo._get_cpu_info_from_proc_cpuinfo()) > 0)
			self.assertEqual({}, cpuinfo._get_cpu_info_from_sysctl())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_kstat())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_sysinfo())
			#self.assertTrue(len(cpuinfo._get_cpu_info_from_cpuid()) > 0)
			self.assertTrue(len(cpuinfo.get_cpu_info()) > 0)
		elif os_type == 'Solaris':
			self.assertEqual({}, cpuinfo._get_cpu_info_from_registry())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cpufreq_info())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_lscpu())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_proc_cpuinfo())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_sysctl())
			self.assertTrue(len(cpuinfo._get_cpu_info_from_kstat()) > 0)
			self.assertEqual({}, cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_sysinfo())
			# FIXME: This fails by segfaulting for some reason
			#self.assertEqual({}, cpuinfo._get_cpu_info_from_cpuid())
			self.assertTrue(len(cpuinfo.get_cpu_info()) > 0)
		elif os_type == 'Windows':
			self.assertTrue(len(cpuinfo._get_cpu_info_from_registry()) > 0)
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cpufreq_info())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_lscpu())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_proc_cpuinfo())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_sysctl())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_kstat())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_dmesg())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot())
			self.assertEqual({}, cpuinfo._get_cpu_info_from_sysinfo())
			#self.assertTrue(len(cpuinfo._get_cpu_info_from_cpuid()) > 0)
			self.assertTrue(len(cpuinfo.get_cpu_info()) > 0)
		else:
			raise AssertionError('Unexpected OS type "{0}".'.format(os_type))
