

import platform


def get_os_type():
	os_type = 'Unknown'

	# Figure out the general OS type
	uname = platform.system().strip().strip('"').strip("'").strip().lower()
	if 'beos' in uname or 'haiku' in uname:
		os_type = 'BeOS'
	elif 'bsd' in uname or 'gnu/kfreebsd' in uname:
		os_type = 'BSD'
	elif 'cygwin' in uname:
		os_type = 'Cygwin'
	elif 'darwin' in uname:
		os_type = 'MacOS'
	elif 'linux' in uname:
		os_type = 'Linux'
	elif 'solaris' in uname or 'sunos' in uname:
		os_type = 'Solaris'
	elif 'windows' in uname:
		os_type = 'Windows'

	return os_type


def monkey_patch_data_source(cpuinfo, DataSource):
	if hasattr(DataSource, 'bits'):
		cpuinfo.DataSource.bits = DataSource.bits
	if hasattr(DataSource, 'cpu_count'):
		cpuinfo.DataSource.cpu_count = DataSource.cpu_count
	if hasattr(DataSource, 'is_windows'):
		cpuinfo.DataSource.is_windows = DataSource.is_windows
	if hasattr(DataSource, 'raw_arch_string'):
		cpuinfo.DataSource.raw_arch_string = DataSource.raw_arch_string

	if hasattr(DataSource, 'has_proc_cpuinfo'):
		cpuinfo.DataSource.has_proc_cpuinfo = staticmethod(DataSource.has_proc_cpuinfo)
	if hasattr(DataSource, 'has_dmesg'):
		cpuinfo.DataSource.has_dmesg = staticmethod(DataSource.has_dmesg)
	if hasattr(DataSource, 'has_cpufreq_info'):
		cpuinfo.DataSource.has_cpufreq_info = staticmethod(DataSource.has_cpufreq_info)
	if hasattr(DataSource, 'has_sestatus'):
		cpuinfo.DataSource.has_sestatus = staticmethod(DataSource.has_sestatus)
	if hasattr(DataSource, 'has_sysctl'):
		cpuinfo.DataSource.has_sysctl = staticmethod(DataSource.has_sysctl)
	if hasattr(DataSource, 'has_isainfo'):
		cpuinfo.DataSource.has_isainfo = staticmethod(DataSource.has_isainfo)
	if hasattr(DataSource, 'has_kstat'):
		cpuinfo.DataSource.has_kstat = staticmethod(DataSource.has_kstat)
	if hasattr(DataSource, 'has_sysinfo'):
		cpuinfo.DataSource.has_sysinfo = staticmethod(DataSource.has_sysinfo)
	if hasattr(DataSource, 'has_lscpu'):
		cpuinfo.DataSource.has_lscpu = staticmethod(DataSource.has_lscpu)
	if hasattr(DataSource, 'cat_proc_cpuinfo'):
		cpuinfo.DataSource.cat_proc_cpuinfo = staticmethod(DataSource.cat_proc_cpuinfo)
	if hasattr(DataSource, 'cpufreq_info'):
		cpuinfo.DataSource.cpufreq_info = staticmethod(DataSource.cpufreq_info)
	if hasattr(DataSource, 'sestatus_allow_execheap'):
		cpuinfo.DataSource.sestatus_allow_execheap = staticmethod(DataSource.sestatus_allow_execheap)
	if hasattr(DataSource, 'sestatus_allow_execmem'):
		cpuinfo.DataSource.sestatus_allow_execmem = staticmethod(DataSource.sestatus_allow_execmem)
	if hasattr(DataSource, 'dmesg_a'):
		cpuinfo.DataSource.dmesg_a = staticmethod(DataSource.dmesg_a)
	if hasattr(DataSource, 'sysctl_machdep_cpu_hw_cpufrequency'):
		cpuinfo.DataSource.sysctl_machdep_cpu_hw_cpufrequency = staticmethod(DataSource.sysctl_machdep_cpu_hw_cpufrequency)
	if hasattr(DataSource, 'isainfo_vb'):
		cpuinfo.DataSource.isainfo_vb = staticmethod(DataSource.isainfo_vb)
	if hasattr(DataSource, 'kstat_m_cpu_info'):
		cpuinfo.DataSource.kstat_m_cpu_info = staticmethod(DataSource.kstat_m_cpu_info)
	if hasattr(DataSource, 'lscpu'):
		cpuinfo.DataSource.lscpu = staticmethod(DataSource.lscpu)
	if hasattr(DataSource, 'sysinfo_cpu'):
		cpuinfo.DataSource.sysinfo_cpu = staticmethod(DataSource.sysinfo_cpu)
	if hasattr(DataSource, 'winreg_processor_brand'):
		cpuinfo.DataSource.winreg_processor_brand = staticmethod(DataSource.winreg_processor_brand)
	if hasattr(DataSource, 'winreg_vendor_id'):
		cpuinfo.DataSource.winreg_vendor_id = staticmethod(DataSource.winreg_vendor_id)
	if hasattr(DataSource, 'winreg_raw_arch_string'):
		cpuinfo.DataSource.winreg_raw_arch_string = staticmethod(DataSource.winreg_raw_arch_string)
	if hasattr(DataSource, 'winreg_hz_actual'):
		cpuinfo.DataSource.winreg_hz_actual = staticmethod(DataSource.winreg_hz_actual)
	if hasattr(DataSource, 'winreg_feature_bits'):
		cpuinfo.DataSource.winreg_feature_bits = staticmethod(DataSource.winreg_feature_bits)
