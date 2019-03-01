

import unittest
from cpuinfo import *
import helpers



class TestCLI(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	def test_json(self):
		command = [sys.executable, 'cpuinfo/cpuinfo.py', '--json']
		p1 = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output = p1.communicate()[0]

		self.assertEqual(0, p1.returncode)

		info = json.loads(output)

		self.assertEqual(list(cpuinfo.CPUINFO_VERSION), info['cpuinfo_version'])

	def test_default(self):
		command = [sys.executable, 'cpuinfo/cpuinfo.py']
		p1 = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output = p1.communicate()[0]

		self.assertEqual(0, p1.returncode)

		version = output.split('Cpuinfo Version: ')[1].split('\n')[0].strip()

		self.assertEqual(str(cpuinfo.CPUINFO_VERSION), version)
