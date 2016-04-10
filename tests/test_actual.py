

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


class TestActual(unittest.TestCase):
	def test_all(self):
		os_type = get_os_type()

		if os_type == 'Windows':
			self.assertNotEqual(0, len(cpuinfo.get_cpu_info_from_registry()))
			self.assertEqual(None, cpuinfo.get_cpu_info_from_proc_cpuinfo())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())
			self.assertEqual(None, cpuinfo.get_cpu_info_from_sysinfo())
			self.assertNotEqual(0, len(cpuinfo.get_cpu_info_from_cpuid()))
			self.assertNotEqual(None, cpuinfo.get_cpu_info())

		self.assertEqual(True, True)
