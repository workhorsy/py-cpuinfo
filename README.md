py-cpuinfo
==========

Py-cpuinfo uses Python to dynamically query the CPU for info using byte code. 
This means that py-cpuinfo will work exactly the same on all OSes. Py-cpuinfo 
will work on any vanilla OS without any thrid party programs or libraries. 
Py-cpuinfo does not need to compile any C/C++ or assembly code. It is only a 
Python script.

Prereq
-----

Requires Python 2.6 to 3.x

Runs on Linux, and Unix x86_32 and x86_64.
Windows support is comming soon.


Alternate aproaches, and why they were not used
-----

__Windows __cpuinfo__: This is a special function of the MSVC compiler, and would
require us to ship a small C/C++ library. It is also not callable by Python.

__Windows registry__: Only available to Windows. Is missing support for many CPU 
flags such as sse3, ssse3, sse4_1, sse4_2, et cetera.
See "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment", and
"HKLM\Hardware\Description\System\CentralProcessor\0" for more information.

__Windows WMI/CIM__: Only runs on Windows. Only has basic CPU info. Is missing 
details like flags and cache.

__Linux & Unix /proc/cpuinfo__: The perfect solution. But does not work on Windows.

__Linux & Unix lscpu__: Not on Windows

__BSD & OS X sysctl__: Requires root. Does not work on Linux & Windows. Only gives
basic info.
sysctl -a | egrep -i 'hw.machine|hw.model|hw.ncpu'

__dmesg__: Does not work on Windows. Only gives basic info.
dmesg | grep -i cpu


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

__PyCPU__: Uses a C library. Requires a compile. Inaccurate MHz calculation. Not 
Python 3 compatible.
http://screeniqsys.com/blog/2012/11/07/pycpu-a-python-library-for-cpu-information/


Bugs and Corrections
-----

Please report a Bug if you suspect any of this information is wrong.

