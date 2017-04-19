

import platform

class EmptyDataSource(object):
	@staticmethod
	def has_proc_cpuinfo():
		return False

	@staticmethod
	def has_lscpu():
		return False

	@staticmethod
	def has_ibm_pa_features():
		return False

	@staticmethod
	def has_dmesg():
		return False

	@staticmethod
	def has_var_run_dmesg_boot():
		return False

	@staticmethod
	def has_cpufreq_info():
		return False

	@staticmethod
	def has_sestatus():
		return False

	@staticmethod
	def has_sysctl():
		return False

	@staticmethod
	def has_isainfo():
		return False

	@staticmethod
	def has_kstat():
		return False

	@staticmethod
	def has_sysinfo():
		return False

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


def monkey_patch_data_source(cpuinfo, NewDataSource):
	# Replace all methods with ones that return false
	_actual_monkey_patch_data_source(cpuinfo, EmptyDataSource)

	# Copy any methods that are the same over
	_actual_monkey_patch_data_source(cpuinfo, NewDataSource)

def _actual_monkey_patch_data_source(cpuinfo, NewDataSource):
	if hasattr(NewDataSource, 'bits'):
		cpuinfo.DataSource.bits = NewDataSource.bits
	if hasattr(NewDataSource, 'cpu_count'):
		cpuinfo.DataSource.cpu_count = NewDataSource.cpu_count
	if hasattr(NewDataSource, 'is_windows'):
		cpuinfo.DataSource.is_windows = NewDataSource.is_windows
	if hasattr(NewDataSource, 'raw_arch_string'):
		cpuinfo.DataSource.raw_arch_string = NewDataSource.raw_arch_string
	if hasattr(NewDataSource, 'can_cpuid'):
		cpuinfo.DataSource.can_cpuid = NewDataSource.can_cpuid

	if hasattr(NewDataSource, 'has_proc_cpuinfo'):
		cpuinfo.DataSource.has_proc_cpuinfo = staticmethod(NewDataSource.has_proc_cpuinfo)
	if hasattr(NewDataSource, 'has_dmesg'):
		cpuinfo.DataSource.has_dmesg = staticmethod(NewDataSource.has_dmesg)
	if hasattr(NewDataSource, 'has_var_run_dmesg_boot'):
		cpuinfo.DataSource.has_var_run_dmesg_boot = staticmethod(NewDataSource.has_var_run_dmesg_boot)
	if hasattr(NewDataSource, 'has_cpufreq_info'):
		cpuinfo.DataSource.has_cpufreq_info = staticmethod(NewDataSource.has_cpufreq_info)
	if hasattr(NewDataSource, 'has_sestatus'):
		cpuinfo.DataSource.has_sestatus = staticmethod(NewDataSource.has_sestatus)
	if hasattr(NewDataSource, 'has_sysctl'):
		cpuinfo.DataSource.has_sysctl = staticmethod(NewDataSource.has_sysctl)
	if hasattr(NewDataSource, 'has_isainfo'):
		cpuinfo.DataSource.has_isainfo = staticmethod(NewDataSource.has_isainfo)
	if hasattr(NewDataSource, 'has_kstat'):
		cpuinfo.DataSource.has_kstat = staticmethod(NewDataSource.has_kstat)
	if hasattr(NewDataSource, 'has_sysinfo'):
		cpuinfo.DataSource.has_sysinfo = staticmethod(NewDataSource.has_sysinfo)
	if hasattr(NewDataSource, 'has_ibm_pa_features'):
		cpuinfo.DataSource.has_ibm_pa_features = staticmethod(NewDataSource.has_ibm_pa_features)
	if hasattr(NewDataSource, 'has_lscpu'):
		cpuinfo.DataSource.has_lscpu = staticmethod(NewDataSource.has_lscpu)
	if hasattr(NewDataSource, 'cat_proc_cpuinfo'):
		cpuinfo.DataSource.cat_proc_cpuinfo = staticmethod(NewDataSource.cat_proc_cpuinfo)
	if hasattr(NewDataSource, 'cpufreq_info'):
		cpuinfo.DataSource.cpufreq_info = staticmethod(NewDataSource.cpufreq_info)
	if hasattr(NewDataSource, 'sestatus_allow_execheap'):
		cpuinfo.DataSource.sestatus_allow_execheap = staticmethod(NewDataSource.sestatus_allow_execheap)
	if hasattr(NewDataSource, 'sestatus_allow_execmem'):
		cpuinfo.DataSource.sestatus_allow_execmem = staticmethod(NewDataSource.sestatus_allow_execmem)
	if hasattr(NewDataSource, 'dmesg_a'):
		cpuinfo.DataSource.dmesg_a = staticmethod(NewDataSource.dmesg_a)
	if hasattr(NewDataSource, 'cat_var_run_dmesg_boot'):
		cpuinfo.DataSource.cat_var_run_dmesg_boot = staticmethod(NewDataSource.cat_var_run_dmesg_boot)
	if hasattr(NewDataSource, 'sysctl_machdep_cpu_hw_cpufrequency'):
		cpuinfo.DataSource.sysctl_machdep_cpu_hw_cpufrequency = staticmethod(NewDataSource.sysctl_machdep_cpu_hw_cpufrequency)
	if hasattr(NewDataSource, 'isainfo_vb'):
		cpuinfo.DataSource.isainfo_vb = staticmethod(NewDataSource.isainfo_vb)
	if hasattr(NewDataSource, 'kstat_m_cpu_info'):
		cpuinfo.DataSource.kstat_m_cpu_info = staticmethod(NewDataSource.kstat_m_cpu_info)
	if hasattr(NewDataSource, 'lscpu'):
		cpuinfo.DataSource.lscpu = staticmethod(NewDataSource.lscpu)
	if hasattr(NewDataSource, 'ibm_pa_features'):
		cpuinfo.DataSource.ibm_pa_features = staticmethod(NewDataSource.ibm_pa_features)
	if hasattr(NewDataSource, 'sysinfo_cpu'):
		cpuinfo.DataSource.sysinfo_cpu = staticmethod(NewDataSource.sysinfo_cpu)
	if hasattr(NewDataSource, 'winreg_processor_brand'):
		cpuinfo.DataSource.winreg_processor_brand = staticmethod(NewDataSource.winreg_processor_brand)
	if hasattr(NewDataSource, 'winreg_vendor_id'):
		cpuinfo.DataSource.winreg_vendor_id = staticmethod(NewDataSource.winreg_vendor_id)
	if hasattr(NewDataSource, 'winreg_raw_arch_string'):
		cpuinfo.DataSource.winreg_raw_arch_string = staticmethod(NewDataSource.winreg_raw_arch_string)
	if hasattr(NewDataSource, 'winreg_hz_actual'):
		cpuinfo.DataSource.winreg_hz_actual = staticmethod(NewDataSource.winreg_hz_actual)
	if hasattr(NewDataSource, 'winreg_feature_bits'):
		cpuinfo.DataSource.winreg_feature_bits = staticmethod(NewDataSource.winreg_feature_bits)

def backup_data_source(cpuinfo):
	BackupDataSource = type('BackupDataSource', (object,), {})
	cpuinfo.BackupDataSource = BackupDataSource()
	cpuinfo.BackupDataSource.bits = cpuinfo.DataSource.bits
	cpuinfo.BackupDataSource.cpu_count = cpuinfo.DataSource.cpu_count
	cpuinfo.BackupDataSource.is_windows = cpuinfo.DataSource.is_windows
	cpuinfo.BackupDataSource.raw_arch_string = cpuinfo.DataSource.raw_arch_string
	cpuinfo.BackupDataSource.can_cpuid = cpuinfo.DataSource.can_cpuid

	cpuinfo.BackupDataSource.has_proc_cpuinfo = staticmethod(cpuinfo.DataSource.has_proc_cpuinfo)
	cpuinfo.BackupDataSource.has_dmesg = staticmethod(cpuinfo.DataSource.has_dmesg)
	cpuinfo.BackupDataSource.has_var_run_dmesg_boot = staticmethod(cpuinfo.DataSource.has_var_run_dmesg_boot)
	cpuinfo.BackupDataSource.has_cpufreq_info = staticmethod(cpuinfo.DataSource.has_cpufreq_info)
	cpuinfo.BackupDataSource.has_sestatus = staticmethod(cpuinfo.DataSource.has_sestatus)
	cpuinfo.BackupDataSource.has_sysctl = staticmethod(cpuinfo.DataSource.has_sysctl)
	cpuinfo.BackupDataSource.has_isainfo = staticmethod(cpuinfo.DataSource.has_isainfo)
	cpuinfo.BackupDataSource.has_kstat = staticmethod(cpuinfo.DataSource.has_kstat)
	cpuinfo.BackupDataSource.has_sysinfo = staticmethod(cpuinfo.DataSource.has_sysinfo)
	cpuinfo.BackupDataSource.has_lscpu = staticmethod(cpuinfo.DataSource.has_lscpu)
	cpuinfo.BackupDataSource.has_ibm_pa_features = staticmethod(cpuinfo.DataSource.has_ibm_pa_features)
	cpuinfo.BackupDataSource.cat_proc_cpuinfo = staticmethod(cpuinfo.DataSource.cat_proc_cpuinfo)
	cpuinfo.BackupDataSource.cpufreq_info = staticmethod(cpuinfo.DataSource.cpufreq_info)
	cpuinfo.BackupDataSource.sestatus_allow_execheap = staticmethod(cpuinfo.DataSource.sestatus_allow_execheap)
	cpuinfo.BackupDataSource.sestatus_allow_execmem = staticmethod(cpuinfo.DataSource.sestatus_allow_execmem)
	cpuinfo.BackupDataSource.dmesg_a = staticmethod(cpuinfo.DataSource.dmesg_a)
	cpuinfo.BackupDataSource.cat_var_run_dmesg_boot = staticmethod(cpuinfo.DataSource.cat_var_run_dmesg_boot)
	cpuinfo.BackupDataSource.sysctl_machdep_cpu_hw_cpufrequency = staticmethod(cpuinfo.DataSource.sysctl_machdep_cpu_hw_cpufrequency)
	cpuinfo.BackupDataSource.isainfo_vb = staticmethod(cpuinfo.DataSource.isainfo_vb)
	cpuinfo.BackupDataSource.kstat_m_cpu_info = staticmethod(cpuinfo.DataSource.kstat_m_cpu_info)
	cpuinfo.BackupDataSource.lscpu = staticmethod(cpuinfo.DataSource.lscpu)
	cpuinfo.BackupDataSource.ibm_pa_features = staticmethod(cpuinfo.DataSource.ibm_pa_features)
	cpuinfo.BackupDataSource.sysinfo_cpu = staticmethod(cpuinfo.DataSource.sysinfo_cpu)
	cpuinfo.BackupDataSource.winreg_processor_brand = staticmethod(cpuinfo.DataSource.winreg_processor_brand)
	cpuinfo.BackupDataSource.winreg_vendor_id = staticmethod(cpuinfo.DataSource.winreg_vendor_id)
	cpuinfo.BackupDataSource.winreg_raw_arch_string = staticmethod(cpuinfo.DataSource.winreg_raw_arch_string)
	cpuinfo.BackupDataSource.winreg_hz_actual = staticmethod(cpuinfo.DataSource.winreg_hz_actual)
	cpuinfo.BackupDataSource.winreg_feature_bits = staticmethod(cpuinfo.DataSource.winreg_feature_bits)

def restore_data_source(cpuinfo):
	cpuinfo.DataSource.bits = cpuinfo.BackupDataSource.bits
	cpuinfo.DataSource.cpu_count = cpuinfo.BackupDataSource.cpu_count
	cpuinfo.DataSource.is_windows = cpuinfo.BackupDataSource.is_windows
	cpuinfo.DataSource.raw_arch_string = cpuinfo.BackupDataSource.raw_arch_string
	cpuinfo.DataSource.can_cpuid = cpuinfo.BackupDataSource.can_cpuid

	cpuinfo.DataSource.has_proc_cpuinfo = cpuinfo.BackupDataSource.has_proc_cpuinfo
	cpuinfo.DataSource.has_dmesg = cpuinfo.BackupDataSource.has_dmesg
	cpuinfo.DataSource.has_var_run_dmesg_boot = cpuinfo.BackupDataSource.has_var_run_dmesg_boot
	cpuinfo.DataSource.has_cpufreq_info = cpuinfo.BackupDataSource.has_cpufreq_info
	cpuinfo.DataSource.has_sestatus = cpuinfo.BackupDataSource.has_sestatus
	cpuinfo.DataSource.has_sysctl = cpuinfo.BackupDataSource.has_sysctl
	cpuinfo.DataSource.has_isainfo = cpuinfo.BackupDataSource.has_isainfo
	cpuinfo.DataSource.has_kstat = cpuinfo.BackupDataSource.has_kstat
	cpuinfo.DataSource.has_sysinfo = cpuinfo.BackupDataSource.has_sysinfo
	cpuinfo.DataSource.has_lscpu = cpuinfo.BackupDataSource.has_lscpu
	cpuinfo.DataSource.has_ibm_pa_features = cpuinfo.BackupDataSource.has_ibm_pa_features
	cpuinfo.DataSource.cat_proc_cpuinfo = cpuinfo.BackupDataSource.cat_proc_cpuinfo
	cpuinfo.DataSource.cpufreq_info = cpuinfo.BackupDataSource.cpufreq_info
	cpuinfo.DataSource.sestatus_allow_execheap = cpuinfo.BackupDataSource.sestatus_allow_execheap
	cpuinfo.DataSource.sestatus_allow_execmem = cpuinfo.BackupDataSource.sestatus_allow_execmem
	cpuinfo.DataSource.dmesg_a = cpuinfo.BackupDataSource.dmesg_a
	cpuinfo.DataSource.cat_var_run_dmesg_boot = cpuinfo.BackupDataSource.cat_var_run_dmesg_boot
	cpuinfo.DataSource.sysctl_machdep_cpu_hw_cpufrequency = cpuinfo.BackupDataSource.sysctl_machdep_cpu_hw_cpufrequency
	cpuinfo.DataSource.isainfo_vb = cpuinfo.BackupDataSource.isainfo_vb
	cpuinfo.DataSource.kstat_m_cpu_info = cpuinfo.BackupDataSource.kstat_m_cpu_info
	cpuinfo.DataSource.lscpu = cpuinfo.BackupDataSource.lscpu
	cpuinfo.DataSource.ibm_pa_features = cpuinfo.BackupDataSource.ibm_pa_features
	cpuinfo.DataSource.sysinfo_cpu = cpuinfo.BackupDataSource.sysinfo_cpu
	cpuinfo.DataSource.winreg_processor_brand = cpuinfo.BackupDataSource.winreg_processor_brand
	cpuinfo.DataSource.winreg_vendor_id = cpuinfo.BackupDataSource.winreg_vendor_id
	cpuinfo.DataSource.winreg_raw_arch_string = cpuinfo.BackupDataSource.winreg_raw_arch_string
	cpuinfo.DataSource.winreg_hz_actual = cpuinfo.BackupDataSource.winreg_hz_actual
	cpuinfo.DataSource.winreg_feature_bits = cpuinfo.BackupDataSource.winreg_feature_bits
