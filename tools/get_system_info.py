#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2014-2015, Matthew Brennan Jones <matthew.brennan.jones@gmail.com>
# Py-cpuinfo is a Python module to show the cpuinfo of a processor
# It uses a MIT style license
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
import platform
import multiprocessing
import subprocess

PY2 = sys.version_info[0] == 2

def run_and_get_stdout(command, pipe_command=None):
	if not pipe_command:
		p1 = subprocess.Popen(command, stdout=subprocess.PIPE)
		output = p1.stdout.read()
		if not PY2:
			output = output.decode(encoding='UTF-8')
		return output
	else:
		p1 = subprocess.Popen(command, stdout=subprocess.PIPE)
		p2 = subprocess.Popen(pipe_command, stdin=p1.stdout, stdout=subprocess.PIPE)
		p1.stdout.close()
		output = p2.communicate()[0]
		if not PY2:
			output = output.decode(encoding='UTF-8')
		return output


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

print('sys.version_info: {0}\n\n'.format(sys.version_info))
print('multiprocessing.cpu_count: {0}\n\n'.format(multiprocessing.cpu_count()))
print('platform.uname: {0}\n\n'.format(platform.uname()))
print('platform.architecture: {0}\n\n'.format(platform.architecture()))
print('platform.system: {0}\n\n'.format(platform.system()))
print('platform.machine: {0}\n\n'.format(platform.machine()))


if program_paths('cpufreq-info'):
	output = run_and_get_stdout(['cpufreq-info'])
	print('cpufreq-info: \n=====================================================================\n{0}\n\n'.format(output))

if program_paths('sestatus'):
	output = run_and_get_stdout(['sestatus', '-b'])
	print('sestatus -b: \n=====================================================================\n{0}\n\n'.format(output))
'''
if program_paths('dmesg'):
	output = run_and_get_stdout(['dmesg', '-a'])
	print('dmesg -a: \n=====================================================================\n{0}\n\n'.format(output))
'''
if os.path.exists('/proc/cpuinfo'):
	output = run_and_get_stdout(['cat', '/proc/cpuinfo'])
	print('cat /proc/cpuinfo: \n=====================================================================\n{0}\n\n'.format(output))

if program_paths('sysctl'):
	output = run_and_get_stdout(['sysctl', 'machdep.cpu'])
	print('sysctl machdep.cpu: \n=====================================================================\n{0}\n\n'.format(output))

if program_paths('isainfo'):
	output = run_and_get_stdout(['isainfo', '-vb'])
	print('isainfo -vb: \n=====================================================================\n{0}\n\n'.format(output))

if program_paths('kstat'):
	output = run_and_get_stdout(['kstat', '-m', 'cpu_info'])
	print('kstat -m cpu_info: \n=====================================================================\n{0}\n\n'.format(output))



