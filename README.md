py-cpuinfo
==========

[![Latest Version](https://img.shields.io/pypi/v/py-cpuinfo.svg)](https://pypi.org/project/py-cpuinfo/)
[![License](https://img.shields.io/pypi/l/py-cpuinfo.svg)](https://github.com/workhorsy/py-cpuinfo/blob/master/LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/py-cpuinfo.svg)](https://pypi.org/project/py-cpuinfo/)

Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work without any
extra programs or libraries, beyond what your OS provides. It does not require
any compilation(C/C++, assembly, et cetera) to use. It works with Python 2
and 3.

OS Support
-----
| OS            | Tested and should work                                 | Untested        |
| :------------ | :----------------------------------------------------- | :-------------- |
| Android       |                                                        | Everything      |
| BSD           | FreeBSD, PC-BSD                                        | OpenBSD, NetBSD |
| Cygwin        | Windows                                                |                 |
| Haiku         | Haiku Nightly                                          | BeOS            |
| Linux         | Arch, Centos, Debian, Fedora, Gentoo, OpenSuse, Ubuntu |                 |
| OS X          | 10.8 - 10.12                                           |                 |
| Solaris       | Oracle Solaris, OpenIndiana                            |                 |
| Windows       | XP, Vista, 7, 8, 10                                    | RT              |


CPU Support
-----
* X86 32bit and 64bit
* Some ARM and PPC CPUs


API
-----
~~~python
'''
Returns the CPU info by using the best sources of information for your OS.
Returns {} if nothing is found.
'''
get_cpu_info()
~~~


Output
-----
| key                           | Example value   |
| :---------------------------- | :-------------- |
| python_version                | "2.7.12.final.0 (64 bit)" |
| cpuinfo_version               | (4, 0, 0) |
| vendor_id                     | "GenuineIntel"  |
| hardware                      | "BCM2708" |
| brand                         | "Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz" |
| hz_advertised                 | "2.9300 GHz" |
| hz_actual                     | "1.7330 GHz" |
| hz_advertised_raw             | (2930000000, 0)|
| hz_actual_raw                 | (1733000000, 0) |
| arch                          | "X86_64" |
| bits                          | 64 |
| count                         | 4 |
| raw_arch_string               | "x86_64" |
| l1_data_cache_size            | "32 KB" |
| l1_instruction_cache_size     | "32 KB" |
| l2_cache_size                 | "256 KB" |
| l2_cache_line_size            | 6 |
| l2_cache_associativity        | 0x100 |
| l3_cache_size                 | "3072 KB" |
| stepping                      | 5 |
| model                         | 30 |
| family                        | 6 |
| processor_type                | 0 |
| extended_model                | 0 |
| extended_family               | 0 |
| flags                         | ['acpi', 'aperfmperf', 'apic', 'arch_perfmon', 'bts', 'clflush', 'cmov', 'constant_tsc', 'cx16', 'cx8', 'de', 'ds_cpl', 'dtes64', 'dtherm', 'dts', 'ept', 'est', 'flexpriority', 'fpu', 'fxsr', 'ht', 'ida', 'lahf_lm', 'lm', 'mca', 'mce', 'mmx', 'monitor', 'msr', 'mtrr', 'nonstop_tsc', 'nopl', 'nx', 'pae', 'pat', 'pbe', 'pdcm', 'pebs', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'rdtscp', 'rep_good', 'sep', 'smx', 'ss', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'ssse3', 'syscall', 'tm', 'tm2', 'tpr_shadow', 'tsc', 'vme', 'vmx', 'vnmi', 'vpid', 'xtopology', 'xtpr'] |


These approaches are used for getting info:
-----
1. Windows Registry (Windows)
2. /proc/cpuinfo (Linux)
3. sysctl (OS X)
4. dmesg (Unix/Linux)
5. /var/run/dmesg.boot (BSD/Unix)
6. isainfo and kstat (Solaris)
7. cpufreq-info (BeagleBone)
8. lscpu (Unix/Linux)
9. sysinfo (Haiku)
10. device-tree ibm features flags (Linux PPC)
11. Querying the CPUID register (Intel X86 CPUs)


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
if __name__ == '__main__':
    import cpuinfo
    info = cpuinfo.get_cpu_info()
    print(info)
~~~

Run under Pyinstaller
-----
~~~python
if __name__ == '__main__':
    import cpuinfo
    from multiprocessing import freeze_support
    freeze_support() # NOTE: Needed for Pyinstaller
    info = cpuinfo.get_cpu_info()
    print(info)
~~~

Install instructions
-----
~~~bash
$ python -m pip install -U py-cpuinfo
~~~


Bugs and Corrections
-----

Please report a Bug if you suspect any of this information is wrong.

If py-cpuinfo does not work on your machine, run the script:

~~~bash
python tools/get_system_info.py
~~~

and create bug report with the generated "system_info.txt" file.
