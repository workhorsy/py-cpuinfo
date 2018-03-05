#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2014-2018, Matthew Brennan Jones <matthew.brennan.jones@gmail.com>
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

PY2 = sys.version_info[0] == 2

out_file_name = 'system_info.txt'
out_file = open(out_file_name, 'w')


def run_and_get_stdout(command, pipe_command=None):
	if not pipe_command:
		p1 = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output = p1.communicate()[0]
		if not PY2:
			output = output.decode(encoding='UTF-8')
		return p1.returncode, output
	else:
		p1 = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		p2 = subprocess.Popen(pipe_command, stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		p1.stdout.close()
		output = p2.communicate()[0]
		if not PY2:
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

def print_output(name, output):
	line = "=" * 79
	out_file.write('{0}:\n{1}\n{2}\n\n\n\n'.format(name, line, output))

print_output('sys.executable', sys.executable)

print_output('sys.version_info', sys.version_info)

print_output('multiprocessing.cpu_count', multiprocessing.cpu_count())

print_output('platform.uname', platform.uname())

print_output('platform.architecture', platform.architecture())

print_output('platform.system', platform.system())

print_output('platform.machine', platform.machine())


if program_paths('cpufreq-info'):
	returncode, output = run_and_get_stdout(['cpufreq-info'])
	print_output('cpufreq-info', output)

if program_paths('sestatus'):
	returncode, output = run_and_get_stdout(['sestatus', '-b'])
	print_output('sestatus', output)

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
	print_output('dmesg', output)

if os.path.exists('/var/run/dmesg.boot'):
	returncode, output = run_and_get_stdout(['cat', '/var/run/dmesg.boot'])
	if len(output) > 20480:
		output = output[0 : 20480]
	print_output('/var/run/dmesg.boot', output)

if program_paths('sysinfo'):
	returncode, output = run_and_get_stdout(['sysinfo', '-cpu'])
	print_output('sysinfo -cpu', output)

if program_paths('lsprop'):
	ibm_features = glob.glob('/proc/device-tree/cpus/*/ibm,pa-features')
	if ibm_features:
		returncode, output = run_and_get_stdout(['lsprop', ibm_features[0]])
		print_output('lsprop /proc/device-tree/cpus/*/ibm,pa-features', output)

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
	raw_arch_string = winreg.QueryValueEx(key, "PROCESSOR_ARCHITECTURE")[0]
	winreg.CloseKey(key)
	print_output('winreg raw_arch_string', raw_arch_string)

	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Hardware\Description\System\CentralProcessor\0")
	hz_actual = winreg.QueryValueEx(key, "~Mhz")[0]
	winreg.CloseKey(key)
	print_output('winreg hz_actual', hz_actual)

	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Hardware\Description\System\CentralProcessor\0")
	feature_bits = winreg.QueryValueEx(key, "FeatureSet")[0]
	winreg.CloseKey(key)
	print_output('winreg feature_bits', feature_bits)

out_file.close()
print('System info written to "{0}"'.format(out_file_name))
