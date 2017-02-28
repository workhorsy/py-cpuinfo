

import os, sys
import unittest

# Add the path of all the tests to this path
sys.path.append(os.path.realpath('tests'))



# Import all the test files
from test_example import TestExample
from test_parse_errors import TestParseErrors
from test_invalid_cpu import TestInvalidCPU
from test_linux_debian_8_x86_64 import TestLinuxDebian_8_X86_64
from test_linux_aarch64_64 import TestLinuxAarch64
from test_linux_gentoo_2_2_x86_64 import TestLinuxGentoo_2_2_X86_64
from test_beagle_bone_arm import TestBeagleBone
from test_raspberry_pi_model_b_arm import TestRaspberryPiModelB
from test_pcbsd_10_x86_64 import TestPCBSD
from test_osx_13_x86_64 import TestOSX
from test_solaris_11_x86_32 import TestSolaris
from test_haiku_x86_32 import TestHaiku
from test_windows_8_x86_64 import TestWindows8
from test_windows_10_x86_64 import TestWindows10
from test_actual import TestActual

if __name__ == '__main__':
	# Create a backup of DataSource to restore before each test
	from cpuinfo import *
	import helpers
	helpers.backup_data_source(cpuinfo)

	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(TestExample))
	suite.addTest(unittest.makeSuite(TestParseErrors))
	suite.addTest(unittest.makeSuite(TestInvalidCPU))
	suite.addTest(unittest.makeSuite(TestLinuxDebian_8_X86_64))
	suite.addTest(unittest.makeSuite(TestLinuxAarch64))
	suite.addTest(unittest.makeSuite(TestLinuxGentoo_2_2_X86_64))
	suite.addTest(unittest.makeSuite(TestBeagleBone))
	suite.addTest(unittest.makeSuite(TestRaspberryPiModelB))
	suite.addTest(unittest.makeSuite(TestPCBSD))
	suite.addTest(unittest.makeSuite(TestOSX))
	suite.addTest(unittest.makeSuite(TestSolaris))
	suite.addTest(unittest.makeSuite(TestHaiku))
	suite.addTest(unittest.makeSuite(TestWindows8))
	suite.addTest(unittest.makeSuite(TestWindows10))
	suite.addTest(unittest.makeSuite(TestActual))

	runner = unittest.TextTestRunner()
	runner.run(suite)
