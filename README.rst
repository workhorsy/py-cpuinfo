py-cpuinfo
==========

A module for getting CPU info with Python 2 & 3

Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work
without any extra programs or libraries, beyond what your OS provides.
It does not require any compilation(C/C++, assembly, et cetera) to use.
Works on Linux, OS X, Windows, BSD, Solaris, Cygwin, and Haiku.

These approaches are used for getting info:

1. Windows Registry
2. /proc/cpuinfo
3. sysctl
4. dmesg
5. isainfo and psrinfo
6. Querying x86 CPUID register

Run as a script
---------------

::

    $ python cpuinfo.py
    python cpuinfo.py 
    Vendor ID: GenuineIntel
    Brand: Genuine Intel(R) CPU           T2050  @ 1.60GHz
    Hz: 1.6000 GHz
    Raw Hz: (1600000000, 0)
    Arch: X86_32
    Bits: 32
    Count: 2
    Raw Arch String: i686
    L2 Cache Size: 2048 KB
    L2 Cache Line Size: 0
    L2 Cache Associativity: 0
    Stepping: 8
    Model: 14
    Family: 6
    Processor Type: 0
    Extended Model: 0
    Extended Family: 0
    Flags: acpi, aperfmperf, apic, arch_perfmon, bts, clflush, cmov, 
    constant_tsc, cx8, de, dtherm, dts, est, fpu, fxsr, ht, mca, mce, mmx, 
    monitor, msr, mtrr, nx, pae, pbe, pdcm, pge, pni, pse, sep, ss, sse, sse2, 
    tm, tm2, tsc, vme, xtpr

Run as a library
----------------

::

    import cpuinfo

    # Have the library pick the best method for getting your CPU info
    info = cpuinfo.get_cpu_info()

    # Or use /proc/cpuinfo
    #info = cpuinfo.get_cpu_info_from_proc_cpuinfo()

    # Or use the Windows registry
    #info = cpuinfo.get_cpu_info_from_registry()

    # Or use sysctl
    #info = cpuinfo.get_cpu_info_from_sysctl()

    # Or use CPU CPUID register
    #info = cpuinfo.get_cpu_info_from_cpuid()

    # Print some CPU values
    print('Vendor ID: {0}'.format(info['vendor_id']))
    print('Brand: {0}'.format(info['brand']))
    print('Hz: {0}'.format(info['hz']))
    print('Raw Hz: {0}'.format(info['raw_hz']))
    print('Arch: {0}'.format(info['arch']))
    print('Bits: {0}'.format(info['bits']))
    print('Count: {0}'.format(info['count']))
    print('Flags: {0}'.format(', '.join(info['flags'])))

Alternate libraries, and how they differ from py-cpuinfo
--------------------------------------------------------

**Numpy**: Great, but just wraps /proc/cpuinfo on unix, and the registry
on Windows. Does not return flags on Windows. The results are different
depending on the OS. Requires all of Numpy to be installed to use. Is
missing new CPU flags like sse4 http://www.numpy.org/

**PyCPUID**: Elegant. But is missing many common CPU flags like 3dnow,
ht, et cetera. Uses a C library that must be compiled. Is missing
features like CPU MHz. Not Python 3 compatible.
https://github.com/FlightDataServices/PyCPUID

**cpuidpy**: Written completly in C++. Requires a compile. Missing CPU
flags and MHz. http://code.google.com/p/cpuidpy/

**PyCPU**: Uses a C library. Requires a compile. Not Python 3
compatible. http://screeniqsys.com/blog/utilities/pycpu/

Bugs and Corrections
--------------------

Please report a Bug if you suspect any of this information is wrong.
