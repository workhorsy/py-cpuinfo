

import unittest
from cpuinfo import *
import helpers



class TestParseCPUString(unittest.TestCase):
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

	def test_to_friendly_hz(self):
		scale, hz_brand = cpuinfo._get_hz_string_from_brand('Intel(R) Pentium(R) CPU G640 @ 2.80GHz')
		self.assertEqual(9, scale)
		self.assertEqual('2.8', hz_brand)
		self.assertEqual('2.8000 GHz', to_friendly_hz(hz_brand, scale))

		scale, hz_brand = cpuinfo._get_hz_string_from_brand('Intel(R) Pentium(R) CPU @ 1.20MHz')
		self.assertEqual(6, scale)
		self.assertEqual('1.2', hz_brand)
		self.assertEqual('1.2000 MHz', to_friendly_hz(hz_brand, scale))

		scale, hz_brand = cpuinfo._get_hz_string_from_brand('Intel(R) Pentium(R) D CPU 3.20GHz')
		self.assertEqual(9, scale)
		self.assertEqual('3.2', hz_brand)
		self.assertEqual('3.2000 GHz', to_friendly_hz(hz_brand, scale))

	def test_to_raw_hz(self):
		scale, hz_brand = cpuinfo._get_hz_string_from_brand('Intel(R) Pentium(R) CPU G640 @ 2.80GHz')
		self.assertEqual(9, scale)
		self.assertEqual('2.8', hz_brand)
		self.assertEqual((2800000000, 0), to_raw_hz(hz_brand, scale))

		scale, hz_brand = cpuinfo._get_hz_string_from_brand('Intel(R) Pentium(R) CPU @ 1.20MHz')
		self.assertEqual(6, scale)
		self.assertEqual('1.2', hz_brand)
		self.assertEqual((1200000, 0), to_raw_hz(hz_brand, scale))

		# NOTE: No @ symbol
		scale, hz_brand = cpuinfo._get_hz_string_from_brand('Intel(R) Pentium(R) D CPU 3.20GHz')
		self.assertEqual(9, scale)
		self.assertEqual('3.2', hz_brand)
		self.assertEqual((3200000000, 0), to_raw_hz(hz_brand, scale))
