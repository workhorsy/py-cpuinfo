

import unittest
from cpuinfo import *
import helpers



class TestCLI(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	def test_json(self):
		from subprocess import Popen, PIPE
		import json

		command = [sys.executable, 'cpuinfo/cpuinfo.py', '--json']
		p1 = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE)
		output = p1.communicate()[0]

		self.assertEqual(0, p1.returncode)

		if not IS_PY2:
			output = output.decode(encoding='UTF-8')

		info = json.loads(output, object_hook = cpuinfo._utf_to_str)

		self.assertEqual(list(cpuinfo.CPUINFO_VERSION), info['cpuinfo_version'])
		self.assertEqual(cpuinfo.CPUINFO_VERSION_STRING, info['cpuinfo_version_string'])

	def test_version(self):
		from subprocess import Popen, PIPE

		command = [sys.executable, 'cpuinfo/cpuinfo.py', '--version']
		p1 = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE)
		output = p1.communicate()[0]

		self.assertEqual(0, p1.returncode)

		if not IS_PY2:
			output = output.decode(encoding='UTF-8')
		output = output.strip()

		self.assertEqual(cpuinfo.CPUINFO_VERSION_STRING, output)

	def test_default(self):
		from subprocess import Popen, PIPE

		command = [sys.executable, 'cpuinfo/cpuinfo.py']
		p1 = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE)
		output = p1.communicate()[0]

		self.assertEqual(0, p1.returncode)

		if not IS_PY2:
			output = output.decode(encoding='UTF-8')

		version = output.split('Cpuinfo Version: ')[1].split('\n')[0].strip()

		self.assertEqual(cpuinfo.CPUINFO_VERSION_STRING, version)
