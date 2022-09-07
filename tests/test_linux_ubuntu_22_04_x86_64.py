

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 16
	is_windows = False
	arch_string_raw = 'x86_64'
	uname_string_raw = 'x86_64'
	can_cpuid = False

	@staticmethod
	def has_proc_cpuinfo():
		return True

	@staticmethod
	def has_lscpu():
		return True

	@staticmethod
	def cat_proc_cpuinfo():
		returncode = 0
		output = r'''
processor	: 0
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 0
cpu cores	: 8
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 1
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 0
cpu cores	: 8
apicid		: 1
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 2
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 1
cpu cores	: 8
apicid		: 2
initial apicid	: 2
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 3
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 1
cpu cores	: 8
apicid		: 3
initial apicid	: 3
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 4
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 3200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 2
cpu cores	: 8
apicid		: 4
initial apicid	: 4
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 5
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 2
cpu cores	: 8
apicid		: 5
initial apicid	: 5
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 6
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 3
cpu cores	: 8
apicid		: 6
initial apicid	: 6
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 7
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 3
cpu cores	: 8
apicid		: 7
initial apicid	: 7
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 8
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 4
cpu cores	: 8
apicid		: 8
initial apicid	: 8
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 9
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 3700.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 4
cpu cores	: 8
apicid		: 9
initial apicid	: 9
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 10
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 1980.565
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 5
cpu cores	: 8
apicid		: 10
initial apicid	: 10
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 11
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 5
cpu cores	: 8
apicid		: 11
initial apicid	: 11
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 12
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 6
cpu cores	: 8
apicid		: 12
initial apicid	: 12
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 13
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 6
cpu cores	: 8
apicid		: 13
initial apicid	: 13
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 14
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 7
cpu cores	: 8
apicid		: 14
initial apicid	: 14
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 15
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 8
model name	: AMD Ryzen 7 2700X Eight-Core Processor
stepping	: 2
microcode	: 0x800820d
cpu MHz		: 2200.000
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 7
cpu cores	: 8
apicid		: 15
initial apicid	: 15
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass retbleed
bogomips	: 7386.22
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]


'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = r'''
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   43 bits physical, 48 bits virtual
Byte Order:                      Little Endian
CPU(s):                          16
On-line CPU(s) list:             0-15
Vendor ID:                       AuthenticAMD
Model name:                      AMD Ryzen 7 2700X Eight-Core Processor
CPU family:                      23
Model:                           8
Thread(s) per core:              2
Core(s) per socket:              8
Socket(s):                       1
Stepping:                        2
Frequency boost:                 enabled
CPU max MHz:                     3700.0000
CPU min MHz:                     2200.0000
BogoMIPS:                        7386.22
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sme sev sev_es
Virtualization:                  AMD-V
L1d cache:                       256 KiB (8 instances)
L1i cache:                       512 KiB (8 instances)
L2 cache:                        4 MiB (8 instances)
L3 cache:                        16 MiB (2 instances)
NUMA node(s):                    1
NUMA node0 CPU(s):               0-15
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Mitigation; untrained return thunk; SMT vulnerable
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:        Mitigation; Retpolines, IBPB conditional, STIBP disabled, RSB filling
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected


'''
		return returncode, output

class TestLinuxUbuntu_22_04_X86_64(unittest.TestCase):
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
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_dmesg()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cat_var_run_dmesg_boot()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_ibm_pa_features()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_sysinfo()))
		self.assertEqual(0, len(cpuinfo._get_cpu_info_from_cpuid()))
		self.assertEqual(21, len(cpuinfo._get_cpu_info_internal()))

	def test_get_cpu_info_from_lscpu(self):
		info = cpuinfo._get_cpu_info_from_lscpu()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('3.7000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.7000 GHz', info['hz_actual_friendly'])
		self.assertEqual((3700000000, 0), info['hz_advertised'])
		self.assertEqual((3700000000, 0), info['hz_actual'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])

		self.assertEqual(512 * 1024, info['l1_instruction_cache_size'])
		self.assertEqual(256 * 1024, info['l1_data_cache_size'])
		self.assertEqual(4 * 1024 * 1024, info['l2_cache_size'])
		self.assertEqual(16 * 1024 * 1024, info['l3_cache_size'])
		self.assertEqual(
			['3dnowprefetch', 'abm', 'adx', 'aes', 'aperfmperf', 'apic', 'arat',
            'avic', 'avx', 'avx2', 'bmi1', 'bmi2', 'bpext', 'clflush',
            'clflushopt', 'clzero', 'cmov', 'cmp_legacy', 'constant_tsc', 'cpb',
            'cpuid', 'cr8_legacy', 'cx16', 'cx8', 'de', 'decodeassists',
            'extapic', 'extd_apicid', 'f16c', 'flushbyasid', 'fma', 'fpu',
            'fsgsbase', 'fxsr', 'fxsr_opt', 'ht', 'hw_pstate', 'ibpb', 'irperf',
            'lahf_lm', 'lbrv', 'lm', 'mca', 'mce', 'misalignsse', 'mmx',
            'mmxext', 'monitor', 'movbe', 'msr', 'mtrr', 'mwaitx', 'nonstop_tsc',
            'nopl', 'npt', 'nrip_save', 'nx', 'osvw', 'overflow_recov', 'pae',
            'pat', 'pausefilter', 'pclmulqdq', 'pdpe1gb', 'perfctr_core',
            'perfctr_llc', 'perfctr_nb', 'pfthreshold', 'pge', 'pni', 'popcnt',
            'pse', 'pse36', 'rapl', 'rdrand', 'rdseed', 'rdtscp', 'rep_good',
            'sep', 'sev', 'sev_es', 'sha_ni', 'skinit', 'smap', 'smca', 'sme',
            'smep', 'ssbd', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'sse4a', 'ssse3',
            'succor', 'svm', 'svm_lock', 'syscall', 'tce', 'topoext', 'tsc',
            'tsc_scale', 'v_vmsave_vmload', 'vgif', 'vmcb_clean', 'vme',
            'vmmcall', 'wdt', 'xgetbv1', 'xsave', 'xsavec', 'xsaveerptr',
            'xsaveopt', 'xsaves']
			,
			info['flags']
		)

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('2.2000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.2000 GHz', info['hz_actual_friendly'])
		self.assertEqual((2200000000, 0), info['hz_advertised'])
		self.assertEqual((2200000000, 0), info['hz_actual'])

		self.assertEqual(512 * 1024, info['l3_cache_size'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])
		self.assertEqual(
			['3dnowprefetch', 'abm', 'adx', 'aes', 'aperfmperf', 'apic', 'arat',
            'avic', 'avx', 'avx2', 'bmi1', 'bmi2', 'bpext', 'clflush',
            'clflushopt', 'clzero', 'cmov', 'cmp_legacy', 'constant_tsc', 'cpb',
            'cpuid', 'cr8_legacy', 'cx16', 'cx8', 'de', 'decodeassists',
            'extapic', 'extd_apicid', 'f16c', 'flushbyasid', 'fma', 'fpu',
            'fsgsbase', 'fxsr', 'fxsr_opt', 'ht', 'hw_pstate', 'ibpb', 'irperf',
            'lahf_lm', 'lbrv', 'lm', 'mca', 'mce', 'misalignsse', 'mmx',
            'mmxext', 'monitor', 'movbe', 'msr', 'mtrr', 'mwaitx', 'nonstop_tsc',
            'nopl', 'npt', 'nrip_save', 'nx', 'osvw', 'overflow_recov', 'pae',
            'pat', 'pausefilter', 'pclmulqdq', 'pdpe1gb', 'perfctr_core',
            'perfctr_llc', 'perfctr_nb', 'pfthreshold', 'pge', 'pni', 'popcnt',
            'pse', 'pse36', 'rapl', 'rdrand', 'rdseed', 'rdtscp', 'rep_good',
            'sep', 'sev', 'sev_es', 'sha_ni', 'skinit', 'smap', 'smca', 'sme',
            'smep', 'ssbd', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'sse4a', 'ssse3',
            'succor', 'svm', 'svm_lock', 'syscall', 'tce', 'topoext', 'tsc',
            'tsc_scale', 'v_vmsave_vmload', 'vgif', 'vmcb_clean', 'vme',
            'vmmcall', 'wdt', 'xgetbv1', 'xsave', 'xsavec', 'xsaveerptr',
            'xsaveopt', 'xsaves']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('2.2000 GHz', info['hz_advertised_friendly'])
		self.assertEqual('2.2000 GHz', info['hz_actual_friendly'])
		self.assertEqual((2200000000, 0), info['hz_advertised'])
		self.assertEqual((2200000000, 0), info['hz_actual'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(16, info['count'])

		self.assertEqual('x86_64', info['arch_string_raw'])

		self.assertEqual(512 * 1024, info['l1_instruction_cache_size'])
		self.assertEqual(256 * 1024, info['l1_data_cache_size'])
		self.assertEqual(4 * 1024 * 1024, info['l2_cache_size'])
		self.assertEqual(512 * 1024, info['l3_cache_size'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])
		self.assertEqual(
			['3dnowprefetch', 'abm', 'adx', 'aes', 'aperfmperf', 'apic', 'arat',
            'avic', 'avx', 'avx2', 'bmi1', 'bmi2', 'bpext', 'clflush',
            'clflushopt', 'clzero', 'cmov', 'cmp_legacy', 'constant_tsc', 'cpb',
            'cpuid', 'cr8_legacy', 'cx16', 'cx8', 'de', 'decodeassists',
            'extapic', 'extd_apicid', 'f16c', 'flushbyasid', 'fma', 'fpu',
            'fsgsbase', 'fxsr', 'fxsr_opt', 'ht', 'hw_pstate', 'ibpb', 'irperf',
            'lahf_lm', 'lbrv', 'lm', 'mca', 'mce', 'misalignsse', 'mmx',
            'mmxext', 'monitor', 'movbe', 'msr', 'mtrr', 'mwaitx', 'nonstop_tsc',
            'nopl', 'npt', 'nrip_save', 'nx', 'osvw', 'overflow_recov', 'pae',
            'pat', 'pausefilter', 'pclmulqdq', 'pdpe1gb', 'perfctr_core',
            'perfctr_llc', 'perfctr_nb', 'pfthreshold', 'pge', 'pni', 'popcnt',
            'pse', 'pse36', 'rapl', 'rdrand', 'rdseed', 'rdtscp', 'rep_good',
            'sep', 'sev', 'sev_es', 'sha_ni', 'skinit', 'smap', 'smca', 'sme',
            'smep', 'ssbd', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'sse4a', 'ssse3',
            'succor', 'svm', 'svm_lock', 'syscall', 'tce', 'topoext', 'tsc',
            'tsc_scale', 'v_vmsave_vmload', 'vgif', 'vmcb_clean', 'vme',
            'vmmcall', 'wdt', 'xgetbv1', 'xsave', 'xsavec', 'xsaveerptr',
            'xsaveopt', 'xsaves']
			,
			info['flags']
		)
