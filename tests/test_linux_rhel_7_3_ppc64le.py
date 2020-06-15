

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 16
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
		output = r'''
/proc/device-tree/cpus/PowerPC,POWER7@1/ibm,pa-features 3ff60006 c08000c7

'''
		return returncode, output

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = r'''
processor	: 0
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 1
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 2
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 3
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 4
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 5
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 6
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 7
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 8
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 9
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 10
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 11
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 12
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 13
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 14
cpu		: POWER8E (raw), altivec supported
clock		: 3425.000000MHz
revision	: 2.1 (pvr 004b 0201)

processor	: 15
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
		output = r'''
[3269512.154534] convolution_var[11236]: unhandled signal 4 at 00003fff6c390004 nip 00003fff6c390004 lr 00003fff9a648d58 code 30001
[3269512.234818] convolution_var[11344]: unhandled signal 5 at 00003fff84390000 nip 00003fff84390000 lr 00003fffb2217ce0 code 30001
[3269512.234823] convolution_var[11347]: unhandled signal 11 at 0000000000000304 nip 00003fff8439001c lr 00003fffb2217ce0 code 30001
[3269512.292530] convolution_var[11435]: unhandled signal 11 at 0000000000000304 nip 00003fff565d001c lr 00003fff84457ce0 code 30001
[3269512.553601] convolution_var[11518]: unhandled signal 11 at 00003fff61278b68 nip 00003fff61278b68 lr 00003fff8f0d7ce0 code 30002
[3269515.267175] convolution_var[11623]: unhandled signal 5 at 00003fff70450000 nip 00003fff70450000 lr 00003fff9e2d7ce0 code 30001
[3269515.278982] convolution_var[11704]: unhandled signal 11 at 00003fff5e028b68 nip 00003fff5e028b68 lr 00003fff8be87ce0 code 30002
[3269516.050175] convolution_var[11803]: unhandled signal 4 at 00003fff73890008 nip 00003fff73890008 lr 00003fffa1717ce0 code 30001
[3269516.494489] convolution_var[11917]: unhandled signal 11 at 00003fff4c588b48 nip 00003fff4c588b48 lr 00003fff7a3e7ce0 code 30002
[3269516.494496] convolution_var[11918]: unhandled signal 11 at 00003fff4c588b98 nip 00003fff4c588b98 lr 00003fff7a3e7ce0 code 30002
[3269517.347386] convolution_var[12040]: unhandled signal 4 at 00003fff7c530000 nip 00003fff7c530000 lr 00003fffaa3b7ce0 code 30001
[3269517.494333] convolution_var[12299]: unhandled signal 4 at 00003fff88fe0008 nip 00003fff88fe0008 lr 00003fffb6e67ce0 code 30001
[3269517.494347] convolution_var[12301]: unhandled signal 5 at 00003fff88fe0100 nip 00003fff88fe0100 lr 00003fffb6e67ce0 code 30001
[3269517.515814] convolution_var[12120]: unhandled signal 4 at 00003fff6fbd0004 nip 00003fff6fbd0004 lr 00003fff9da57ce0 code 30001
[3269517.516110] convolution_var[12121]: unhandled signal 4 at 00003fff6fbd00c8 nip 00003fff6fbd00c8 lr 00003fff9da57ce0 code 30001
[3269520.521582] _exception: 10 callbacks suppressed
[3269520.521591] convolution_var[12805]: unhandled signal 5 at 00003fff53c70000 nip 00003fff53c70000 lr 00003fff81af7ce0 code 30001
[3269528.348091] convolution_var[12977]: unhandled signal 4 at 00003fff51190008 nip 00003fff51190008 lr 00003fff7f017ce0 code 30001
[3269528.490362] convolution_var[13076]: unhandled signal 5 at 00003fff77e80000 nip 00003fff77e80000 lr 00003fffa5d07ce0 code 30001
[3269528.529240] convolution_var[13168]: unhandled signal 4 at 00003fff5cf70018 nip 00003fff5cf70018 lr 00003fff8adf7ce0 code 30001
[3269528.529260] convolution_var[13165]: unhandled signal 5 at 00003fff5cf70000 nip 00003fff5cf70000 lr 00003fff8adf7ce0 code 30001
[3269528.582530] convolution_var[13249]: unhandled signal 5 at 00003fff58660000 nip 00003fff58660000 lr 00003fff864e7ce0 code 30001
[3269528.582599] convolution_var[13242]: unhandled signal 5 at 00003fff586600c0 nip 00003fff586600c0 lr 00003fff864e7ce0 code 30001
[3269528.754904] convolution_var[13330]: unhandled signal 4 at 00003fff6c870018 nip 00003fff6c870018 lr 00003fff9a6f7ce0 code 30001
[3269528.754911] convolution_var[13328]: unhandled signal 5 at 00003fff6c870000 nip 00003fff6c870000 lr 00003fff9a6f7ce0 code 30001
[3269529.063266] convolution_var[13411]: unhandled signal 5 at 00003fff88e00000 nip 00003fff88e00000 lr 00003fffb6c87ce0 code 30001
[3269539.946696] _exception: 8 callbacks suppressed
[3269539.946703] convolution_tes[14002]: unhandled signal 11 at 0000000000005359 nip 00003fff4a2b0008 lr 00003fff4a2b0004 code 30001
[3269540.270205] convolution_tes[14014]: unhandled signal 11 at 000000000000535a nip 00003fff5d8f0000 lr 00003fff8bba8d58 code 30001
[3269540.370546] convolution_tes[14007]: unhandled signal 4 at 00003fff4e3d0000 nip 00003fff4e3d0000 lr 00003fff7c688d58 code 30001
[3269540.410762] convolution_tes[14057]: unhandled signal 4 at 00003fff6e140004 nip 00003fff6e140004 lr 00003fff9c3f8d58 code 30001
[3269540.426502] convolution_tes[14034]: unhandled signal 11 at 0000000000005359 nip 00003fff5fd10008 lr 00003fff5fd10004 code 30001
[3269540.702543] convolution_tes[14059]: unhandled signal 11 at 00003fff63518b50 nip 00003fff63518b50 lr 00003fff91628d58 code 30002
[3269542.514020] convolution_tes[14155]: unhandled signal 11 at 0000000000005357 nip 00003fff63c40008 lr 00003fff63c40004 code 30001
[3269542.879959] convolution_tes[14889]: unhandled signal 5 at 00003fff87610030 nip 00003fff87610030 lr 00003fffb5497ce0 code 30001
[3269543.056385] convolution_tes[14979]: unhandled signal 5 at 00003fff85bf0030 nip 00003fff85bf0030 lr 00003fffb3a77ce0 code 30001
[3269543.106248] convolution_tes[14809]: unhandled signal 11 at 0000000000006354 nip 00003fff78930008 lr 00003fff78930004 code 30001
[3269549.407969] _exception: 4 callbacks suppressed
[3269549.407976] convolution_dim[15825]: unhandled signal 4 at 00003fff656201b0 nip 00003fff656201b0 lr 00003fff934a7ce0 code 30001
[3269549.407989] convolution_dim[15821]: unhandled signal 4 at 00003fff65620008 nip 00003fff65620008 lr 00003fff934a7ce0 code 30001
[3269549.691129] convolution_dim[15792]: unhandled signal 11 at 00003fff5b49535c nip 00003fff5b49535c lr 00003fff5af90004 code 30002
[3269553.222974] copy_test_cpu[16296]: unhandled signal 4 at 00003fff96790004 nip 00003fff96790004 lr 00003fffb0a38d58 code 30001
[3269553.346577] pad_test_cpu_pa[16409]: unhandled signal 4 at 00003fff5d7a0000 nip 00003fff5d7a0000 lr 00003fff8b627ce0 code 30001
[3269556.099815] params_test_cpu[16532]: unhandled signal 4 at 00003fff7d8b0008 nip 00003fff7d8b0008 lr 00003fffab737ce0 code 30001
[3269556.192880] prng_test_cpu_p[16637]: unhandled signal 11 at 00003fff7f178b48 nip 00003fff7f178b48 lr 00003fffacfd7ce0 code 30002
[3269556.870898] reshape_test_cp[16728]: unhandled signal 11 at 00003fff7b048b48 nip 00003fff7b048b48 lr 00003fffa8ea7ce0 code 30002
[3269556.903001] reshape_test_cp[16795]: unhandled signal 11 at 00003fff7c708b48 nip 00003fff7c708b48 lr 00003fffaa567ce0 code 30002
[3269557.003338] dot_operation_t[16891]: unhandled signal 4 at 00003fff66c70000 nip 00003fff66c70000 lr 00003fff94af7ce0 code 30001
[3269557.370482] reduce_test_cpu[16967]: unhandled signal 5 at 00003fff857a0000 nip 00003fff857a0000 lr 00003fffb3a37ce0 code 30001
[3269557.880800] dynamic_ops_tes[17047]: unhandled signal 5 at 00003fff73650000 nip 00003fff73650000 lr 00003fffa14d7ce0 code 30001
[3269560.308483] replay_test_cpu[17146]: unhandled signal 11 at 0000000000000100 nip 00003fff79300004 lr 00003fffa7187ce0 code 30001
[3269560.367931] dot_operation_s[17227]: unhandled signal 4 at 00003fff699e0000 nip 00003fff699e0000 lr 00003fff97867ce0 code 30001
[3269562.120943] slice_test_cpu_[17324]: unhandled signal 4 at 00003fff7fa10008 nip 00003fff7fa10008 lr 00003fffad897ce0 code 30001
[3269562.219657] slice_test_cpu_[17390]: unhandled signal 4 at 00003fff5a4d0008 nip 00003fff5a4d0008 lr 00003fff88357ce0 code 30001
[3269562.955471] vector_ops_redu[17512]: unhandled signal 11 at 00003fff57778b48 nip 00003fff57778b48 lr 00003fff855d7ce0 code 30002
[3269563.076629] multidimensiona[17593]: unhandled signal 5 at 00003fff57870004 nip 00003fff57870004 lr 00003fff856f7ce0 code 30001
[3269563.221596] slice_test_cpu_[17676]: unhandled signal 4 at 00003fff4cee0008 nip 00003fff4cee0008 lr 00003fff7adb7ce0 code 30001
[3269563.698994] reshape_motion_[17773]: unhandled signal 11 at 00003fff70e08b98 nip 00003fff70e08b98 lr 00003fff9ec67ce0 code 30002
[3269564.681067] select_test_cpu[17872]: unhandled signal 11 at 00003fff5ba08b48 nip 00003fff5ba08b48 lr 00003fff89867ce0 code 30002
[3269564.777619] scalar_computat[17953]: unhandled signal 4 at 00003fff6d3b0008 nip 00003fff6d3b0008 lr 00003fff9b237ce0 code 30001
[3269564.790486] scalar_computat[18034]: unhandled signal 5 at 00003fff83610000 nip 00003fff83610000 lr 00003fffb1497ce0 code 30001
[3269565.287122] scalar_computat[18115]: unhandled signal 11 at 00003fff86588b48 nip 00003fff86588b48 lr 00003fffb43e7ce0 code 30002
[3269569.216594] scalar_computat[18241]: unhandled signal 5 at 00003fff5b360004 nip 00003fff5b360004 lr 00003fff891e7ce0 code 30001
[3269569.621130] scalar_computat[18346]: unhandled signal 5 at 00003fff82d70004 nip 00003fff82d70004 lr 00003fffb0bf7ce0 code 30001
[3269569.710500] scalar_computat[18427]: unhandled signal 5 at 00003fff4b4f0000 nip 00003fff4b4f0000 lr 00003fff79377ce0 code 30001
[3269569.876037] scalar_computat[18514]: unhandled signal 5 at 00003fff76050000 nip 00003fff76050000 lr 00003fffa3ed7ce0 code 30001
[3269569.898662] scalar_computat[18606]: unhandled signal 11 at 00003fff7d7f8b48 nip 00003fff7d7f8b48 lr 00003fffab657ce0 code 30002
[3269570.506464] scalar_computat[18691]: unhandled signal 5 at 00003fff716a0000 nip 00003fff716a0000 lr 00003fff9f527ce0 code 30001
[3269570.599202] scalar_computat[18774]: unhandled signal 5 at 00003fff64410000 nip 00003fff64410000 lr 00003fff92297ce0 code 30001
[3269572.942730] scalar_computat[18867]: unhandled signal 5 at 00003fff77d30000 nip 00003fff77d30000 lr 00003fffa5bb7ce0 code 30001
[3269576.610680] scalar_computat[18966]: unhandled signal 5 at 00003fff87c00000 nip 00003fff87c00000 lr 00003fffb5a87ce0 code 30001
[3269576.708070] scalar_computat[19047]: unhandled signal 11 at 000000000000100c nip 000000000000100c lr 00003fff52a80008 code 30001
[3269581.598515] scalar_computat[19139]: unhandled signal 5 at 00003fff54490000 nip 00003fff54490000 lr 00003fff82317ce0 code 30001
[3269582.171060] scalar_computat[19237]: unhandled signal 4 at 00003fff68110008 nip 00003fff68110008 lr 00003fff95f97ce0 code 30001
[3269583.009677] scalar_computat[19337]: unhandled signal 4 at 00003fff67130008 nip 00003fff67130008 lr 00003fff94fb7ce0 code 30001
[3269583.292630] slice_test_cpu_[19413]: unhandled signal 4 at 00003fff6f110000 nip 00003fff6f110000 lr 00003fff9cf97ce0 code 30001
[3269583.448451] slice_test_cpu_[19497]: unhandled signal 4 at 00003fff7eac0000 nip 00003fff7eac0000 lr 00003fffac947ce0 code 30001
[3269584.161867] slice_test_cpu_[19598]: unhandled signal 4 at 00003fff78720000 nip 00003fff78720000 lr 00003fffa65a7ce0 code 30001
[3269584.600430] slice_test_cpu_[19679]: unhandled signal 5 at 00003fff6c510004 nip 00003fff6c510004 lr 00003fff9a397ce0 code 30001
[3269586.198292] slice_test_cpu_[19769]: unhandled signal 5 at 00003fff60dc0004 nip 00003fff60dc0004 lr 00003fff8ec47ce0 code 30001
[3269587.335554] slice_test_cpu_[19868]: unhandled signal 4 at 00003fff7c460008 nip 00003fff7c460008 lr 00003fffaa3a7ce0 code 30001
[3269587.337351] slice_test_cpu_[19945]: unhandled signal 4 at 00003fff4cf50008 nip 00003fff4cf50008 lr 00003fff7aea7ce0 code 30001
[3269587.812645] slice_test_cpu_[20039]: unhandled signal 5 at 00003fff60c60000 nip 00003fff60c60000 lr 00003fff8eae7ce0 code 30001
[3269593.957612] slice_test_cpu_[20237]: unhandled signal 5 at 00003fff6bc10000 nip 00003fff6bc10000 lr 00003fff99a97ce0 code 30001
[3269594.113130] slice_test_cpu_[20327]: unhandled signal 5 at 00003fff50680000 nip 00003fff50680000 lr 00003fff7e507ce0 code 30001
[3269594.478182] slice_test_cpu_[20451]: unhandled signal 5 at 00003fff49ed0004 nip 00003fff49ed0004 lr 00003fff77d57ce0 code 30001
[3269594.480120] slice_test_cpu_[20534]: unhandled signal 5 at 00003fff864f0000 nip 00003fff864f0000 lr 00003fffb4377ce0 code 30001
[3269594.910096] slice_test_cpu_[20641]: unhandled signal 5 at 00003fff71b90004 nip 00003fff71b90004 lr 00003fff9fa17ce0 code 30001
[3269595.075412] slice_test_cpu_[20742]: unhandled signal 5 at 00003fff6e850004 nip 00003fff6e850004 lr 00003fff9c6d7ce0 code 30001
[3269595.201874] slice_test_cpu_[20823]: unhandled signal 5 at 00003fff860c0000 nip 00003fff860c0000 lr 00003fffb3f47ce0 code 30001
[3269595.376406] slice_test_cpu_[20905]: unhandled signal 5 at 00003fff840d0000 nip 00003fff840d0000 lr 00003fffb1f57ce0 code 30001
[3269595.392470] slice_test_cpu_[20980]: unhandled signal 4 at 00003fff590b0000 nip 00003fff590b0000 lr 00003fff86f37ce0 code 30001
[3269595.956190] slice_test_cpu_[21073]: unhandled signal 4 at 00003fff4f540000 nip 00003fff4f540000 lr 00003fff7d3c7ce0 code 30001
[3269599.193940] _exception: 4 callbacks suppressed
[3269599.193949] reshape_test_cp[21584]: unhandled signal 4 at 00003fff81e20000 nip 00003fff81e20000 lr 00003fffafca7ce0 code 30001
[3269599.216800] slice_test_cpu_[21665]: unhandled signal 4 at 00003fff69f70000 nip 00003fff69f70000 lr 00003fff97e67ce0 code 30001
[3269599.445597] reshape_test_cp[21746]: unhandled signal 4 at 00003fff78d40000 nip 00003fff78d40000 lr 00003fffa6bc7ce0 code 30001
[3269602.512667] reshape_test_cp[21841]: unhandled signal 11 at 00003fff52e88b48 nip 00003fff52e88b48 lr 00003fff80ce7ce0 code 30002
[3269602.605673] reshape_test_cp[21936]: unhandled signal 11 at 00003fff54a68b48 nip 00003fff54a68b48 lr 00003fff828c7ce0 code 30002
[3269603.484456] reshape_test_cp[22051]: unhandled signal 11 at 00003fff5b038b50 nip 00003fff5b038b50 lr 00003fff5b010004 code 30002
[3269603.644983] reshape_test_cp[22144]: unhandled signal 4 at 00003fff73370000 nip 00003fff73370000 lr 00003fffa11f7ce0 code 30001
[3269603.695153] reshape_test_cp[22225]: unhandled signal 11 at 00003fff80e08b48 nip 00003fff80e08b48 lr 00003fffaec67ce0 code 30002
[3269603.856123] reshape_test_cp[22306]: unhandled signal 4 at 00003fff684e0000 nip 00003fff684e0000 lr 00003fff96367ce0 code 30001
[3269604.061299] reshape_test_cp[22396]: unhandled signal 11 at 0000000000006354 nip 00003fff51890008 lr 00003fff51890004 code 30001
[3269604.457348] reshape_test_cp[22478]: unhandled signal 4 at 00003fff72eb0000 nip 00003fff72eb0000 lr 00003fffa0d37ce0 code 30001
[3269604.642991] reshape_test_cp[22559]: unhandled signal 11 at 0000000000006354 nip 00003fff61d20008 lr 00003fff61d20004 code 30001
[3269605.527665] reshape_test_cp[22658]: unhandled signal 4 at 00003fff713e0000 nip 00003fff713e0000 lr 00003fff9f267ce0 code 30001
[3269605.976692] reshape_test_cp[22748]: unhandled signal 11 at 00003fff87608b48 nip 00003fff87608b48 lr 00003fffb5467ce0 code 30002
[3269605.992050] reshape_test_cp[22829]: unhandled signal 11 at 00003fff518c8b50 nip 00003fff518c8b50 lr 00003fff518a0004 code 30002
[3269608.472197] reshape_test_cp[22919]: unhandled signal 11 at 00003fff79bb8b48 nip 00003fff79bb8b48 lr 00003fffa7a17ce0 code 30002
[3269611.248566] reshape_test_cp[23045]: unhandled signal 11 at 0000000000006354 nip 00003fff81aa0008 lr 00003fff81aa0004 code 30001
[3269611.412038] reshape_test_cp[23138]: unhandled signal 11 at 0000000000006354 nip 00003fff80170008 lr 00003fff80170004 code 30001
[3269612.034633] reshape_test_cp[23249]: unhandled signal 4 at 00003fff79bb0000 nip 00003fff79bb0000 lr 00003fffa7a37ce0 code 30001
[3269612.349955] reshape_test_cp[23341]: unhandled signal 11 at 00003fff65c68b48 nip 00003fff65c68b48 lr 00003fff93ac7ce0 code 30002
[3269612.369781] reshape_test_cp[23424]: unhandled signal 11 at 0000000000006354 nip 00003fff7f190008 lr 00003fff7f190004 code 30001
[3269612.496757] reshape_test_cp[23587]: unhandled signal 4 at 00003fff81db0008 nip 00003fff81db0008 lr 00003fffafc37ce0 code 30001
[3269612.631287] reshape_test_cp[23693]: unhandled signal 11 at 00003fff6db38b50 nip 00003fff6db38b50 lr 00003fff6db10004 code 30002
[3269612.639145] reshape_test_cp[23677]: unhandled signal 11 at 0000000000006354 nip 00003fff49750008 lr 00003fff49750004 code 30001
[3269612.935010] reshape_test_cp[23932]: unhandled signal 4 at 00003fff7ef00000 nip 00003fff7ef00000 lr 00003fffacd87ce0 code 30001
[3269613.204962] reshape_test_cp[24005]: unhandled signal 11 at 0000000000006354 nip 00003fff6e890008 lr 00003fff6e890004 code 30001
[3269622.226190] _exception: 1 callbacks suppressed
[3269622.226199] reduce_test_cpu[24212]: unhandled signal 5 at 00003fff563f0000 nip 00003fff563f0000 lr 00003fff84277ce0 code 30001
[3269622.452519] reduce_test_cpu[24314]: unhandled signal 11 at 00003fff7d7943e1 nip 00003fff5c780008 lr 00003fff8a607ce0 code 30002
[3269622.733732] reduce_test_cpu[24394]: unhandled signal 5 at 00003fff4c8e0000 nip 00003fff4c8e0000 lr 00003fff7a767ce0 code 30001
[3269622.965474] reduce_test_cpu[24489]: unhandled signal 11 at 00003fff4e1c8b48 nip 00003fff4e1c8b48 lr 00003fff7c027ce0 code 30002
[3269623.056180] reduce_test_cpu[24570]: unhandled signal 11 at 00003fff85a18b48 nip 00003fff85a18b48 lr 00003fffb3877ce0 code 30002
[3269623.126112] reduce_test_cpu[24651]: unhandled signal 5 at 00003fff73240000 nip 00003fff73240000 lr 00003fffa10c7ce0 code 30001
[3269623.346425] reduce_test_cpu[24742]: unhandled signal 11 at 00003fff708d8b48 nip 00003fff708d8b48 lr 00003fff9e737ce0 code 30002
[3269623.850463] reduce_test_cpu[24823]: unhandled signal 5 at 00003fff72f70000 nip 00003fff72f70000 lr 00003fffa0df7ce0 code 30001
[3269627.974103] reduce_test_cpu[24992]: unhandled signal 4 at 00003fff72600000 nip 00003fff72600000 lr 00003fffa0487ce0 code 30001
[3269628.219758] reduce_test_cpu[25085]: unhandled signal 11 at c0000005b700c08b nip 00003fff7b570004 lr 00003fffa94f7ce0 code 30001
[3269628.255963] reduce_test_cpu[25161]: unhandled signal 5 at 00003fff4acc0000 nip 00003fff4acc0000 lr 00003fff78b47ce0 code 30001
[3269628.304725] reduce_test_cpu[25236]: unhandled signal 5 at 00003fff69bc0000 nip 00003fff69bc0000 lr 00003fff97a47ce0 code 30001
[3269628.397040] reduce_test_cpu[25324]: unhandled signal 5 at 00003fff81880000 nip 00003fff81880000 lr 00003fffaf707ce0 code 30001
[3269628.463472] reduce_test_cpu[25410]: unhandled signal 4 at 00003fff648b0008 nip 00003fff648b0008 lr 00003fff92737ce0 code 30001
[3269629.249223] reduce_test_cpu[25560]: unhandled signal 11 at 00003fff6c718b48 nip 00003fff6c718b48 lr 00003fff9a577ce0 code 30002
[3269629.249869] reduce_test_cpu[25491]: unhandled signal 4 at 00003fff4fe20000 nip 00003fff4fe20000 lr 00003fff7e267ce0 code 30001
[3269629.291868] reduce_test_cpu[25653]: unhandled signal 5 at 00003fff593c0000 nip 00003fff593c0000 lr 00003fff87247ce0 code 30001
[3269629.316239] reduce_test_cpu[25736]: unhandled signal 4 at 00003fff4af30000 nip 00003fff4af30000 lr 00003fff78db7ce0 code 30001
[3269633.231330] _exception: 1 callbacks suppressed
[3269633.231337] reduce_test_cpu[25990]: unhandled signal 11 at 00003fff4f0c8b48 nip 00003fff4f0c8b48 lr 00003fff7cf27ce0 code 30002
[3269633.323894] reduce_test_cpu[26070]: unhandled signal 11 at 00003fff53008b48 nip 00003fff53008b48 lr 00003fff80e67ce0 code 30002
[3269633.551347] reduce_test_cpu[26161]: unhandled signal 11 at 00003fff9f4143e1 nip 00003fff7ec00008 lr 00003fffaca87ce0 code 30002
[3269633.600659] reduce_test_cpu[26234]: unhandled signal 5 at 00003fff88dd0000 nip 00003fff88dd0000 lr 00003fffb6c57ce0 code 30001
[3269633.639976] reduce_test_cpu[26323]: unhandled signal 11 at 00003fff6d2e8b48 nip 00003fff6d2e8b48 lr 00003fff9b147ce0 code 30002
[3269633.944369] reduce_test_cpu[26488]: unhandled signal 11 at 00003fff80b58b48 nip 00003fff80b58b48 lr 00003fffae9b7ce0 code 30002
[3269634.096959] reduce_test_cpu[26650]: unhandled signal 5 at 00003fff5f520000 nip 00003fff5f520000 lr 00003fff8d3a7ce0 code 30001
[3269634.098910] reduce_test_cpu[26407]: unhandled signal 5 at 00003fff4cfd0000 nip 00003fff4cfd0000 lr 00003fff7b417ce0 code 30001
[3269634.138050] reduce_test_cpu[26728]: unhandled signal 5 at 00003fff51e10000 nip 00003fff51e10000 lr 00003fff7fc97ce0 code 30001
[3269634.198210] reduce_test_cpu[26799]: unhandled signal 11 at 00003fff52758b48 nip 00003fff52758b48 lr 00003fff805b7ce0 code 30002
[3269641.876559] _exception: 2 callbacks suppressed
[3269641.876568] reduce_test_cpu[27004]: unhandled signal 5 at 00003fff67700000 nip 00003fff67700000 lr 00003fff95587ce0 code 30001
[3269641.881005] reduce_test_cpu[27043]: unhandled signal 11 at c0000005eefe008b nip 00003fff59770004 lr 00003fff876f7ce0 code 30001
[3269642.639571] reduce_test_cpu[27183]: unhandled signal 5 at 00003fff7f4f0000 nip 00003fff7f4f0000 lr 00003fffad377ce0 code 30001
[3269644.519379] reduce_test_cpu[27296]: unhandled signal 5 at 00003fff60340000 nip 00003fff60340000 lr 00003fff8e1c7ce0 code 30001
[3269644.778430] reduce_test_cpu[27378]: unhandled signal 5 at 00003fff4eb40000 nip 00003fff4eb40000 lr 00003fff7ca67ce0 code 30001
[3269645.284242] reduce_test_cpu[27473]: unhandled signal 5 at 00003fff74ec0000 nip 00003fff74ec0000 lr 00003fffa2d47ce0 code 30001
[3269645.538095] reduce_test_cpu[27555]: unhandled signal 5 at 00003fff84c80000 nip 00003fff84c80000 lr 00003fffb2b07ce0 code 30001
[3269647.309798] reduce_test_cpu[27649]: unhandled signal 5 at 00003fff82a30000 nip 00003fff82a30000 lr 00003fffb08b7ce0 code 30001
[

'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = r'''
Architecture:          ppc64le
Byte Order:            Little Endian
CPU(s):                16
On-line CPU(s) list:   0-15
Thread(s) per core:    1
Core(s) per socket:    16
Socket(s):             1
NUMA node(s):          1
Model:                 2.1 (pvr 004b 0201)
Model name:            POWER8E (raw), altivec supported
L1d cache:             64K
L1i cache:             32K
NUMA node0 CPU(s):     0-15

'''
		return returncode, output


class TestLinuxRHEL_7_3_ppc64le(unittest.TestCase):
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
		self.assertEqual(3, len(cpuinfo._get_cpu_info_from_lscpu()))
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
		self.assertEqual(32 * 1024, info['l1_instruction_cache_size'])
		self.assertEqual(64 * 1024, info['l1_data_cache_size'])
		self.assertEqual('POWER8E (raw), altivec supported', info['brand_raw'])

	def test_get_cpu_info_from_ibm_pa_features(self):
		info = cpuinfo._get_cpu_info_from_ibm_pa_features()
		self.assertEqual(
			['dss_2.02', 'dss_2.05', 'dss_2.06', 'fpu', 'lsd_in_dscr', 'ppr', 'slb', 'sso_2.06', 'ugr_in_dscr'],
			info['flags']
		)

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('POWER8E (raw), altivec supported', info['brand_raw'])
		self.assertEqual('3.4250 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.4250 GHz', info['hz_actual_friendly'])
		self.assertEqual((3425000000, 0), info['hz_advertised'])
		self.assertEqual((3425000000, 0), info['hz_actual'])

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('POWER8E (raw), altivec supported', info['brand_raw'])
		self.assertEqual('3.4250 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.4250 GHz', info['hz_actual_friendly'])
		self.assertEqual((3425000000, 0), info['hz_advertised'])
		self.assertEqual((3425000000, 0), info['hz_actual'])
		self.assertEqual('PPC_64', info['arch'])
		self.assertEqual(32 * 1024, info['l1_instruction_cache_size'])
		self.assertEqual(64 * 1024, info['l1_data_cache_size'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(16, info['count'])
		self.assertEqual('ppc64le', info['arch_string_raw'])
		self.assertEqual(
			['dss_2.02', 'dss_2.05', 'dss_2.06', 'fpu', 'lsd_in_dscr', 'ppr', 'slb', 'sso_2.06', 'ugr_in_dscr'],
			info['flags']
		)
