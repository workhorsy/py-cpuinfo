

import unittest
from cpuinfo import *
import helpers




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

	def test_hz_short_to_raw(self):
		self.assertEqual((2800000000, 0), cpuinfo._hz_short_to_raw('2.8', 9))
		self.assertEqual((1200000, 0), cpuinfo._hz_short_to_raw('1.2', 6))
		self.assertEqual((3200000000, 0), cpuinfo._hz_short_to_raw('3.2', 9))
		self.assertEqual((9001200000, 0), cpuinfo._hz_short_to_raw('9001.2', 6))
		self.assertEqual((0, 0), cpuinfo._hz_short_to_raw('0.0', 0))
		self.assertEqual((2, 87), cpuinfo._hz_short_to_raw('2.87', 0))

		self.assertEqual((0, 0), cpuinfo._hz_short_to_raw('invalid', 0))
		self.assertEqual((0, 0), cpuinfo._hz_short_to_raw('8.778.9', 0))
		self.assertEqual((0, 0), cpuinfo._hz_short_to_raw('', 0))
		self.assertEqual((0, 0), cpuinfo._hz_short_to_raw(None, 0))

	def test_hz_friendly_to_raw(self):
		self.assertEqual((2800000000, 0), cpuinfo._hz_friendly_to_raw('2.80GHz'))
		self.assertEqual((1200000, 0), cpuinfo._hz_friendly_to_raw('1.20 mHz'))
		self.assertEqual((3693150000, 0), cpuinfo._hz_friendly_to_raw('3693.15-MHz'))
		self.assertEqual((12000000000, 0), cpuinfo._hz_friendly_to_raw('12 GHz'))
		self.assertEqual((2, 6), cpuinfo._hz_friendly_to_raw('2.6 Hz'))
		self.assertEqual((0, 0), cpuinfo._hz_friendly_to_raw('0 Hz'))

		self.assertEqual((0, 0), cpuinfo._hz_friendly_to_raw('invalid'))
		self.assertEqual((0, 0), cpuinfo._hz_friendly_to_raw('8.778.9'))
		self.assertEqual((0, 0), cpuinfo._hz_friendly_to_raw(''))
		self.assertEqual((0, 0), cpuinfo._hz_friendly_to_raw(None))

	def test_hz_short_to_friendly(self):
		self.assertEqual('2.8000 GHz', cpuinfo._hz_short_to_friendly('2.8', 9))
		self.assertEqual('1.2000 MHz', cpuinfo._hz_short_to_friendly('1.2', 6))
		self.assertEqual('3.2000 GHz', cpuinfo._hz_short_to_friendly('3.2', 9))
		self.assertEqual('1.3000 Hz', cpuinfo._hz_short_to_friendly('1.3', 0))
		self.assertEqual('0.0000 Hz', cpuinfo._hz_short_to_friendly('0.0', 0))

		self.assertEqual('0.0000 Hz', cpuinfo._hz_short_to_friendly('invalid', 0))
		self.assertEqual('0.0000 Hz', cpuinfo._hz_short_to_friendly('8.778.9', 0))
		self.assertEqual('0.0000 Hz', cpuinfo._hz_short_to_friendly('', 0))
		self.assertEqual('0.0000 Hz', cpuinfo._hz_short_to_friendly(None, 0))

	def test_parse_cpu_brand_string(self):
		hz, scale = cpuinfo._parse_cpu_brand_string('Intel(R) Pentium(R) CPU G640 @ 2.80GHz')
		self.assertEqual((hz, scale), ('2.8', 9))

		hz, scale = cpuinfo._parse_cpu_brand_string('Intel(R) Pentium(R) CPU @ 1.20MHz')
		self.assertEqual((hz, scale), ('1.2', 6))

		# NOTE: No @ symbol
		hz, scale = cpuinfo._parse_cpu_brand_string('Intel(R) Pentium(R) D CPU 3.20GHz')
		self.assertEqual((hz, scale), ('3.2', 9))

		# NOTE: No @ symbol and no Hz
		hz, scale = cpuinfo._parse_cpu_brand_string('AMD Ryzen 7 2700X Eight-Core Processor')
		self.assertEqual((hz, scale), ('0.0', 0))

	def test_parse_cpu_brand_string_dx(self):
		processor_brand, hz, scale, vendor_id, stepping, model, family = \
		cpuinfo._parse_cpu_brand_string_dx("Intel(R) Pentium(R) CPU G640 @ 2.80GHz (fam: 06, model: 2a, stepping: 07)")
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', processor_brand)
		self.assertEqual((scale, hz), (9, '2.8'))
		self.assertEqual((vendor_id, stepping, model, family), (None, 7, 42, 6))

		processor_brand, hz, scale, vendor_id, stepping, model, family = \
		cpuinfo._parse_cpu_brand_string_dx("Intel(R) Pentium(R) CPU G640 @ 2.80GHz (family: 0x6, model: 0x2a, stepping: 0x7)")
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', processor_brand)
		self.assertEqual((scale, hz), (9, '2.8'))
		self.assertEqual((vendor_id, stepping, model, family), (None, 7, 42, 6))

		processor_brand, hz, scale, vendor_id, stepping, model, family = \
		cpuinfo._parse_cpu_brand_string_dx("Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz")
		self.assertEqual("Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz", processor_brand)
		self.assertEqual((scale, hz), (9, '2.93'))
		self.assertEqual((vendor_id, stepping, model, family), (None, None, None, None))

		processor_brand, hz, scale, vendor_id, stepping, model, family = \
		cpuinfo._parse_cpu_brand_string_dx("Intel(R) Pentium(R) CPU G640 @ 2.80GHz (2793.73-MHz K8-class CPU)")
		self.assertEqual("Intel(R) Pentium(R) CPU G640 @ 2.80GHz", processor_brand)
		self.assertEqual((scale, hz), (9, '2.8'))
		self.assertEqual((vendor_id, stepping, model, family), (None, None, None, None))

		# NOTE: No @ symbol
		processor_brand, hz, scale, vendor_id, stepping, model, family = \
		cpuinfo._parse_cpu_brand_string_dx("Intel(R) Pentium(R) D CPU 3.20GHz")
		self.assertEqual("Intel(R) Pentium(R) D CPU 3.20GHz", processor_brand)
		self.assertEqual((scale, hz), (9, '3.2'))
		self.assertEqual((vendor_id, stepping, model, family), (None, None, None, None))

		# NOTE: No @ symbol and no Hz
		processor_brand, hz, scale, vendor_id, stepping, model, family = \
		cpuinfo._parse_cpu_brand_string_dx("AMD Ryzen 7 2700X Eight-Core Processor          (3693.15-MHz K8-class CPU) (fam: 06, model: 2a, stepping: 07)")
		self.assertEqual("AMD Ryzen 7 2700X Eight-Core Processor", processor_brand)
		self.assertEqual((scale, hz), (6, '3693.15'))
		self.assertEqual((vendor_id, stepping, model, family), (None, 7, 42, 6))
