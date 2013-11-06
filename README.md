py-cpuinfo
==========

Prereq
-----

Requires Python 2.6 to 3.x

Runs on Linux, Unix, and Windows XP, Vista, and 7

Currently only works on x86_32


What
-----

Py-cpuinfo uses Python to dynamically query the CPU for info using byte code. 
This means that py-cpuinfo will work exactly the same on all OSes. Py-cpuinfo 
will work on any vanilla OS without any thrid party programs or libraries. 
Py-cpuinfo does not need to compile any C/C++ or assembly code. It is only a 
Python script.


Alternate aproaches, and why the do not work
-----

Windows __cpuinfo: This is a special function of the MSVC compiler, and would
require us to ship a small C/C++ library. It is also not callable by Python.

Windows registry: Only available to Windows. Is missing support for many CPU 
flags such as sse3, ssse3, sse4_1, sse4_2, et cetera
See "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment", and
"HKLM\Hardware\Description\System\CentralProcessor\0" for more information.

Windows WMI/CIM: Only runs on Windows. Only has basic CPU info. Is missing 
details like flags and cache.

Linux & Unix /proc/cpuinfo: The perfect solution. But does not work on Windows.

Linux & Unix lscpu: Not on Windows

BSD & OS X sysctl: Requires root. Does not work on Linux & Windows. Only gives
basic info.
sysctl -a | egrep -i 'hw.machine|hw.model|hw.ncpu'

dmesg: Does not work on Windows. Only gives basic info.
dmesg | grep -i cpu


Alternate libraries, and how they differ from py-cpuinfo
-----

Numpy: Great, but just wraps /proc/cpuinfo on unix, and the registry on Windows.
Does not return flags on Windows. The results are different depending on the OS.
Requires all of Numpy to be installed to use. Is missing new CPU flags like sse4

PyCPUID:
Elegant. But is missing many common CPU flags like 3dnow, ht, et cetera. Uses a C library 
that must be compiled. Is missing features like CPU MHz.
https://github.com/FlightDataServices/PyCPUID

cpuidpy: Written in C++. Requires a compile. Missing CPU flags and MHz.
http://code.google.com/p/cpuidpy/


