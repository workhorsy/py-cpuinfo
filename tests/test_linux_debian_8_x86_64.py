

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	arch_string_raw = 'x86_64'
	uname_string_raw = 'x86_64'
	can_cpuid = False

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = r'''
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 30
model name	: Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz
stepping	: 5
microcode	: 0x616
cpu MHz		: 2928.283
cache size	: 6144 KB
physical id	: 0
siblings	: 4
core id		: 0
cpu cores	: 4
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 5
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl pni ssse3 lahf_lm
bogomips	: 5856.56
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:


'''
		return returncode, output



class TestLinuxDebian_8_X86_64(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	'''
	Make sure calls return the expected number of fields.
	'''
	def test_returns(self):
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_registry()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpufreq_info()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_lscpu()))
		self.assertEqual(12, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(19, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz', info['brand_raw'])
		self.assertEqual('2.9300 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.9283 GHz', info['hz_actual_friendly'])
		self.assertEqual((2930000000, 0), info['hz_advertised'])
		self.assertEqual((2928283000, 0), info['hz_actual'])

		self.assertEqual(6144 * 1024, info['l3_cache_size'])

		self.assertEqual(5, info['stepping'])
		self.assertEqual(30, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['apic', 'clflush', 'cmov', 'constant_tsc', 'cx8', 'de', 'fpu',
			'fxsr', 'ht', 'lahf_lm', 'lm', 'mca', 'mce', 'mmx', 'msr', 'mtrr',
			'nopl', 'nx', 'pae', 'pat', 'pge', 'pni', 'pse', 'pse36', 'rdtscp',
			'rep_good', 'sep', 'sse', 'sse2', 'ssse3', 'syscall', 'tsc', 'vme']
			,
			info['flags']
		)
		self.assertEqual(1, info['socket_count'])

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz', info['brand_raw'])
		self.assertEqual('2.9300 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.9283 GHz', info['hz_actual_friendly'])
		self.assertEqual((2930000000, 0), info['hz_advertised'])
		self.assertEqual((2928283000, 0), info['hz_actual'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(1, info['count'])

		self.assertEqual('x86_64', info['arch_string_raw'])

		self.assertEqual(6144 * 1024, info['l3_cache_size'])

		self.assertEqual(5, info['stepping'])
		self.assertEqual(30, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['apic', 'clflush', 'cmov', 'constant_tsc', 'cx8', 'de', 'fpu',
			'fxsr', 'ht', 'lahf_lm', 'lm', 'mca', 'mce', 'mmx', 'msr', 'mtrr',
			'nopl', 'nx', 'pae', 'pat', 'pge', 'pni', 'pse', 'pse36', 'rdtscp',
			'rep_good', 'sep', 'sse', 'sse2', 'ssse3', 'syscall', 'tsc', 'vme']
			,
			info['flags']
		)
		self.assertEqual(1, info['socket_count'])
