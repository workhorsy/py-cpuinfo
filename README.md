py-cpuinfo
==========

Py-cpuinfo gets CPU info. Py-cpuinfo will work on any vanilla OS without any 
thrid party programs or libraries. Py-cpuinfo is only a Python script. It does 
not use any C/C++ or assembly code.

These approaches are used for getting info:
1. /proc/cpuinfo
2. Querying x86 CPUID register
3. Windows Registry

Prereq
-----

Requires Python 2.6 to 3.x

Runs on Linux, FreeBSD, and Windows x86_32 and x86_64.



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

