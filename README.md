py-cpuinfo
==========

[![Downloads](https://img.shields.io/pypi/dm/py-cpuinfo.svg)](https://pypi.python.org/pypi/py-cpuinfo/)
[![Latest Version](https://img.shields.io/pypi/v/py-cpuinfo.svg)](https://pypi.python.org/pypi/py-cpuinfo/)
[![License](https://img.shields.io/pypi/l/py-cpuinfo.svg)](https://pypi.python.org/pypi/py-cpuinfo/)
[![License](https://img.shields.io/pypi/pyversions/py-cpuinfo.svg)](https://pypi.python.org/pypi/py-cpuinfo/)

Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work without any
extra programs or libraries, beyond what your OS provides. It does not require
any compilation(C/C++, assembly, et cetera) to use. It works with Python 2
and 3.

OS Support
-----
* BSD
* Cygwin
* Haiku (Tested on Haiku)
* Linux (Tested on Arch, Centos, Debian, Gentoo, Fedora, OpenSuse, Ubuntu)
* OS X (Tested on 10.11)
* Solaris (Tested on Oracle, OpenIndiana)
* Windows (Tested on XP, Vista, 7, 8, 10)


CPU Support
-----
* X86 32bit and 64bit
* Some ARM CPUs (tested on BeagleBone armv7l)


API
-----
~~~python
get_cpu_info()
'''
Returns the CPU info by using the best source of information for your OS.
This is the recommended function for getting CPU info.
Returns None if nothing is found.
'''
get_cpu_info_from_registry()
'''
Returns the CPU info gathered from the Windows Registry.
Returns None if not on Windows.
'''
get_cpu_info_from_proc_cpuinfo()
'''
Returns the CPU info gathered from /proc/cpuinfo.
Returns None if /proc/cpuinfo is not found.
'''
get_cpu_info_from_sysctl()
'''
Returns the CPU info gathered from sysctl.
Returns None if sysctl is not found.
'''
get_cpu_info_from_kstat()
'''
Returns the CPU info gathered from isainfo and kstat.
Returns None if isainfo or kstat are not found.
'''
get_cpu_info_from_dmesg()
'''
Returns the CPU info gathered from dmesg.
Returns None if dmesg is not found or does not have the desired info.
'''
get_cpu_info_from_sysinfo()
'''
Returns the CPU info gathered from sysinfo.
Returns None if sysinfo is not found.
'''
get_cpu_info_from_cpuid()
'''
Returns the CPU info gathered by querying the X86 cpuid register in a new process.
Returns None of non X86 cpus.
Returns None if SELinux is in enforcing mode.
'''
~~~

These approaches are used for getting info:
-----
1. Windows Registry (Windows)
2. /proc/cpuinfo (Linux)
3. sysctl (OS X)
4. dmesg (Unix/Linux)
5. isainfo and kstat (Solaris)
6. cpufreq-info (BeagleBone)
7. lscpu (Unix/Linux)
8. sysinfo (Haiku)
9. Querying the CPUID register (Intel X86 CPUs)


Run as a script
-----
~~~bash
$ python cpuinfo/cpuinfo.py
~~~

Run as a module
-----
~~~bash
$ python -m cpuinfo
~~~

Run as a library
-----
~~~python
import cpuinfo
info = cpuinfo.get_cpu_info()
print(info)
~~~

Bugs and Corrections
-----

Please report a Bug if you suspect any of this information is wrong.

If py-cpuinfo does not work on your machine, run the script:

~~~bash
python tools/get_system_info.py
~~~

and create bug report with the generated "system_info.txt" file.
