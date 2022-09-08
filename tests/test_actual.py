

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

	def test_result_patterns(self):
		os_type = helpers.get_os_type()

		if os_type == 'BeOS':
			raise AssertionError('Not implemented')
		elif os_type == 'BSD':
			raise AssertionError('Not implemented')
		elif os_type == 'Cygwin':
			raise AssertionError('Not implemented')
		elif os_type == 'MacOS':
			raise AssertionError('Not implemented')
		elif os_type == 'Linux':
			info = cpuinfo.get_cpu_info()

			assertMatchPattern(self, str, r'^\d.\d.\d$', info["cpuinfo_version_string"])

			assertMatchPattern(self, str, r'^\S+$', info["arch"])
			assertMatchPattern(self, int, r'^\d+$', info["bits"])
			assertMatchPattern(self, int, r'^\d+$', info["count"])

			assertMatchPattern(self, list, None, info["hz_advertised"])
			assertMatchPattern(self, list, None, info["hz_actual"])

			assertMatchPattern(self, int, r'^\d+$', info["l1_data_cache_size"])
			assertMatchPattern(self, int, r'^\d+$', info["l1_instruction_cache_size"])
			assertMatchPattern(self, int, r'^\d+$', info["l2_cache_size"])
			assertMatchPattern(self, int, r'^\d+$', info["l2_cache_line_size"])
			assertMatchPattern(self, int, r'^\d+$', info["l2_cache_associativity"])
			assertMatchPattern(self, int, r'^\d+$', info["l3_cache_size"])

			assertMatchPattern(self, list, None, info["flags"])
		elif os_type == 'Solaris':
			raise AssertionError('Not implemented')
		elif os_type == 'Windows':
			raise AssertionError('Not implemented')
		else:
			raise AssertionError('Unexpected OS type "{0}".'.format(os_type))

def assertMatchPattern(test_case, data_type, pattern, data):
	import re
	test_case.assertEqual(data_type, type(data))
	if pattern:
		text_data = "{0}".format(data)
		test_case.assertIsNotNone(re.fullmatch(pattern, text_data))
