

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 2
	is_windows = False
	raw_arch_string = 'ppc64le'
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
	def has_ibm_pa_features():
		return True

	@staticmethod
	def ibm_pa_features():
		returncode = 0
		output = '''
/proc/device-tree/cpus/PowerPC,POWER7@1/ibm,pa-features 3ff60006 c08000c7

'''
		return returncode, output

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = '''
processor	: 0
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)
processor	: 1
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)
timebase	: 512000000
platform	: pSeries
model		: IBM pSeries (emulated by qemu)
machine		: CHRP IBM pSeries (emulated by qemu)

'''
		return returncode, output

	@staticmethod
	def dmesg_a():
		returncode = 0
		output = '''
[    0.000000] Allocated 2359296 bytes for 1024 pacas at c00000000fdc0000
[    0.000000] Using pSeries machine description
[    0.000000] Page sizes from device-tree:
[    0.000000] base_shift=12: shift=12, sllp=0x0000, avpnm=0x00000000, tlbiel=1, penc=0
[    0.000000] base_shift=16: shift=16, sllp=0x0110, avpnm=0x00000000, tlbiel=1, penc=1
[    0.000000] Page orders: linear mapping = 16, virtual = 16, io = 12, vmemmap = 16
[    0.000000] Using 1TB segments
[    0.000000] Found initrd at 0xc000000003700000:0xc00000000492fa44
[    0.000000] bootconsole [udbg0] enabled
[    0.000000] Partition configured for 2 cpus.
[    0.000000] CPU maps initialized for 1 thread per core
[    0.000000]  (thread shift is 0)
[    0.000000] Freed 2293760 bytes for unused pacas
[    0.000000] Starting Linux ppc64le #1 SMP Tue May 24 12:23:26 UTC 2016
[    0.000000] -----------------------------------------------------
[    0.000000] ppc64_pft_size    = 0x1a
[    0.000000] phys_mem_size     = 0x140000000
[    0.000000] cpu_features      = 0x17fc7a6c18500249
[    0.000000]   possible        = 0x1fffffef18500649
[    0.000000]   always          = 0x0000000018100040
[    0.000000] cpu_user_features = 0xdc0065c2 0xef000000
[    0.000000] mmu_features      = 0x58000001
[    0.000000] firmware_features = 0x000000014052440b
[    0.000000] htab_hash_mask    = 0x7ffff
[    0.000000] -----------------------------------------------------
[    0.000000] Linux version 4.5.5-300.fc24.ppc64le (mockbuild@buildvm-ppc64le-02.ppc.fedoraproject.org) (gcc version 6.1.1 20160510 (Red Hat 6.1.1-2) (GCC) ) #1 SMP Tue May 24 12:23:26 UTC 2016
[    0.000000] Node 0 Memory: 0x0-0x140000000
[    0.000000] numa: Initmem setup node 0 [mem 0x00000000-0x13fffffff]
[    0.000000] numa:   NODE_DATA [mem 0x13ffda100-0x13ffe3fff]
[    0.000000] Section 317 and 319 (node 0) have a circular dependency on usemap and pgdat allocations
[    0.000000] PCI host bridge /pci@800000020000000  ranges:
[    0.000000]   IO 0x0000010080000000..0x000001008000ffff -> 0x0000000000000000
[    0.000000]  MEM 0x00000100a0000000..0x000001101fffffff -> 0x0000000080000000
[    0.000000] PPC64 nvram contains 65536 bytes
[    0.000000] Top of RAM: 0x140000000, Total RAM: 0x140000000
[    0.000000] Memory hole size: 0MB
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000000000-0x000000013fffffff]
[    0.000000]   DMA32    empty
[    0.000000]   Normal   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000000000-0x000000013fffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x000000013fffffff]
[    0.000000] On node 0 totalpages: 81920
[    0.000000]   DMA zone: 80 pages used for memmap
[    0.000000]   DMA zone: 0 pages reserved
[    0.000000]   DMA zone: 81920 pages, LIFO batch:1
[    0.000000] PERCPU: Embedded 3 pages/cpu @c00000013fe00000 s128792 r0 d67816 u524288
[    0.000000] pcpu-alloc: s128792 r0 d67816 u524288 alloc=1*1048576
[    0.000000] pcpu-alloc: [0] 0 1
[    0.000000] Built 1 zonelists in Node order, mobility grouping on.  Total pages: 81840
[    0.000000] Policy zone: DMA
[    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-4.5.5-300.fc24.ppc64le root=UUID=e310499a-7ae9-46e6-aeeb-e9babe31e019 ro no_timer_check console=tty1 console=ttyS0,115200n8 rhgb quiet console=hvc1 LANG=en_US.UTF-8
[    0.000000] PID hash table entries: 4096 (order: -1, 32768 bytes)
[    0.000000] Sorting __ex_table...
[    0.000000] Memory: 5129088K/5242880K available (10048K kernel code, 1344K rwdata, 3028K rodata, 5312K init, 2684K bss, 113792K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=128, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	Build-time adjustment of leaf fanout to 64.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=1024 to nr_cpu_ids=2.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=64, nr_cpu_ids=2
[    0.000000] NR_IRQS:512 nr_irqs:512 16
[    0.000000] pic: no ISA interrupt controller
[    0.000000] time_init: decrementer frequency = 512.000000 MHz
[    0.000000] time_init: processor frequency   = 3425.000000 MHz
[    0.000001] clocksource: timebase: mask: 0xffffffffffffffff max_cycles: 0x761537d007, max_idle_ns: 440795202126 ns
[    0.000003] clocksource: timebase mult[1f40000] shift[24] registered
[    0.000005] clockevent: decrementer mult[83126e98] shift[32] cpu[0]
[    0.000040] Console: colour dummy device 80x25
[    0.000068] console [tty1] enabled
[    0.000088] pid_max: default: 32768 minimum: 301
[    0.000125] Security Framework initialized
[    0.000127] Yama: becoming mindful.
[    0.000131] SELinux:  Initializing.
[    0.000146] SELinux:  Starting in permissive mode
[    0.000227] Dentry cache hash table entries: 1048576 (order: 7, 8388608 bytes)
[    0.001739] Inode-cache hash table entries: 524288 (order: 6, 4194304 bytes)
[    0.002484] Mount-cache hash table entries: 16384 (order: 1, 131072 bytes)
[    0.002486] Mountpoint-cache hash table entries: 16384 (order: 1, 131072 bytes)
[    0.002754] ftrace: allocating 25021 entries in 10 pages
[    0.012417] EEH: pSeries platform initialized
[    0.012430] POWER8 performance monitor hardware support registered
[    0.012433] power8-pmu: PMAO restore workaround active.
[    0.014048] Brought up 2 CPUs
[    0.014066] Node 0 CPUs: 0-1
[    0.014588] devtmpfs: initialized
[    0.025860] EEH: devices created
[    0.025904] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
[    0.025964] atomic64_test: passed
[    0.026060] NET: Registered protocol family 16
[    0.026973] EEH: No capable adapters found
[    0.027024] IBM eBus Device Driver
[    0.052266] cpuidle: using governor menu
[    0.052392] pstore: Registered nvram as persistent store backend
[    0.053138] PCI: Probing PCI hardware
[    0.053169] PCI host bridge to bus 0000:00
[    0.053172] pci_bus 0000:00: root bus resource [io  0x10000-0x1ffff] (bus address [0x0000-0xffff])
[    0.053174] pci_bus 0000:00: root bus resource [mem 0x100a0000000-0x1101fffffff] (bus address [0x80000000-0xfffffffff])
[    0.053176] pci_bus 0000:00: root bus resource [bus 00-ff]
[    0.079786] IOMMU table initialized, virtual merging enabled
[    0.080038] PCI: Probing PCI hardware done
[    0.102679] vgaarb: loaded
[    0.102739] SCSI subsystem initialized
[    0.102766] libata version 3.00 loaded.
[    0.102802] usbcore: registered new interface driver usbfs
[    0.102810] usbcore: registered new interface driver hub
[    0.102823] usbcore: registered new device driver usb
[    0.103034] NetLabel: Initializing
[    0.103035] NetLabel:  domain hash size = 128
[    0.103035] NetLabel:  protocols = UNLABELED CIPSOv4
[    0.103044] NetLabel:  unlabeled traffic allowed by default
[    0.103108] clocksource: Switched to clocksource timebase
[    0.110649] VFS: Disk quotas dquot_6.6.0
[    0.110680] VFS: Dquot-cache hash table entries: 8192 (order 0, 65536 bytes)
[    0.110724] hugetlbfs: disabling because there are no supported hugepage sizes
[    0.113993] NET: Registered protocol family 2
[    0.114128] TCP established hash table entries: 65536 (order: 3, 524288 bytes)
[    0.114243] TCP bind hash table entries: 65536 (order: 4, 1048576 bytes)
[    0.114372] TCP: Hash tables configured (established 65536 bind 65536)
[    0.114381] UDP hash table entries: 4096 (order: 1, 131072 bytes)
[    0.114398] UDP-Lite hash table entries: 4096 (order: 1, 131072 bytes)
[    0.114445] NET: Registered protocol family 1
[    0.173318] PCI: CLS 0 bytes, default 128
[    0.173399] Unpacking initramfs...
[    0.476072] Freeing initrd memory: 18560K (c000000003700000 - c000000004920000)
[    0.476263] RTAS daemon started
[    0.476812] rtas_flash: no firmware flash support
[    0.513298] futex hash table entries: 512 (order: 0, 65536 bytes)
[    0.513327] audit: initializing netlink subsys (disabled)
[    0.513355] audit: type=2000 audit(1491783180.510:1): initialized
[    0.513515] Initialise system trusted keyring
[    0.515510] zbud: loaded
[    0.516023] Key type big_key registered
[    0.516025] SELinux:  Registering netfilter hooks
[    0.521239] NET: Registered protocol family 38
[    0.521248] Key type asymmetric registered
[    0.521251] Asymmetric key parser 'x509' registered
[    0.521288] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 252)
[    0.521315] io scheduler noop registered
[    0.521317] io scheduler deadline registered
[    0.521350] io scheduler cfq registered (default)
[    0.521402] pci_hotplug: PCI Hot Plug PCI Core version: 0.5
[    0.521659] console [hvc1] enabled
[    0.521660] bootconsole [udbg0] disabled
[    0.521735] Linux agpgart interface v0.103
[    0.521845] libphy: Fixed MDIO Bus: probed
[    0.521881] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.521889] ehci-pci: EHCI PCI platform driver
[    0.521898] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.521906] ohci-pci: OHCI PCI platform driver
[    0.522111] ohci-pci 0000:00:02.0: OHCI PCI host controller
[    0.522141] ohci-pci 0000:00:02.0: new USB bus registered, assigned bus number 1
[    0.522220] ohci-pci 0000:00:02.0: irq 20, io mem 0x100e0002000
[    0.573380] usb usb1: New USB device found, idVendor=1d6b, idProduct=0001
[    0.573382] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.573384] usb usb1: Product: OHCI PCI host controller
[    0.573385] usb usb1: Manufacturer: Linux 4.5.5-300.fc24.ppc64le ohci_hcd
[    0.573386] usb usb1: SerialNumber: 0000:00:02.0
[    0.573477] hub 1-0:1.0: USB hub found
[    0.573496] hub 1-0:1.0: 3 ports detected
[    0.573656] uhci_hcd: USB Universal Host Controller Interface driver
[    0.573694] usbcore: registered new interface driver usbserial
[    0.573699] usbcore: registered new interface driver usbserial_generic
[    0.573706] usbserial: USB Serial support registered for generic
[    0.573763] mousedev: PS/2 mouse device common for all mice
[    0.573863] rtc-generic rtc-generic: rtc core: registered rtc-generic as rtc0
[    0.573932] device-mapper: uevent: version 1.0.3
[    0.573994] device-mapper: ioctl: 4.34.0-ioctl (2015-10-28) initialised: dm-devel@redhat.com
[    0.574075] pseries_idle_driver registered
[    0.574087] hidraw: raw HID events driver (C) Jiri Kosina
[    0.574122] usbcore: registered new interface driver usbhid
[    0.574123] usbhid: USB HID core driver
[    0.574161] drop_monitor: Initializing network drop monitor service
[    0.574234] ip_tables: (C) 2000-2006 Netfilter Core Team
[    0.574249] Initializing XFRM netlink socket
[    0.574386] NET: Registered protocol family 10
[    0.574535] mip6: Mobile IPv6
[    0.574538] NET: Registered protocol family 17
[    0.574586] Running MSI bitmap self-tests ...
[    0.574723] registered taskstats version 1
[    0.574738] Loading compiled-in X.509 certificates
[    0.575418] Loaded X.509 cert 'Fedora kernel signing key: 5a5f33c227f5a1d54cd2ff7c19cb096bd38186c0'
[    0.575455] zswap: loaded using pool lzo/zbud
[    0.575662] rtc-generic rtc-generic: setting system clock to 2017-04-10 00:13:00 UTC (1491783180)
[    0.576274] Freeing unused kernel memory: 5312K (c000000000cd0000 - c000000001200000)
[    0.605405] random: systemd urandom read with 6 bits of entropy available
[    0.606905] systemd[1]: systemd 229 running in system mode. (+PAM +AUDIT +SELINUX +IMA -APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD +IDN)
[    0.606941] systemd[1]: Detected virtualization kvm.
[    0.606945] systemd[1]: Detected architecture ppc64-le.
[    0.606947] systemd[1]: Running in initial RAM disk.
[    0.606954] systemd[1]: No hostname configured.
[    0.606958] systemd[1]: Set hostname to <localhost>.
[    0.606978] systemd[1]: Initializing machine ID from random generator.
[    0.668692] systemd[1]: Reached target Timers.
[    0.669077] systemd[1]: Created slice System Slice.
[    0.669110] systemd[1]: Listening on Journal Socket (/dev/log).
[    0.669126] systemd[1]: Listening on udev Kernel Socket.
[    0.669149] systemd[1]: Listening on udev Control Socket.
[    0.669175] systemd[1]: Listening on Journal Socket.
[    0.669586] systemd[1]: Starting Setup Virtual Console...
[    0.669653] systemd[1]: Listening on Journal Audit Socket.
[    0.672129] systemd[1]: Starting Journal Service...
[    0.672138] systemd[1]: Reached target Sockets.
[    0.672147] systemd[1]: Reached target Slices.
[    0.672232] systemd[1]: Reached target Local File Systems.
[    0.672240] systemd[1]: Reached target Swap.
[    0.672673] systemd[1]: Starting Create list of required static device nodes for the current kernel...
[    0.674014] systemd[1]: Starting Apply Kernel Variables...
[    0.674919] systemd[1]: Started Setup Virtual Console.
[    0.679667] audit: type=1130 audit(1491783180.590:2): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=kernel msg='unit=systemd-vconsole-setup comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[    0.679905] systemd[1]: Started Create list of required static device nodes for the current kernel.
[    0.679919] audit: type=1130 audit(1491783180.590:3): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=kernel msg='unit=kmod-static-nodes comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[    0.680081] systemd[1]: Started Apply Kernel Variables.
[    0.680092] audit: type=1130 audit(1491783180.590:4): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=kernel msg='unit=systemd-sysctl comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[    0.680162] systemd[1]: Started Journal Service.
[    0.680185] audit: type=1130 audit(1491783180.590:5): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=kernel msg='unit=systemd-journald comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[    0.694615] audit: type=1130 audit(1491783180.610:6): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=kernel msg='unit=systemd-tmpfiles-setup-dev comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[    0.699549] audit: type=1130 audit(1491783180.610:7): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=kernel msg='unit=systemd-udevd comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[    0.728515] audit: type=1130 audit(1491783180.640:8): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=kernel msg='unit=systemd-udev-trigger comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[    0.739200] virtio-pci 0000:00:05.0: enabling device (0100 -> 0101)
[    0.739411] virtio-pci 0000:00:05.0: virtio_pci: leaving for legacy driver
[    0.740075] virtio-pci 0000:00:04.0: enabling device (0100 -> 0103)
[    0.740437] virtio-pci 0000:00:04.0: virtio_pci: leaving for legacy driver
[    0.757865] virtio-pci 0000:00:03.0: enabling device (0100 -> 0103)
[    0.758321] virtio-pci 0000:00:03.0: virtio_pci: leaving for legacy driver
[    0.763011] virtio-pci 0000:00:01.0: enabling device (0100 -> 0103)
[    0.763502] virtio-pci 0000:00:01.0: virtio_pci: leaving for legacy driver
[    0.768465]  vdb: vdb1 vdb2 vdb3
[    0.830235] audit: type=1130 audit(1491783180.740:9): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=kernel msg='unit=plymouth-start comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[    2.148482] audit: type=1130 audit(1491783182.060:10): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=kernel msg='unit=systemd-fsck-root comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[    2.189824] EXT4-fs (vdb3): mounted filesystem with ordered data mode. Opts: (null)
[    2.301223] systemd-journald[109]: Received SIGTERM from PID 1 (systemd).
[    2.351807] SELinux: 32768 avtab hash slots, 104786 rules.
[    2.365146] SELinux: 32768 avtab hash slots, 104786 rules.
[    2.383721] SELinux:  8 users, 14 roles, 5012 types, 303 bools, 1 sens, 1024 cats
[    2.383724] SELinux:  92 classes, 104786 rules
[    2.386155] SELinux:  Permission validate_trans in class security not defined in policy.
[    2.386249] SELinux: the above unknown classes and permissions will be allowed
[    2.386252] SELinux:  Completing initialization.
[    2.386253] SELinux:  Setting up existing superblocks.
[    2.426718] systemd[1]: Successfully loaded SELinux policy in 103.506ms.
[    2.444699] systemd[1]: Relabelled /dev and /run in 11.979ms.
[    2.589401] EXT4-fs (vdb3): re-mounted. Opts: (null)
[    2.599542] systemd-journald[240]: Received request to flush runtime journal from PID 1
[    2.779725] systemd-journald[240]: File /var/log/journal/4e9a0e2b5c824908abfd9075364301d9/system.journal corrupted or uncleanly shut down, renaming and replacing.
[    2.850831] Adding 102399936k swap on /dev/vda.  Priority:-1 extents:1 across:102399936k FS
[    3.237747] EXT4-fs (vdb2): mounted filesystem with ordered data mode. Opts: (null)
[   16.065643] netlink: 12 bytes leftover after parsing attributes in process `ip'.
[   20.101004] random: nonblocking pool is initialized
[   26.987127] systemd-journald[240]: File /var/log/journal/4e9a0e2b5c824908abfd9075364301d9/user-1000.journal corrupted or uncleanly shut down, renaming and replacing.
[   95.273698] systemd-journald[240]: File /var/log/journal/4e9a0e2b5c824908abfd9075364301d9/user-1001.journal corrupted or uncleanly shut down, renaming and replacing.

'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = '''
Architecture:          ppc64le
Byte Order:            Little Endian
CPU(s):                2
On-line CPU(s) list:   0,1
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             2
NUMA node(s):          1
Model:                 2.1 (pvr 004b 0201)
Model name:            POWER8E (raw), altivec supported
Hypervisor vendor:     KVM
Virtualization type:   para
L1d cache:             64K
L1i cache:             32K
NUMA node0 CPU(s):     0,1

'''
		return returncode, output


class TestLinuxFedora_24_ppc64le(unittest.TestCase):
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
		self.assertEqual(1, len(cpuinfo._get_cpu_info_from_lscpu()))
		self.assertEqual(5, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(1, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(11, len(cpuinfo.get_cpu_info()))

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()

		self.assertEqual('POWER8E (raw), altivec supported', info['brand'])

	def test_get_cpu_info_from_ibm_pa_features(self):
		info = cpuinfo._get_cpu_info_from_ibm_pa_features()
		self.assertEqual(
			['dss_2.02', 'dss_2.05', 'dss_2.06', 'fpu', 'lsd_in_dscr', 'ppr', 'slb', 'sso_2.06', 'ugr_in_dscr'],
			info['flags']
		)

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('POWER8E (raw), altivec supported', info['brand'])
		self.assertEqual('3.4250 GHz', info['hz_advertised'])
		self.assertEqual('3.4250 GHz', info['hz_actual'])
		self.assertEqual((3425000000, 0), info['hz_advertised_raw'])
		self.assertEqual((3425000000, 0), info['hz_actual_raw'])

	def test_all(self):
		info = cpuinfo.get_cpu_info()

		self.assertEqual('POWER8E (raw), altivec supported', info['brand'])
		self.assertEqual('3.4250 GHz', info['hz_advertised'])
		self.assertEqual('3.4250 GHz', info['hz_actual'])
		self.assertEqual((3425000000, 0), info['hz_advertised_raw'])
		self.assertEqual((3425000000, 0), info['hz_actual_raw'])
		self.assertEqual('PPC_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(2, info['count'])
		self.assertEqual('ppc64le', info['raw_arch_string'])
		self.assertEqual(
			['dss_2.02', 'dss_2.05', 'dss_2.06', 'fpu', 'lsd_in_dscr', 'ppr', 'slb', 'sso_2.06', 'ugr_in_dscr'],
			info['flags']
		)
