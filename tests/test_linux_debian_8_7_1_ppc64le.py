

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 2
	is_windows = False
	arch_string_raw = 'ppc64le'
	uname_string_raw = ''
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
/proc/device-tree/cpus/PowerPC,POWER8@0/ibm,pa-features
                 18 00 f6 3f c7 c0 80 f0 80 00 00 00 00 00 00 00...?............
                 00 00 80 00 80 00 80 00 80 00                  ..........

'''
		return returncode, output

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = '''
processor	: 0
cpu		: POWER7 (raw), altivec supported
clock		: 1000.000000MHz
revision	: 2.3 (pvr 003f 0203)

processor	: 1
cpu		: POWER7 (raw), altivec supported
clock		: 1000.000000MHz
revision	: 2.3 (pvr 003f 0203)

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
[    0.000000] Allocated 4718592 bytes for 2048 pacas at c00000000fb80000
[    0.000000] Using pSeries machine description
[    0.000000] Page sizes from device-tree:
[    0.000000] base_shift=12: shift=12, sllp=0x0000, avpnm=0x00000000, tlbiel=1, penc=0
[    0.000000] base_shift=24: shift=24, sllp=0x0100, avpnm=0x00000001, tlbiel=0, penc=0
[    0.000000] Page orders: linear mapping = 24, virtual = 12, io = 12, vmemmap = 24
[    0.000000] Using 1TB segments
[    0.000000] kvm_cma: CMA: reserved 128 MiB
[    0.000000] Found initrd at 0xc000000002f00000:0xc000000003e49d2c
[    0.000000] Partition configured for 2 cpus.
[    0.000000] CPU maps initialized for 1 thread per core
[    0.000000]  (thread shift is 0)
[    0.000000] Freed 4653056 bytes for unused pacas
[    0.000000] Starting Linux PPC64 #1 SMP Debian 3.16.39-1+deb8u2 (2017-03-07)
[    0.000000] -----------------------------------------------------
[    0.000000] ppc64_pft_size                = 0x18
[    0.000000] physicalMemorySize            = 0x80000000
[    0.000000] htab_hash_mask                = 0x1ffff
[    0.000000] -----------------------------------------------------
[    0.000000] Initializing cgroup subsys cpuset
[    0.000000] Initializing cgroup subsys cpu
[    0.000000] Initializing cgroup subsys cpuacct
[    0.000000] Linux version 3.16.0-4-powerpc64le (debian-kernel@lists.debian.org) (gcc version 4.8.4 (Debian 4.8.4-1) ) #1 SMP Debian 3.16.39-1+deb8u2 (2017-03-07)
[    0.000000] [boot]0012 Setup Arch
[    0.000000] Node 0 Memory: 0x0-0x80000000
[    0.000000] PCI host bridge /pci@800000020000000  ranges:
[    0.000000]   IO 0x0000010080000000..0x000001008000ffff -> 0x0000000000000000
[    0.000000]  MEM 0x00000100a0000000..0x000001101fffffff -> 0x0000000080000000
[    0.000000] PPC64 nvram contains 65536 bytes
[    0.000000] Unable to enable relocation on exceptions: -55
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x00000000-0x7fffffff]
[    0.000000]   Normal   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x00000000-0x7fffffff]
[    0.000000] On node 0 totalpages: 32768
[    0.000000]   DMA zone: 28 pages used for memmap
[    0.000000]   DMA zone: 0 pages reserved
[    0.000000]   DMA zone: 32768 pages, LIFO batch:1
[    0.000000] [boot]0015 Setup Done
[    0.000000] PERCPU: Embedded 2 pages/cpu @c000000000e00000 s102400 r0 d28672 u524288
[    0.000000] pcpu-alloc: s102400 r0 d28672 u524288 alloc=1*1048576
[    0.000000] pcpu-alloc: [0] 0 1
[    0.000000] Built 1 zonelists in Node order, mobility grouping on.  Total pages: 32740
[    0.000000] Policy zone: DMA
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinux-3.16.0-4-powerpc64le root=UUID=35034901-f68b-4f2f-8073-ced7a2a5cd6f ro quiet
[    0.000000] PID hash table entries: 4096 (order: -1, 32768 bytes)
[    0.000000] Sorting __ex_table...
[    0.000000] Memory: 1918848K/2097152K available (7168K kernel code, 1280K rwdata, 1740K rodata, 896K init, 2197K bss, 178304K reserved)
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	CONFIG_RCU_FANOUT set to non-default value of 32
[    0.000000] 	RCU dyntick-idle grace-period acceleration is enabled.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=2048 to nr_cpu_ids=2.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=2
[    0.000000] NR_IRQS:512 nr_irqs:512 16
[    0.000000] pic: no ISA interrupt controller
[    0.000000] time_init: decrementer frequency = 512.000000 MHz
[    0.000000] time_init: processor frequency   = 1000.000000 MHz
[    0.000350] clocksource: timebase mult[1f40000] shift[24] registered
[    0.000553] clockevent: decrementer mult[83126e98] shift[32] cpu[0]
[    0.013730] Console: colour dummy device 80x25
[    0.014989] console [tty0] enabled
[    0.016748] pid_max: default: 32768 minimum: 301
[    0.018500] Security Framework initialized
[    0.021966] AppArmor: AppArmor disabled by boot time parameter
[    0.022018] Yama: disabled by default; enable with sysctl kernel.yama.*
[    0.024790] Dentry cache hash table entries: 262144 (order: 5, 2097152 bytes)
[    0.037906] Inode-cache hash table entries: 131072 (order: 4, 1048576 bytes)
[    0.044210] Mount-cache hash table entries: 8192 (order: 0, 65536 bytes)
[    0.044309] Mountpoint-cache hash table entries: 8192 (order: 0, 65536 bytes)
[    0.057531] Initializing cgroup subsys memory
[    0.058793] Initializing cgroup subsys devices
[    0.062342] Initializing cgroup subsys freezer
[    0.062505] Initializing cgroup subsys net_cls
[    0.062628] Initializing cgroup subsys blkio
[    0.062729] Initializing cgroup subsys perf_event
[    0.062819] Initializing cgroup subsys net_prio
[    0.063556] ftrace: allocating 19452 entries in 8 pages
[    0.184012] EEH: pSeries platform initialized
[    0.184491] POWER7 performance monitor hardware support registered
[    0.751584] Brought up 2 CPUs
[    0.753947] Node 0 CPUs: 0-1
[    0.755683] Enabling Asymmetric SMT scheduling
[    0.781637] devtmpfs: initialized
[    0.860457] EEH: devices created
[    0.890259] NET: Registered protocol family 16
[    0.894867] EEH: No capable adapters found
[    0.896240] IBM eBus Device Driver
[    0.904539] cpuidle: using governor ladder
[    0.904768] cpuidle: using governor menu
[    0.915985] PCI: Probing PCI hardware
[    0.917879] no ibm,pcie-link-speed-stats property
[    0.919431] PCI host bridge to bus 0000:00
[    0.919853] pci_bus 0000:00: root bus resource [io  0x10000-0x1ffff] (bus address [0x0000-0xffff])
[    0.919975] pci_bus 0000:00: root bus resource [mem 0x100a0000000-0x1101fffffff] (bus address [0x80000000-0xfffffffff])
[    0.920199] pci_bus 0000:00: root bus resource [bus 00-ff]
[    0.934921] IOMMU table initialized, virtual merging enabled
[    0.957593] PCI: Probing PCI hardware done
[    0.957881] opal: Node not found
[    0.957994] opal_async_comp_init: Opal node not found
[    1.068654] vgaarb: device added: PCI:0000:00:06.0,decodes=io+mem,owns=mem,locks=none
[    1.068755] vgaarb: loaded
[    1.068811] vgaarb: bridge control possible 0000:00:06.0
[    1.084667] SCSI subsystem initialized
[    1.086205] libata version 3.00 loaded.
[    1.106689] Switched to clocksource timebase
[    1.285639] NET: Registered protocol family 2
[    1.325801] TCP established hash table entries: 16384 (order: 1, 131072 bytes)
[    1.326813] TCP bind hash table entries: 16384 (order: 2, 262144 bytes)
[    1.329251] TCP: Hash tables configured (established 16384 bind 16384)
[    1.330103] TCP: reno registered
[    1.330292] UDP hash table entries: 2048 (order: 0, 65536 bytes)
[    1.331073] UDP-Lite hash table entries: 2048 (order: 0, 65536 bytes)
[    1.343933] NET: Registered protocol family 1
[    1.402765] PCI: CLS 0 bytes, default 128
[    1.408278] Unpacking initramfs...
[    3.824598] Freeing initrd memory: 15616K (c000000002f00000 - c000000003e40000)
[    3.827574] RTAS daemon started
[    3.850567] Hypercall H_BEST_ENERGY not supported
[    3.870435] futex hash table entries: 512 (order: 0, 65536 bytes)
[    3.875072] audit: initializing netlink subsys (disabled)
[    3.876188] audit: type=2000 audit(1489574672.324:1): initialized
[    3.897565] HugeTLB registered 16 MB page size, pre-allocated 0 pages
[    3.898287] zbud: loaded
[    3.955364] VFS: Disk quotas dquot_6.5.2
[    3.957415] Dquot-cache hash table entries: 8192 (order 0, 65536 bytes)
[    3.962329] msgmni has been set to 4036
[    3.991438] alg: No test for stdrng (krng)
[    3.993562] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 252)
[    3.995908] io scheduler noop registered
[    3.996000] io scheduler deadline registered
[    3.999199] io scheduler cfq registered (default)
[    4.002993] pci_hotplug: PCI Hot Plug PCI Core version: 0.5
[    4.003323] pciehp: PCI Express Hot Plug Controller Driver version: 0.4
[    4.005685] Using unsupported 800x600 vga at 100a0000000, depth=32, pitch=3200
[    4.038614] Console: switching to colour frame buffer device 100x37
[    4.050446] fb0: Open Firmware frame buffer device on /pci@800000020000000/vga@6
[    4.064118] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
[    4.069855] Linux agpgart interface v0.103
[    4.074416] mousedev: PS/2 mouse device common for all mice
[    4.076553] rtc-generic rtc-generic: rtc core: registered rtc-generic as rtc0
[    4.078500] pseries_idle_driver registered
[    4.078781] ledtrig-cpu: registered to indicate activity on CPUs
[    4.079478] TCP: cubic registered
[    4.236623] NET: Registered protocol family 10
[    4.297808] mip6: Mobile IPv6
[    4.298028] NET: Registered protocol family 17
[    4.298291] mpls_gso: MPLS GSO support
[    4.306632] registered taskstats version 1
[    4.326061] rtc-generic rtc-generic: setting system clock to 2017-03-15 10:44:33 UTC (1489574673)
[    4.326427] PM: Hibernation image not present or could not be loaded.
[    4.378547] Freeing unused kernel memory: 896K (c0000000008c0000 - c0000000009a0000)
[    5.397702] systemd-udevd[62]: starting version 215
[    5.465837] random: systemd-udevd: uninitialized urandom read (16 bytes read, 12 bits of entropy available)
[    6.151699] virtio-pci 0000:00:05.0: enabling device (0100 -> 0101)
[    6.199143] virtio-pci 0000:00:04.0: enabling device (0100 -> 0103)
[    6.201578] virtio-pci 0000:00:03.0: enabling device (0100 -> 0103)
[    6.376882] 8139cp: 8139cp: 10/100 PCI Ethernet driver v1.3 (Mar 22, 2004)
[    6.383373] 8139cp 0000:00:01.0: enabling device (0100 -> 0103)
[    6.391941] usbcore: registered new interface driver usbfs
[    6.392361] usbcore: registered new interface driver hub
[    6.395494] 8139cp 0000:00:01.0 eth0: RTL-8139C+ at 0xd000080080022100, 52:54:00:f7:51:69, IRQ 17
[    6.422151] usbcore: registered new device driver usb
[    6.489837] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    6.545154] 8139too: 8139too Fast Ethernet driver 0.9.28
[    6.558285] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    6.563301] ehci-pci: EHCI PCI platform driver
[    6.577800] ohci-pci: OHCI PCI platform driver
[    6.583639] ohci-pci 0000:00:02.0: OHCI PCI host controller
[    6.584250] ohci-pci 0000:00:02.0: new USB bus registered, assigned bus number 1
[    6.588455] ohci-pci 0000:00:02.0: irq 20, io mem 0x100e0022000
[    6.683252] usb usb1: New USB device found, idVendor=1d6b, idProduct=0001
[    6.683315] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    6.684539] usb usb1: Product: OHCI PCI host controller
[    6.684614] usb usb1: Manufacturer: Linux 3.16.0-4-powerpc64le ohci_hcd
[    6.684655] usb usb1: SerialNumber: 0000:00:02.0
[    6.706756] hub 1-0:1.0: USB hub found
[    6.709342] hub 1-0:1.0: 3 ports detected
[    6.856073] ibmvscsi 2000: SRP_VERSION: 16.a
[    6.858663] scsi0 : IBM POWER Virtual SCSI Adapter 1.5.9
[    6.890482] ibmvscsi 2000: partner initialization complete
[    6.892225] ibmvscsi 2000: host srp version: 16.a, host partition qemu (0), OS 2, max io 2097152
[    6.892445] ibmvscsi 2000: sent SRP login
[    6.892623] ibmvscsi 2000: SRP_LOGIN succeeded
[    6.960435] scsi 0:0:0:0: CD-ROM            QEMU     QEMU CD-ROM      2.5+ PQ: 0 ANSI: 5
[    7.110257] usb 1-1: new full-speed USB device number 2 using ohci-pci
[    7.354618] usb 1-1: New USB device found, idVendor=0627, idProduct=0001
[    7.354884] usb 1-1: New USB device strings: Mfr=1, Product=4, SerialNumber=5
[    7.354915] usb 1-1: Product: QEMU USB Keyboard
[    7.354941] usb 1-1: Manufacturer: QEMU
[    7.354965] usb 1-1: SerialNumber: 42
[    7.593230] usb 1-2: new full-speed USB device number 3 using ohci-pci
[    7.803140] usb 1-2: New USB device found, idVendor=0627, idProduct=0001
[    7.803189] usb 1-2: New USB device strings: Mfr=1, Product=2, SerialNumber=5
[    7.803217] usb 1-2: Product: QEMU USB Mouse
[    7.803243] usb 1-2: Manufacturer: QEMU
[    7.803271] usb 1-2: SerialNumber: 42
[    8.001788] usb 1-3: new full-speed USB device number 4 using ohci-pci
[    8.236126] usb 1-3: New USB device found, idVendor=0409, idProduct=55aa
[    8.236170] usb 1-3: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    8.236197] usb 1-3: Product: QEMU USB Hub
[    8.236221] usb 1-3: Manufacturer: QEMU
[    8.236246] usb 1-3: SerialNumber: 314159-pci@800000020000000:02.0-3
[    8.247796] hub 1-3:1.0: USB hub found
[    8.252272]  vda: vda1 vda2 vda3
[    8.255820] hub 1-3:1.0: 8 ports detected
[    8.575937] hidraw: raw HID events driver (C) Jiri Kosina
[    8.710814] usbcore: registered new interface driver usbhid
[    8.710897] usbhid: USB HID core driver
[    8.800556] input: QEMU QEMU USB Keyboard as /devices/pci0000:00/0000:00:02.0/usb1/1-1/1-1:1.0/0003:0627:0001.0001/input/input0
[    8.813522] hid-generic 0003:0627:0001.0001: input,hidraw0: USB HID v1.11 Keyboard [QEMU QEMU USB Keyboard] on usb-0000:00:02.0-1/input0
[    8.838628] input: QEMU QEMU USB Mouse as /devices/pci0000:00/0000:00:02.0/usb1/1-2/1-2:1.0/0003:0627:0001.0002/input/input1
[    8.852773] hid-generic 0003:0627:0001.0002: input,hidraw1: USB HID v0.01 Mouse [QEMU QEMU USB Mouse] on usb-0000:00:02.0-2/input0
[    9.684157] sr0: scsi3-mmc drive: 16x/50x cd/rw xa/form2 cdda tray
[    9.684447] cdrom: Uniform CD-ROM driver Revision: 3.20
[    9.694687] sr 0:0:0:0: Attached scsi CD-ROM sr0
[    9.733955] sr 0:0:0:0: Attached scsi generic sg0 type 5
[   12.126890] EXT4-fs (vda2): mounted filesystem with ordered data mode. Opts: (null)
[   13.780089] random: systemd: uninitialized urandom read (16 bytes read, 86 bits of entropy available)
[   13.820325] systemd[1]: systemd 215 running in system mode. (+PAM +AUDIT +SELINUX +IMA +SYSVINIT +LIBCRYPTSETUP +GCRYPT +ACL +XZ -SECCOMP -APPARMOR)
[   13.827143] systemd[1]: Detected architecture 'ppc64-le'.
[   13.993889] systemd[1]: Inserted module 'autofs4'
[   14.005253] systemd[1]: Set hostname to <debian>.
[   14.043401] systemd[1]: /etc/mtab is not a symlink or not pointing to /proc/self/mounts. This is not supported anymore. Please make sure to replace this file by a symlink to avoid incorrect or misleading mount(8) output.
[   15.192167] random: systemd-sysv-ge: uninitialized urandom read (16 bytes read, 97 bits of entropy available)
[   15.731488] random: systemd: uninitialized urandom read (16 bytes read, 106 bits of entropy available)
[   15.735903] random: systemd: uninitialized urandom read (16 bytes read, 106 bits of entropy available)
[   15.738841] random: systemd: uninitialized urandom read (16 bytes read, 106 bits of entropy available)
[   15.835926] random: systemd: uninitialized urandom read (16 bytes read, 108 bits of entropy available)
[   15.838244] random: systemd: uninitialized urandom read (16 bytes read, 108 bits of entropy available)
[   15.839286] random: systemd: uninitialized urandom read (16 bytes read, 108 bits of entropy available)
[   15.950852] random: systemd: uninitialized urandom read (16 bytes read, 108 bits of entropy available)
[   16.361318] systemd[1]: Starting Forward Password Requests to Wall Directory Watch.
[   16.365674] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[   16.370172] systemd[1]: Expecting device dev-hvc0.device...
[   16.373395] systemd[1]: Starting Remote File Systems (Pre).
[   16.373853] systemd[1]: Reached target Remote File Systems (Pre).
[   16.375171] systemd[1]: Starting Arbitrary Executable File Formats File System Automount Point.
[   16.385704] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
[   16.386238] systemd[1]: Starting Encrypted Volumes.
[   16.386600] systemd[1]: Reached target Encrypted Volumes.
[   16.387000] systemd[1]: Starting Dispatch Password Requests to Console Directory Watch.
[   16.388184] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[   16.388464] systemd[1]: Starting Paths.
[   16.388712] systemd[1]: Reached target Paths.
[   16.391942] systemd[1]: Expecting device dev-vda3.device...
[   16.392254] systemd[1]: Expecting device dev-disk-by\x2duuid-5a63f1d4\x2ddd93\x2d45fa\x2d8b04\x2d531d13b2f573.device...
[   16.392543] systemd[1]: Starting Root Slice.
[   16.394191] systemd[1]: Created slice Root Slice.
[   16.394525] systemd[1]: Starting /dev/initctl Compatibility Named Pipe.
[   16.397746] systemd[1]: Listening on /dev/initctl Compatibility Named Pipe.
[   16.398476] systemd[1]: Starting Delayed Shutdown Socket.
[   16.400495] systemd[1]: Listening on Delayed Shutdown Socket.
[   16.401265] systemd[1]: Starting Journal Socket (/dev/log).
[   16.402434] systemd[1]: Listening on Journal Socket (/dev/log).
[   16.402815] systemd[1]: Starting udev Control Socket.
[   16.403586] systemd[1]: Listening on udev Control Socket.
[   16.403922] systemd[1]: Starting udev Kernel Socket.
[   16.404558] systemd[1]: Listening on udev Kernel Socket.
[   16.405281] systemd[1]: Starting User and Session Slice.
[   16.407097] systemd[1]: Created slice User and Session Slice.
[   16.407376] systemd[1]: Starting Journal Socket.
[   16.408701] systemd[1]: Listening on Journal Socket.
[   16.409425] systemd[1]: Starting System Slice.
[   16.411517] systemd[1]: Created slice System Slice.
[   16.412696] systemd[1]: Starting Increase datagram queue length...
[   16.471051] systemd[1]: Mounting Debug File System...
[   16.534646] systemd[1]: Mounting Huge Pages File System...
[   16.609411] systemd[1]: Started Set Up Additional Binary Formats.
[   16.624922] systemd[1]: Starting Create list of required static device nodes for the current kernel...
[   16.699997] systemd[1]: Mounting POSIX Message Queue File System...
[   16.858052] systemd[1]: Starting Load Kernel Modules...
[   16.997970] systemd[1]: Starting udev Coldplug all Devices...
[   17.162057] systemd[1]: Starting system-getty.slice.
[   17.170940] systemd[1]: Created slice system-getty.slice.
[   17.182649] systemd[1]: Starting system-serial\x2dgetty.slice.
[   17.202996] systemd[1]: Created slice system-serial\x2dgetty.slice.
[   17.225948] systemd[1]: Started File System Check on Root Device.
[   17.227635] systemd[1]: Starting Slices.
[   17.227932] systemd[1]: Reached target Slices.
[   17.474563] systemd[1]: Started Increase datagram queue length.
[   17.576418] systemd[1]: Started Create list of required static device nodes for the current kernel.
[   17.643118] systemd[1]: Mounted Debug File System.
[   17.698436] systemd[1]: Mounted Huge Pages File System.
[   17.790500] systemd[1]: Mounted POSIX Message Queue File System.
[   18.208240] fuse init (API version 7.23)
[   18.405814] systemd[1]: Started Load Kernel Modules.
[   19.057106] systemd[1]: Mounting FUSE Control File System...
[   19.099902] systemd[1]: Starting Apply Kernel Variables...
[   19.175166] systemd[1]: Mounted Configuration File System.
[   19.191354] systemd[1]: Starting Create Static Device Nodes in /dev...
[   19.252059] systemd[1]: Starting Syslog Socket.
[   19.264507] systemd[1]: Listening on Syslog Socket.
[   19.293762] systemd[1]: Starting Journal Service...
[   19.424427] systemd[1]: Started Journal Service.
[   21.339528] systemd-udevd[153]: starting version 215
[   22.636196] random: nonblocking pool is initialized
[   26.801725] [drm] Initialized drm 1.1.0 20060810
[   27.190191] checking generic (100a0000000 1d4c00) vs hw (100a0000000 1000000)
[   27.190254] fb: switching to bochsdrmfb from OFfb vga
[   27.192042] Console: switching to colour dummy device 80x25
[   27.316647] [drm] Found bochs VGA, ID 0xb0c5.
[   27.316718] [drm] Framebuffer size 16384 kB @ 0x100a0000000, mmio @ 0x100e0000000.
[   27.352534] [TTM] Zone  kernel: Available graphics memory: 1033696 kiB
[   27.352610] [TTM] Initializing pool allocator
[   27.699633] Console: switching to colour frame buffer device 128x48
[   28.241859] bochs-drm 0000:00:06.0: fb0: bochsdrmfb frame buffer device
[   28.241914] bochs-drm 0000:00:06.0: registered panic notifier
[   28.270473] [drm] Initialized bochs-drm 1.0.0 20130925 for 0000:00:06.0 on minor 0
[   32.871945] Adding 2187200k swap on /dev/vda3.  Priority:-1 extents:1 across:2187200k FS
[   37.271870] EXT4-fs (vda2): re-mounted. Opts: errors=remount-ro
[   39.257446] systemd-journald[148]: Received request to flush runtime journal from PID 1
[   66.682979] RPC: Registered named UNIX socket transport module.
[   66.683180] RPC: Registered udp transport module.
[   66.683239]


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
Model:                 IBM pSeries (emulated by qemu)
L1d cache:             32K
L1i cache:             32K
NUMA node0 CPU(s):     0,1


'''
		return returncode, output


class TestLinuxDebian_8_7_1_ppc64le(unittest.TestCase):
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
		self.assertEqual(2, len(cpuinfo._get_cpu_info_from_lscpu()))
		self.assertEqual(5, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(1, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(15, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()
		self.assertEqual('32 KB', info['l1_instruction_cache_size'])
		self.assertEqual('32 KB', info['l1_data_cache_size'])
		self.assertEqual(2, len(info))

	def test_get_cpu_info_from_ibm_pa_features(self):
		info = cpuinfo._get_cpu_info_from_ibm_pa_features()
		self.assertEqual(
			['dabr', 'dabrx', 'dsisr', 'fpu', 'lp', 'mmu', 'pp', 'rislb', 'run', 'slb', 'sprg3'],
			info['flags']
		)

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('POWER7 (raw), altivec supported', info['brand_raw'])
		self.assertEqual('1.0000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('1.0000 GHz', info['hz_actual_friendly'])
		self.assertEqual((1000000000, 0), info['hz_advertised'])
		self.assertEqual((1000000000, 0), info['hz_actual'])

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('POWER7 (raw), altivec supported', info['brand_raw'])
		self.assertEqual('1.0000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('1.0000 GHz', info['hz_actual_friendly'])
		self.assertEqual((1000000000, 0), info['hz_advertised'])
		self.assertEqual((1000000000, 0), info['hz_actual'])
		self.assertEqual('PPC_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(2, info['count'])
		self.assertEqual('32 KB', info['l1_instruction_cache_size'])
		self.assertEqual('32 KB', info['l1_data_cache_size'])
		self.assertEqual('ppc64le', info['arch_string_raw'])
		self.assertEqual(
			['dabr', 'dabrx', 'dsisr', 'fpu', 'lp', 'mmu', 'pp', 'rislb', 'run', 'slb', 'sprg3'],
			info['flags']
		)
