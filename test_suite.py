

import os, sys
import unittest

# Add the path of all the tests to this path
sys.path.append(os.path.realpath('tests'))



# Import all the test files
from test_example import TestExample
from test_parse_errors import TestParseErrors
from test_invalid_cpu import TestInvalidCPU
from test_debian_8_x86_64 import TestDebian
from test_pcbsd_10_x86_64 import TestPCBSD
from test_osx_13_x86_64 import TestOSX
from test_beagle_bone_arm import TestBeagleBone
from test_raspberry_pi_model_b_arm import TestRaspberryPiModelB
from test_windows_8_x86_64 import TestWindows8
from test_solaris_11_x86_32 import TestSolaris
from test_haiku_x86_32 import TestHaiku
from test_actual import TestActual

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(TestActual))
	suite.addTest(unittest.makeSuite(TestExample))
	suite.addTest(unittest.makeSuite(TestParseErrors))
	suite.addTest(unittest.makeSuite(TestInvalidCPU))
	suite.addTest(unittest.makeSuite(TestDebian))
	suite.addTest(unittest.makeSuite(TestPCBSD))
	suite.addTest(unittest.makeSuite(TestOSX))
	suite.addTest(unittest.makeSuite(TestBeagleBone))
	suite.addTest(unittest.makeSuite(TestRaspberryPiModelB))
	suite.addTest(unittest.makeSuite(TestWindows8))
	suite.addTest(unittest.makeSuite(TestSolaris))
	suite.addTest(unittest.makeSuite(TestHaiku))

	runner = unittest.TextTestRunner()
	runner.run(suite)
