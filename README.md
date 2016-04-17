py-cpuinfo
==========

[![Downloads](https://img.shields.io/pypi/dm/py-cpuinfo.svg)](https://pypi.python.org/pypi/py-cpuinfo/)
[![Latest Version](https://img.shields.io/pypi/v/py-cpuinfo.svg)](https://pypi.python.org/pypi/py-cpuinfo/)
[![License](https://img.shields.io/pypi/l/py-cpuinfo.svg)](https://pypi.python.org/pypi/py-cpuinfo/)
[![License](https://img.shields.io/pypi/pyversions/py-cpuinfo.svg)](https://pypi.python.org/pypi/py-cpuinfo/)

Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work without any
extra programs or libraries, beyond what your OS provides. It does not require
any compilation(C/C++, assembly, et cetera) to use.

OS Support
-----
* BSD
* Cygwin
* Haiku
* Linux
* OS X
* Solaris
* Windows


CPU Support
-----
* X86 32bit and 64bit
* Some ARM CPUs (tested on BeagleBone armv7l)


API
-----
get_cpu_info_from_registry()
get_cpu_info_from_proc_cpuinfo()
get_cpu_info_from_sysctl()
get_cpu_info_from_kstat()
get_cpu_info_from_dmesg()
get_cpu_info_from_sysinfo()
get_cpu_info_from_cpuid()
get_cpu_info()


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
