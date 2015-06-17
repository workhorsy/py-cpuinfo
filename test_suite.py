

import os, sys
import unittest

# Import the unit tests
sys.path.append(os.path.realpath('tests'))

from test_example import TestExample
from test_debian_8_x86_64 import TestDebian
from test_pcbsd_10_x86_64 import TestPCBSD
from test_osx_13_x86_64 import TestOSX
from test_beagle_bone_arm import TestBeagleBone


if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(TestExample))
	suite.addTest(unittest.makeSuite(TestDebian))
	suite.addTest(unittest.makeSuite(TestPCBSD))
	suite.addTest(unittest.makeSuite(TestOSX))
	suite.addTest(unittest.makeSuite(TestBeagleBone))

	runner = unittest.TextTestRunner()
	runner.run(suite)


