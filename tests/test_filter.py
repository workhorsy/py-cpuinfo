

import unittest
from cpuinfo import *
import helpers


class TestFilter(unittest.TestCase):
	def test_filter(self):
		# Make sure NON empty values DON'T get filtered out
		for x in [2, "abc", ("one"), {"key" : "val"}, [9, 8, 7]]:
			info = { 'example' : x }
			info = cpuinfo._filter_dict_keys_with_empty_values(info)
			self.assertEqual(info, { 'example' : x })

		# Make sure empty values get filtered out
		for x in [None, 0, -1, "", (), {}, [], (0, 0), "0.0"]:
			info = { 'example' : x }
			info = cpuinfo._filter_dict_keys_with_empty_values(info)
			self.assertEqual(info, {})

		# Make sure 0 values get filtered out
		info = { 'aaa':1, 'bbb':0, 'ccc':2 }
		info = cpuinfo._filter_dict_keys_with_empty_values(info)
		self.assertEqual(info, { 'aaa':1, 'ccc':2 })

		# Make sure 0 values dont get filtered out with 0 as acceptable value
		info = { 'aaa':1, 'bbb':0, 'ccc':2 }
		info = cpuinfo._filter_dict_keys_with_empty_values(info, { 'bbb' : 0 })
		self.assertEqual(info, { 'aaa':1, 'bbb':0, 'ccc':2 })
