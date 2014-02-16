py-cpuinfo
==========

Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work without any 
extra programs or libraries, beyond what your OS provides. It does not require 
any compilation(C/C++, assembly, et cetera) to use.

These approaches are used for getting info:

1. /proc/cpuinfo
2. Querying x86 CPUID register
3. Windows Registry


Prereq
-----

Requires Python 2.6 to 3.x

Runs on Linux, FreeBSD, and Windows x86_32 and x86_64.

Only tested on X86 CPUs.

Example
-----

    import cpuinfo

    # Have the library pick the best method for getting your CPU info
    info = cpuinfo.get_cpu_info()

    # Or use /proc/cpuinfo
    #info = cpuinfo.get_cpu_info_from_proc_cpuinfo()

    # Or use the Windows registry
    #info = cpuinfo.get_cpu_info_from_registry()

    # Or use CPU CPUID register
    #info = cpuinfo.get_cpu_info_from_cpuid()

    # Print some CPU values
    print('Vendor ID', info['vendor_id'])
    print('Brand', info['brand'])
    print('Hz', info['hz'])
    print('Arch', info['arch'])
    print('Bits', info['bits'])
    print('Count', info['count'])
    print('Flags:', info['flags'])


Alternate libraries, and how they differ from py-cpuinfo
-----

__Numpy__: Great, but just wraps /proc/cpuinfo on unix, and the registry on Windows.
Does not return flags on Windows. The results are different depending on the OS.
Requires all of Numpy to be installed to use. Is missing new CPU flags like sse4
http://www.numpy.org/

__PyCPUID__:
Elegant. But is missing many common CPU flags like 3dnow, ht, et cetera. Uses a 
C library that must be compiled. Is missing features like CPU MHz. Not Python 3 
compatible.
https://github.com/FlightDataServices/PyCPUID

__cpuidpy__: Written completly in C++. Requires a compile. Missing CPU flags and 
MHz.
http://code.google.com/p/cpuidpy/

__PyCPU__: Uses a C library. Requires a compile. Not Python 3 compatible.
http://screeniqsys.com/blog/utilities/pycpu/


Bugs and Corrections
-----

Please report a Bug if you suspect any of this information is wrong.

