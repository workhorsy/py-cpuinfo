

import unittest
from cpuinfo import *
import helpers



class TestParseCPUString(unittest.TestCase):
	'''
	def test_parse_cpu_string(self):
		processor_brand, hz_actual, scale, vendor_id, stepping, model, family = \
		cpuinfo._parse_cpu_string("Intel(R) Pentium(R) CPU G640 @ 2.80GHz (fam: 06, model: 2a, stepping: 07)")
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', processor_brand)
		self.assertEqual('2.8', hz_actual)
		self.assertEqual(9, scale)
		self.assertEqual(None, vendor_id)
		self.assertEqual(7, stepping)
		self.assertEqual(42, model)
		self.assertEqual(6, family)

		processor_brand, hz_actual, scale, vendor_id, stepping, model, family = \
		cpuinfo._parse_cpu_string("Intel(R) Pentium(R) CPU G640 @ 2.80GHz (family: 0x6, model: 0x2a, stepping: 0x7)")
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', processor_brand)
		self.assertEqual('2.8', hz_actual)
		self.assertEqual(9, scale)
		self.assertEqual(None, vendor_id)
		self.assertEqual(7, stepping)
		self.assertEqual(42, model)
		self.assertEqual(6, family)

		processor_brand, hz_actual, scale, vendor_id, stepping, model, family = \
		cpuinfo._parse_cpu_string("Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz")
		self.assertEqual("Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz", processor_brand)
		self.assertEqual('2.93', hz_actual)
		self.assertEqual(9, scale)
		self.assertEqual(None, vendor_id)
		self.assertEqual(None, stepping)
		self.assertEqual(None, model)
		self.assertEqual(None, family)

		processor_brand, hz_actual, scale, vendor_id, stepping, model, family = \
		cpuinfo._parse_cpu_string("Intel(R) Pentium(R) CPU G640 @ 2.80GHz (2793.73-MHz K8-class CPU)")
		self.assertEqual("Intel(R) Pentium(R) CPU G640 @ 2.80GHz", processor_brand)
		self.assertEqual('2.8', hz_actual)
		self.assertEqual(9, scale)
		self.assertEqual(None, vendor_id)
		self.assertEqual(None, stepping)
		self.assertEqual(None, model)
		self.assertEqual(None, family)

		# NOTE: No @ symbol
		processor_brand, hz_actual, scale, vendor_id, stepping, model, family = \
		cpuinfo._parse_cpu_string("Intel(R) Pentium(R) D CPU 3.20GHz")
		self.assertEqual("Intel(R) Pentium(R) D CPU 3.20GHz", processor_brand)
		self.assertEqual('3.2', hz_actual)
		self.assertEqual(9, scale)
		self.assertEqual(None, vendor_id)
		self.assertEqual(None, stepping)
		self.assertEqual(None, model)
		self.assertEqual(None, family)

		# NOTE: No @ symbol or Hz
		# FIXME: change cpu string to "AMD Ryzen 7 2700X Eight-Core Processor          (3693.15-MHz K8-class CPU)")
		# FIXME: Parsing this CPU brand string fails, because it is missing the @ and includes the Hz in quotes
		processor_brand, hz_actual, scale, vendor_id, stepping, model, family = \
		cpuinfo._parse_cpu_string("AMD Ryzen 7 2700X Eight-Core Processor          (3693.15-MHz K8-class CPU) (fam: 06, model: 2a, stepping: 07)")
		self.assertEqual("AMD Ryzen 7 2700X Eight-Core Processor", processor_brand)
		self.assertEqual('3.693', hz_actual)
		self.assertEqual(9, scale)
		self.assertEqual(None, vendor_id)
		self.assertEqual(None, stepping)
		self.assertEqual(None, model)
		self.assertEqual(None, family)
	'''
	'''
	def test_to_friendly_hz(self):
		scale, hz_brand = cpuinfo._get_hz_string_from_brand('Intel(R) Pentium(R) CPU G640 @ 2.80GHz')
		self.assertEqual(9, scale)
		self.assertEqual('2.8', hz_brand)
		self.assertEqual('2.8000 GHz', cpuinfo._to_friendly_hz(hz_brand, scale))

		scale, hz_brand = cpuinfo._get_hz_string_from_brand('Intel(R) Pentium(R) CPU @ 1.20MHz')
		self.assertEqual(6, scale)
		self.assertEqual('1.2', hz_brand)
		self.assertEqual('1.2000 MHz', cpuinfo._to_friendly_hz(hz_brand, scale))

		# NOTE: No @ symbol
		scale, hz_brand = cpuinfo._get_hz_string_from_brand('Intel(R) Pentium(R) D CPU 3.20GHz')
		self.assertEqual(9, scale)
		self.assertEqual('3.2', hz_brand)
		self.assertEqual('3.2000 GHz', cpuinfo._to_friendly_hz(hz_brand, scale))

		# NOTE: No @ symbol or Hz
		scale, hz_brand = cpuinfo._get_hz_string_from_brand('AMD Ryzen 7 2700X Eight-Core Processor')
		self.assertEqual(1, scale)
		self.assertEqual('0.0', hz_brand)
		self.assertEqual('0.0000 Hz', cpuinfo._to_friendly_hz(hz_brand, scale))

	def test_to_raw_hz(self):
		scale, hz_brand = cpuinfo._get_hz_string_from_brand('Intel(R) Pentium(R) CPU G640 @ 2.80GHz')
		self.assertEqual(9, scale)
		self.assertEqual('2.8', hz_brand)
		self.assertEqual((2800000000, 0), cpuinfo._to_raw_hz(hz_brand, scale))

		scale, hz_brand = cpuinfo._get_hz_string_from_brand('Intel(R) Pentium(R) CPU @ 1.20MHz')
		self.assertEqual(6, scale)
		self.assertEqual('1.2', hz_brand)
		self.assertEqual((1200000, 0), cpuinfo._to_raw_hz(hz_brand, scale))

		# NOTE: No @ symbol
		scale, hz_brand = cpuinfo._get_hz_string_from_brand('Intel(R) Pentium(R) D CPU 3.20GHz')
		self.assertEqual(9, scale)
		self.assertEqual('3.2', hz_brand)
		self.assertEqual((3200000000, 0), cpuinfo._to_raw_hz(hz_brand, scale))

		# NOTE: No @ symbol or Hz
		scale, hz_brand = cpuinfo._get_hz_string_from_brand('AMD Ryzen 7 2700X Eight-Core Processor')
		self.assertEqual(1, scale)
		self.assertEqual('0.0', hz_brand)
		self.assertEqual((0, 0), cpuinfo._to_raw_hz(hz_brand, scale))
	'''

	def test_to_hz_string(self):
		self.assertEqual('2.8', cpuinfo._to_hz_string('2.80'))
		self.assertEqual('2.0', cpuinfo._to_hz_string('2'))
		self.assertEqual('3.0', cpuinfo._to_hz_string(3))
		self.assertEqual('6.5', cpuinfo._to_hz_string(6.5))
		self.assertEqual('7.002', cpuinfo._to_hz_string(7.002))
		self.assertEqual('4.0000000000001', cpuinfo._to_hz_string('4.0000000000001'))
		self.assertEqual('5.0', cpuinfo._to_hz_string('5.000000000000'))

	def test_parse_hz(self):
		'''
		scale, hz = cpuinfo._parse_hz(None)
		self.assertEqual((1, '0.0'), (scale, hz))

		scale, hz = cpuinfo._parse_hz('')
		self.assertEqual((1, '0.0'), (scale, hz))

		scale, hz = cpuinfo._parse_hz('8.778.9')
		self.assertEqual((1, '0.0'), (scale, hz))
		'''
		scale, hz = cpuinfo._parse_hz('2.80GHz')
		self.assertEqual((9, '2.8000'), (scale, hz))

		scale, hz = cpuinfo._parse_hz('1.20 mHz')
		self.assertEqual((6, '1.2000'), (scale, hz))

		scale, hz = cpuinfo._parse_hz('3693.15-MHz')
		self.assertEqual((9, '3.6931'), (scale, hz))

		scale, hz = cpuinfo._parse_hz('12 GHz')
		self.assertEqual((9, '12.0000'), (scale, hz))
