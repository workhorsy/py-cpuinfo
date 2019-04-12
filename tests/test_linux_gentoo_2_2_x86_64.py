

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 2
	is_windows = False
	arch_string_raw = 'x86_64'
	uname_string_raw = 'x86_64'
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
bugs		:
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
bugs		:
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
===============================================================================
[    0.000000] Linux version 4.5.2-aufs-r1 (root@jasmin) (gcc version 5.4.0 (Gentoo 5.4.0 p1.0, pie-0.6.5) ) #1 SMP Sun Jul 3 17:17:11 UTC 2016
[    0.000000] Command line: BOOT_IMAGE=/isolinux/gentoo root=/dev/ram0 init=/linuxrc dokeymap aufs looptype=squashfs loop=/image.squashfs cdroot initrd=/isolinux/gentoo.xz console=tty1
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Centaur CentaurHauls
[    0.000000] x86/fpu: Supporting XSAVE feature 0x01: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x02: 'SSE registers'
[    0.000000] x86/fpu: Enabled xstate features 0x3, context size is 576 bytes, using 'standard' format.
[    0.000000] x86/fpu: Using 'lazy' FPU context switches.
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
[    0.000000] e820: last_pfn = 0x120000 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: uncachable
[    0.000000] MTRR variable ranges disabled:
[    0.000000] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WC  UC- WT
[    0.000000] MTRR: Disabled
[    0.000000] CPU MTRRs all blank - virtualized system.
[    0.000000] e820: last_pfn = 0xdfff0 max_arch_pfn = 0x400000000
[    0.000000] found SMP MP-table at [mem 0x0009fff0-0x0009ffff] mapped at [ffff88000009fff0]
[    0.000000] Base memory trampoline at [ffff880000099000] 99000 size 24576
[    0.000000] BRK [0x13b4e000, 0x13b4efff] PGTABLE
[    0.000000] BRK [0x13b4f000, 0x13b4ffff] PGTABLE
[    0.000000] BRK [0x13b50000, 0x13b50fff] PGTABLE
[    0.000000] BRK [0x13b51000, 0x13b51fff] PGTABLE
[    0.000000] RAMDISK: [mem 0x7f894000-0x7fffffff]
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
[    0.000000] kvm-clock: Using msrs 4b564d01 and 4b564d00
[    0.000000] kvm-clock: cpu 0, msr 1:1fffb001, primary cpu clock
[    0.000000] kvm-clock: using sched offset of 7895112535 cycles
[    0.000000] clocksource: kvm-clock: mask: 0xffffffffffffffff max_cycles: 0x1cd42e4dffb, max_idle_ns: 881590591483 ns
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.000000]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x000000011fffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000001000-0x000000000009efff]
[    0.000000]   node   0: [mem 0x0000000000100000-0x00000000dffeffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x000000011fffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000001000-0x000000011fffffff]
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
[    0.000000] IOAPIC[0]: apic_id 2, version 32, address 0xfec00000, GSI 0-23
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] smpboot: Allowing 2 CPUs, 0 hotplug CPUs
[    0.000000] e820: [mem 0xe0000000-0xfebfffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on KVM
[    0.000000] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 1910969940391419 ns
[    0.000000] setup_percpu: NR_CPUS:64 nr_cpumask_bits:64 nr_cpu_ids:2 nr_node_ids:1
[    0.000000] PERCPU: Embedded 32 pages/cpu @ffff88011fc00000 s90328 r8192 d32552 u1048576
[    0.000000] pcpu-alloc: s90328 r8192 d32552 u1048576 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 0 1
[    0.000000] PV qspinlock hash table entries: 256 (order: 0, 4096 bytes)
[    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 1034105
[    0.000000] Kernel command line: BOOT_IMAGE=/isolinux/gentoo root=/dev/ram0 init=/linuxrc dokeymap aufs looptype=squashfs loop=/image.squashfs cdroot initrd=/isolinux/gentoo.xz console=tty1
[    0.000000] PID hash table entries: 4096 (order: 3, 32768 bytes)
[    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes)
[    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes)
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 4026248K/4193848K available (5358K kernel code, 481K rwdata, 2712K rodata, 1016K init, 16188K bss, 167600K reserved, 0K cma-reserved)
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	Build-time adjustment of leaf fanout to 64.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=64 to nr_cpu_ids=2.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=64, nr_cpu_ids=2
[    0.000000] NR_IRQS:4352 nr_irqs:440 16
[    0.000000] Console: colour VGA+ 80x25
[    0.000000] console [tty1] enabled
[    0.000000] tsc: Detected 2793.652 MHz processor
[    0.141160] Calibrating delay loop (skipped) preset value.. 5587.30 BogoMIPS (lpj=2793652)
[    0.142104] pid_max: default: 32768 minimum: 301
[    0.142638] ACPI: Core revision 20160108
[    0.144223] ACPI: 2 ACPI AML tables successfully acquired and loaded

[    0.145332] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes)
[    0.145866] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes)
[    0.147608] CPU: Physical Processor ID: 0
[    0.148126] CPU: Processor Core ID: 0
[    0.148586] mce: CPU supports 0 MCE banks
[    0.149092] Last level iTLB entries: 4KB 512, 2MB 8, 4MB 8
[    0.149586] Last level dTLB entries: 4KB 512, 2MB 32, 4MB 32, 1GB 0
[    0.152341] Freeing SMP alternatives memory: 24K (ffffffff92b78000 - ffffffff92b7e000)
[    0.163230] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.265101] smpboot: CPU0: Intel(R) Pentium(R) CPU G640 @ 2.80GHz (family: 0x6, model: 0x2a, stepping: 0x7)
[    0.266299] Performance Events: unsupported p6 CPU model 42 no PMU driver, software events only.
[    0.267306] KVM setup paravirtual spinlock
[    0.267966] x86: Booting SMP configuration:
[    0.269313] .... node  #0, CPUs:      #1
[    0.270050] kvm-clock: cpu 1, msr 1:1fffb041, secondary cpu clock
[    0.270195] mce: CPU supports 0 MCE banks
[    0.272308] x86: Booted up 1 node, 2 CPUs
[    0.274066] smpboot: Total of 2 processors activated (11174.60 BogoMIPS)
[    0.277750] devtmpfs: initialized
[    0.278904] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 1911260446275000 ns
[    0.280007] NET: Registered protocol family 16
[    0.282919] cpuidle: using governor ladder
[    0.287045] cpuidle: using governor menu
[    0.287596] ACPI: bus type PCI registered
[    0.288197] PCI: Using configuration type 1 for base access
[    0.296438] ACPI: Added _OSI(Module Device)
[    0.296920] ACPI: Added _OSI(Processor Device)
[    0.297365] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.297812] ACPI: Added _OSI(Processor Aggregator Device)
[    0.298811] ACPI: Executed 1 blocks of module-level executable AML code
[    0.301871] ACPI: Interpreter enabled
[    0.302325] ACPI: (supports S0 S5)
[    0.302733] ACPI: Using IOAPIC for interrupt routing
[    0.303373] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.311397] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])
[    0.311943] acpi PNP0A03:00: _OSC: OS supports [ASPM ClockPM Segments MSI]
[    0.312695] acpi PNP0A03:00: _OSC failed (AE_NOT_FOUND); disabling ASPM
[    0.313427] acpi PNP0A03:00: fail to add MMCONFIG information, can't access extended PCI configuration space under this bridge.
[    0.314671] PCI host bridge to bus 0000:00
[    0.315139] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[    0.315651] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.316170] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.316921] pci_bus 0000:00: root bus resource [mem 0xe0000000-0xffdfffff window]
[    0.317667] pci_bus 0000:00: root bus resource [bus 00-ff]
[    0.318183] pci 0000:00:00.0: [8086:1237] type 00 class 0x060000
[    0.318651] pci 0000:00:01.0: [8086:7000] type 00 class 0x060100
[    0.319190] pci 0000:00:01.1: [8086:7111] type 00 class 0x01018a
[    0.319507] pci 0000:00:01.1: reg 0x20: [io  0xd000-0xd00f]
[    0.319637] pci 0000:00:01.1: legacy IDE quirk: reg 0x10: [io  0x01f0-0x01f7]
[    0.320177] pci 0000:00:01.1: legacy IDE quirk: reg 0x14: [io  0x03f6]
[    0.320691] pci 0000:00:01.1: legacy IDE quirk: reg 0x18: [io  0x0170-0x0177]
[    0.321218] pci 0000:00:01.1: legacy IDE quirk: reg 0x1c: [io  0x0376]
[    0.321916] pci 0000:00:02.0: [80ee:beef] type 00 class 0x030000
[    0.331110] pci 0000:00:02.0: reg 0x10: [mem 0xe0000000-0xe0ffffff pref]
[    0.355210] pci 0000:00:03.0: [8086:100e] type 00 class 0x020000
[    0.362376] pci 0000:00:03.0: reg 0x10: [mem 0xf0000000-0xf001ffff]
[    0.368405] pci 0000:00:03.0: reg 0x18: [io  0xd010-0xd017]
[    0.382823] pci 0000:00:04.0: [80ee:cafe] type 00 class 0x088000
[    0.385993] pci 0000:00:04.0: reg 0x10: [io  0xd020-0xd03f]
[    0.390088] pci 0000:00:04.0: reg 0x14: [mem 0xf0400000-0xf07fffff]
[    0.396674] pci 0000:00:04.0: reg 0x18: [mem 0xf0800000-0xf0803fff pref]
[    0.408760] pci 0000:00:05.0: [8086:2415] type 00 class 0x040100
[    0.408846] pci 0000:00:05.0: reg 0x10: [io  0xd100-0xd1ff]
[    0.408903] pci 0000:00:05.0: reg 0x14: [io  0xd200-0xd23f]
[    0.409378] pci 0000:00:06.0: [106b:003f] type 00 class 0x0c0310
[    0.412327] pci 0000:00:06.0: reg 0x10: [mem 0xf0804000-0xf0804fff]
[    0.438003] pci 0000:00:07.0: [8086:7113] type 00 class 0x068000
[    0.438389] pci 0000:00:07.0: quirk: [io  0x4000-0x403f] claimed by PIIX4 ACPI
[    0.439849] pci 0000:00:07.0: quirk: [io  0x4100-0x410f] claimed by PIIX4 SMB
[    0.440790] pci 0000:00:0d.0: [8086:2829] type 00 class 0x010601
[    0.446112] pci 0000:00:0d.0: reg 0x10: [io  0xd240-0xd247]
[    0.453981] pci 0000:00:0d.0: reg 0x18: [io  0xd250-0xd257]
[    0.465205] pci 0000:00:0d.0: reg 0x20: [io  0xd260-0xd26f]
[    0.468499] pci 0000:00:0d.0: reg 0x24: [mem 0xf0806000-0xf0807fff]
[    0.473155] pci_bus 0000:00: on NUMA node 0
[    0.474092] ACPI: PCI Interrupt Link [LNKA] (IRQs 5 9 10 *11)
[    0.476734] ACPI: PCI Interrupt Link [LNKB] (IRQs 5 9 10 *11)
[    0.478927] ACPI: PCI Interrupt Link [LNKC] (IRQs 5 9 *10 11)
[    0.480187] ACPI: PCI Interrupt Link [LNKD] (IRQs 5 *9 10 11)
[    0.483221] ACPI: Enabled 2 GPEs in block 00 to 07
[    0.484401] vgaarb: setting as boot device: PCI:0000:00:02.0
[    0.484962] vgaarb: device added: PCI:0000:00:02.0,decodes=io+mem,owns=io+mem,locks=none
[    0.486436] vgaarb: loaded
[    0.486866] vgaarb: bridge control possible 0000:00:02.0
[    0.487529] SCSI subsystem initialized
[    0.488105] libata version 3.00 loaded.
[    0.488124] ACPI: bus type USB registered
[    0.488601] usbcore: registered new interface driver usbfs
[    0.489127] usbcore: registered new interface driver hub
[    0.489642] usbcore: registered new device driver usb
[    0.493140] PCI: Using ACPI for IRQ routing
[    0.493596] PCI: pci_cache_line_size set to 64 bytes
[    0.493741] e820: reserve RAM buffer [mem 0x0009fc00-0x0009ffff]
[    0.493748] e820: reserve RAM buffer [mem 0xdfff0000-0xdfffffff]
[    0.501262] clocksource: Switched to clocksource kvm-clock
[    0.501975] VFS: Disk quotas dquot_6.6.0
[    0.502483] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.515233] pnp: PnP ACPI init
[    0.515724] pnp 00:00: Plug and Play ACPI device, IDs PNP0303 (active)
[    0.515794] pnp 00:01: Plug and Play ACPI device, IDs PNP0f03 (active)
[    0.516395] pnp: PnP ACPI: found 2 devices
[    0.521420] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.523924] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7 window]
[    0.523928] pci_bus 0000:00: resource 5 [io  0x0d00-0xffff window]
[    0.523930] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff window]
[    0.523932] pci_bus 0000:00: resource 7 [mem 0xe0000000-0xffdfffff window]
[    0.526813] NET: Registered protocol family 2
[    0.527577] TCP established hash table entries: 32768 (order: 6, 262144 bytes)
[    0.528532] TCP bind hash table entries: 32768 (order: 7, 524288 bytes)
[    0.529234] TCP: Hash tables configured (established 32768 bind 32768)
[    0.529765] UDP hash table entries: 2048 (order: 4, 65536 bytes)
[    0.530287] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes)
[    0.544043] NET: Registered protocol family 1
[    0.544613] pci 0000:00:00.0: Limiting direct PCI/PCI transfers
[    0.545245] pci 0000:00:01.0: Activating ISA DMA hang workarounds
[    0.545791] pci 0000:00:02.0: Video device with shadowed ROM
[    0.547149] PCI: CLS 0 bytes, default 64
[    0.547884] Trying to unpack rootfs image as initramfs...
[    1.394034] Freeing initrd memory: 7600K (ffff88007f894000 - ffff880080000000)
[    1.394891] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    1.395861] software IO TLB [mem 0xdbff0000-0xdfff0000] (64MB) mapped at [ffff8800dbff0000-ffff8800dffeffff]
[    1.397095] platform rtc_cmos: registered platform RTC device (no PNP device found)
[    1.397910] RAPL PMU detected, API unit is 2^-32 Joules, 3 fixed counters 10737418240 ms ovfl timer
[    1.398684] hw unit of domain pp0-core 2^-0 Joules
[    1.399166] hw unit of domain package 2^-0 Joules
[    1.399618] hw unit of domain pp1-gpu 2^-0 Joules
[    1.400492] futex hash table entries: 512 (order: 3, 32768 bytes)
[    1.401169] audit: initializing netlink subsys (disabled)
[    1.401668] audit: type=2000 audit(1488272619.420:1): initialized
[    1.402282] Initialise system trusted keyring
[    1.403474] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    1.404117] JFS: nTxBlock = 8192, nTxLock = 65536
[    1.406745] SGI XFS with ACLs, security attributes, realtime, no debug enabled
[    1.408178] aufs 4.5-20160328
[    1.418164] Key type asymmetric registered
[    1.418627] Asymmetric key parser 'x509' registered
[    1.419179] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 253)
[    1.419974] io scheduler noop registered
[    1.420429] io scheduler deadline registered (default)
[    1.421010] start plist test
[    1.422756] end plist test
[    1.422768] Running rhashtable test nelem=8, max_size=0, shrinking=0
[    1.423312] Test 00:
[    1.425541]   Adding 50000 keys
[    1.453370]   Traversal complete: counted=50000, nelems=50000, entries=50000, table-jumps=0
[    1.465493]   Traversal complete: counted=50000, nelems=50000, entries=50000, table-jumps=0
[    1.466339]   Deleting 50000 keys
[    1.472526]   Duration of test: 46526457 ns
[    1.473240] Test 01:
[    1.474878]   Adding 50000 keys
[    1.487127]   Traversal complete: counted=50000, nelems=50000, entries=50000, table-jumps=0
[    1.496559]   Traversal complete: counted=50000, nelems=50000, entries=50000, table-jumps=0
[    1.497384]   Deleting 50000 keys
[    1.506520]   Duration of test: 31074162 ns
[    1.507191] Test 02:
[    1.509281]   Adding 50000 keys
[    1.522531]   Traversal complete: counted=50000, nelems=50000, entries=50000, table-jumps=0
[    1.532936]   Traversal complete: counted=50000, nelems=50000, entries=50000, table-jumps=0
[    1.533744]   Deleting 50000 keys
[    1.541847]   Duration of test: 32005815 ns
[    1.543742] Test 03:
[    1.545394]   Adding 50000 keys
[    1.560340]   Traversal complete: counted=50000, nelems=50000, entries=50000, table-jumps=0
[    1.568083]   Traversal complete: counted=50000, nelems=50000, entries=50000, table-jumps=0
[    1.568920]   Deleting 50000 keys
[    1.578421]   Duration of test: 32488444 ns
[    1.578926] Average test time: 35523719
[    1.579370] Testing concurrent rhashtable access from 10 threads
[    1.649031]   thread[6]: rhashtable_insert_fast failed
[    1.649033]   thread[7]: rhashtable_insert_fast failed
[    1.649038]   thread[9]: rhashtable_insert_fast failed
[    1.649039]   thread[3]: rhashtable_insert_fast failed
[    1.649041]   thread[8]: rhashtable_insert_fast failed
[    1.649043]   thread[5]: rhashtable_insert_fast failed
[    1.649044]   thread[1]: rhashtable_insert_fast failed
[    1.831026] Test failed: thread 1 returned: -12
[    1.855279] Test failed: thread 3 returned: -12
[    1.859276] Test failed: thread 5 returned: -12
[    1.859887] Test failed: thread 6 returned: -12
[    1.860379] Test failed: thread 7 returned: -12
[    1.860838] Test failed: thread 8 returned: -12
[    1.861335] Test failed: thread 9 returned: -12
[    1.861782] Started 10 threads, 7 failed
[    1.862508] glob: 64 self-tests passed, 0 failed
[    1.863134] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    1.863988] Linux agpgart interface v0.103
[    1.864625] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input0
[    1.865411] ACPI: Power Button [PWRF]
[    1.865899] input: Sleep Button as /devices/LNXSYSTM:00/LNXSLPBN:00/input/input1
[    1.867173] ACPI: Sleep Button [SLPF]
[    1.868220] ACPI: Video Device [GFX0] (multi-head: yes  rom: no  post: no)
[    1.868877] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/LNXVIDEO:00/input/input2
[    1.870085] xenfs: not registering filesystem on non-xen platform
[    1.877055] brd: module loaded
[    1.879394] loop: module loaded
[    1.880002] usbcore: registered new interface driver hwa-rc
[    1.880518] usbcore: registered new interface driver i1480-dfu-usb
[    1.881078] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    1.881591] ehci-pci: EHCI PCI platform driver
[    1.882074] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    1.882586] uhci_hcd: USB Universal Host Controller Interface driver
[    1.883306] usbcore: registered new interface driver wusb-cbaf
[    1.883805] usbcore: registered new interface driver cdc_wdm
[    1.884348] i8042: PNP: PS/2 Controller [PNP0303:PS2K,PNP0f03:PS2M] at 0x60,0x64 irq 1,12
[    1.885658] serio: i8042 KBD port at 0x60,0x64 irq 1
[    1.886150] serio: i8042 AUX port at 0x60,0x64 irq 12
[    1.887401] mousedev: PS/2 mouse d
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
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc pni pclmulqdq ssse3 cx16 sse4_1 sse4_2 popcnt xsave hypervisor lahf_lm


'''
		return returncode, output


class TestLinuxGentoo_2_2_X86_64(unittest.TestCase):
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
		self.assertEqual(14, len(cpuinfo._get_cpu_info_from_lscpu()))
		self.assertEqual(11, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(8, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(21, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand_raw'])
		self.assertEqual('2.7937 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.7937 GHz', info['hz_actual_friendly'])
		self.assertEqual((2793652000, 0), info['hz_advertised'])
		self.assertEqual((2793652000, 0), info['hz_actual'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])

		self.assertEqual('32 KB', info['l1_instruction_cache_size'])
		self.assertEqual('32 KB', info['l1_data_cache_size'])
		self.assertEqual('256 KB', info['l2_cache_size'])
		self.assertEqual('3072 KB', info['l3_cache_size'])

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

	def test_get_cpu_info_from_dmesg(self):
		info = cpuinfo._get_cpu_info_from_dmesg()

		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand_raw'])
		self.assertEqual('2.8000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.8000 GHz', info['hz_actual_friendly'])
		self.assertEqual((2800000000, 0), info['hz_advertised'])
		self.assertEqual((2800000000, 0), info['hz_actual'])

		self.assertEqual(7, info['stepping'])
		self.assertEqual(42, info['model'])
		self.assertEqual(6, info['family'])

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand_raw'])
		self.assertEqual('2.8000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.7937 GHz', info['hz_actual_friendly'])
		self.assertEqual((2800000000, 0), info['hz_advertised'])
		self.assertEqual((2793652000, 0), info['hz_actual'])

		self.assertEqual('3072 KB', info['l3_cache_size'])

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
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('GenuineIntel', info['vendor_id_raw'])
		self.assertEqual('Intel(R) Pentium(R) CPU G640 @ 2.80GHz', info['brand_raw'])
		self.assertEqual('2.8000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.7937 GHz', info['hz_actual_friendly'])
		self.assertEqual((2800000000, 0), info['hz_advertised'])
		self.assertEqual((2793652000, 0), info['hz_actual'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(2, info['count'])

		self.assertEqual('x86_64', info['arch_string_raw'])

		self.assertEqual('32 KB', info['l1_instruction_cache_size'])
		self.assertEqual('32 KB', info['l1_data_cache_size'])
		self.assertEqual('256 KB', info['l2_cache_size'])
		self.assertEqual('3072 KB', info['l3_cache_size'])

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
