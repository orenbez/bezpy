# https://www.geeksforgeeks.org/psutil-module-in-python/
# https://pypi.org/project/psutil/
# https://psutil.readthedocs.io/en/latest/

# psutil is a cross platform library
# also see \bezpy\01_MISC\pc_monitor_2.py

import os
from datetime import datetime as dt
import platform  # built-in library
import cpuinfo   # requires pip install py-cpuinfo
import psutil    # requires pip install psutil


# ======================================================================================================================
# os methods
# ======================================================================================================================
os.getcwd()   # Return the current working directory  e.g. C:\bezpy\bezpy
os.getcwdb()  # as bytes  e.g. b'C:\bezpy\bezpy'
os.getpid()   # Returns process id  e.g. 12612
os.getppid()  # Returns parent process id
os.getlogin() # Returns current user
os.getenv('env_key', 'default')   # Returns environment variable value or assigns default if doesn't exist


# ======================================================================================================================
# platform library (standard)
# ======================================================================================================================
platform.system()                  # 'Windows'
platform.release()                 # '10'
platform.version()                 # '10.0.19041'
platform.platform()                # 'Windows-10-10.0.19041-SP0'
platform.node()                    # 'BezKids'  - Name of Computer or System Name
platform.machine()                 # 'AMD64'
platform.processor()               # 'Intel64 Family 6 Model 60 Stepping 3, GenuineIntel'
platform.win32_ver()               # ('10', '10.0.19041', 'SP0', 'Multiprocessor Free')
platform.win32_edition()           # 'Professional'
platform.architecture()            # ('64bit', 'WindowsPE')
platform.uname()                   # uname_result(system='Windows', node='BezKids', release='10', version='10.0.19041', machine='AMD64', processor='Intel64 Family 6 Model 60 Stepping 3, GenuineIntel')
platform.python_build()            # ('tags/v3.10.1:2cd268a', 'Dec  6 2021 19:10:37')
platform.python_version()          # '3.10.1'
platform.python_version_tuple()    # ('3', '10', '1')
platform.python_compiler()         # 'MSC v.1929 64 bit (AMD64)'
platform.python_branch()           # 'tags/v3.10.1'
platform.python_implementation()   # 'CPython'


# ======================================================================================================================
# getpass library (standard)
# ======================================================================================================================
import getpass
user = getpass.getuser()     # returns current user
passwd = getpass.getpass()   # PROMPTS user for their password, will not show entered keys on cmd/linux. returns the password

# ======================================================================================================================
# cpuinfo library
# ======================================================================================================================
cpuinfo.get_cpu_info()                   # {'python_version': '3.7.9.final.0 (64 bit)', 'cpuinfo_version': [8, 0, 0], 'cpuinfo_version_string': '8.0.0', 'arch': 'X86_64', 'bits': 64, 'count': 4, 'arch_string_raw': 'AMD64', 'vendor_id_raw': 'GenuineIntel', 'brand_raw': 'Intel(R) Core(TM) i5-4590T CPU @ 2.00GHz', 'hz_advertised_friendly': '2.0000 GHz', 'hz_actual_friendly': '2.0010 GHz', 'hz_advertised': [2000000000, 0], 'hz_actual': [2001000000, 0], 'l2_cache_size': 1048576, 'stepping': 3, 'model': 60, 'family': 6, 'l3_cache_size': 6291456, 'flags': ['3dnow', 'abm', 'acpi', 'aes', 'apic', 'avx', 'avx2', 'bmi1', 'bmi2', 'clflush', 'cmov', 'cx16', 'cx8', 'de', 'ds_cpl', 'dtes64', 'dts', 'erms', 'est', 'f16c', 'fma', 'fpu', 'fxsr', 'ht', 'ia64', 'invpcid', 'lahf_lm', 'mca', 'mce', 'mmx', 'monitor', 'movbe',  'msr', 'mtrr', 'osxsave', 'pae', 'pat', 'pbe', 'pcid', 'pclmulqdq', 'pdcm', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'rdrnd', 'sep', 'serial', 'smep', 'smx', 'ss', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'ssse3', 'tm', 'tm2', 'tsc', 'tscdeadline', 'vme', 'vmx', 'x2apic', 'xsave', 'xtpr'], 'l2_cache_line_size': 256, 'l2_cache_associativity': 6}
cpuinfo.get_cpu_info_json()              # returns above dictionary in json format
cpuinfo.get_cpu_info().get('brand_raw')  # 'Intel(R) Core(TM) i5-4590T CPU @ 2.00GHz'


# ======================================================================================================================
# psutil (process and system utilities)  SysMon = System Monitoring, PMon = Process Monitoring
# ======================================================================================================================
# cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) 
# It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes. 
# It implements many functionalities offered by classic UNIX command line tools such ...
# as ps, top, iotop, lsof, netstat, ifconfig, free and others. 
# psutil currently supports the following platforms: Linux, Windows, macOS, FreeBSD, OpenBSD, NetBSD, Sun Solaris, AIX


# LINUX PROCESS METRICS: see unix tool smem: https://linux.die.net/man/8/smem
# VSS = virtual set size
# RSS = resident set size
# PSS = proportional set size
# USS = unique set size


# ======================================================================================================================
# System Information, the CPU
# ======================================================================================================================
# Returns the system CPU times as a named tuple
# user – time spent by normal processes executing in user mode
# system – time spent by processes executing in kernel mode
# idle – time when system was idle
# nice – time spent by priority processes executing in user mode
# iowait – time spent waiting for I/O to complete. This is not accounted in idle time counter.
# irq – time spent for servicing hardware interrupts
# softirq – time spent for servicing software interrupts
# steal – time spent by other operating systems running in a virtualized environment
# guest – time spent running a virtual CPU for guest operating systems under the control of the
psutil.cpu_times()  # scputimes(user=174666.0, system=93257.37499999953, idle=3560662.375, interrupt=5096.40625, dpc=1431.890625)

# Returns the system-wide CPU utilization as a percentage
psutil.cpu_percent()  # 55.6, compares system CPU times elapsed since last call or module import
psutil.cpu_percent(interval=2)  # compares system CPU times elapsed before and after the interval
psutil.cpu_percent(interval=2, percpu=True)  # [14.7, 17.8, 12.4, 16.3]

# Returns the number of logical CPUs in the system
psutil.cpu_count()               # 4 logical processors
psutil.cpu_count(logical=False)  # 2 Physical Cores 

# Returns the various CPU statistics as a tuple
# ctx_switches – number of context switches since boot.
# interrupts – number of interrupts since boot.
# soft_interrupts – number of software interrupts since boot.
# syscalls – number of system calls since boot. Always set to 0 in Ubuntu.
psutil.cpu_stats()  # scpustats(ctx_switches=974171324, interrupts=3144618771, soft_interrupts=0, syscalls=3204362)

# Returns the CPU frequency as a nameduple
psutil.cpu_freq()  # scpufreq(current=2001.0, min=0.0, max=2001.0)   # note 2000 = 2.0 GHz


# average system load in last 1, 5, and 15 minutes as a tuple
psutil.getloadavg()  # (0.22, 0.33, 0.35) 
 
psutil.disk_partitions()
# [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260),
#  sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260)]

psutil.disk_usage('/')  # for combinded drives -> sdiskusage(total=254721126400, used=216050003968, free=38671122432, percent=84.8)
psutil.disk_usage('C:/').total/2**30 #  460.08327865600586  total disk usage on C drive in GB for Windows, can provide full path



# Returns the Ram details
# total – total physical memory excluding swap.
# available – the memory that can be given instantly to processes without the system going into swap.
# used – memory used.
# free – memory not used at and is readily available
# active – memory currently in use or very recently used.
# inactive – memory that is marked as not used.
# buffers – cache data like file system metadata.
# cached – cached data
# shared – memory that may be accessed by multiple processes.
vm = psutil.virtual_memory()  # svmem(total=17026523136, available=8168816640, percent=52.0, used=8857706496, free=8168816640)
if psutil.WINDOWS:
    vm.total / 2 ** 30   # Returns total Ram in GB
else:
    vm.total / 10 ** 9   # Returns total Ram in GB for linux platforms


# This function provides details of swap memory statistics as a tuple
# total – total swap memory in bytes
# used – used swap memory in bytes
# free – free swap memory in bytes
# percent – the percentage usage that is calculated as (total – available) / total * 100
# sin – the number of bytes the system has swapped in from disk
# sout – the number of bytes the system has swapped out from disk
psutil.swap_memory()  # sswap(total=2550136832, used=1689100288, free=861036544, percent=66.2, sin=0, sout=0)




# ======================================================================================================================
# Processes
# ======================================================================================================================
# Returning a sorted list of currently running processes
psutil.pids()   # [0, 4, 100, 448, 504, 508, 656, 680, 748, 752, 756, 764, 832, 840, 848, 908, 1120, 1144, 1164, 1196, 1216, 1260, 1296, 1424, 1436, 1476, 1484, 1564, 1572, 1660, 1744, 1804, 1812, 1832, 1848, 1876, 1888, 1956, 2072, 2128, 2156, 2188, 2204, 2228, 2240, 2276, 2332, 2372, 2408, 2576, 2612, 2632, 2684, 2744, 2788, 2796, 2820, 2856, 2904, 3000, 3040, 3060, 3108, 3116, 3136, 3172, 3180, 3200, 3220, 3276, 3396, 3472, 3476, 3572, 3588, 3596, 3656, 3664, 3692, 3812, 3860, 3904, 3968, 4048, 4088, 4188, 4208, 4228, 4252, 4372, 4448, 4456, 4464, 4516, 4596, 4604, 4612, 4620, 4628, 4636, 4644, 4652, 4660, 4680, 4696, 4704, 4720, 4732, 4744, 4752, 4760, 4768, 4776, 4784, 4792, 4800, 4808, 4820, 4828, 4832, 4840, 4860, 4876, 4988, 5136, 5260, 5272, 5280, 5312, 5468, 5532, 5588, 5608, 5656, 5804, 5864, 5948, 6024, 6120, 6616, 6636, 6680, 6760, 6828, 6836, 6900, 6916, 6964, 7012, 7052, 7176, 7288, 7316, 7452, 7660, 7708, 7880, 7928, 8000, 8108, 8260, 8336, 8364, 8412, 8420, 8432, 8488, 8500, 8536, 8580, 8608, 8616, 8880, 8888, 8972, 8984, 9176, 9248, 9288, 9376, 9492, 9496, 9564, 9668, 9776, 9936, 9976, 10004, 10068, 10104, 10248, 10412, 10424, 10436, 10496, 10644, 10712, 10728, 10832, 10892, 10912, 11012, 11116, 11188, 11232, 11296, 11312, 11316, 11332, 11344, 11588, 11688, 11716, 11760, 11936, 12140, 12216, 12340, 12492, 12496, 12588, 12700, 12752, 12772, 12780, 12800, 12828, 12944, 12972, 13116, 13128, 13304, 13392, 13508, 13524, 13604, 13832, 13852, 13944, 14104, 14236, 14304, 14396, 14544, 14632, 14644, 14684, 14700, 14840, 14912, 15084, 15136, 15144, 15500, 15552, 15616, 15776, 16328, 16336, 16364, 17144, 17764, 17872, 17968, 18232, 18372, 18492, 18664, 18716, 18756, 19004, 19060, 19160, 19168, 19196, 19352, 19412, 19420, 19428, 19484, 20092, 20364, 20428, 21316, 21448, 21456, 22512, 22644, 22928, 23040, 23212, 23216, 23260, 23408, 23824, 23940, 24052, 24272, 24388, 24488, 24732, 24848, 25048, 25108, 25196, 25276, 25380, 25428, 25724, 25760, 25948, 26176, 26408, 26560, 26716, 26812, 26960, 27356, 27728, 27840, 27896, 28120, 28124, 28168, 28328, 28344, 28368, 28504]


psutil.Process() # returns running process -> psutil.Process(pid=1200, name='python.exe', status='running', started='11:47:38')
psutil.pid_exists(pid=14136)  # returns bool, Used to check whether a certain process exists in the current process list
p = psutil.Process(pid=14136)  # returns specified process -> psutil.Process(pid=14136, name='OneDrive.exe', status='running', started='08:39:39')
p.memory_full_info() # pfullmem(rss=68947968, vms=21975040, num_page_faults=106768, peak_wset=86147072, wset=68947968, peak_paged_pool=574280, paged_pool=544696, peak_nonpaged_pool=186328, nonpaged_pool=49224, pagefile=21975040, peak_pagefile=45629440, private=21975040, uss=6225920)
p.memory_full_info().uss/(1024*1024) #  5.9296875 MB  - memory used by pid=14136
p.memory_percent()  # 0.40331286376575026  percent of RAM used
# Returns an iterator which prevents the race condition for process stats
i = psutil.process_iter() 
next(i)  #  psutil.Process(pid=0, name='System Idle Process', status='running')




# An example to terminate and wait for the children
def on_terminate(proc):
   print("process {} terminated with exit code {}".format(proc, proc.returncode))


procs = psutil.Process().children()
for p in procs:
   p.terminate()
gone, alive = psutil.wait_procs(procs, timeout=3, callback=on_terminate)
for p in alive:
   p.kill()

# Check whether the given PID exists in the current process list.
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name'])
    except psutil.NoSuchProcess:
        pass
    else:
        print(pinfo)


# Linux based OS?
psutil.LINUX   # False

# Windows based OS?
psutil.WINDOWS  # True

# Returns an iterator yielding a WindowsService class instance
psutil.win_service_iter()
# [<WindowsService(name='AdobeARMservice', display_name='Adobe Acrobat Update Service') at 2499703651848>,
#  <WindowsService(name='AJRouter', display_name='AllJoyn Router Service') at 2499703651912>,
#  <WindowsService(name='ALG', display_name='Application Layer Gateway Service') at 2499703651976>,
# ...
#  <WindowsService(name='UnistoreSvc_bb3f1', display_name='User Data Storage_bb3f1') at 2499703703112>,
#  <WindowsService(name='UserDataSvc_bb3f1', display_name='User Data Access_bb3f1') at 2499703703176>,
#  <WindowsService(name='WpnUserService_bb3f1', display_name='Windows Push Notifications User Service_bb3f1') at 2499703703240>,
#  <WindowsService(name='TeamViewer', display_name='TeamViewer') at 2499703703304>]

# Gets a Windows service by name, returning a WindowsService instance
psutil.win_service_get('TeamViewer')
# <WindowsService(name='TeamViewer', display_name='TeamViewer') at 2499704397448>

# System boot time expressed in seconds since the epoch
bt = psutil.boot_time()
# 1658628770.5131664

# System boot time converted to datetime
dt.fromtimestamp(bt) # datetime.datetime(2022, 7, 23, 22, 12, 50, 513166)

# returns list of current users
# user – It is the system name of the user.
# terminal – the tty of the user.
# host – the host name of the user.
# started – the creation time as a floating point number expressed in seconds since the epoch.
# pid – the PID of the login process.
psutil.users()  # [suser(name='orenb', terminal=None, host=None, started=1658628767.0065024, pid=None)]

# ======================================================================================================================
# Sensors
# ======================================================================================================================
psutil.sensors_battery()    # sbattery(percent=95, secsleft=<BatteryTime.POWER_TIME_UNLIMITED: -2>, power_plugged=True)


# ======================================================================================================================
# Network
# ======================================================================================================================
# returns details of network Input output statistics as a tuple
# bytes_sent – number of bytes sent
# bytes_recv – number of bytes received
# packets_sent – number of packets sent
# packets_recv – number of packets received
# errin – total number of errors while receiving
# errout – total number of errors while sending
# dropin – total number of incoming packets which were dropped
# dropout – total number of outgoing packets which were dropped
psutil.net_io_counters()   # snetio(bytes_sent=6941756107, bytes_recv=37212344367, packets_sent=10704514, packets_recv=19891531, errin=0, errout=0, dropin=0, dropout=0)


# returns list of socket connections of a system as a named tuples
# fd – the socket file descriptor.
# family – the socket family, either AF_INET, AF_INET6 or AF_UNIX.
# type – the socket type, either SOCK_STREAM, SOCK_DGRAM or SOCK_SEQPACKET.
# laddr – the local address as a (ip, port) named tuple
# raddr – the remote address as a (ip, port) named tuple
# status – represents the status of a TCP connection.
# pid – the PID of the process which opened the socket, if retrievable, else None.
psutil.net_connections()  #  [sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=<SocketKind.SOCK_DGRAM: 2>, laddr=addr(ip='::', port=58902), raddr=(), status='NONE', pid=8984), ...


# returns addresses of each network interface card installed on the system
# family – the socket family, either AF_INET or AF_INET6
# address – the primary NIC address
# netmask – the netmask address
# broadcast – the broadcast address.
# ptp – “point to point” it is the destination address on a point to point interface.
psutil.net_if_addrs()  #  {'Local Area Connection* 3': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='62-6D-C7-C2-4D-C5', netmask=None, broadcast=None, ptp=None), ...


# return information about each NIC (network interface card)
psutil.net_if_stats() # {'Bluetooth Network Connection': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=3, mtu=1500), 'Loopback Pseudo-Interface 1': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=1073, mtu=1500),  'Wi-Fi': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=505, mtu=1500),  'Local Area Connection* 3': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500),  'Local Area Connection* 4': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500)}


# ======================================================================================================================
# CPU
# cpu_count()
# cpu_freq()
# cpu_percent()
# cpu_stats()
# cpu_times()
# cpu_times_percent()
#
#
# DISK
# disk_io_counters()
# disk_partitions()
# disk_usage()
#
# MEMORY
# swap_memory()
# virtual_memory()
#
# NETWORK
# net_connections()
# net_if_addrs()
# net_if_stats()
# net_io_counters()
#
# PROCESS
# pid_exists()
# pids()
# process_iter()
# wait_procs()
#
# SYSTEM INFO
# boot_time()
# users()
# version_info()
# ======================================================================================================================
