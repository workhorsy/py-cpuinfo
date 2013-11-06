#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2013, Matthew Brennan Jones <mattjones@workhorsy.org>
# This is a Python module to show the cpuinfo of a processor
# It should work on Linux, Unix, and Windows, as it does not use /proc/cpuinfo 
# or any external native libraries.
# It uses Python CTypes to run x86 assembly byte code directly.
# It should work on Python 2.6 to 3.X
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# FIXME: How do we get the MHz?
# FIXME: Figure out how /proc/cpuinfo simulates cpuinfo on non x86 cpus
# FIXME: Make sure this works on 64bit machines, and with memory execution protection.
# FIXME: See if running this in a multiprocessing process will stop it from segfaulting when it breaks
# FIXME: Check how this compares to numpy. How does numpy get MHz and sse3 detection when the registry
# does not have this info, and there is no /proc/cpuinfo ? Does it use win32 __cpuinfo ?

import ctypes

def is_bit_set(reg, bit):
	mask = 1 << bit
	is_set = reg & mask > 0
	return is_set

def run_asm(raw_byte_code):
	byte_code = ctypes.create_string_buffer(raw_byte_code, len(raw_byte_code))
	fun = ctypes.CFUNCTYPE(ctypes.c_uint)(ctypes.addressof(byte_code))
	return fun()

# http://en.wikipedia.org/wiki/CPUID#EAX.3D0:_Get_vendor_ID
def get_vendor_id():
	# EBX
	ebx = run_asm(
		b"\x31\xC0"     # xor ax, ax
		b"\x0f\xa2"     # cpuid
		b"\x89\xD8"     # mov ax,bx
		b"\xc3"         # ret
	)

	# ECX
	ecx = run_asm(
		b"\x31\xC0"     # xor ax, ax
		b"\x0f\xa2"     # cpuid
		b"\x89\xC8"     # mov ax,cx
		b"\xc3"         # ret
	)

	# EDX
	edx = run_asm(
		b"\x31\xC0"     # xor ax, ax
		b"\x0f\xa2"     # cpuid
		b"\x89\xD0"     # mov ax,dx
		b"\xc3"         # ret
	)

	# Each 4bits is a ascii letter in the name
	vendor_id = []
	for reg in [ebx, edx, ecx]:
		for n in [0, 8, 16, 24]:
			vendor_id.append(chr((reg >> n) & 0xFF))
	vendor_id = str.join('', vendor_id)

	return vendor_id

# http://en.wikipedia.org/wiki/CPUID#EAX.3D1:_Processor_Info_and_Feature_Bits
def get_info():
	# EAX
	eax = run_asm(
		b"\x31\xC0"     # xor ax, ax
		b"\x40"         # inc ax
		b"\x0f\xa2"     # cpuid
		b"\xc3"         # ret
	)

	# Get the CPU info
	stepping = (eax >> 0) & 0xF # 4 bits
	model = (eax >> 4) & 0xF # 4 bits
	family = (eax >> 8) & 0xF # 4 bits
	processor_type = (eax >> 12) & 0x3 # 2 bits
	extended_model = (eax >> 16) & 0xF # 4 bits
	extended_family = (eax >> 20) & 0xFF # 8 bits

	return (
		stepping, 
		model, 
		family,
		processor_type,
		extended_model,
		extended_family
	)

# http://en.wikipedia.org/wiki/CPUID#EAX.3D1:_Processor_Info_and_Feature_Bits
def get_flags():
	# EDX
	edx = run_asm(
		b"\x31\xC0"     # xor ax, ax
		b"\x40"         # inc ax
		b"\x0f\xa2"     # cpuid
		b"\x89\xD0"     # mov ax,dx
		b"\xc3"         # ret
	)

	# ECX
	ecx = run_asm(
		b"\x31\xC0"     # xor ax, ax
		b"\x40"         # inc ax
		b"\x0f\xa2"     # cpuid
		b"\x89\xC8"     # mov ax,cx
		b"\xc3"         # ret
	)

	# Get the CPU flags
	flags = {
		'fpu' : is_bit_set(edx, 0),
		'vme' : is_bit_set(edx, 1),
		'de' : is_bit_set(edx, 2),
		'pse' : is_bit_set(edx, 3),
		'tsc' : is_bit_set(edx, 4),
		'msr' : is_bit_set(edx, 5),
		'pae' : is_bit_set(edx, 6),
		'mce' : is_bit_set(edx, 7),
		'cx8' : is_bit_set(edx, 8),
		'apic' : is_bit_set(edx, 9),
		#'reserved1' : is_bit_set(edx, 10),
		'sep' : is_bit_set(edx, 11),
		'mtrr' : is_bit_set(edx, 12),
		'pge' : is_bit_set(edx, 13),
		'mca' : is_bit_set(edx, 14),
		'cmov' : is_bit_set(edx, 15),
		'pat' : is_bit_set(edx, 16),
		'pse36' : is_bit_set(edx, 17),
		'pn' : is_bit_set(edx, 18),
		'clflush' : is_bit_set(edx, 19),
		#'reserved2' : is_bit_set(edx, 20),
		'dts' : is_bit_set(edx, 21),
		'acpi' : is_bit_set(edx, 22),
		'mmx' : is_bit_set(edx, 23),
		'fxsr' : is_bit_set(edx, 24),
		'sse' : is_bit_set(edx, 25),
		'sse2' : is_bit_set(edx, 26),
		'ss' : is_bit_set(edx, 27),
		'ht' : is_bit_set(edx, 28),
		'tm' : is_bit_set(edx, 29),
		'ia64' : is_bit_set(edx, 30),
		'pbe' : is_bit_set(edx, 31),

		'pni' : is_bit_set(ecx, 0),
		'pclmulqdq' : is_bit_set(ecx, 1),
		'dtes64' : is_bit_set(ecx, 2),
		'monitor' : is_bit_set(ecx, 3),
		'ds_cpi' : is_bit_set(ecx, 4),
		'vmx' : is_bit_set(ecx, 5),
		'smx' : is_bit_set(ecx, 6),
		'est' : is_bit_set(ecx, 7),
		'tm2' : is_bit_set(ecx, 8),
		'ssse3' : is_bit_set(ecx, 9),
		'cid' : is_bit_set(ecx, 10),
		#'reserved3' : is_bit_set(ecx, 11),
		'fma' : is_bit_set(ecx, 12),
		'cx16' : is_bit_set(ecx, 13),
		'xtpr' : is_bit_set(ecx, 14),
		'pdcm' : is_bit_set(ecx, 15),
		#'reserved4' : is_bit_set(ecx, 16),
		'pcid' : is_bit_set(ecx, 17),
		'dca' : is_bit_set(ecx, 18),
		'sse4_1' : is_bit_set(ecx, 19),
		'sse4_2' : is_bit_set(ecx, 20),
		'x2apic' : is_bit_set(ecx, 21),
		'movbe' : is_bit_set(ecx, 22),
		'popcnt' : is_bit_set(ecx, 23),
		'tscdeadline' : is_bit_set(ecx, 24),
		'aes' : is_bit_set(ecx, 25),
		'xsave' : is_bit_set(ecx, 26),
		'osxsave' : is_bit_set(ecx, 27),
		'avx' : is_bit_set(ecx, 28),
		'f16c' : is_bit_set(ecx, 29),
		'rdrnd' : is_bit_set(ecx, 30),
		'hypervisor' : is_bit_set(ecx, 31)
	}

	# Get a list of only the flags that are true
	flags = [k for k, v in flags.items() if v]
	flags.sort()

	return flags


print(get_info())
print('vendor_id', get_vendor_id())
'''
print('cpu_stepping', cpu_stepping)
print('cpu_model', cpu_model)
print('cpu_family', cpu_family)
print('cpu_type', cpu_type)
print('cpu_extended_model', cpu_extended_model)
print('cpu_extended_family', cpu_extended_family)
'''
print(get_flags())


