

import unittest
from cpuinfo import *
import helpers

'''
_to_decimal_string
_to_raw_hz
_parse_hz
_to_friendly_hz
_get_hz_string_from_brand
_parse_cpu_string
'''


class TestParseCPUString(unittest.TestCase):
	def test_to_decimal_string(self):
		self.assertEqual('2.8', cpuinfo._to_decimal_string('2.80'))
		self.assertEqual('2.0', cpuinfo._to_decimal_string('2'))
		self.assertEqual('3.0', cpuinfo._to_decimal_string(3))
		self.assertEqual('6.5', cpuinfo._to_decimal_string(6.5))
		self.assertEqual('7.002', cpuinfo._to_decimal_string(7.002))
		self.assertEqual('4.0000000000001', cpuinfo._to_decimal_string('4.0000000000001'))
		self.assertEqual('5.0', cpuinfo._to_decimal_string('5.000000000000'))

		self.assertEqual('0.0', cpuinfo._to_decimal_string('invalid'))
		self.assertEqual('0.0', cpuinfo._to_decimal_string('8.778.9'))
		self.assertEqual('0.0', cpuinfo._to_decimal_string(''))
		self.assertEqual('0.0', cpuinfo._to_decimal_string(None))

	def test_to_raw_hz(self):
		self.assertEqual((2800000000, 0), cpuinfo._to_raw_hz('2.8', 9))
		self.assertEqual((1200000, 0), cpuinfo._to_raw_hz('1.2', 6))
		self.assertEqual((3200000000, 0), cpuinfo._to_raw_hz('3.2', 9))
		self.assertEqual((0, 0), cpuinfo._to_raw_hz('0.0', 1))

		self.assertEqual((0, 0), cpuinfo._to_raw_hz('invalid', 1))
		self.assertEqual((0, 0), cpuinfo._to_raw_hz('8.778.9', 1))
		self.assertEqual((0, 0), cpuinfo._to_raw_hz('', 1))
		self.assertEqual((0, 0), cpuinfo._to_raw_hz(None, 1))

	def test_parse_hz(self):
		self.assertEqual((0, 2800000000), cpuinfo._parse_hz('2.80GHz'))
		self.assertEqual((0, 1200000), cpuinfo._parse_hz('1.20 mHz'))
		self.assertEqual((0, 3693150000), cpuinfo._parse_hz('3693.15-MHz'))
		self.assertEqual((0, 12000000000), cpuinfo._parse_hz('12 GHz'))

		self.assertEqual((0, 0), cpuinfo._parse_hz('invalid'))
		self.assertEqual((0, 0), cpuinfo._parse_hz('8.778.9'))
		self.assertEqual((0, 0), cpuinfo._parse_hz(''))
		self.assertEqual((0, 0), cpuinfo._parse_hz(None))

	def test_to_friendly_hz(self):
		self.assertEqual('2.8000 GHz', cpuinfo._to_friendly_hz('2.8', 9))
		self.assertEqual('1.2000 MHz', cpuinfo._to_friendly_hz('1.2', 6))
		self.assertEqual('3.2000 GHz', cpuinfo._to_friendly_hz('3.2', 9))
		self.assertEqual('0.0000 Hz', cpuinfo._to_friendly_hz('0.0', 1))

		self.assertEqual('0.0000 Hz', cpuinfo._to_friendly_hz('invalid', 0))
		self.assertEqual('0.0000 Hz', cpuinfo._to_friendly_hz('8.778.9', 0))
		self.assertEqual('0.0000 Hz', cpuinfo._to_friendly_hz('', 0))
		self.assertEqual('0.0000 Hz', cpuinfo._to_friendly_hz(None, 0))

	def test_get_hz_string_from_brand(self):
		pass

	def test_parse_cpu_string(self):
		pass

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

	def test_get_hz_string_from_brand(self):
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
