

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
	def has_dmesg():
		return True

	@staticmethod
	def has_lscpu():
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
cpu MHz		: 2793.652
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
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc pni pclmulqdq ssse3 cx16 sse4_1 sse4_2 popcnt xsave hypervisor lahf_lm
bogomips	: 5587.30
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
cpu MHz		: 2793.652
cache size	: 3072 KB
physical id	: 0
siblings	: 2
core id		: 1
cpu cores	: 2
apicid		: 1
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc pni pclmulqdq ssse3 cx16 sse4_1 sse4_2 popcnt xsave hypervisor lahf_lm
bogomips	: 5587.30
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:


'''
		return returncode, output

	@staticmethod
	def dmesg_a():
		returncode = 0
		output = '''
[    0.000000] Initializing cgroup subsys cpuset
[    0.000000] Initializing cgroup subsys cpu
[    0.000000] Initializing cgroup subsys cpuacct
[    0.000000] Linux version 3.16.0-4-amd64 (debian-kernel@lists.debian.org) (gcc version 4.8.4 (Debian 4.8.4-1) ) #1 SMP Debian 3.16.36-1+deb8u2 (2016-10-19)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-3.16.0-4-amd64 root=UUID=12618f16-cbe6-4b2b-9f80-b71195be06e7 ro quiet
[    0.000000] e820: BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000dffeffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000dfff0000-0x00000000dfffffff] ACPI data
[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fffc0000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000011fffffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] SMBIOS 2.5 present.
[    0.000000] DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006
[    0.000000] Hypervisor detected: KVM
[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000000] AGP: No AGP bridge found
[    0.000000] e820: last_pfn = 0x120000 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: uncachable
[    0.000000] MTRR variable ranges disabled:
[    0.000000] x86 PAT enabled: cpu 0, old 0x7040600070406, new 0x7010600070106
[    0.000000] CPU MTRRs all blank - virtualized system.
[    0.000000] e820: last_pfn = 0xdfff0 max_arch_pfn = 0x400000000
[    0.000000] found SMP MP-table at [mem 0x0009fff0-0x0009ffff] mapped at [ffff88000009fff0]
[    0.000000] Base memory trampoline at [ffff880000099000] 99000 size 24576
[    0.000000] init_memory_mapping: [mem 0x00000000-0x000fffff]
[    0.000000]  [mem 0x00000000-0x000fffff] page 4k
[    0.000000] BRK [0x01af4000, 0x01af4fff] PGTABLE
[    0.000000] BRK [0x01af5000, 0x01af5fff] PGTABLE
[    0.000000] BRK [0x01af6000, 0x01af6fff] PGTABLE
[    0.000000] init_memory_mapping: [mem 0x11fe00000-0x11fffffff]
[    0.000000]  [mem 0x11fe00000-0x11fffffff] page 2M
[    0.000000] BRK [0x01af7000, 0x01af7fff] PGTABLE
[    0.000000] init_memory_mapping: [mem 0x11c000000-0x11fdfffff]
[    0.000000]  [mem 0x11c000000-0x11fdfffff] page 2M
[    0.000000] init_memory_mapping: [mem 0x100000000-0x11bffffff]
[    0.000000]  [mem 0x100000000-0x11bffffff] page 2M
[    0.000000] init_memory_mapping: [mem 0x00100000-0xdffeffff]
[    0.000000]  [mem 0x00100000-0x001fffff] page 4k
[    0.000000]  [mem 0x00200000-0xdfdfffff] page 2M
[    0.000000]  [mem 0xdfe00000-0xdffeffff] page 4k
[    0.000000] RAMDISK: [mem 0x3634a000-0x3719cfff]
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x00000000000E0000 000024 (v02 VBOX  )
[    0.000000] ACPI: XSDT 0x00000000DFFF0030 00003C (v01 VBOX   VBOXXSDT 00000001 ASL  00000061)
[    0.000000] ACPI: FACP 0x00000000DFFF00F0 0000F4 (v04 VBOX   VBOXFACP 00000001 ASL  00000061)
[    0.000000] ACPI: DSDT 0x00000000DFFF0470 00210F (v01 VBOX   VBOXBIOS 00000002 INTL 20160108)
[    0.000000] ACPI: FACS 0x00000000DFFF0200 000040
[    0.000000] ACPI: FACS 0x00000000DFFF0200 000040
[    0.000000] ACPI: APIC 0x00000000DFFF0240 00005C (v02 VBOX   VBOXAPIC 00000001 ASL  00000061)
[    0.000000] ACPI: SSDT 0x00000000DFFF02A0 0001CC (v01 VBOX   VBOXCPUT 00000002 INTL 20160108)
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] No NUMA configuration found
[    0.000000] Faking a node at [mem 0x0000000000000000-0x000000011fffffff]
[    0.000000] Initmem setup node 0 [mem 0x00000000-0x11fffffff]
[    0.000000]   NODE_DATA [mem 0x11fff7000-0x11fffbfff]
[    0.000000] kvm-clock: Using msrs 4b564d01 and 4b564d00
[    0.000000] kvm-clock: cpu 0, msr 1:1ffef001, primary cpu clock
[    0.000000]  [ffffea0000000000-ffffea0003ffffff] PMD -> [ffff88011b600000-ffff88011effffff] on node 0
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x00001000-0x00ffffff]
[    0.000000]   DMA32    [mem 0x01000000-0xffffffff]
[    0.000000]   Normal   [mem 0x100000000-0x11fffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x00001000-0x0009efff]
[    0.000000]   node   0: [mem 0x00100000-0xdffeffff]
[    0.000000]   node   0: [mem 0x100000000-0x11fffffff]
[    0.000000] On node 0 totalpages: 1048462
[    0.000000]   DMA zone: 56 pages used for memmap
[    0.000000]   DMA zone: 21 pages reserved
[    0.000000]   DMA zone: 3998 pages, LIFO batch:0
[    0.000000]   DMA32 zone: 12488 pages used for memmap
[    0.000000]   DMA32 zone: 913392 pages, LIFO batch:31
[    0.000000]   Normal zone: 1792 pages used for memmap
[    0.000000]   Normal zone: 131072 pages, LIFO batch:31
[    0.000000] ACPI: PM-Timer IO Port: 0x4008
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] ACPI: LAPIC (acpi_id[0x00] lapic_id[0x00] enabled)
[    0.000000] ACPI: LAPIC (acpi_id[0x01] lapic_id[0x01] enabled)
[    0.000000] ACPI: IOAPIC (id[0x02] address[0xfec00000] gsi_base[0])
[    0.000000] IOAPIC[0]: apic_id 2, version 32, address 0xfec00000, GSI 0-23
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ2 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] smpboot: Allowing 2 CPUs, 0 hotplug CPUs
[    0.000000] nr_irqs_gsi: 40
[    0.000000] PM: Registered nosave memory: [mem 0x0009f000-0x0009ffff]
[    0.000000] PM: Registered nosave memory: [mem 0x000a0000-0x000effff]
[    0.000000] PM: Registered nosave memory: [mem 0x000f0000-0x000fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xdfff0000-0xdfffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xe0000000-0xfebfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec00000-0xfec00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec01000-0xfedfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee01000-0xfffbffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfffc0000-0xffffffff]
[    0.000000] e820: [mem 0xe0000000-0xfebfffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on KVM
[    0.000000] setup_percpu: NR_CPUS:512 nr_cpumask_bits:512 nr_cpu_ids:2 nr_node_ids:1
[    0.000000] PERCPU: Embedded 27 pages/cpu @ffff88011fc00000 s80960 r8192 d21440 u1048576
[    0.000000] pcpu-alloc: s80960 r8192 d21440 u1048576 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 0 1
[    0.000000] Built 1 zonelists in Node order, mobility grouping on.  Total pages: 1034105
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-3.16.0-4-amd64 root=UUID=12618f16-cbe6-4b2b-9f80-b71195be06e7 ro quiet
[    0.000000] PID hash table entries: 4096 (order: 3, 32768 bytes)
[    0.000000] xsave: enabled xstate_bv 0x3, cntxt size 0x240
[    0.000000] AGP: Checking aperture...
[    0.000000] AGP: No AGP bridge found
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 4041880K/4193848K available (5237K kernel code, 947K rwdata, 1836K rodata, 1204K init, 840K bss, 151968K reserved)
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	RCU dyntick-idle grace-period acceleration is enabled.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=512 to nr_cpu_ids=2.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=2
[    0.000000] NR_IRQS:33024 nr_irqs:512 16
[    0.000000] Console: colour VGA+ 80x25
[    0.000000] console [tty0] enabled
[    0.000000] tsc: Detected 2793.652 MHz processor
[    9.015923] Calibrating delay loop (skipped) preset value.. 5587.30 BogoMIPS (lpj=11174608)
[    9.015926] pid_max: default: 32768 minimum: 301
[    9.015934] ACPI: Core revision 20140424
[    9.017020] ACPI: All ACPI Tables successfully acquired
[    9.017050] Security Framework initialized
[    9.017058] AppArmor: AppArmor disabled by boot time parameter
[    9.017059] Yama: disabled by default; enable with sysctl kernel.yama.*
[    9.017855] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes)
[    9.019277] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes)
[    9.019613] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes)
[    9.019619] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes)
[    9.019883] Initializing cgroup subsys memory
[    9.019888] Initializing cgroup subsys devices
[    9.019895] Initializing cgroup subsys freezer
[    9.019897] Initializing cgroup subsys net_cls
[    9.019901] Initializing cgroup subsys blkio
[    9.019904] Initializing cgroup subsys perf_event
[    9.019906] Initializing cgroup subsys net_prio
[    9.019987] CPU: Physical Processor ID: 0
[    9.019988] CPU: Processor Core ID: 0
[    9.020005] mce: CPU supports 0 MCE banks
[    9.020039] Last level iTLB entries: 4KB 512, 2MB 8, 4MB 8
Last level dTLB entries: 4KB 512, 2MB 32, 4MB 32, 1GB 0
tlb_flushall_shift: 6
[    9.020376] Freeing SMP alternatives memory: 20K (ffffffff81a1b000 - ffffffff81a20000)
[    9.024990] ftrace: allocating 21697 entries in 85 pages
[    9.059874] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    9.059878] smpboot: CPU0: Intel(R) Pentium(R) CPU G640 @ 2.80GHz (fam: 06, model: 2a, stepping: 07)
[    9.164299] Performance Events: unsupported p6 CPU model 42 no PMU driver, software events only.
[    9.165780] NMI watchdog: disabled (cpu0): hardware events not enabled
[    9.165895] x86: Booting SMP configuration:
[    9.165897] .... node  #0, CPUs:      #1
[    9.176166] kvm-clock: cpu 1, msr 1:1ffef041, secondary cpu clock
[    9.177165] mce: CPU supports 0 MCE banks
[    9.179301] x86: Booted up 1 node, 2 CPUs
[    9.179305] smpboot: Total of 2 processors activated (11174.60 BogoMIPS)
[    9.180688] devtmpfs: initialized
[    9.187316] pinctrl core: initialized pinctrl subsystem
[    9.187487] NET: Registered protocol family 16
[    9.187619] cpuidle: using governor ladder
[    9.187623] cpuidle: using governor menu
[    9.187667] ACPI: bus type PCI registered
[    9.187669] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    9.187894] PCI: Using configuration type 1 for base access
[    9.204747] ACPI: Added _OSI(Module Device)
[    9.204751] ACPI: Added _OSI(Processor Device)
[    9.204752] ACPI: Added _OSI(3.0 _SCP Extensions)
[    9.204753] ACPI: Added _OSI(Processor Aggregator Device)
[    9.205356] ACPI: Executed 1 blocks of module-level executable AML code
[    9.207882] ACPI: Interpreter enabled
[    9.207888] ACPI Exception: AE_NOT_FOUND, While evaluating Sleep State [\_S1_] (20140424/hwxface-580)
[    9.207891] ACPI Exception: AE_NOT_FOUND, While evaluating Sleep State [\_S2_] (20140424/hwxface-580)
[    9.207894] ACPI Exception: AE_NOT_FOUND, While evaluating Sleep State [\_S3_] (20140424/hwxface-580)
[    9.207897] ACPI Exception: AE_NOT_FOUND, While evaluating Sleep State [\_S4_] (20140424/hwxface-580)
[    9.207902] ACPI: (supports S0 S5)
[    9.207904] ACPI: Using IOAPIC for interrupt routing
[    9.208077] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    9.211597] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])
[    9.211603] acpi PNP0A03:00: _OSC: OS supports [ASPM ClockPM Segments MSI]
[    9.211607] acpi PNP0A03:00: _OSC failed (AE_NOT_FOUND); disabling ASPM
[    9.211681] acpi PNP0A03:00: fail to add MMCONFIG information, can't access extended PCI configuration space under this bridge.
[    9.211887] PCI host bridge to bus 0000:00
[    9.211890] pci_bus 0000:00: root bus resource [bus 00-ff]
[    9.211892] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7]
[    9.211893] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff]
[    9.211895] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff]
[    9.211896] pci_bus 0000:00: root bus resource [mem 0xe0000000-0xffdfffff]
[    9.211930] pci 0000:00:00.0: [8086:1237] type 00 class 0x060000
[    9.212373] pci 0000:00:01.0: [8086:7000] type 00 class 0x060100
[    9.212889] pci 0000:00:01.1: [8086:7111] type 00 class 0x01018a
[    9.213393] pci 0000:00:01.1: reg 0x20: [io  0xd000-0xd00f]
[    9.213530] pci 0000:00:01.1: legacy IDE quirk: reg 0x10: [io  0x01f0-0x01f7]
[    9.213532] pci 0000:00:01.1: legacy IDE quirk: reg 0x14: [io  0x03f6]
[    9.213533] pci 0000:00:01.1: legacy IDE quirk: reg 0x18: [io  0x0170-0x0177]
[    9.213534] pci 0000:00:01.1: legacy IDE quirk: reg 0x1c: [io  0x0376]
[    9.213732] pci 0000:00:02.0: [80ee:beef] type 00 class 0x030000
[    9.216760] pci 0000:00:02.0: reg 0x10: [mem 0xe0000000-0xe0ffffff pref]
[    9.239260] pci 0000:00:03.0: [8086:100e] type 00 class 0x020000
[    9.242528] pci 0000:00:03.0: reg 0x10: [mem 0xf0000000-0xf001ffff]
[    9.250446] pci 0000:00:03.0: reg 0x18: [io  0xd010-0xd017]
[    9.267404] pci 0000:00:04.0: [80ee:cafe] type 00 class 0x088000
[    9.270818] pci 0000:00:04.0: reg 0x10: [io  0xd020-0xd03f]
[    9.276122] pci 0000:00:04.0: reg 0x14: [mem 0xf0400000-0xf07fffff]
[    9.279813] pci 0000:00:04.0: reg 0x18: [mem 0xf0800000-0xf0803fff pref]
[    9.293767] pci 0000:00:05.0: [8086:2415] type 00 class 0x040100
[    9.293857] pci 0000:00:05.0: reg 0x10: [io  0xd100-0xd1ff]
[    9.293917] pci 0000:00:05.0: reg 0x14: [io  0xd200-0xd23f]
[    9.294374] pci 0000:00:06.0: [106b:003f] type 00 class 0x0c0310
[    9.297803] pci 0000:00:06.0: reg 0x10: [mem 0xf0804000-0xf0804fff]
[    9.317868] pci 0000:00:07.0: [8086:7113] type 00 class 0x068000
[    9.318252] pci 0000:00:07.0: quirk: [io  0x4000-0x403f] claimed by PIIX4 ACPI
[    9.318262] pci 0000:00:07.0: quirk: [io  0x4100-0x410f] claimed by PIIX4 SMB
[    9.318538] pci 0000:00:0d.0: [8086:2829] type 00 class 0x010601
[    9.321461] pci 0000:00:0d.0: reg 0x10: [io  0xd240-0xd247]
[    9.328895] pci 0000:00:0d.0: reg 0x18: [io  0xd250-0xd257]
[    9.336455] pci 0000:00:0d.0: reg 0x20: [io  0xd260-0xd26f]
[    9.339258] pci 0000:00:0d.0: reg 0x24: [mem 0xf0806000-0xf0807fff]
[    9.345202] ACPI: PCI Interrupt Link [LNKA] (IRQs 5 9 10 *11)
[    9.345408] ACPI: PCI Interrupt Link [LNKB] (IRQs 5 9 10 *11)
[    9.345488] ACPI: PCI Interrupt Link [LNKC] (IRQs 5 9 *10 11)
[    9.345567] ACPI: PCI Interrupt Link [LNKD] (IRQs 5 *9 10 11)
[    9.345694] ACPI: Enabled 2 GPEs in block 00 to 07
[    9.346069] vgaarb: setting as boot device: PCI:0000:00:02.0
[    9.346072] vgaarb: device added: PCI:0000:00:02.0,decodes=io+mem,owns=io+mem,locks=none
[    9.346074] vgaarb: loaded
[    9.346075] vgaarb: bridge control possible 0000:00:02.0
[    9.346163] PCI: Using ACPI for IRQ routing
[    9.346165] PCI: pci_cache_line_size set to 64 bytes
[    9.346311] e820: reserve RAM buffer [mem 0x0009fc00-0x0009ffff]
[    9.346317] e820: reserve RAM buffer [mem 0xdfff0000-0xdfffffff]
[    9.346558] Switched to clocksource kvm-clock
[    9.353995] pnp: PnP ACPI init
[    9.354008] ACPI: bus type PNP registered
[    9.354101] pnp 00:00: Plug and Play ACPI device, IDs PNP0303 (active)
[    9.354188] pnp 00:01: Plug and Play ACPI device, IDs PNP0f03 (active)
[    9.354752] pnp: PnP ACPI: found 2 devices
[    9.354753] ACPI: bus type PNP unregistered
[    9.371389] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7]
[    9.371393] pci_bus 0000:00: resource 5 [io  0x0d00-0xffff]
[    9.371395] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff]
[    9.371396] pci_bus 0000:00: resource 7 [mem 0xe0000000-0xffdfffff]
[    9.371619] NET: Registered protocol family 2
[    9.372196] TCP established hash table entries: 32768 (order: 6, 262144 bytes)
[    9.372267] TCP bind hash table entries: 32768 (order: 7, 524288 bytes)
[    9.372334] TCP: Hash tables configured (established 32768 bind 32768)
[    9.372351] TCP: reno registered
[    9.372357] UDP hash table entries: 2048 (order: 4, 65536 bytes)
[    9.372372] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes)
[    9.372507] NET: Registered protocol family 1
[    9.372527] pci 0000:00:00.0: Limiting direct PCI/PCI transfers
[    9.372559] pci 0000:00:01.0: Activating ISA DMA hang workarounds
[    9.372585] pci 0000:00:02.0: Video device with shadowed ROM
[    9.374015] PCI: CLS 0 bytes, default 64
[    9.374087] Unpacking initramfs...
[    9.647919] Freeing initrd memory: 14668K (ffff88003634a000 - ffff88003719d000)
[    9.648004] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    9.648007] software IO TLB [mem 0xdbff0000-0xdfff0000] (64MB) mapped at [ffff8800dbff0000-ffff8800dffeffff]
[    9.648272] platform rtc_cmos: registered platform RTC device (no PNP device found)
[    9.648443] RAPL PMU detected, hw unit 2^-0 Joules, API unit is 2^-32 Joules, 3 fixed counters 10737418240 ms ovfl timer
[    9.648548] microcode: CPU0 sig=0x206a7, pf=0x10, revision=0x0
[    9.648562] microcode: CPU1 sig=0x206a7, pf=0x10, revision=0x0
[    9.648612] microcode: Microcode Update Driver: v2.00 <tigran@aivazian.fsnet.co.uk>, Peter Oruba
[    9.649451] futex hash table entries: 512 (order: 3, 32768 bytes)
[    9.649573] audit: initializing netlink subsys (disabled)
[    9.649598] audit: type=2000 audit(1488395362.069:1): initialized
[    9.650419] HugeTLB registered 2 MB page size, pre-allocated 0 pages
[    9.650441] zbud: loaded
[    9.650973] VFS: Disk quotas dquot_6.5.2
[    9.651008] Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    9.651084] msgmni has been set to 7922
[    9.651798] alg: No test for stdrng (krng)
[    9.651846] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 252)
[    9.651937] io scheduler noop registered
[    9.651941] io scheduler deadline registered
[    9.652016] io scheduler cfq registered (default)
[    9.652115] pci_hotplug: PCI Hot Plug PCI Core version: 0.5
[    9.652132] pciehp: PCI Express Hot Plug Controller Driver version: 0.4
[    9.652154] intel_idle: does not run on family 6 model 42
[    9.652172] GHES: HEST is not enabled!
[    9.652242] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    9.652548] Linux agpgart interface v0.103
[    9.652677] i8042: PNP: PS/2 Controller [PNP0303:PS2K,PNP0f03:PS2M] at 0x60,0x64 irq 1,12
[    9.653166] serio: i8042 KBD port at 0x60,0x64 irq 1
[    9.653171] serio: i8042 AUX port at 0x60,0x64 irq 12
[    9.653271] mousedev: PS/2 mouse device common for all mice
[    9.653687] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input0
[    9.653824] rtc_cmos rtc_cmos: rtc core: registered rtc_cmos as rtc0
[    9.653882] rtc_cmos rtc_cmos: alarms up to one day, 114 bytes nvram
[    9.653896] ledtrig-cpu: registered to indicate activity on CPUs
[    9.653961] AMD IOMMUv2 driver by Joerg Roedel <joerg.roedel@amd.com>
[    9.653962] AMD IOMMUv2 functionality not available on this system
[    9.654038] TCP: cubic registered
[    9.654234] NET: Registered protocol family 10
[    9.654554] mip6: Mobile IPv6
[    9.654558] NET: Registered protocol family 17
[    9.654564] mpls_gso: MPLS GSO support
[    9.654770] registered taskstats version 1
[    9.656357] rtc_cmos rtc_cmos: setting system clock to 2017-03-01 19:09:11 UTC (1488395351)
[    9.656427] PM: Hibernation image not present or could not be loaded.
[    9.663167] Freeing unused kernel memory: 1204K (ffffffff818ee000 - ffffffff81a1b000)
[    9.663171] Write protecting the kernel read-only data: 8192k
[    9.663645] Freeing unused kernel memory: 896K (ffff880001520000 - ffff880001600000)
[    9.664120] Freeing unused kernel memory: 212K (ffff8800017cb000 - ffff880001800000)
[    9.677467] systemd-udevd[60]: starting version 215
[    9.677730] random: systemd-udevd urandom read with 2 bits of entropy available
[    9.698416] ACPI: bus type USB registered
[    9.698445] usbcore: registered new interface driv

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
CPU MHz:               2793.652
BogoMIPS:              5587.30
Hypervisor vendor:     KVM
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              3072K
NUMA node0 CPU(s):     0,1

'''
		return returncode, output


class TestLinuxFedora_24_X86_64(unittest.TestCase):
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
		self.assertEqual(9, len(cpuinfo._get_cpu_info_from_lscpu()))
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
		self.assertEqual('2.7937 GHz', info['hz_advertised'])
		self.assertEqual('2.7937 GHz', info['hz_actual'])
		self.assertEqual((2793652000, 0), info['hz_advertised_raw'])
		self.assertEqual((2793652000, 0), info['hz_actual_raw'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])

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
		self.assertEqual('2.7937 GHz', info['hz_actual'])
		self.assertEqual((2800000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2793652000, 0), info['hz_actual_raw'])

		self.assertEqual('3072 KB', info['l2_cache_size'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['apic', 'clflush', 'cmov', 'constant_tsc', 'cx16', 'cx8', 'de',
			'fpu', 'fxsr', 'ht', 'hypervisor', 'lahf_lm', 'lm', 'mca', 'mce',
			'mmx', 'msr', 'mtrr', 'nonstop_tsc', 'nopl', 'nx', 'pae', 'pat',
			'pclmulqdq', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'rdtscp',
			'rep_good', 'sep', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'ssse3',
			'syscall', 'tsc', 'vme', 'xsave', 'xtopology']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo.get_cpu_info()

		self.assertEqual('GenuineIntel', info['vendor_id'])
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand'])
		self.assertEqual('2.8000 GHz', info['hz_advertised'])
		self.assertEqual('2.7937 GHz', info['hz_actual'])
		self.assertEqual((2800000000, 0), info['hz_advertised_raw'])
		self.assertEqual((2793652000, 0), info['hz_actual_raw'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(2, info['count'])

		self.assertEqual('x86_64', info['raw_arch_string'])

		self.assertEqual('3072 KB', info['l2_cache_size'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])
		self.assertEqual(
			['apic', 'clflush', 'cmov', 'constant_tsc', 'cx16', 'cx8', 'de',
			'fpu', 'fxsr', 'ht', 'hypervisor', 'lahf_lm', 'lm', 'mca', 'mce',
			'mmx', 'msr', 'mtrr', 'nonstop_tsc', 'nopl', 'nx', 'pae', 'pat',
			'pclmulqdq', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'rdtscp',
			'rep_good', 'sep', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'ssse3',
			'syscall', 'tsc', 'vme', 'xsave', 'xtopology']
			,
			info['flags']
		)
