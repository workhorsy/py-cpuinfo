py-cpuinfo
==========


Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work
without any extra programs or libraries, beyond what your OS provides.
It does not require any compilation(C/C++, assembly, et cetera) to use.
It works on Linux, OS X, Windows, BSD, Solaris, Cygwin, Haiku, and
BeagleBone. It currently only works on X86 and some ARM CPUs.

These approaches are used for getting info:

1. Windows Registry (Window)
2. /proc/cpuinfo (Unix/Linux/Haiku)
3. sysctl (BSD)
4. dmesg (Unix/Linux)
5. isainfo and kstat (OS X)
6. cpufreq-info (BeagleBone)
7. Querying the CPUID register (Intel X86 CPUs)

Run as a script
---------------

.. code:: bash

        $ python cpuinfo/cpuinfo.py
        Vendor ID: GenuineIntel
        Hardware Raw:
        Brand: Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz
        Hz Advertised: 3.1000 GHz
        Hz Actual: 3.0794 GHz
        Hz Advertised Raw: (3100000000, 0)
        Hz Actual Raw: (3079444000, 0)
        Arch: X86_64
        Bits: 64
        Count: 4
        Raw Arch String: x86_64
        L2 Cache Size: 6144 KB
        L2 Cache Line Size: 0
        L2 Cache Associativity: 0
        Stepping: 3
        Model: 60
        Family: 6
        Processor Type: 0
        Extended Model: 0
        Extended Family: 0
        Flags: apic, clflush, cmov, constant_tsc, cx8, de, fpu, fxsr, ht, lahf_lm, 
        lm, mca, mce, mmx, msr, mtrr, nopl, nx, pae, pat, pge, pni, pse, pse36, 
        rdtscp, rep_good, sep, sse, sse2, ssse3, syscall, tsc, vme

Run as a library
----------------

.. code:: python

        from cpuinfo import cpuinfo # from installed with pip
        #import cpuinfo # from path

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
        print('Hz Advertised: {0}'.format(info['hz_advertised']))
        print('Hz Actual: {0}'.format(info['hz_actual']))
        print('Hz Advertised Raw: {0}'.format(info['hz_advertised_raw']))
        print('Hz Actual Raw: {0}'.format(info['hz_actual_raw']))
        print('Arch: {0}'.format(info['arch']))
        print('Bits: {0}'.format(info['bits']))
        print('Count: {0}'.format(info['count']))
        print('Flags: {0}'.format(', '.join(info['flags'])))

Bugs and Corrections
--------------------

Please report a Bug if you suspect any of this information is wrong.

If py-cpuinfo does not work on your machine, run the script:

.. code:: bash

    python tools/get_system_info.py

and create bug report with the generated "system\_info.txt" file.


