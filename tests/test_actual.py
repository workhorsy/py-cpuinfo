

import unittest
import cpuinfo
import helpers
import platform


def get_os_type():
	os_type = 'Unknown'

	# Figure out the general OS type
	uname = platform.system().strip().strip('"').strip("'").strip().lower()
	if 'beos' in uname or 'haiku' in uname:
		os_type = 'BeOS'
	elif 'bsd' in uname or 'gnu/kfreebsd' in uname:
		os_type = 'BSD'
	elif 'cygwin' in uname:
		os_type = 'Cygwin'
	elif 'darwin' in uname:
		os_type = 'MacOS'
	elif 'linux' in uname:
		os_type = 'Linux'
	elif 'solaris' in uname or 'sunos' in uname:
		os_type = 'Solaris'
	elif 'windows' in uname:
		os_type = 'Windows'

	return os_type

class TestHasResult(object):
	def assertHasResult(self, result):
		'''
		Fails if the result is None or an empty Dict
		'''
		if not result:
			raise AssertionError('Expected result, but there was none.')

class TestActual(unittest.TestCase, TestHasResult):
	def test_all(self):
		os_type = get_os_type()

		if os_type == 'BeOS':
			self.assertEqual(None, cpuinfo.get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())
			self.assertHasResult(cpuinfo.get_cpu_info_from_sysinfo())
			self.assertHasResult(cpuinfo.get_cpu_info_from_cpuid())
			self.assertNotEqual(None, cpuinfo.get_cpu_info())
		elif os_type == 'BSD':
			self.assertEqual(None, cpuinfo.get_cpu_info_from_registry())
			self.assertHasResult(cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())
			self.assertHasResult(cpuinfo.get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysinfo())
			self.assertHasResult(cpuinfo.get_cpu_info_from_cpuid())
			self.assertNotEqual(None, cpuinfo.get_cpu_info())
		elif os_type == 'Linux':
			self.assertEqual(None, cpuinfo.get_cpu_info_from_registry())
			self.assertHasResult(cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysinfo())
			self.assertHasResult(cpuinfo.get_cpu_info_from_cpuid())
			self.assertNotEqual(None, cpuinfo.get_cpu_info())
		elif os_type == 'Solaris':
			self.assertEqual(None, cpuinfo.get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())
			self.assertHasResult(cpuinfo.get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysinfo())
			self.assertHasResult(cpuinfo.get_cpu_info_from_cpuid())
			self.assertNotEqual(None, cpuinfo.get_cpu_info())
		elif os_type == 'Windows':
			self.assertHasResult(cpuinfo.get_cpu_info_from_registry())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysinfo())
			self.assertHasResult(cpuinfo.get_cpu_info_from_cpuid())
			self.assertNotEqual(None, cpuinfo.get_cpu_info())
		else:
			raise AssertionError('Unexpected OS type "{0}".'.format(os_type))

		self.assertEqual(True, True)
