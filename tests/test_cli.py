

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

	def test_trace(self):
		import os
		import re
		from subprocess import Popen, PIPE

		# Get all log files before test
		before_log_files = [f for f in os.listdir('.') if os.path.isfile(f) and re.match(r'^cpuinfo_trace_\d+-\d+-\d+_\d+-\d+-\d+-\d+.trace$', f)]
		#print('\n', before_log_files)

		# Run with trace to generate new log file
		command = [sys.executable, 'cpuinfo/cpuinfo.py', '--trace']
		p1 = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE)
		output = p1.communicate()[0]
		self.assertEqual(0, p1.returncode)

		# Get all log files after test
		after_log_files = [f for f in os.listdir('.') if os.path.isfile(f) and re.match(r'^cpuinfo_trace_\d+-\d+-\d+_\d+-\d+-\d+-\d+.trace$', f)]
		#print('\n', after_log_files)

		# Read the new log file into a string
		new_log_file = list(set(after_log_files) - set(before_log_files))[0]
		with open(new_log_file, 'r') as f:
			output = f.read().strip()

		# Remove the new log file
		os.remove(new_log_file)

		self.assertTrue(len(output) > 200)
		self.assertTrue(output.startswith('!' * 80))
		self.assertTrue(output.endswith('!' * 80))

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
