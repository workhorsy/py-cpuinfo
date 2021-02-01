#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2014-2021 Matthew Brennan Jones <matthew.brennan.jones@gmail.com>
# Py-cpuinfo gets CPU info with pure Python 2 & 3
# It uses the MIT License
# It is hosted at: https://github.com/workhorsy/py-cpuinfo
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


import os, sys
import glob
import platform
import multiprocessing
import subprocess

try:
	import _winreg as winreg
except ImportError as err:
	try:
		import winreg
	except ImportError as err:
		pass

IS_PY2 = sys.version_info[0] == 2
is_windows = platform.system().lower() == 'windows'

out_file_name = 'system_info.txt'
out_file = open(out_file_name, 'w')


def run_and_get_stdout(command, pipe_command=None):
	from subprocess import Popen, PIPE

	if not pipe_command:
		p1 = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE)
		output = p1.communicate()[0]
		if not IS_PY2:
			output = output.decode(encoding='UTF-8')
		return p1.returncode, output
	else:
		p1 = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE)
		p2 = Popen(pipe_command, stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
		p1.stdout.close()
		output = p2.communicate()[0]
		if not IS_PY2:
			output = output.decode(encoding='UTF-8')
		return p2.returncode, output

def program_paths(program_name):
	paths = []
	exts = filter(None, os.environ.get('PATHEXT', '').split(os.pathsep))
	path = os.environ['PATH']
	for p in os.environ['PATH'].split(os.pathsep):
		p = os.path.join(p, program_name)
		if os.access(p, os.X_OK):
			paths.append(p)
		for e in exts:
			pext = p + e
			if os.access(pext, os.X_OK):
				paths.append(pext)
	return paths

def has_sestatus():
	return len(program_paths('sestatus')) > 0

def sestatus_b():
	return run_and_get_stdout(['sestatus', '-b'])

def _is_selinux_enforcing():
	# Just return if the SE Linux Status Tool is not installed
	if not has_sestatus():
		return False

	# Run the sestatus, and just return if it failed to run
	returncode, output = sestatus_b()
	if returncode != 0:
		return False

	# Figure out if explicitly in enforcing mode
	for line in output.splitlines():
		line = line.strip().lower()
		if line.startswith("current mode:"):
			if line.endswith("enforcing"):
				return True
			else:
				return False

	# Figure out if we can execute heap and execute memory
	can_selinux_exec_heap = False
	can_selinux_exec_memory = False
	for line in output.splitlines():
		line = line.strip().lower()
		if line.startswith("allow_execheap") and line.endswith("on"):
			can_selinux_exec_heap = True
		elif line.startswith("allow_execmem") and line.endswith("on"):
			can_selinux_exec_memory = True

	return (not can_selinux_exec_heap or not can_selinux_exec_memory)

def parse_arch(arch_string_raw):
	import re

	arch, bits = None, None
	arch_string_raw = arch_string_raw.lower()

	# X86
	if re.match(r'^i\d86$|^x86$|^x86_32$|^i86pc$|^ia32$|^ia-32$|^bepc$', arch_string_raw):
		arch = 'X86_32'
		bits = 32
	elif re.match(r'^x64$|^x86_64$|^x86_64t$|^i686-64$|^amd64$|^ia64$|^ia-64$', arch_string_raw):
		arch = 'X86_64'
		bits = 64
	# ARM
	elif re.match(r'^armv8-a|aarch64$', arch_string_raw):
		arch = 'ARM_8'
		bits = 64
	elif re.match(r'^armv7$|^armv7[a-z]$|^armv7-[a-z]$|^armv6[a-z]$', arch_string_raw):
		arch = 'ARM_7'
		bits = 32
	elif re.match(r'^armv8$|^armv8[a-z]$|^armv8-[a-z]$', arch_string_raw):
		arch = 'ARM_8'
		bits = 32
	# PPC
	elif re.match(r'^ppc32$|^prep$|^pmac$|^powermac$', arch_string_raw):
		arch = 'PPC_32'
		bits = 32
	elif re.match(r'^powerpc$|^ppc64$|^ppc64le$', arch_string_raw):
		arch = 'PPC_64'
		bits = 64
	# SPARC
	elif re.match(r'^sparc32$|^sparc$', arch_string_raw):
		arch = 'SPARC_32'
		bits = 32
	elif re.match(r'^sparc64$|^sun4u$|^sun4v$', arch_string_raw):
		arch = 'SPARC_64'
		bits = 64
	# S390X
	elif re.match(r'^s390x$', arch_string_raw):
		arch = 'S390X'
		bits = 64

	return (arch, bits)

def print_output(name, output):
	line = "=" * 79
	out_file.write('{0}:\n{1}\n{2}\n\n\n\n'.format(name, line, output))

print_output('sys.executable', sys.executable)

print_output('sys.version_info', sys.version_info)

if hasattr(sys, 'maxsize'):
	sizes = {
		2**31-1: '32 bit',
		2**63-1: '64 bit',
	}
	friendly_maxsize = sizes.get(sys.maxsize) or 'unknown'
	print_output('sys.maxsize', "{0} ({1})".format(sys.maxsize, friendly_maxsize))

print_output('multiprocessing.cpu_count', multiprocessing.cpu_count())

if hasattr(os, 'cpu_count'):
	print_output('os.cpu_count', os.cpu_count())

if 'NUMBER_OF_PROCESSORS' in os.environ:
	print_output("os.environ['NUMBER_OF_PROCESSORS']", os.environ['NUMBER_OF_PROCESSORS'])

if hasattr(os, 'sysconf'):
	print_output("os.sysconf('SC_NPROCESSORS_ONLN')", os.sysconf('SC_NPROCESSORS_ONLN'))

if program_paths('sysctl'):
	returncode, output = run_and_get_stdout(['sysctl', '-n', 'hw.ncpu'])
	print_output('sysctl -n hw.ncpu', output)

print_output('platform.uname', platform.uname())

print_output('platform.architecture', platform.architecture())

print_output('platform.system', platform.system())

print_output('platform.machine', platform.machine())


if program_paths('cpufreq-info'):
	returncode, output = run_and_get_stdout(['cpufreq-info'])
	print_output('cpufreq-info', output)

if program_paths('sestatus'):
	returncode, output = run_and_get_stdout(['sestatus', '-b'])
	print_output('sestatus -b', output)

if os.path.exists('/proc/cpuinfo'):
	returncode, output = run_and_get_stdout(['cat', '/proc/cpuinfo'])
	print_output('cat /proc/cpuinfo', output)

if program_paths('sysctl'):
	returncode, output = run_and_get_stdout(['sysctl', 'machdep.cpu', 'hw.cpufrequency'])
	print_output('sysctl machdep.cpu hw.cpufrequency', output)

if program_paths('sysctl'):
	returncode, output = run_and_get_stdout(['sysctl', 'hw.model', 'hw.machine'])
	print_output('sysctl hw.model hw.machine', output)

if program_paths('isainfo'):
	returncode, output = run_and_get_stdout(['isainfo', '-vb'])
	print_output('isainfo -vb', output)

if program_paths('kstat'):
	returncode, output = run_and_get_stdout(['kstat', '-m', 'cpu_info'])
	print_output('kstat -m cpu_info', output)

if program_paths('lscpu'):
	returncode, output = run_and_get_stdout(['lscpu'])
	print_output('lscpu', output)

if program_paths('dmesg'):
	returncode, output = run_and_get_stdout(['dmesg', '-a'])
	if returncode != 0:
		returncode, output = run_and_get_stdout(['dmesg'])
	if len(output) > 20480:
		output = output[0 : 20480]
	print_output('dmesg -a', output)

if os.path.exists('/var/run/dmesg.boot'):
	returncode, output = run_and_get_stdout(['cat', '/var/run/dmesg.boot'])
	if len(output) > 20480:
		output = output[0 : 20480]
	print_output('cat /var/run/dmesg.boot', output)

if program_paths('sysinfo'):
	uname = platform.system().strip().strip('"').strip("'").strip().lower()
	is_beos = 'beos' in uname or 'haiku' in uname
	if is_beos:
		returncode, output = run_and_get_stdout(['sysinfo', '-cpu'])
		print_output('sysinfo -cpu', output)

if program_paths('lsprop'):
	ibm_features = glob.glob('/proc/device-tree/cpus/*/ibm,pa-features')
	if ibm_features:
		returncode, output = run_and_get_stdout(['lsprop', ibm_features[0]])
		print_output('lsprop /proc/device-tree/cpus/*/ibm,pa-features', output)

if program_paths('wmic'):
	returncode, output = run_and_get_stdout(['wmic', 'os', 'get', 'Version'])
	if returncode == 0 and len(output) > 0:
		returncode, output = run_and_get_stdout(['wmic', 'cpu', 'get', 'Name,CurrentClockSpeed,L2CacheSize,L3CacheSize,Description,Caption,Manufacturer', '/format:list'])
		if returncode == 0 and len(output) > 0:
			print_output('wmic cpu get Name,CurrentClockSpeed,L2CacheSize,L3CacheSize,Description,Caption,Manufacturer /format:list', output)

if 'winreg' in sys.modules or '_winreg' in sys.modules:
	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Hardware\Description\System\CentralProcessor\0")
	processor_brand = winreg.QueryValueEx(key, "ProcessorNameString")[0]
	winreg.CloseKey(key)
	print_output('winreg processor_brand', processor_brand)

	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Hardware\Description\System\CentralProcessor\0")
	vendor_id = winreg.QueryValueEx(key, "VendorIdentifier")[0]
	winreg.CloseKey(key)
	print_output('winreg vendor_id', vendor_id)

	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment")
	arch_string_raw = winreg.QueryValueEx(key, "PROCESSOR_ARCHITECTURE")[0]
	winreg.CloseKey(key)
	print_output('winreg arch_string_raw', arch_string_raw)

	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Hardware\Description\System\CentralProcessor\0")
	hz_actual = winreg.QueryValueEx(key, "~Mhz")[0]
	winreg.CloseKey(key)
	print_output('winreg hz_actual', hz_actual)

	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Hardware\Description\System\CentralProcessor\0")
	feature_bits = winreg.QueryValueEx(key, "FeatureSet")[0]
	winreg.CloseKey(key)
	print_output('winreg feature_bits', feature_bits)


class ASM(object):
	def __init__(self, restype=None, argtypes=(), machine_code=[]):
		self.restype = restype
		self.argtypes = argtypes
		self.machine_code = machine_code
		self.prochandle = None
		self.mm = None
		self.func = None
		self.address = None
		self.size = 0
		self.is_selinux_enforcing = _is_selinux_enforcing()

	def compile(self):
		import ctypes

		machine_code = bytes.join(b'', self.machine_code)
		self.size = ctypes.c_size_t(len(machine_code))

		if is_windows:
			# Allocate a memory segment the size of the machine code, and make it executable
			size = len(machine_code)
			# Alloc at least 1 page to ensure we own all pages that we want to change protection on
			if size < 0x1000: size = 0x1000
			MEM_COMMIT = ctypes.c_ulong(0x1000)
			PAGE_READWRITE = ctypes.c_ulong(0x4)
			pfnVirtualAlloc = ctypes.windll.kernel32.VirtualAlloc
			pfnVirtualAlloc.restype = ctypes.c_void_p
			self.address = pfnVirtualAlloc(None, ctypes.c_size_t(size), MEM_COMMIT, PAGE_READWRITE)
			if not self.address:
				raise Exception("Failed to VirtualAlloc")

			# Copy the machine code into the memory segment
			memmove = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)(ctypes._memmove_addr)
			if memmove(self.address, machine_code, size) < 0:
				raise Exception("Failed to memmove")

			# Enable execute permissions
			PAGE_EXECUTE = ctypes.c_ulong(0x10)
			old_protect = ctypes.c_ulong(0)
			pfnVirtualProtect = ctypes.windll.kernel32.VirtualProtect
			res = pfnVirtualProtect(ctypes.c_void_p(self.address), ctypes.c_size_t(size), PAGE_EXECUTE, ctypes.byref(old_protect))
			if not res:
				raise Exception("Failed VirtualProtect")

			# Flush Instruction Cache
			# First, get process Handle
			if not self.prochandle:
				pfnGetCurrentProcess = ctypes.windll.kernel32.GetCurrentProcess
				pfnGetCurrentProcess.restype = ctypes.c_void_p
				self.prochandle = ctypes.c_void_p(pfnGetCurrentProcess())
			# Actually flush cache
			res = ctypes.windll.kernel32.FlushInstructionCache(self.prochandle, ctypes.c_void_p(self.address), ctypes.c_size_t(size))
			if not res:
				raise Exception("Failed FlushInstructionCache")
		else:
			from mmap import mmap, MAP_PRIVATE, MAP_ANONYMOUS, PROT_WRITE, PROT_READ, PROT_EXEC

			# Allocate a private and executable memory segment the size of the machine code
			machine_code = bytes.join(b'', self.machine_code)
			self.size = len(machine_code)
			self.mm = mmap(-1, self.size, flags=MAP_PRIVATE | MAP_ANONYMOUS, prot=PROT_WRITE | PROT_READ | PROT_EXEC)

			# Copy the machine code into the memory segment
			self.mm.write(machine_code)
			self.address = ctypes.addressof(ctypes.c_int.from_buffer(self.mm))

		# Cast the memory segment into a function
		functype = ctypes.CFUNCTYPE(self.restype, *self.argtypes)
		self.func = functype(self.address)

	def run(self):
		# Call the machine code like a function
		retval = self.func()

		return retval

	def free(self):
		import ctypes

		# Free the function memory segment
		if is_windows:
			MEM_RELEASE = ctypes.c_ulong(0x8000)
			ctypes.windll.kernel32.VirtualFree(ctypes.c_void_p(self.address), ctypes.c_size_t(0), MEM_RELEASE)
		else:
			self.mm.close()

		self.prochandle = None
		self.mm = None
		self.func = None
		self.address = None
		self.size = 0

class CPUID(object):
	def __init__(self):
		# Figure out if SE Linux is on and in enforcing mode
		self.is_selinux_enforcing = _is_selinux_enforcing()

	def _asm_func(self, restype=None, argtypes=(), machine_code=[]):
		asm = ASM(restype, argtypes, machine_code)
		asm.compile()
		return asm

	def _run_asm(self, *machine_code):
		import ctypes

		asm = ASM(ctypes.c_uint32, (), machine_code)
		asm.compile()
		retval = asm.run()
		asm.free()
		return retval

	# http://en.wikipedia.org/wiki/CPUID#EAX.3D0:_Get_vendor_ID
	def get_vendor_id(self):
		rets = []

		# EBX
		ebx = self._run_asm(
			b"\x31\xC0",        # xor eax,eax
			b"\x0F\xA2"         # cpuid
			b"\x89\xD8"         # mov ax,bx
			b"\xC3"             # ret
		)
		#print('!!! ebx: ', hex(ebx))
		rets.append(ebx)

		# ECX
		ecx = self._run_asm(
			b"\x31\xC0",        # xor eax,eax
			b"\x0f\xa2"         # cpuid
			b"\x89\xC8"         # mov ax,cx
			b"\xC3"             # ret
		)
		#print('!!! ecx: ', hex(ecx))
		rets.append(ecx)

		# EDX
		edx = self._run_asm(
			b"\x31\xC0",        # xor eax,eax
			b"\x0f\xa2"         # cpuid
			b"\x89\xD0"         # mov ax,dx
			b"\xC3"             # ret
		)
		#print('!!! edx: ', hex(edx))
		rets.append(edx)

		return rets

	# http://en.wikipedia.org/wiki/CPUID#EAX.3D1:_Processor_Info_and_Feature_Bits
	def get_info(self):
		# EAX
		eax = self._run_asm(
			b"\xB8\x01\x00\x00\x00",   # mov eax,0x1"
			b"\x0f\xa2"                # cpuid
			b"\xC3"                    # ret
		)
		#print('!!! eax: ', hex(eax))
		return eax

	# http://en.wikipedia.org/wiki/CPUID#EAX.3D80000000h:_Get_Highest_Extended_Function_Supported
	def get_max_extension_support(self):
		# Check for extension support
		max_extension_support = self._run_asm(
			b"\xB8\x00\x00\x00\x80" # mov ax,0x80000000
			b"\x0f\xa2"             # cpuid
			b"\xC3"                 # ret
		)

		return max_extension_support

	# http://en.wikipedia.org/wiki/CPUID#EAX.3D1:_Processor_Info_and_Feature_Bits
	def get_flags(self, max_extension_support):
		rets = []

		# EDX
		edx = self._run_asm(
			b"\xB8\x01\x00\x00\x00",   # mov eax,0x1"
			b"\x0f\xa2"                # cpuid
			b"\x89\xD0"                # mov ax,dx
			b"\xC3"                    # ret
		)
		#print('!!! edx: ', hex(edx))
		rets.append(edx)

		# ECX
		ecx = self._run_asm(
			b"\xB8\x01\x00\x00\x00",   # mov eax,0x1"
			b"\x0f\xa2"                # cpuid
			b"\x89\xC8"                # mov ax,cx
			b"\xC3"                    # ret
		)
		#print('!!! ecx: ', hex(ecx))
		rets.append(ecx)

		# http://en.wikipedia.org/wiki/CPUID#EAX.3D7.2C_ECX.3D0:_Extended_Features
		if max_extension_support >= 7:
			# EBX
			ebx = self._run_asm(
				b"\x31\xC9",            # xor ecx,ecx
				b"\xB8\x07\x00\x00\x00" # mov eax,7
				b"\x0f\xa2"         # cpuid
				b"\x89\xD8"         # mov ax,bx
				b"\xC3"             # ret
			)
			#print('!!! ebx: ', hex(ebx))
			rets.append(ebx)

			# ECX
			ecx = self._run_asm(
				b"\x31\xC9",            # xor ecx,ecx
				b"\xB8\x07\x00\x00\x00" # mov eax,7
				b"\x0f\xa2"         # cpuid
				b"\x89\xC8"         # mov ax,cx
				b"\xC3"             # ret
			)
			#print('!!! ecx: ', hex(ecx))
			rets.append(ecx)

		# http://en.wikipedia.org/wiki/CPUID#EAX.3D80000001h:_Extended_Processor_Info_and_Feature_Bits
		if max_extension_support >= 0x80000001:
			# EBX
			ebx = self._run_asm(
				b"\xB8\x01\x00\x00\x80" # mov ax,0x80000001
				b"\x0f\xa2"         # cpuid
				b"\x89\xD8"         # mov ax,bx
				b"\xC3"             # ret
			)
			#print('!!! ebx: ', hex(ebx))
			rets.append(ebx)

			# ECX
			ecx = self._run_asm(
				b"\xB8\x01\x00\x00\x80" # mov ax,0x80000001
				b"\x0f\xa2"         # cpuid
				b"\x89\xC8"         # mov ax,cx
				b"\xC3"             # ret
			)
			#print('!!! ecx: ', hex(ecx))
			rets.append(ecx)

		return rets


	# http://en.wikipedia.org/wiki/CPUID#EAX.3D80000002h.2C80000003h.2C80000004h:_Processor_Brand_String
	def get_processor_brand(self, max_extension_support):
		rets = []

		# Processor brand string
		if max_extension_support >= 0x80000004:
			instructions = [
				b"\xB8\x02\x00\x00\x80", # mov ax,0x80000002
				b"\xB8\x03\x00\x00\x80", # mov ax,0x80000003
				b"\xB8\x04\x00\x00\x80"  # mov ax,0x80000004
			]
			for instruction in instructions:
				# EAX
				eax = self._run_asm(
					instruction,  # mov ax,0x8000000?
					b"\x0f\xa2"   # cpuid
					b"\x89\xC0"   # mov ax,ax
					b"\xC3"       # ret
				)
				#print('!!! eax: ', hex(eax))
				rets.append(eax)

				# EBX
				ebx = self._run_asm(
					instruction,  # mov ax,0x8000000?
					b"\x0f\xa2"   # cpuid
					b"\x89\xD8"   # mov ax,bx
					b"\xC3"       # ret
				)
				#print('!!! ebx: ', hex(ebx))
				rets.append(ebx)

				# ECX
				ecx = self._run_asm(
					instruction,  # mov ax,0x8000000?
					b"\x0f\xa2"   # cpuid
					b"\x89\xC8"   # mov ax,cx
					b"\xC3"       # ret
				)
				#print('!!! ecx: ', hex(ecx))
				rets.append(ecx)

				# EDX
				edx = self._run_asm(
					instruction,  # mov ax,0x8000000?
					b"\x0f\xa2"   # cpuid
					b"\x89\xD0"   # mov ax,dx
					b"\xC3"       # ret
				)
				#print('!!! edx: ', hex(edx))
				rets.append(edx)

		return rets

	# http://en.wikipedia.org/wiki/CPUID#EAX.3D80000006h:_Extended_L2_Cache_Features
	def get_cache(self, max_extension_support):
		# Just return if the cache feature is not supported
		if max_extension_support < 0x80000006:
			return

		# ECX
		ecx = self._run_asm(
			b"\xB8\x06\x00\x00\x80"  # mov ax,0x80000006
			b"\x0f\xa2"              # cpuid
			b"\x89\xC8"              # mov ax,cx
			b"\xC3"                   # ret
		)

		return ecx

def get_cpu_info_from_cpuid():
	# Just return if not X86
	arch_string_raw = platform.machine()
	arch, bits = parse_arch(arch_string_raw)
	if not arch in ['X86_32', 'X86_64']:
		return {}

	# FIXME: Return none if SE Linux is in enforcing mode
	cpuid = CPUID()
	if cpuid.is_selinux_enforcing:
		return {}

	output = ''
	max_extension_support = cpuid.get_max_extension_support()
	output += '# max_extension_support\n'
	output += hex(max_extension_support) + ',\n'

	rets = cpuid.get_cache(max_extension_support)
	output += '# get_cache\n'
	output += hex(rets) + ',\n'

	rets = cpuid.get_info()
	output += '# get_info\n'
	output += hex(rets) + ',\n'

	rets = cpuid.get_processor_brand(max_extension_support)
	output += '# get_processor_brand\n'
	output += ', '.join([hex(n) for n in rets]) + ',\n'

	rets = cpuid.get_vendor_id()
	output += '# get_vendor_id\n'
	output += ', '.join([hex(n) for n in rets]) + ',\n'

	rets = cpuid.get_flags(max_extension_support)
	output += '# get_flags\n'
	output += ', '.join([hex(n) for n in rets]) + ',\n'

	return output


try:
	output = get_cpu_info_from_cpuid()
	print_output('CPUID', output)
except:
	pass

out_file.close()
print('System info written to "{0}"'.format(out_file_name))
