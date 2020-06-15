

import unittest
from cpuinfo import *
import helpers


class TestCompileErrors(unittest.TestCase):
	def test_all(self):
		self.maxDiff = None

		import os
		from subprocess import Popen, PIPE

		# Find all the python files
		py_files = []
		for root, dirs, files in os.walk("."):
			for file in files:
					if file.lower().endswith(".py"):
						py_files.append(os.path.join(root, file).lstrip(".\\").lstrip('/'))


		# Compile the files and check for errors
		command = sys.executable + " -Wall -m py_compile " + ' '.join(py_files)
		p1 = Popen(command.split(' '), stdout=PIPE, stderr=PIPE, stdin=PIPE)
		p1_stdout, p1_stderr = p1.communicate()

		if not cpuinfo.IS_PY2:
			p1_stdout = p1_stdout.decode(encoding='UTF-8')

		if not cpuinfo.IS_PY2:
			p1_stderr = p1_stderr.decode(encoding='UTF-8')

		# Check for no errors
		self.assertEqual("", p1_stderr)
		self.assertEqual("", p1_stdout)
		self.assertEqual(0, p1.returncode)
