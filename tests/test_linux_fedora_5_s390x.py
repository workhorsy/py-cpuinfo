

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 4
	is_windows = False
	arch_string_raw = 's390x'
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
	def cat_proc_cpuinfo():
		returncode = 0
		output = r'''
vendor_id       : IBM/S390
# processors    : 4
bogomips per cpu: 2913.00
max thread id   : 0
features	: esan3 zarch stfle msa ldisp eimm dfp edat etf3eh highgprs te sie
cache0          : level=1 type=Data scope=Private size=96K line_size=256 associativity=6
cache1          : level=1 type=Instruction scope=Private size=64K line_size=256 associativity=4
cache2          : level=2 type=Data scope=Private size=1024K line_size=256 associativity=8
cache3          : level=2 type=Instruction scope=Private size=1024K line_size=256 associativity=8
cache4          : level=3 type=Unified scope=Shared size=49152K line_size=256 associativity=12
cache5          : level=4 type=Unified scope=Shared size=393216K line_size=256 associativity=24
processor 0: version = FF,  identification = 14C047,  machine = 2827
processor 1: version = FF,  identification = 14C047,  machine = 2827
processor 2: version = FF,  identification = 14C047,  machine = 2827
processor 3: version = FF,  identification = 14C047,  machine = 2827
cpu number      : 0
cpu MHz dynamic : 5504
cpu MHz static  : 5504
cpu number      : 1
cpu MHz dynamic : 5504
cpu MHz static  : 5504
cpu number      : 2
cpu MHz dynamic : 5504
cpu MHz static  : 5504
cpu number      : 3
cpu MHz dynamic : 5504
cpu MHz static  : 5504


'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = r'''
Architecture:          s390x
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Big Endian
CPU(s):                4
On-line CPU(s) list:   0-3
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s) per book:    1
Book(s) per drawer:    1
Drawer(s):             4
Vendor ID:             IBM/S390
Machine type:          2827
CPU dynamic MHz:       5504
CPU static MHz:        5504
BogoMIPS:              2913.00
Hypervisor:            z/VM 5.4.0
Hypervisor vendor:     IBM
Virtualization type:   full
Dispatching mode:      horizontal
L1d cache:             96K
L1i cache:             64K
L2d cache:             1024K
L2i cache:             1024K
L3 cache:              49152K
L4 cache:              393216K
Flags:                 esan3 zarch stfle msa ldisp eimm dfp etf3eh highgprs sie


'''
		return returncode, output

	@staticmethod
	def dmesg_a():
		returncode = 0
		output = r'''
[623985.026158]            000003ffda1f9118 00e1526ff184ab35 00000000800008a0 000003ffda1f90f0
[623985.026161]            0000000080000740 0000000000000000 000002aa4b1cf0a0 000003ffaa476f30
[623985.026165]            000003ffaa428f58 000002aa4b1bf6b0 000003ffa9e22b9e 000003ffda1f8ee0
[623985.026175] User Code: 0000000080000828: c0f4ffffffc0	brcl	15,800007a8
[623985.026175]            000000008000082e: 0707		bcr	0,%r7
[623985.026175]           #0000000080000830: a7f40001		brc	15,80000832
[623985.026175]           >0000000080000834: 0707		bcr	0,%r7
[623985.026175]            0000000080000836: 0707		bcr	0,%r7
[623985.026175]            0000000080000838: eb7ff0380024	stmg	%r7,%r15,56(%r15)
[623985.026175]            000000008000083e: e3f0ff60ff71	lay	%r15,-160(%r15)
[623985.026175]            0000000080000844: b9040092		lgr	%r9,%r2
[623985.026211] Last Breaking-Event-Address:
[623985.026214]  [<0000000080000830>] 0x80000830
[624418.306980] User process fault: interruption code 0038 ilc:3 in libstdc++.so.6.0.23[3ff9d000000+1b9000]
[624418.306992] Failing address: 46726f6200005000 TEID: 46726f6200005800
[624418.306994] Fault in primary space mode while using user ASCE.
[624418.306997] AS:0000000081d081c7 R3:0000000000000024
[624418.307003] CPU: 3 PID: 56744 Comm: try-catch-2.exe Not tainted 4.8.15-300.fc25.s390x #1
[624418.307005] Hardware name: IBM              2827 H43              400              (z/VM)
[624418.307009] task: 00000000f74c1c80 task.stack: 00000000ab6f0000
[624418.307012] User PSW : 0705000180000000 000003ff9d0a7f58
[624418.307016]            R:0 T:1 IO:1 EX:1 Key:0 M:1 W:0 P:1 AS:0 CC:0 PM:0 RI:0 EA:3
[624418.307016] User GPRS: 0000000000000000 46726f6200005465 0000000080003528 000003ff9d1bba00
[624418.307024]            000003fff8278e88 000003fff8278dc0 000000008000187a fffffffffffffffd
[624418.307028]            000003ff00000000 000003fff8278e88 0000000080003528 000003ff9d1bba00
[624418.307032]            0000000080003428 000003ff9d172658 000003ff9d0a7f32 000003fff8278d20
[624418.307050] User Code: 000003ff9d0a7f4a: e310a0000004	lg	%r1,0(%r10)
[624418.307050]            000003ff9d0a7f50: b904003b		lgr	%r3,%r11
[624418.307050]           #000003ff9d0a7f54: b904002a		lgr	%r2,%r10
[624418.307050]           >000003ff9d0a7f58: e31010200004	lg	%r1,32(%r1)
[624418.307050]            000003ff9d0a7f5e: a7590001		lghi	%r5,1
[624418.307050]            000003ff9d0a7f62: 4140f0a0		la	%r4,160(%r15)
[624418.307050]            000003ff9d0a7f66: 0de1		basr	%r14,%r1
[624418.307050]            000003ff9d0a7f68: ec280009007c	cgij	%r2,0,8,3ff9d0a7f7a
[624418.307061] Last Breaking-Event-Address:
[624418.307065]  [<000003ff9d0a7f32>] 0x3ff9d0a7f32
[624418.806616] User process fault: interruption code 0038 ilc:3 in libstdc++.so.6.0.23[3ffac780000+1b9000]
[624418.806627] Failing address: 5465737473756000 TEID: 5465737473756800
[624418.806629] Fault in primary space mode while using user ASCE.
[624418.806633] AS:00000000a44441c7 R3:0000000000000024
[624418.806638] CPU: 3 PID: 56971 Comm: try-catch-9.exe Not tainted 4.8.15-300.fc25.s390x #1
[624418.806641] Hardware name: IBM              2827 H43              400              (z/VM)
[624418.806644] task: 0000000001a9b900 task.stack: 0000000082968000
[624418.806647] User PSW : 0705000180000000 000003ffac827f58
[624418.806650]            R:0 T:1 IO:1 EX:1 Key:0 M:1 W:0 P:1 AS:0 CC:0 PM:0 RI:0 EA:3
[624418.806650] User GPRS: 0000000000000000 5465737473756974 00000000800032a4 000003ffac93ba00
[624418.806658]            000003ffdd4f8bb0 000003ffdd4f8ae8 0000000080001338 0000000000000000
[624418.806662]            000003ff00000000 000003ffdd4f8bb0 00000000800032a4 000003ffac93ba00
[624418.806666]            0000000087919e90 000003ffac8f2658 000003ffac827f32 000003ffdd4f8a48
[624418.806683] User Code: 000003ffac827f4a: e310a0000004	lg	%r1,0(%r10)
[624418.806683]            000003ffac827f50: b904003b		lgr	%r3,%r11
[624418.806683]           #000003ffac827f54: b904002a		lgr	%r2,%r10
[624418.806683]           >000003ffac827f58: e31010200004	lg	%r1,32(%r1)
[624418.806683]            000003ffac827f5e: a7590001		lghi	%r5,1
[624418.806683]            000003ffac827f62: 4140f0a0		la	%r4,160(%r15)
[624418.806683]            000003ffac827f66: 0de1		basr	%r14,%r1
[624418.806683]            000003ffac827f68: ec280009007c	cgij	%r2,0,8,3ffac827f7a
[624418.806694] Last Breaking-Event-Address:
[624418.806697]  [<000003ffac827f32>] 0x3ffac827f32
[624457.542811] User process fault: interruption code 0038 ilc:3 in libstdc++.so.6.0.23[3ffbc080000+1b9000]
[624457.542823] Failing address: 46726f6200005000 TEID: 46726f6200005800
[624457.542825] Fault in primary space mode while using user ASCE.
[624457.542829] AS:0000000002e701c7 R3:0000000000000024
[624457.542834] CPU: 2 PID: 6763 Comm: try-catch-2.exe Not tainted 4.8.15-300.fc25.s390x #1
[624457.542837] Hardware name: IBM              2827 H43              400              (z/VM)
[624457.542840] task: 00000000f7aa0000 task.stack: 0000000003530000
[624457.542844] User PSW : 0705000180000000 000003ffbc127f58
[624457.542847]            R:0 T:1 IO:1 EX:1 Key:0 M:1 W:0 P:1 AS:0 CC:0 PM:0 RI:0 EA:3
[624457.542847] User GPRS: 0000000000000000 46726f6200005465 0000000080003528 000003ffbc23ba00
[624457.542856]            000003ffc14f8dd8 000003ffc14f8d10 000000008000187a fffffffffffffffd
[624457.542859]            000003ff00000000 000003ffc14f8dd8 0000000080003528 000003ffbc23ba00
[624457.542863]            0000000080003428 000003ffbc1f2658 000003ffbc127f32 000003ffc14f8c70
[624457.542882] User Code: 000003ffbc127f4a: e310a0000004	lg	%r1,0(%r10)
[624457.542882]            000003ffbc127f50: b904003b		lgr	%r3,%r11
[624457.542882]           #000003ffbc127f54: b904002a		lgr	%r2,%r10
[624457.542882]           >000003ffbc127f58: e31010200004	lg	%r1,32(%r1)
[624457.542882]            000003ffbc127f5e: a7590001		lghi	%r5,1
[624457.542882]            000003ffbc127f62: 4140f0a0		la	%r4,160(%r15)
[624457.542882]            000003ffbc127f66: 0de1		basr	%r14,%r1
[624457.542882]            000003ffbc127f68: ec280009007c	cgij	%r2,0,8,3ffbc127f7a
[624457.542893] Last Breaking-Event-Address:
[624457.542896]  [<000003ffbc127f32>] 0x3ffbc127f32
[624458.013783] User process fault: interruption code 0038 ilc:3 in libstdc++.so.6.0.23[3ff94f00000+1b9000]
[624458.013795] Failing address: 5465737473756000 TEID: 5465737473756800
[624458.013797] Fault in primary space mode while using user ASCE.
[624458.013801] AS:0000000004be41c7 R3:0000000000000024
[624458.013806] CPU: 1 PID: 6896 Comm: try-catch-9.exe Not tainted 4.8.15-300.fc25.s390x #1
[624458.013809] Hardware name: IBM              2827 H43              400              (z/VM)
[624458.013812] task: 00000000f5b4b900 task.stack: 00000000061f4000
[624458.013815] User PSW : 0705000180000000 000003ff94fa7f58
[624458.013818]            R:0 T:1 IO:1 EX:1 Key:0 M:1 W:0 P:1 AS:0 CC:0 PM:0 RI:0 EA:3
[624458.013818] User GPRS: 0000000000000000 5465737473756974 00000000800032a4 000003ff950bba00
[624458.013826]            000003ffd0df96f0 000003ffd0df9628 0000000080001338 0000000000000000
[624458.013830]            000003ff00000000 000003ffd0df96f0 00000000800032a4 000003ff950bba00
[624458.013834]            00000000a19d4e90 000003ff95072658 000003ff94fa7f32 000003ffd0df9588
[624458.013852] User Code: 000003ff94fa7f4a: e310a0000004	lg	%r1,0(%r10)
[624458.013852]            000003ff94fa7f50: b904003b		lgr	%r3,%r11
[624458.013852]           #000003ff94fa7f54: b904002a		lgr	%r2,%r10
[624458.013852]           >000003ff94fa7f58: e31010200004	lg	%r1,32(%r1)
[624458.013852]            000003ff94fa7f5e: a7590001		lghi	%r5,1
[624458.013852]            000003ff94fa7f62: 4140f0a0		la	%r4,160(%r15)
[624458.013852]            000003ff94fa7f66: 0de1		basr	%r14,%r1
[624458.013852]            000003ff94fa7f68: ec280009007c	cgij	%r2,0,8,3ff94fa7f7a
[624458.013863] Last Breaking-Event-Address:
[624458.013866]  [<000003ff94fa7f32>] 0x3ff94fa7f32
[682281.933336] User process fault: interruption code 003b ilc:3 in cmsysTestProcess[2aa16200000+9000]
[682281.933347] Failing address: 0000000000000000 TEID: 0000000000000400
[682281.933349] Fault in primary space mode while using user ASCE.
[682281.933353] AS:00000000829e01c7 R3:0000000000000024
[682281.933358] CPU: 0 PID: 29755 Comm: cmsysTestProces Not tainted 4.8.15-300.fc25.s390x #1
[682281.933362] Hardware name: IBM              2827 H43              400              (z/VM)
[682281.933365] task: 00000000f5f13900 task.stack: 00000000c2610000
[682281.933368] User PSW : 0705000180000000 000002aa162027a2
[682281.933371]            R:0 T:1 IO:1 EX:1 Key:0 M:1 W:0 P:1 AS:0 CC:0 PM:0 RI:0 EA:3
[682281.933371] User GPRS: 0000000000000000 000003ff00000000 0000000000000000 0000000000000001
[682281.933380]            000000000000002e 000003ff7f848c88 000002aa16207430 000003ffe33ff0a0
[682281.933383]            000002aa1620769e 0000000000000000 000003ff7f848d70 000003ff7f848d68
[682281.933388]            000003ff7f928f58 000002aa16207df0 000002aa16202794 000003ffe33feb68
[682281.934367] User Code: 000002aa16202794: e350a0000004	lg	%r5,0(%r10)
[682281.934367]            000002aa1620279a: a749002e		lghi	%r4,46
[682281.934367]           #000002aa1620279e: a7390001		lghi	%r3,1
[682281.934367]           >000002aa162027a2: e54c00040000	mvhi	4,0
[682281.934367]            000002aa162027a8: c02000002867	larl	%r2,2aa16207876
[682281.934367]            000002aa162027ae: c0e5fffffabd	brasl	%r14,2aa16201d28
[682281.934367]            000002aa162027b4: e350b0000004	lg	%r5,0(%r11)
[682281.934367]            000002aa162027ba: a749002e		lghi	%r4,46
[682281.934379] Last Breaking-Event-Address:
[682281.934382]  [<000003ff7f6fccb8>] 0x3ff7f6fccb8
[682281.935888] User process fault: interruption code 003b ilc:3 in cmsysTestProcess[2aa36500000+9000]
[682281.935896] Failing address: 0000000000000000 TEID: 0000000000000400
[682281.935900] Fault in primary space mode while using user ASCE.
[682281.935910] AS:00000000ab3f01c7 R3:0000000000000024
[682281.935917] CPU: 0 PID: 29759 Comm: cmsysTestProces Not tainted 4.8.15-300.fc25.s390x #1
[682281.935940] Hardware name: IBM              2827 H43              400              (z/VM)
[682281.935941] task: 0000000083025580 task.stack: 00000000bebf4000
[682281.935942] User PSW : 0705000180000000 000002aa365027a2
[682281.935943]            R:0 T:1 IO:1 EX:1 Key:0 M:1 W:0 P:1 AS:0 CC:0 PM:0 RI:0 EA:3
[682281.935943] User GPRS: 0000000000000000 000003ff00000000 0000000000000000 0000000000000001
[682281.935946]            000000000000002e 000003ff9ce48c88 000002aa36507430 000003ffd60febe0
[682281.935947]            000002aa3650769e 0000000000000000 000003ff9ce48d70 000003ff9ce48d68
[682281.935948]            000003ff9cf28f58 000002aa36507df0 000002aa36502794 000003ffd60fe6a8
[682281.935954] User Code: 000002aa36502794: e350a0000004	lg	%r5,0(%r10)
[682281.935954]            000002aa3650279a: a749002e		lghi	%r4,46
[682281.935954]           #000002aa3650279e: a7390001		lghi	%r3,1
[682281.935954]           >000002aa365027a2: e54c00040000	mvhi	4,0
[682281.935954]            000002aa365027a8: c02000002867	larl	%r2,2aa36507876
[682281.935954]            000002aa365027ae: c0e5fffffabd	brasl	%r14,2aa36501d28
[682281.935954]            000002aa365027b4: e350b0000004	lg	%r5,0(%r11)
[682281.935954]            000002aa365027ba: a749002e		lghi	%r4,46
[682281.935964] Last Breaking-Event-Address:
[682281.935965]  [<000003ff9ccfccb8>] 0x3ff9ccfccb8
[682695.568959] User process fault: interruption code 0010 ilc:3 in Crash[1000000+1000]
[682695.568971] Failing address: 0000000000000000 TEID: 0000000000000400
[682695.568973] Fault in primary space mode while using user ASCE.
[682695.568977] AS:00000000549a41c7 R3:000000006654c007 S:0000000000000020
[682695.568983] CPU: 0 PID: 6485 Comm: Crash Not tainted 4.8.15-300.fc25.s390x #1
[682695.568986] Hardware name: IBM              2827 H43              400              (z/VM)
[682695.568989] task: 00000000f81fb900 task.stack: 0000000004058000
[682695.568992] User PSW : 0705100180000000 0000000001000776
[682695.568995]            R:0 T:1 IO:1 EX:1 Key:0 M:1 W:0 P:1 AS:0 CC:1 PM:0 RI:0 EA:3
[682695.568995] User GPRS: 0000000000000000 0000000000000000 0000000000000001 000003ffd4cfe438
[682695.569003]            000003ffd4cfe448 0090305969303276 0000000001000800 000003ffd4cfe420
[682695.569007]            0000000001000668 0000000000000000 000002aa3e31b1f0 000003ffd4cfe168
[682695.569011]            000003ff91328f58 000002aa3e3251f0 000003ff90d22b9e 000003ffd4cfe168
[682695.572673] User Code: 0000000001000766: b90400bf		lgr	%r11,%r15
[682695.572673]            000000000100076a: e548b0a00000	mvghi	160(%r11),0
[682695.572673]           #0000000001000770: e310b0a00004	lg	%r1,160(%r11)
[682695.572673]           >0000000001000776: e54c10000001	mvhi	0(%r1),1
[682695.572673]            000000000100077c: a7180000		lhi	%r1,0
[682695.572673]            0000000001000780: b9140011		lgfr	%r1,%r1
[682695.572673]            0000000001000784: b9040021		lgr	%r2,%r1
[682695.572673]            0000000001000788: b3cd00b2		lgdr	%r11,%f2
[682695.572686] Last Breaking-Event-Address:
[682695.572690]  [<000003ff90d22b9c>] 0x3ff90d22b9c
[699521.918071] User process fault: interruption code 0004 ilc:3 in conftest[1000000+c5000]
[699521.918083] Failing address: 00000000010c6000 TEID: 00000000010c6404
[699521.918085] Fault in primary space mode while using user ASCE.
[699521.918089] AS:00000000a80d41c7 R3:00000000a462c007 S:000000008267e000 P:00000000918ff21d
[699521.918095] CPU: 2 PID: 42951 Comm: conftest Not tainted 4.8.15-300.fc25.s390x #1
[699521.918098] Hardware name: IBM              2827 H43              400              (z/VM)
[699521.918101] task: 00000000f4a41c80 task.stack: 0000000082ff0000
[699521.918104] User PSW : 0705000180000000 000000000100de62
[699521.918107]            R:0 T:1 IO:1 EX:1 Key:0 M:1 W:0 P:1 AS:0 CC:0 PM:0 RI:0 EA:3
[699521.918107] User GPRS: fffffffffffffff0 0000000000000000 000003ffde67c020 0000000000000001
[699521.918116]            000003ffde67c0d8 000000000100e590 000000000100e638 000003ffde67c0c0
[699521.918120]            000000000100dca8 000002aa3f932170 0000000000000000 000002aa3f9d0e10
[699521.918124]            000000000100e590 000002aa3f9d1010 000000000100dce6 000003ffde67beb0
[699521.918140] User Code: 000000000100de54: a71affff		ahi	%r1,-1
[699521.918140]            000000000100de58: 8810001f		srl	%r1,31
[699521.918140]           #000000000100de5c: c41f0005d5a6	strl	%r1,10c89a8
[699521.918140]           >000000000100de62: c42b0005c7ff	stgrl	%r2,10c6e60
[699521.918140]            000000000100de68: e310f0a00004	lg	%r1,160(%r15)
[699521.918140]            000000000100de6e: ec21000100d9	aghik	%r2,%r1,1
[699521.918140]            000000000100de74: eb220003000d	sllg	%r2,%r2,3
[699521.918140]            000000000100de7a: e320f0a80008	ag	%r2,168(%r15)
[699521.918152] Last Breaking-Event-Address:
[699521.918155]  [<000000000100dce0>] 0x100dce0
[701836.544344] User process fault: interruption code 0004 ilc:3 in conftest[1000000+c5000]
[701836.544354] Failing address: 00000000010c6000 TEID: 00000000010c6404
[701836.544357] Fault in primary space mode while using user ASCE.
[701836.544360] AS:00000000ef6401c7 R3:00000000b52c0007 S:00000000a9721000 P:00000000ce7c021d
[701836.544367] CPU: 3 PID: 48640 Comm: conftest Not tainted 4.8.15-300.fc25.s390x #1
[701836.544370] Hardware name: IBM              2827 H43              400              (z/VM)
[701836.544374] task: 00000000f5b4b900 task.stack: 000000008287c000
[701836.544377] User PSW : 0705000180000000 000000000100de62
[701836.544380]            R:0 T:1 IO:1 EX:1 Key:0 M:1 W:0 P:1 AS:0 CC:0 PM:0 RI:0 EA:3
[701836.544380] User GPRS: fffffffffffffff0 0000000000000000 000003ffeaf7bfa0 0000000000000001
[701836.544389]            000003ffeaf7c058 000000000100e590 000000000100e638 000003ffeaf7c040
[701836.544393]            000000000100dca8 000002aa48a418c0 0000000000000000 000002aa48a4b240
[701836.544397]            000000000100e590 000002aa48a52730 000000000100dce6 000003ffeaf7be30
[701836.544414] User Code: 000000000100de54: a71affff		ahi	%r1,-1
[701836.544414]            000000000100de58: 8810001f		srl	%r1,31
[701836.544414]           #000000000100de5c: c41f0005d5a6	strl	%r1,10c89a8
[701836.544414]           >000000000100de62: c42b0005c7ff	stgrl	%r2,10c6e60
[701836.544414]            000000000100de68: e310f0a00004	lg	%r1,160(%r15)
[701836.544414]            000000000100de6e: ec21000100d9	aghik	%r2,%r1,1
[701836.544414]            000000000100de74: eb220003000d	sllg	%r2,%r2,3
[701836.544414]            000000000100de7a: e320f0a80008	ag	%r2,168(%r15)
[701836.544427] Last Breaking-Event-Address:
[701836.544429]  [<000000000100dce0>] 0x100dce0
[702856.049112] User process fault: interruption code 0004 ilc:3 in conftest[1000000+c5000]
[702856.049125] Failing address: 00000000010c6000 TEID: 00000000010c6404
[702856.049127] Fault in primary space mode while using user ASCE.
[702856.049131] AS:00000000801581c7 R3:00000000a7da4007 S:00000000802e9000 P:00000000a540621d
[702856.049138] CPU: 2 PID: 53342 Comm: conftest Not tainted 4.8.15-300.fc25.s390x #1
[702856.049141] Hardware name: IBM              2827 H43              400              (z/VM)
[702856.049144] task: 00000000f5b49c80 task.stack: 00000000f3f70000
[702856.049147] User PSW : 0705000180000000 000000000100de62
[702856.049151]            R:0 T:1 IO:1 EX:1 Key:0 M:1 W:0 P:1 AS:0 CC:0 PM:0 RI:0 EA:3
[702856.049151] User GPRS: fffffffffffffff0 0000000000000000 000003fff267b9b0 0000000000000001
[702856.049160]            000003fff267ba68 000000000100e590 000000000100e638 000003fff267ba50
[702856.049163]            000000000100dca8 000002aa1fc0f9b0 0000000000000000 000002aa1fced3e0
[702856.049168]            000000000100e590 000002aa1fceda20 000000000100dce6 000003fff267b840
[702856.049188] User Code: 000000000100de54: a71affff		ahi	%r1,-1
[702856.049188]            000000000100de58: 8810001f		srl	%r1,31
[702856.049188]           #000000000100de5c: c41f0005d5a6	strl	%r1,10c89a8
[702856.049188]           >000000000100de62: c42b0005c7ff	stgrl	%r2,10c6e60
[702856.049188]            000000000100de68: e310f0a00004	lg	%r1,160(%r15)
[702856.049188]            000000000100de6e: ec21000100d9	aghik	%r2,%r1,1
[702856.049188]            000000000100de74: eb220003000d	sllg	%r2,%r2,3
[702856.049188]            000000000100de7a: e320f0a80008	ag	%r2,168(%r15)
[702856.049200] Last Breaking-Event-Address:
[702856.049203]  [<000000000100dce0>] 0x100dce0
[703009.939101] User process fault: interruption code 0004 ilc:3 in conftest[1000000+c5000]
[703009.939113] Failing address: 00000000010c6000 TEID: 00000000010c6404
[703009.939116] Fault in primary space mode while using user ASCE.
[703009.939119] AS:0000000000dd41c7 R3:00000000014e8007 S:0000000000ea3000 P:00000000405c321d
[703009.939126] CPU: 0 PID: 47870 Comm: conftest Not tainted 4.8.15-300.fc25.s390x #1
[703009.939129] Hardware name: IBM              2827 H43              400              (z/VM)
[703009.939132] task: 0000000005645580 task.stack: 000000000c554000
[703009.939135] User PSW : 0705000180000000 000000000100de62
[703009.939139]            R:0 T:1 IO:1 EX:1 Key:0 M:1 W:0 P:1 AS:0 CC:0 PM:0 RI:0 EA:3
[703009.939139] User GPRS: fffffffffffffff0 0000000000000000 000003fff327c090 0000000000000001
[703009.939147]            000003fff327c148 000000000100e590 000000000100e638 000003fff327c130
[703009.939151]            000000000100dca8 000002aa309f3570 0000000000000000 000002aa309ee380
[703009.939155]            000000000100e590 000002aa30a96c80 000000000100dce6 000003fff327bf20
[703009.939894] User Code: 000000000100de54: a71affff		ahi	%r1,-1
[703009.939894]            000000000100de58: 8810001f		srl	%r1,31
[703009.939894]           #000000000100de5c: c41f0005d5a6	strl	%r1,10c89a8
[703009.939894]           >000000000100de62: c42b0005c7ff	stgrl	%r2,10c6e60
[703009.939894]            000000000100de68: e310f0a00004	lg	%r1,160(%r15)
[703009.939894]            000000000100de6e: ec21000100d9	aghik	%r2,%r1,1
[703009.939894]            000000000100de74: eb220003000d	sllg	%r2,%r2,3
[703009.939894]            000000000100de7a: e320f0a80008	ag	%r2,168(%r15)
[703009.939931] Last Breaking-Event-Address:
[703009.939936]  [<000000000100dce0>] 0x100dce0
[703026.481842] User process fault: interruption code 0004 ilc:3 in conftest[1000000+c5000]
[703026.481852] Failing address: 00000000010c6000 TEID: 00000000010c6404
[703026.481854]

'''
		return returncode, output


class TestLinuxFedora_5_s390x(unittest.TestCase):
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
		self.assertEqual(7, len(cpuinfo._get_cpu_info_from_proc_cpuinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysctl()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_kstat()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(17, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()

		self.assertEqual('IBM/S390', info['vendor_id_raw'])
		#self.assertEqual('FIXME', info['brand'])
		self.assertEqual('5.5040 GHz', info['hz_advertised_friendly'])
		self.assertEqual('5.5040 GHz', info['hz_actual_friendly'])
		self.assertEqual((5504000000, 0), info['hz_advertised'])
		self.assertEqual((5504000000, 0), info['hz_actual'])

		#self.assertEqual(7, info['stepping'])
		#self.assertEqual(42, info['model'])
		#self.assertEqual(6, info['family'])

		self.assertEqual(64 * 1024, info['l1_instruction_cache_size'])
		self.assertEqual(96 * 1024, info['l1_data_cache_size'])

		self.assertEqual(1024 * 1024, info['l2_cache_size'])
		self.assertEqual(49152 * 1024, info['l3_cache_size'])

		self.assertEqual(
			['dfp', 'eimm', 'esan3', 'etf3eh', 'highgprs', 'ldisp',
			'msa', 'sie', 'stfle', 'zarch']
			,
			info['flags']
		)

	def test_get_cpu_info_from_dmesg(self):
		info = cpuinfo._get_cpu_info_from_dmesg()

		#self.assertEqual('FIXME', info['brand'])

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('IBM/S390', info['vendor_id_raw'])
		#self.assertEqual('FIXME', info['brand'])
		self.assertEqual('5.5040 GHz', info['hz_advertised_friendly'])
		self.assertEqual('5.5040 GHz', info['hz_actual_friendly'])
		self.assertEqual((5504000000, 0), info['hz_advertised'])
		self.assertEqual((5504000000, 0), info['hz_actual'])

		self.assertEqual(49152 * 1024, info['l3_cache_size'])

		#self.assertEqual(7, info['stepping'])
		#self.assertEqual(42, info['model'])
		#self.assertEqual(6, info['family'])
		self.assertEqual(
			['dfp', 'edat', 'eimm', 'esan3', 'etf3eh', 'highgprs', 'ldisp',
			'msa', 'sie', 'stfle', 'te', 'zarch']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()
		self.assertEqual('IBM/S390', info['vendor_id_raw'])
		#self.assertEqual('FIXME', info['brand'])
		self.assertEqual('5.5040 GHz', info['hz_advertised_friendly'])
		self.assertEqual('5.5040 GHz', info['hz_actual_friendly'])
		self.assertEqual((5504000000, 0), info['hz_advertised'])
		self.assertEqual((5504000000, 0), info['hz_actual'])
		self.assertEqual('S390X', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(4, info['count'])

		self.assertEqual('s390x', info['arch_string_raw'])

		self.assertEqual(64 * 1024, info['l1_instruction_cache_size'])
		self.assertEqual(96 * 1024, info['l1_data_cache_size'])

		self.assertEqual(1024 * 1024, info['l2_cache_size'])
		self.assertEqual(49152 * 1024, info['l3_cache_size'])

		#self.assertEqual(7, info['stepping'])
		#self.assertEqual(42, info['model'])
		#self.assertEqual(6, info['family'])
		self.assertEqual(
			['dfp', 'edat', 'eimm', 'esan3', 'etf3eh', 'highgprs', 'ldisp',
			'msa', 'sie', 'stfle', 'te', 'zarch'],
			info['flags']
		)
