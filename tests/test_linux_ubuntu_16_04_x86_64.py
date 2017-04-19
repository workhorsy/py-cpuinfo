

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 2
	is_windows = False
	raw_arch_string = 'x86_64'
	can_cpuid = False

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def has_lscpu():
		return True

	@staticmethod
	def has_dmesg():
		return True

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = '''
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Pentium(R) CPU G640 @ 2.80GHz
stepping	: 7
microcode	: 0x29
cpu MHz		: 1901.375
cache size	: 3072 KB
physical id	: 0
siblings	: 2
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave lahf_lm epb tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm arat pln pts
bugs		:
bogomips	: 5587.32
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Pentium(R) CPU G640 @ 2.80GHz
stepping	: 7
microcode	: 0x29
cpu MHz		: 2070.796
cache size	: 3072 KB
physical id	: 0
siblings	: 2
core id		: 1
cpu cores	: 2
apicid		: 2
initial apicid	: 2
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave lahf_lm epb tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm arat pln pts
bugs		:
bogomips	: 5587.32
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:


'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = '''
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                2
On-line CPU(s) list:   0,1
Thread(s) per core:    1
Core(s) per socket:    2
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 42
Model name:            Intel(R) Pentium(R) CPU G640 @ 2.80GHz
Stepping:              7
CPU MHz:               2070.796
CPU max MHz:           2800.0000
CPU min MHz:           1600.0000
BogoMIPS:              5587.32
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              3072K
NUMA node0 CPU(s):     0,1
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave lahf_lm epb tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm arat pln pts


'''
		return returncode, output

	@staticmethod
	def dmesg_a():
		returncode = 0
		output = '''
[    0.000000] microcode: CPU0 microcode updated early to revision 0x29, date = 2013-06-12
[    0.000000] Initializing cgroup subsys cpuset
[    0.000000] Initializing cgroup subsys cpu
[    0.000000] Initializing cgroup subsys cpuacct
[    0.000000] Linux version 4.4.0-64-generic (buildd@lgw01-56) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) ) #85-Ubuntu SMP Mon Feb 20 11:50:30 UTC 2017 (Ubuntu 4.4.0-64.85-generic 4.4.44)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.4.0-64-generic root=UUID=9112213a-3570-4904-8969-d5aab8825f6b ro quiet splash vt.handoff=7
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Centaur CentaurHauls
[    0.000000] x86/fpu: Supporting XSAVE feature 0x01: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x02: 'SSE registers'
[    0.000000] x86/fpu: Enabled xstate features 0x3, context size is 576 bytes, using 'standard' format.
[    0.000000] x86/fpu: Using 'eager' FPU context switches.
[    0.000000] e820: BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009d7ff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009d800-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000000e0000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x000000001fffffff] usable
[    0.000000] BIOS-e820: [mem 0x0000000020000000-0x00000000201fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000020200000-0x000000003fffffff] usable
[    0.000000] BIOS-e820: [mem 0x0000000040000000-0x00000000401fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000040200000-0x00000000d878dfff] usable
[    0.000000] BIOS-e820: [mem 0x00000000d878e000-0x00000000d8792fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000d8793000-0x00000000d8796fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000d8797000-0x00000000d8db1fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000d8db2000-0x00000000d9018fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000d9019000-0x00000000d9024fff] ACPI data
[    0.000000] BIOS-e820: [mem 0x00000000d9025000-0x00000000d9031fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000d9032000-0x00000000d9036fff] ACPI data
[    0.000000] BIOS-e820: [mem 0x00000000d9037000-0x00000000d9079fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000d907a000-0x00000000d9d3dfff] usable
[    0.000000] BIOS-e820: [mem 0x00000000d9d3e000-0x00000000d9ff1fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000d9ff2000-0x00000000d9ffffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000db000000-0x00000000df1fffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000f8000000-0x00000000fbffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed00000-0x00000000fed03fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed1c000-0x00000000fed1ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000041fdfffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] SMBIOS 2.7 present.
[    0.000000] DMI: Hewlett-Packard s5-1224/2ADA, BIOS 7.11 04/28/2012
[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000000] e820: last_pfn = 0x41fe00 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: uncachable
[    0.000000] MTRR fixed ranges enabled:
[    0.000000]   00000-9FFFF write-back
[    0.000000]   A0000-BFFFF uncachable
[    0.000000]   C0000-CFFFF write-protect
[    0.000000]   D0000-E7FFF uncachable
[    0.000000]   E8000-FFFFF write-protect
[    0.000000] MTRR variable ranges enabled:
[    0.000000]   0 base 000000000 mask C00000000 write-back
[    0.000000]   1 base 400000000 mask FE0000000 write-back
[    0.000000]   2 base 0E0000000 mask FE0000000 uncachable
[    0.000000]   3 base 0DC000000 mask FFC000000 uncachable
[    0.000000]   4 base 0DB000000 mask FFF000000 uncachable
[    0.000000]   5 base 41FE00000 mask FFFE00000 uncachable
[    0.000000]   6 disabled
[    0.000000]   7 disabled
[    0.000000]   8 disabled
[    0.000000]   9 disabled
[    0.000000] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WC  UC- WT
[    0.000000] original variable MTRRs
[    0.000000] reg 0, base: 0GB, range: 16GB, type WB
[    0.000000] reg 1, base: 16GB, range: 512MB, type WB
[    0.000000] reg 2, base: 3584MB, range: 512MB, type UC
[    0.000000] reg 3, base: 3520MB, range: 64MB, type UC
[    0.000000] reg 4, base: 3504MB, range: 16MB, type UC
[    0.000000] reg 5, base: 16894MB, range: 2MB, type UC
[    0.000000] total RAM covered: 16302M
[    0.000000] Found optimal setting for mtrr clean up
[    0.000000]  gran_size: 64K 	chunk_size: 128M 	num_reg: 9  	lose cover RAM: 0G
[    0.000000] New variable MTRRs
[    0.000000] reg 0, base: 0GB, range: 2GB, type WB
[    0.000000] reg 1, base: 2GB, range: 1GB, type WB
[    0.000000] reg 2, base: 3GB, range: 512MB, type WB
[    0.000000] reg 3, base: 3504MB, range: 16MB, type UC
[    0.000000] reg 4, base: 3520MB, range: 64MB, type UC
[    0.000000] reg 5, base: 4GB, range: 4GB, type WB
[    0.000000] reg 6, base: 8GB, range: 8GB, type WB
[    0.000000] reg 7, base: 16GB, range: 512MB, type WB
[    0.000000] reg 8, base: 16894MB, range: 2MB, type UC
[    0.000000] e820: update [mem 0xdb000000-0xffffffff] usable ==> reserved
[    0.000000] e820: last_pfn = 0xda000 max_arch_pfn = 0x400000000
[    0.000000] found SMP MP-table at [mem 0x000fcc40-0x000fcc4f] mapped at [ffff8800000fcc40]
[    0.000000] Scanning 1 areas for low memory corruption
[    0.000000] Base memory trampoline at [ffff880000097000] 97000 size 24576
[    0.000000] reserving inaccessible SNB gfx pages
[    0.000000] BRK [0x0220c000, 0x0220cfff] PGTABLE
[    0.000000] BRK [0x0220d000, 0x0220dfff] PGTABLE
[    0.000000] BRK [0x0220e000, 0x0220efff] PGTABLE
[    0.000000] BRK [0x0220f000, 0x0220ffff] PGTABLE
[    0.000000] BRK [0x02210000, 0x02210fff] PGTABLE
[    0.000000] BRK [0x02211000, 0x02211fff] PGTABLE
[    0.000000] RAMDISK: [mem 0x337fe000-0x35bf6fff]
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x00000000000F0450 000024 (v02 HPQOEM)
[    0.000000] ACPI: XSDT 0x00000000D9019078 00006C (v01 HPQOEM SLIC-CPC 01072009 AMI  00010013)
[    0.000000] ACPI: FACP 0x00000000D90227B8 0000F4 (v04 HPQOEM SLIC-CPC 01072009 AMI  00010013)
[    0.000000] ACPI: DSDT 0x00000000D9019170 009645 (v02 HPQOEM SLIC-CPC 00000711 INTL 20051117)
[    0.000000] ACPI: FACS 0x00000000D9030F80 000040
[    0.000000] ACPI: APIC 0x00000000D90228B0 000062 (v03 HPQOEM SLIC-CPC 01072009 AMI  00010013)
[    0.000000] ACPI: MCFG 0x00000000D9022918 00003C (v01 HPQOEM SLIC-CPC 01072009 MSFT 00000097)
[    0.000000] ACPI: SLIC 0x00000000D9022958 000176 (v01 HPQOEM SLIC-CPC 01072009 AMI  00010013)
[    0.000000] ACPI: HPET 0x00000000D9022AD0 000038 (v01 HPQOEM SLIC-CPC 01072009 AMI. 00000005)
[    0.000000] ACPI: SSDT 0x00000000D9022B08 00036D (v01 HPQOEM SLIC-CPC 00001000 INTL 20091112)
[    0.000000] ACPI: SSDT 0x00000000D9022E78 0008E4 (v01 HPQOEM SLIC-CPC 00003000 INTL 20051117)
[    0.000000] ACPI: SSDT 0x00000000D9023760 000A92 (v01 HPQOEM SLIC-CPC 00003000 INTL 20051117)
[    0.000000] ACPI: DBGP 0x00000000D90241F8 000034 (v01 HPQOEM SLIC-CPC 01072009 AMI  00010013)
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] No NUMA configuration found
[    0.000000] Faking a node at [mem 0x0000000000000000-0x000000041fdfffff]
[    0.000000] NODE_DATA(0) allocated [mem 0x41fdea000-0x41fdeefff]
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.000000]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x000000041fdfffff]
[    0.000000]   Device   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000001000-0x000000000009cfff]
[    0.000000]   node   0: [mem 0x0000000000100000-0x000000001fffffff]
[    0.000000]   node   0: [mem 0x0000000020200000-0x000000003fffffff]
[    0.000000]   node   0: [mem 0x0000000040200000-0x00000000d878dfff]
[    0.000000]   node   0: [mem 0x00000000d8793000-0x00000000d8796fff]
[    0.000000]   node   0: [mem 0x00000000d907a000-0x00000000d9d3dfff]
[    0.000000]   node   0: [mem 0x00000000d9ff2000-0x00000000d9ffffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x000000041fdfffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000001000-0x000000041fdfffff]
[    0.000000] On node 0 totalpages: 4165120
[    0.000000]   DMA zone: 64 pages used for memmap
[    0.000000]   DMA zone: 156 pages reserved
[    0.000000]   DMA zone: 3996 pages, LIFO batch:0
[    0.000000]   DMA32 zone: 13826 pages used for memmap
[    0.000000]   DMA32 zone: 884836 pages, LIFO batch:31
[    0.000000]   Normal zone: 51192 pages used for memmap
[    0.000000]   Normal zone: 3276288 pages, LIFO batch:31
[    0.000000] Reserving Intel graphics stolen memory at 0xdb200000-0xdf1fffff
[    0.000000] ACPI: PM-Timer IO Port: 0x408
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0xff] high edge lint[0x1])
[    0.000000] IOAPIC[0]: apic_id 2, version 32, address 0xfec00000, GSI 0-23
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] ACPI: HPET id: 0x8086a701 base: 0xfed00000
[    0.000000] smpboot: Allowing 2 CPUs, 0 hotplug CPUs
[    0.000000] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.000000] PM: Registered nosave memory: [mem 0x0009d000-0x0009dfff]
[    0.000000] PM: Registered nosave memory: [mem 0x0009e000-0x0009ffff]
[    0.000000] PM: Registered nosave memory: [mem 0x000a0000-0x000dffff]
[    0.000000] PM: Registered nosave memory: [mem 0x000e0000-0x000fffff]
[    0.000000] PM: Registered nosave memory: [mem 0x20000000-0x201fffff]
[    0.000000] PM: Registered nosave memory: [mem 0x40000000-0x401fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xd878e000-0xd8792fff]
[    0.000000] PM: Registered nosave memory: [mem 0xd8797000-0xd8db1fff]
[    0.000000] PM: Registered nosave memory: [mem 0xd8db2000-0xd9018fff]
[    0.000000] PM: Registered nosave memory: [mem 0xd9019000-0xd9024fff]
[    0.000000] PM: Registered nosave memory: [mem 0xd9025000-0xd9031fff]
[    0.000000] PM: Registered nosave memory: [mem 0xd9032000-0xd9036fff]
[    0.000000] PM: Registered nosave memory: [mem 0xd9037000-0xd9079fff]
[    0.000000] PM: Registered nosave memory: [mem 0xd9d3e000-0xd9ff1fff]
[    0.000000] PM: Registered nosave memory: [mem 0xda000000-0xdaffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xdb000000-0xdf1fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xdf200000-0xf7ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xf8000000-0xfbffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfc000000-0xfebfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec00000-0xfec00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec01000-0xfecfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed00000-0xfed03fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed04000-0xfed1bfff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed1c000-0xfed1ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed20000-0xfedfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee01000-0xfeffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xff000000-0xffffffff]
[    0.000000] e820: [mem 0xdf200000-0xf7ffffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on bare hardware
[    0.000000] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.000000] setup_percpu: NR_CPUS:512 nr_cpumask_bits:512 nr_cpu_ids:2 nr_node_ids:1
[    0.000000] PERCPU: Embedded 33 pages/cpu @ffff88041fa00000 s98264 r8192 d28712 u1048576
[    0.000000] pcpu-alloc: s98264 r8192 d28712 u1048576 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 0 1
[    0.000000] Built 1 zonelists in Node order, mobility grouping on.  Total pages: 4099882
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.4.0-64-generic root=UUID=9112213a-3570-4904-8969-d5aab8825f6b ro quiet splash vt.handoff=7
[    0.000000] PID hash table entries: 4096 (order: 3, 32768 bytes)
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 16275716K/16660480K available (8452K kernel code, 1293K rwdata, 3980K rodata, 1488K init, 1316K bss, 384764K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	Build-time adjustment of leaf fanout to 64.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=512 to nr_cpu_ids=2.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=64, nr_cpu_ids=2
[    0.000000] NR_IRQS:33024 nr_irqs:440 16
[    0.000000] vt handoff: transparent VT on vt#7
[    0.000000] Console: colour dummy device 80x25
[    0.000000] console [tty0] enabled
[    0.000000] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 133484882848 ns
[    0.000000] hpet clockevent registered
[    0.000000] tsc: Fast TSC calibration using PIT
[    0.000000] tsc: Detected 2793.634 MHz processor
[    0.000031] Calibrating delay loop (skipped), value calculated using timer frequency.. 5587.26 BogoMIPS (lpj=11174536)
[    0.000033] pid_max: default: 32768 minimum: 301
[    0.000038] ACPI: Core revision 20150930
[    0.005982] ACPI: 4 ACPI AML tables successfully acquired and loaded
[    0.005999] Security Framework initialized
[    0.006001] Yama: becoming mindful.
[    0.006015] AppArmor: AppArmor initialized
[    0.006874] Dentry cache hash table entries: 2097152 (order: 12, 16777216 bytes)
[    0.009794] Inode-cache hash table entries: 1048576 (order: 11, 8388608 bytes)
[    0.011066] Mount-cache hash table entries: 32768 (order: 6, 262144 bytes)
[    0.011082] Mountpoint-cache hash table entries: 32768 (order: 6, 262144 bytes)
[    0.011317] Initializing cgroup subsys io
[    0.011320] Initializing cgroup subsys memory
[    0.011326] Initializing cgroup subsys devices
[    0.011328] Initializing cgroup subsys freezer
[    0.011330] Initializing cgroup subsys net_cls
[    0.011332] Initializing cgroup subsys perf_event
[    0.011334] Initializing cgroup subsys net_prio
[    0.011337] Initializing cgroup subsys hugetlb
[    0.011338] Initializing cgroup subsys pids
[    0.011357] CPU: Physical Processor ID: 0
[    0.011358] CPU: Processor Core ID: 0
[    0.011362] ENERGY_PERF_BIAS: Set to 'normal', was 'performance'
[    0.011363] ENERGY_PERF_BIAS: View and update with x86_energy_perf_policy(8)
[    0.011365] mce: CPU supports 7 MCE banks
[    0.011375] CPU0: Thermal monitoring enabled (TM1)
[    0.011381] process: using mwait in idle threads
[    0.011384] Last level iTLB entries: 4KB 512, 2MB 8, 4MB 8
[    0.011384] Last level dTLB entries: 4KB 512, 2MB 32, 4MB 32, 1GB 0
[    0.011758] Freeing SMP alternatives memory: 32K (ffffffff820b9000 - ffffffff820c1000)
[    0.015837] ftrace: allocating 32123 entries in 126 pages
[    0.029893] smpboot: APIC(0) Converting physical 0 to logical package 0
[    0.029895] smpboot: Max logical packages: 1
[    0.030318] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.070006] TSC deadline timer enabled
[    0.070009] smpboot: CPU0: Intel(R) Pentium(R) CPU G640 @ 2.80GHz (family: 0x6, model: 0x2a, stepping: 0x7)
[    0.070028] Performance Events: PEBS fmt1+, 16-deep LBR, SandyBridge events, full-width counters, Intel PMU driver.
[    0.070047] ... version:                3
[    0.070048] ... bit width:              48
[    0.070049] ... generic registers:      8
[    0.070050] ... value mask:             0000ffffffffffff
[    0.070051] ... max period:             00007fffffffffff
[    0.070051] ... fixed-purpose events:   3
[    0.070052] ... event mask:             00000007000000ff
[    0.070751] x86: Booting SMP configuration:
[    0.070752] .... node  #0, CPUs:      #1
[    0.071267] microcode: CPU1 microcode updated early to revision 0x29, date = 2013-06-12
[    0.073348] x86: Booted up 1 node, 2 CPUs
[    0.073351] smpboot: Total of 2 processors activated (11174.53 BogoMIPS)
[    0.073388] NMI watchdog: enabled on all CPUs, permanently consumes one hw-PMU counter.
[    0.074762] devtmpfs: initialized
[    0.078897] evm: security.selinux
[    0.078899] evm: security.SMACK64
[    0.078899] evm: security.SMACK64EXEC
[    0.078900] evm: security.SMACK64TRANSMUTE
[    0.078901] evm: security.SMACK64MMAP
[    0.078902] evm: security.ima
[    0.078903] evm: security.capability
[    0.078959] PM: Registering ACPI NVS region [mem 0xd8db2000-0xd9018fff] (2519040 bytes)
[    0.078988] PM: Registering ACPI NVS region [mem 0xd9025000-0xd9031fff] (53248 bytes)
[    0.078990] PM: Registering ACPI NVS region [mem 0xd9037000-0xd9079fff] (274432 bytes)
[    0.079062] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.079131] pinctrl core: initialized pinctrl subsystem
[    0.079239] RTC time: 18:18:42, date: 03/01/17
[    0.079337] NET: Registered protocol family 16
[    0.090637] cpuidle: using governor ladder
[    0.097353] cpuidle: using governor menu
[    0.097358] PCCT header not found.
[    0.097447] ACPI FADT declares the system doesn't support PCIe ASPM, so disable it
[    0.097448] ACPI: bus type PCI registered
[    0.097450] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.097510] PCI: MMCONFIG for domain 0000 [bus 00-3f] at [mem 0xf8000000-0xfbffffff] (base 0xf8000000)
[    0.097512] PCI: MMCONFIG at [mem 0xf8000000-0xfbffffff] reserved in E820
[    0.097522] PCI: Using configuration type 1 for base access
[    0.097611] NMI watchdog: enabled on all CPUs, permanently consumes one hw-PMU counter.
[    0.097618] core: PMU erratum BJ122, BV98, HSD29 workaround disabled, HT off
[    0.109668] ACPI: Added _OSI(Module Device)
[    0.109670] ACPI: Added _OSI(Processor Device)
[    0.109671] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.109672] ACPI: Added _OSI(Processor Aggregator Device)
[    0.111896] ACPI: Executed 1 blocks of module-level executable AML code
[    0.114009] ACPI: Dynamic OEM Table Load:
[    0.114015] ACPI: SSDT 0xFFFF88040D710000 00083B (v01 PmRef  Cpu0Cst  00003001 INTL 20051117)
[    0.114446] ACPI: Dynamic OEM Table Load:
[    0.114450] ACPI: SSDT 0xFFFF88040D02A000 000303 (v01 PmRef  ApIst    00003000 INTL 20051117)
[    0.114826] ACPI: Dynamic OEM Table Load:
[    0.114829] ACPI: SSDT 0xFFFF88040D63AC00 000119 (v01 PmRef  ApCst    00003000 INTL 20051117)
[    0.115263] ACPI: Interpreter enabled
[    0.115279] ACPI: (supports S0 S3 S4 S5)
[    0.115280] ACPI: Using IOAPIC for interrupt routing
[    0.115303] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.120695] ACPI: Power Resource [FN00] (off)
[    0.120766] ACPI: Power Resource [FN01] (off)
[    0.120834] ACPI: Power Resource [FN02] (off)
[    0.120902] ACPI: Power Resource [FN03] (off)
[    0.120970] ACPI: Power Resource [FN04] (off)
[    0.121440] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-3e])
[    0.121445] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI]
[    0.121548] \_SB_.PCI0:_OSC invalid UUID
[    0.121549] _OSC request data:1 1f 0
[    0.121553] acpi PNP0A08:00: _OSC failed (AE_ERROR); disabling ASPM
[    0.121947] PCI host bridge to bus 0000:00
[    0.121950] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[    0.121951] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]

'''
		return returncode, output

class TestLinuxUbuntu_16_04_X86_64(unittest.TestCase):
	def setUp(self):
		helpers.backup_data_source(cpuinfo)
		helpers.monkey_patch_data_source(cpuinfo, MockDataSource)

	def tearDown(self):
		helpers.restore_data_source(cpuinfo)

	'''
	Make sure calls return the expected number of fields.
	'''
	def test_returns(self):
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_registry()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpufreq_info()))
		self.assertEqual(10, len(cpuinfo._get_cpu_info_from_lscpu()))
		self.assertEqual(11, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(8, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(16, len(cpuinfo.get_cpu_info()))

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand'])
		self.assertEqual('2.0708 GHz', info['hz_advertised'])
		self.assertEqual('2.0708 GHz', info['hz_actual'])
		self.assertEqual((2070796000, 0), info['hz_advertised_raw'])
		self.assertEqual((2070796000, 0), info['hz_actual_raw'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['acpi', 'aperfmperf', 'apic', 'arat', 'arch_perfmon', 'bts',
			'clflush', 'cmov', 'constant_tsc', 'cx16', 'cx8', 'de', 'ds_cpl',
			'dtes64', 'dtherm', 'dts', 'eagerfpu', 'epb', 'ept', 'est',
			'flexpriority', 'fpu', 'fxsr', 'ht', 'lahf_lm', 'lm', 'mca',
			'mce', 'mmx', 'monitor', 'msr', 'mtrr', 'nonstop_tsc', 'nopl',
			'nx', 'pae', 'pat', 'pbe', 'pcid', 'pclmulqdq', 'pdcm', 'pebs',
			'pge', 'pln', 'pni', 'popcnt', 'pse', 'pse36', 'pts', 'rdtscp',
			'rep_good', 'sep', 'ss', 'sse', 'sse2', 'sse4_1', 'sse4_2',
			'ssse3', 'syscall', 'tm', 'tm2', 'tpr_shadow', 'tsc',
			'tsc_deadline_timer', 'vme', 'vmx', 'vnmi', 'vpid', 'xsave',
			'xsaveopt', 'xtopology', 'xtpr']
			,
			info['flags']
		)

	def test_get_cpu_info_from_dmesg(self):
		info = cpuinfo._get_cpu_info_from_dmesg()

		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand'])
		self.assertEqual('2.8000 GHz', info['hz_advertised'])
		self.assertEqual('2.8000 GHz', info['hz_actual'])
		self.assertEqual((2800000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2800000000, 0), info['hz_actual_raw'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand'])
		self.assertEqual('2.8000 GHz', info['hz_advertised'])
		self.assertEqual('1.9014 GHz', info['hz_actual'])
		self.assertEqual((2800000000, 0), info['hz_advertised_raw'])
		self.assertEqual((1901375000, 0), info['hz_actual_raw'])

		self.assertEqual('3072 KB', info['l2_cache_size'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['acpi', 'aperfmperf', 'apic', 'arat', 'arch_perfmon', 'bts',
			'clflush', 'cmov', 'constant_tsc', 'cx16', 'cx8', 'de', 'ds_cpl',
			'dtes64', 'dtherm', 'dts', 'eagerfpu', 'epb', 'ept', 'est',
			'flexpriority', 'fpu', 'fxsr', 'ht', 'lahf_lm', 'lm', 'mca',
			'mce', 'mmx', 'monitor', 'msr', 'mtrr', 'nonstop_tsc', 'nopl',
			'nx', 'pae', 'pat', 'pbe', 'pcid', 'pclmulqdq', 'pdcm', 'pebs',
			'pge', 'pln', 'pni', 'popcnt', 'pse', 'pse36', 'pts', 'rdtscp',
			'rep_good', 'sep', 'ss', 'sse', 'sse2', 'sse4_1', 'sse4_2',
			'ssse3', 'syscall', 'tm', 'tm2', 'tpr_shadow', 'tsc',
			'tsc_deadline_timer', 'vme', 'vmx', 'vnmi', 'vpid', 'xsave',
			'xsaveopt', 'xtopology', 'xtpr']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo.get_cpu_info()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand'])
		self.assertEqual('2.8000 GHz', info['hz_advertised'])
		self.assertEqual('1.9014 GHz', info['hz_actual'])
		self.assertEqual((2800000000, 0), info['hz_advertised_raw'])
		self.assertEqual((1901375000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(2, info['count'])

		self.assertEqual('x86_64', info['raw_arch_string'])

		self.assertEqual('3072 KB', info['l2_cache_size'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['acpi', 'aperfmperf', 'apic', 'arat', 'arch_perfmon', 'bts',
			'clflush', 'cmov', 'constant_tsc', 'cx16', 'cx8', 'de', 'ds_cpl',
			'dtes64', 'dtherm', 'dts', 'eagerfpu', 'epb', 'ept', 'est',
			'flexpriority', 'fpu', 'fxsr', 'ht', 'lahf_lm', 'lm', 'mca',
			'mce', 'mmx', 'monitor', 'msr', 'mtrr', 'nonstop_tsc', 'nopl',
			'nx', 'pae', 'pat', 'pbe', 'pcid', 'pclmulqdq', 'pdcm', 'pebs',
			'pge', 'pln', 'pni', 'popcnt', 'pse', 'pse36', 'pts', 'rdtscp',
			'rep_good', 'sep', 'ss', 'sse', 'sse2', 'sse4_1', 'sse4_2',
			'ssse3', 'syscall', 'tm', 'tm2', 'tpr_shadow', 'tsc',
			'tsc_deadline_timer', 'vme', 'vmx', 'vnmi', 'vpid', 'xsave',
			'xsaveopt', 'xtopology', 'xtpr']
			,
			info['flags']
		)
