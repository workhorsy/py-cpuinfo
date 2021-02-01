py-cpuinfo
==========

[![Latest Version](https://img.shields.io/pypi/v/py-cpuinfo.svg)](https://pypi.org/project/py-cpuinfo/)
[![License](https://img.shields.io/pypi/l/py-cpuinfo.svg)](https://github.com/workhorsy/py-cpuinfo/blob/master/LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/py-cpuinfo.svg)](https://pypi.org/project/py-cpuinfo/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/py-cpuinfo)](https://pypi.org/project/py-cpuinfo/)

Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work without any
extra programs or libraries, beyond what your OS provides. It does not require
any compilation(C/C++, assembly, et cetera) to use. It works with Python 2
and 3.


Example
-----
~~~python
if __name__ == '__main__':
    from cpuinfo import get_cpu_info

    for key, value in get_cpu_info().items():
        print("{0}: {1}".format(key, value))
~~~


API
-----
~~~python
'''
Returns the CPU info by using the best sources of information for your OS.
Returns the result in a dict
'''
get_cpu_info()

'''
Returns the CPU info by using the best sources of information for your OS.
Returns the result in a json string
'''
get_cpu_info_json()
~~~


Fields
-----
| key                           | Example value             | Return Format         |
| :---------------------------- | :------------------------ | :-------------------- |
| "python_version"              | "2.7.12.final.0 (64 bit)" | string                |
| "cpuinfo_version"             | (4, 0, 0)                 | (int, int, int)       |
| "cpuinfo_version_string"      | "4.0.0"                   | string                |
| "hz_advertised_friendly"      | "2.9300 GHz"              | string                |
| "hz_actual_friendly"          | "1.7330 GHz"              | string                |
| "hz_advertised"               | (2930000000, 0)           | (int, int)            |
| "hz_actual"                   | (1733000000, 0)           | (int, int)            |
| "arch"                        | "X86_64"                  | "X86_32", "X86_64", "ARM_8", "ARM_7", "PPC_32", "PPC_64", "SPARC_32", "SPARC_64", "S390X", "MIPS_32", "MIPS_64" |
| "bits"                        | 64                        | int                   |
| "count"                       | 4                         | int                   |
| "l1_data_cache_size"          | 32768                     | int                   |
| "l1_instruction_cache_size"   | 32768                     | int                   |
| "l2_cache_size"               | 262144                    | int                   |
| "l2_cache_line_size"          | 256                       | int                   |
| "l2_cache_associativity"      | 6                         | int                   |
| "l3_cache_size"               | 3145728                   | int                   |
| "stepping"                    | 5                         | int                   |
| "model"                       | 30                        | int                   |
| "family"                      | 6                         | int                   |
| "processor_type"              | 0                         | int                   |
| "flags"                       | ['acpi', 'aperfmperf', 'apic', 'arch_perfmon', 'bts', 'clflush', 'cmov', 'constant_tsc', 'cx16', 'cx8', 'de', 'ds_cpl', 'dtes64', 'dtherm', 'dts', 'ept', 'est', 'flexpriority', 'fpu', 'fxsr', 'ht', 'ida', 'lahf_lm', 'lm', 'mca', 'mce', 'mmx', 'monitor', 'msr', 'mtrr', 'nonstop_tsc', 'nopl', 'nx', 'pae', 'pat', 'pbe', 'pdcm', 'pebs', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'rdtscp', 'rep_good', 'sep', 'smx', 'ss', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'ssse3', 'syscall', 'tm', 'tm2', 'tpr_shadow', 'tsc', 'vme', 'vmx', 'vnmi', 'vpid', 'xtopology', 'xtpr'] | [string] |


Raw Fields
-----

These fields are pulled directly from the CPU and are unverified. They may
contain expected results. Other times they may contain wildly unexpected
results or garbage. So it would be a bad idea to rely on them.

| key                           | Example value             | Return Format         |
| :---------------------------- | :------------------------ | :-------------------- |
| "vendor_id_raw"               | "GenuineIntel"            | string                |
| "hardware_raw"                | "BCM2708"                 | string                |
| "brand_raw"                   | "Intel(R) Core(TM) i7 CPU         870  @ 2.93GHz" | string                |
| "arch_string_raw"             | "x86_64"                  | string                |



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
    from cpuinfo import get_cpu_info
    info = get_cpu_info()
    print(info)
~~~

Run under Pyinstaller
-----
~~~python
# NOTE: Pyinstaller may spawn infinite processes if __main__ is not used
if __name__ == '__main__':
    from cpuinfo import get_cpu_info
    from multiprocessing import freeze_support

    # NOTE: Pyinstaller also requires freeze_support
    freeze_support()
    info = get_cpu_info()
    print(info)
~~~

Install instructions
-----
~~~bash
$ python -m pip install -U py-cpuinfo
~~~


Command Line Arguments
----
~~~
--help: show this help message and exit
--json: Return the info in JSON format
--version: Return the version of py-cpuinfo
--trace: Traces code paths used to find CPU info to file
~~~


OS Support
-----
| OS            | Tested and should work                                 | Untested        |
| :------------ | :----------------------------------------------------- | :-------------- |
| Android       |                                                        | Everything      |
| BSD           | FreeBSD, PC-BSD, TrueOS                                | OpenBSD, NetBSD |
| Cygwin        | Windows                                                |                 |
| Haiku         | Haiku Nightly                                          | BeOS            |
| Linux         | Arch, Centos, Debian, Fedora, Gentoo, OpenSuse, Ubuntu |                 |
| OS X          | 10.8 - 10.14                                           |                 |
| Solaris       | Oracle Solaris, OpenIndiana                            |                 |
| Windows       | XP, Vista, 7, 8, 10                                    | RT              |


CPU Support
-----
* X86 32bit and 64bit
* Some ARM, PPC, S390X and MIPS CPUs


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


Run Test Suite
-----

~~~bash
python test_suite.py
~~~


Bugs and Corrections
-----

Please report a Bug if you suspect any of this information is wrong.

If py-cpuinfo does not work on your machine, run the script:

~~~bash
python tools/get_system_info.py
~~~

and create bug report with the generated "system_info.txt" file.
