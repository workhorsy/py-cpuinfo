

import unittest
from cpuinfo import *
import helpers


class MockDataSource(object):
	bits = '64bit'
	cpu_count = 8
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
	def has_sestatus():
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
microcode	: 0x6000626
cpu MHz		: 3693.060
cache size	: 512 KB
physical id	: 0
siblings	: 8
core id		: 0
cpu cores	: 8
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid tsc_known_freq pni pclmulqdq ssse3 cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx rdrand hypervisor lahf_lm cmp_legacy cr8_legacy abm sse4a misalignsse 3dnowprefetch cpb ssbd vmmcall fsgsbase avx2 rdseed clflushopt arat
bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
bogomips	: 7386.12
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 48 bits physical, 48 bits virtual
power management:


'''
		return returncode, output

	@staticmethod
	def lscpu():
		returncode = 0
		output = r'''
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              8
On-line CPU(s) list: 0-7
Thread(s) per core:  1
Core(s) per socket:  8
Socket(s):           1
NUMA node(s):        1
Vendor ID:           AuthenticAMD
CPU family:          23
Model:               8
Model name:          AMD Ryzen 7 2700X Eight-Core Processor
Stepping:            2
CPU MHz:             3693.060
BogoMIPS:            7386.12
Hypervisor vendor:   KVM
Virtualization type: full
L1d cache:           32K
L1i cache:           64K
L2 cache:            512K
L3 cache:            16384K
NUMA node0 CPU(s):   0-7
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid tsc_known_freq pni pclmulqdq ssse3 cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx rdrand hypervisor lahf_lm cmp_legacy cr8_legacy abm sse4a misalignsse 3dnowprefetch cpb ssbd vmmcall fsgsbase avx2 rdseed clflushopt arat


'''
		return returncode, output

	@staticmethod
	def sestatus_b():
		returncode = 0
		output = r'''
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      31

Policy booleans:
abrt_anon_write                             off
abrt_handle_event                           off
abrt_upload_watch_anon_write                on
antivirus_can_scan_system                   off
antivirus_use_jit                           off
auditadm_exec_content                       on
authlogin_nsswitch_use_ldap                 off
authlogin_radius                            off
authlogin_yubikey                           off
awstats_purge_apache_log_files              off
boinc_execmem                               on
cdrecord_read_content                       off
cluster_can_network_connect                 off
cluster_manage_all_files                    off
cluster_use_execmem                         off
cobbler_anon_write                          off
cobbler_can_network_connect                 off
cobbler_use_cifs                            off
cobbler_use_nfs                             off
collectd_tcp_network_connect                off
colord_use_nfs                              off
condor_tcp_network_connect                  off
conman_can_network                          off
conman_use_nfs                              off
cron_can_relabel                            off
cron_system_cronjob_use_shares              off
cron_userdomain_transition                  on
cups_execmem                                off
cvs_read_shadow                             off
daemons_dump_core                           off
daemons_enable_cluster_mode                 off
daemons_use_tcp_wrapper                     off
daemons_use_tty                             off
dbadm_exec_content                          on
dbadm_manage_user_files                     off
dbadm_read_user_files                       off
deny_execmem                                off
deny_ptrace                                 off
dhcpc_exec_iptables                         off
dhcpd_use_ldap                              off
domain_can_mmap_files                       off
domain_can_write_kmsg                       off
domain_fd_use                               on
domain_kernel_load_modules                  off
entropyd_use_audio                          on
exim_can_connect_db                         off
exim_manage_user_files                      off
exim_read_user_files                        off
fcron_crond                                 off
fenced_can_network_connect                  off
fenced_can_ssh                              off
fips_mode                                   on
ftpd_anon_write                             off
ftpd_connect_all_unreserved                 off
ftpd_connect_db                             off
ftpd_full_access                            off
ftpd_use_cifs                               off
ftpd_use_fusefs                             off
ftpd_use_nfs                                off
ftpd_use_passive_mode                       off
git_cgi_enable_homedirs                     off
git_cgi_use_cifs                            off
git_cgi_use_nfs                             off
git_session_bind_all_unreserved_ports       off
git_session_users                           off
git_system_enable_homedirs                  off
git_system_use_cifs                         off
git_system_use_nfs                          off
gitosis_can_sendmail                        off
glance_api_can_network                      off
glance_use_execmem                          off
glance_use_fusefs                           off
global_ssp                                  off
gluster_anon_write                          off
gluster_export_all_ro                       off
gluster_export_all_rw                       on
gluster_use_execmem                         off
gpg_web_anon_write                          off
gssd_read_tmp                               on
guest_exec_content                          on
haproxy_connect_any                         off
httpd_anon_write                            off
httpd_builtin_scripting                     on
httpd_can_check_spam                        off
httpd_can_connect_ftp                       off
httpd_can_connect_ldap                      off
httpd_can_connect_mythtv                    off
httpd_can_connect_zabbix                    off
httpd_can_network_connect                   off
httpd_can_network_connect_cobbler           off
httpd_can_network_connect_db                off
httpd_can_network_memcache                  off
httpd_can_network_relay                     off
httpd_can_sendmail                          off
httpd_dbus_avahi                            off
httpd_dbus_sssd                             off
httpd_dontaudit_search_dirs                 off
httpd_enable_cgi                            on
httpd_enable_ftp_server                     off
httpd_enable_homedirs                       off
httpd_execmem                               off
httpd_graceful_shutdown                     off
httpd_manage_ipa                            off
httpd_mod_auth_ntlm_winbind                 off
httpd_mod_auth_pam                          off
httpd_read_user_content                     off
httpd_run_ipa                               off
httpd_run_preupgrade                        off
httpd_run_stickshift                        off
httpd_serve_cobbler_files                   off
httpd_setrlimit                             off
httpd_ssi_exec                              off
httpd_sys_script_anon_write                 off
httpd_tmp_exec                              off
httpd_tty_comm                              off
httpd_unified                               off
httpd_use_cifs                              off
httpd_use_fusefs                            off
httpd_use_gpg                               off
httpd_use_nfs                               off
httpd_use_openstack                         off
httpd_use_sasl                              off
httpd_verify_dns                            off
icecast_use_any_tcp_ports                   off
irc_use_any_tcp_ports                       off
irssi_use_full_network                      off
kdumpgui_run_bootloader                     off
keepalived_connect_any                      off
kerberos_enabled                            on
ksmtuned_use_cifs                           off
ksmtuned_use_nfs                            off
logadm_exec_content                         on
logging_syslogd_can_sendmail                off
logging_syslogd_run_nagios_plugins          off
logging_syslogd_use_tty                     on
login_console_enabled                       on
logrotate_read_inside_containers            off
logrotate_use_nfs                           off
logwatch_can_network_connect_mail           off
lsmd_plugin_connect_any                     off
mailman_use_fusefs                          off
mcelog_client                               off
mcelog_exec_scripts                         on
mcelog_foreground                           off
mcelog_server                               off
minidlna_read_generic_user_content          off
mmap_low_allowed                            off
mock_enable_homedirs                        off
mount_anyfile                               on
mozilla_plugin_bind_unreserved_ports        off
mozilla_plugin_can_network_connect          on
mozilla_plugin_use_bluejeans                off
mozilla_plugin_use_gps                      off
mozilla_plugin_use_spice                    off
mozilla_read_content                        off
mpd_enable_homedirs                         off
mpd_use_cifs                                off
mpd_use_nfs                                 off
mplayer_execstack                           off
mysql_connect_any                           off
mysql_connect_http                          off
nagios_run_pnp4nagios                       off
nagios_run_sudo                             off
nagios_use_nfs                              off
named_tcp_bind_http_port                    off
named_write_master_zones                    off
neutron_can_network                         off
nfs_export_all_ro                           on
nfs_export_all_rw                           on
nfsd_anon_write                             off
nis_enabled                                 off
nscd_use_shm                                on
openshift_use_nfs                           off
openvpn_can_network_connect                 on
openvpn_enable_homedirs                     on
openvpn_run_unconfined                      off
pcp_bind_all_unreserved_ports               off
pcp_read_generic_logs                       off
pdns_can_network_connect_db                 off
piranha_lvs_can_network_connect             off
polipo_connect_all_unreserved               off
polipo_session_bind_all_unreserved_ports    off
polipo_session_users                        off
polipo_use_cifs                             off
polipo_use_nfs                              off
polyinstantiation_enabled                   off
postfix_local_write_mail_spool              on
postgresql_can_rsync                        off
postgresql_selinux_transmit_client_label    off
postgresql_selinux_unconfined_dbadm         on
postgresql_selinux_users_ddl                on
pppd_can_insmod                             off
pppd_for_user                               off
privoxy_connect_any                         on
prosody_bind_http_port                      off
puppetagent_manage_all_files                off
puppetmaster_use_db                         off
racoon_read_shadow                          off
radius_use_jit                              off
redis_enable_notify                         off
rpcd_use_fusefs                             off
rsync_anon_write                            off
rsync_client                                off
rsync_export_all_ro                         off
rsync_full_access                           off
samba_create_home_dirs                      off
samba_domain_controller                     off
samba_enable_home_dirs                      off
samba_export_all_ro                         off
samba_export_all_rw                         off
samba_load_libgfapi                         off
samba_portmapper                            off
samba_run_unconfined                        off
samba_share_fusefs                          off
samba_share_nfs                             off
sanlock_enable_home_dirs                    off
sanlock_use_fusefs                          off
sanlock_use_nfs                             off
sanlock_use_samba                           off
saslauthd_read_shadow                       off
secadm_exec_content                         on
secure_mode                                 off
secure_mode_insmod                          off
secure_mode_policyload                      off
selinuxuser_direct_dri_enabled              on
selinuxuser_execheap                        off
selinuxuser_execmod                         on
selinuxuser_execstack                       on
selinuxuser_mysql_connect_enabled           off
selinuxuser_ping                            on
selinuxuser_postgresql_connect_enabled      off
selinuxuser_rw_noexattrfile                 on
selinuxuser_share_music                     off
selinuxuser_tcp_server                      off
selinuxuser_udp_server                      off
selinuxuser_use_ssh_chroot                  off
sge_domain_can_network_connect              off
sge_use_nfs                                 off
smartmon_3ware                              off
smbd_anon_write                             off
spamassassin_can_network                    off
spamd_enable_home_dirs                      on
spamd_update_can_network                    off
squid_connect_any                           on
squid_use_tproxy                            off
ssh_chroot_rw_homedirs                      off
ssh_keysign                                 off
ssh_sysadm_login                            off
ssh_use_tcpd                                off
sslh_can_bind_any_port                      off
sslh_can_connect_any_port                   off
staff_exec_content                          on
staff_use_svirt                             off
swift_can_network                           off
sysadm_exec_content                         on
telepathy_connect_all_ports                 off
telepathy_tcp_connect_generic_network_ports on
tftp_anon_write                             off
tftp_home_dir                               off
tmpreaper_use_cifs                          off
tmpreaper_use_nfs                           off
tmpreaper_use_samba                         off
tomcat_can_network_connect_db               off
tomcat_read_rpm_db                          off
tomcat_use_execmem                          off
tor_bind_all_unreserved_ports               off
tor_can_network_relay                       off
tor_can_onion_services                      off
unconfined_chrome_sandbox_transition        on
unconfined_login                            on
unconfined_mozilla_plugin_transition        on
unprivuser_use_svirt                        off
use_ecryptfs_home_dirs                      off
use_fusefs_home_dirs                        off
use_lpd_server                              off
use_nfs_home_dirs                           off
use_samba_home_dirs                         off
use_virtualbox                              off
user_exec_content                           on
varnishd_connect_any                        off
virt_read_qemu_ga_data                      off
virt_rw_qemu_ga_data                        off
virt_sandbox_share_apache_content           off
virt_sandbox_use_all_caps                   on
virt_sandbox_use_audit                      on
virt_sandbox_use_fusefs                     off
virt_sandbox_use_mknod                      off
virt_sandbox_use_netlink                    off
virt_sandbox_use_sys_admin                  off
virt_transition_userdomain                  off
virt_use_comm                               off
virt_use_execmem                            off
virt_use_fusefs                             off
virt_use_glusterd                           off
virt_use_nfs                                off
virt_use_pcscd                              off
virt_use_rawip                              off
virt_use_samba                              off
virt_use_sanlock                            off
virt_use_usb                                on
virt_use_xserver                            off
webadm_manage_user_files                    off
webadm_read_user_files                      off
wine_mmap_zero_ignore                       off
xdm_bind_vnc_tcp_port                       off
xdm_exec_bootloader                         off
xdm_sysadm_login                            off
xdm_write_home                              off
xen_use_nfs                                 off
xend_run_blktap                             on
xend_run_qemu                               on
xguest_connect_network                      on
xguest_exec_content                         on
xguest_mount_media                          on
xguest_use_bluetooth                        on
xserver_clients_write_xshm                  off
xserver_execmem                             off
xserver_object_manager                      off
zabbix_can_network                          off
zabbix_run_sudo                             off
zarafa_setrlimit                            off
zebra_write_config                          off
zoneminder_anon_write                       off
zoneminder_run_sudo off
'''
		return returncode, output


class Test_Linux_Fedora_29_X86_64_Ryzen_7(unittest.TestCase):
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
		self.assertEqual('3.6931 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6931 GHz', info['hz_actual_friendly'])
		self.assertEqual((3693060000, 0), info['hz_advertised'])
		self.assertEqual((3693060000, 0), info['hz_actual'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])

		self.assertEqual(64 * 1024, info['l1_instruction_cache_size'])
		self.assertEqual(32 * 1024, info['l1_data_cache_size'])
		self.assertEqual(512 * 1024, info['l2_cache_size'])
		self.assertEqual(16384 * 1024, info['l3_cache_size'])

		self.assertEqual(
			['3dnowprefetch', 'abm', 'aes', 'apic', 'arat', 'avx', 'avx2',
			'clflush', 'clflushopt', 'cmov', 'cmp_legacy', 'constant_tsc',
			'cpb', 'cpuid', 'cr8_legacy', 'cx16', 'cx8', 'de', 'extd_apicid',
			'fpu', 'fsgsbase', 'fxsr', 'fxsr_opt', 'ht', 'hypervisor',
			'lahf_lm', 'lm', 'mca', 'mce', 'misalignsse', 'mmx', 'mmxext',
			'movbe', 'msr', 'mtrr', 'nonstop_tsc', 'nopl', 'nx', 'pae', 'pat',
			'pclmulqdq', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'rdrand',
			'rdseed', 'rdtscp', 'rep_good', 'sep', 'ssbd', 'sse', 'sse2',
			'sse4_1', 'sse4_2', 'sse4a', 'ssse3', 'syscall', 'tsc',
			'tsc_known_freq', 'vme', 'vmmcall', 'x2apic', 'xsave']
			,
			info['flags']
		)

	def test_get_cpu_info_from_proc_cpuinfo(self):
		info = cpuinfo._get_cpu_info_from_proc_cpuinfo()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('3.6931 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6931 GHz', info['hz_actual_friendly'])
		self.assertEqual((3693060000, 0), info['hz_advertised'])
		self.assertEqual((3693060000, 0), info['hz_actual'])

		# FIXME: This is l2 cache size not l3 cache size
		self.assertEqual(512 * 1024, info['l3_cache_size'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])
		self.assertEqual(
			['3dnowprefetch', 'abm', 'aes', 'apic', 'arat', 'avx', 'avx2',
			'clflush', 'clflushopt', 'cmov', 'cmp_legacy', 'constant_tsc',
			'cpb', 'cpuid', 'cr8_legacy', 'cx16', 'cx8', 'de', 'extd_apicid',
			'fpu', 'fsgsbase', 'fxsr', 'fxsr_opt', 'ht', 'hypervisor',
			'lahf_lm', 'lm', 'mca', 'mce', 'misalignsse', 'mmx', 'mmxext',
			'movbe', 'msr', 'mtrr', 'nonstop_tsc', 'nopl', 'nx', 'pae',
			'pat', 'pclmulqdq', 'pge', 'pni', 'popcnt', 'pse', 'pse36',
			'rdrand', 'rdseed', 'rdtscp', 'rep_good', 'sep', 'ssbd', 'sse',
			'sse2', 'sse4_1', 'sse4_2', 'sse4a', 'ssse3', 'syscall', 'tsc',
			'tsc_known_freq', 'vme', 'vmmcall', 'x2apic', 'xsave']
			,
			info['flags']
		)

	def test_all(self):
		info = cpuinfo._get_cpu_info_internal()

		self.assertEqual('AuthenticAMD', info['vendor_id_raw'])
		self.assertEqual('AMD Ryzen 7 2700X Eight-Core Processor', info['brand_raw'])
		self.assertEqual('3.6931 GHz', info['hz_advertised_friendly'])
		self.assertEqual('3.6931 GHz', info['hz_actual_friendly'])
		self.assertEqual((3693060000, 0), info['hz_advertised'])
		self.assertEqual((3693060000, 0), info['hz_actual'])
		self.assertEqual('X86_64', info['arch'])
		self.assertEqual(64, info['bits'])
		self.assertEqual(8, info['count'])

		self.assertEqual('x86_64', info['arch_string_raw'])

		self.assertEqual(64 * 1024, info['l1_instruction_cache_size'])
		self.assertEqual(32 * 1024, info['l1_data_cache_size'])

		self.assertEqual(512 * 1024, info['l2_cache_size'])
		# FIXME: This is l2 cache size not l3 cache size
		# it is wrong in /proc/cpuinfo
		self.assertEqual(512 * 1024, info['l3_cache_size'])

		self.assertEqual(2, info['stepping'])
		self.assertEqual(8, info['model'])
		self.assertEqual(23, info['family'])
		self.assertEqual(
			['3dnowprefetch', 'abm', 'aes', 'apic', 'arat', 'avx', 'avx2',
			'clflush', 'clflushopt', 'cmov', 'cmp_legacy', 'constant_tsc',
			'cpb', 'cpuid', 'cr8_legacy', 'cx16', 'cx8', 'de', 'extd_apicid',
			'fpu', 'fsgsbase', 'fxsr', 'fxsr_opt', 'ht', 'hypervisor',
			'lahf_lm', 'lm', 'mca', 'mce', 'misalignsse', 'mmx', 'mmxext',
			'movbe', 'msr', 'mtrr', 'nonstop_tsc', 'nopl', 'nx', 'pae', 'pat',
			'pclmulqdq', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'rdrand',
			'rdseed', 'rdtscp', 'rep_good', 'sep', 'ssbd', 'sse', 'sse2',
			'sse4_1', 'sse4_2', 'sse4a', 'ssse3', 'syscall', 'tsc',
			'tsc_known_freq', 'vme', 'vmmcall', 'x2apic', 'xsave']
			,
			info['flags']
		)
