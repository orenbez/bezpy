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
# for System & CPU Information
# ======================================================================================================================
# cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors)
# It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes.
# It implements many functionalities offered by classic UNIX command line tools such as ...
# ps, top, iotop, lsof, netstat, ifconfig, free and others.
# psutil currently supports the following platforms: Linux, Windows, macOS, FreeBSD, OpenBSD, NetBSD, Sun Solaris, AIX
# LINUX PROCESS METRICS: see unix tool smem: https://linux.die.net/man/8/smem
# ======================================================================================================================
# VSS = virtual set size
# RSS = resident set size
# PSS = proportional set size
# USS = unique set size

# ======================================================================================================================
# CPU
# ======================================================================================================================
psutil.cpu_count()               # Returns the number of logical CPUs in the system, e.g. 4 logical processors
psutil.cpu_count(logical=False)  # 2 Physical Cores

# Returns the CPU frequency as a nameduple
psutil.cpu_freq()  # scpufreq(current=2001.0, min=0.0, max=2001.0)   # note 2000 = 2.0 GHz

# Returns the system-wide CPU utilization as a percentage
psutil.cpu_percent() # e.g. 55.6, compares system CPU times elapsed since last call or module import (see 'Warning' below regarding first call)
psutil.cpu_percent(interval=None, percpu=False)  # same as above call
psutil.cpu_percent(interval=2)  # compares system CPU times elapsed before and after the interval
psutil.cpu_percent(interval=2, percpu=True)  # [14.7, 17.8, 12.4, 16.3]
# interval: This parameter represents the time interval over which the method calculates the CPU usage.
#           Giving interval > 0 results in a blocking call where the CPU usage is calculated over the interval time.
#           Warning - When interval is 0.0 or None compares process times to system CPU times elapsed since last call, returning value immediately.  However the first call will always return 0.0 which is useless information
# percpu: This is a boolean parameter. When set to true, the method returns a list indicating the utilization of each CPU in the system.
# Returns the various CPU statistics as a tuple

psutil.cpu_stats()  # scpustats(ctx_switches=974171324, interrupts=3144618771, soft_interrupts=0, syscalls=3204362)
# ctx_switches – number of context switches since boot.
# interrupts – number of interrupts since boot.
# soft_interrupts – number of software interrupts since boot.
# syscalls – number of system calls since boot. Always set to 0 in Ubuntu.
# Returns the system CPU times as a named tuple

psutil.cpu_times()  # scputimes(user=174666.0, system=93257.37499999953, idle=3560662.375, interrupt=5096.40625, dpc=1431.890625)
# user – time spent by normal processes executing in user mode
# system – time spent by processes executing in kernel mode
# idle – time when system was idle
# nice – time spent by priority processes executing in user mode
# iowait – time spent waiting for I/O to complete. This is not accounted in idle time counter.
# irq – time spent for servicing hardware interrupts
# softirq – time spent for servicing software interrupts
# steal – time spent by other operating systems running in a virtualized environment
# guest – time spent running a virtual CPU for guest operating systems under the control of the

psutil.cpu_times(percpu=True)  # returns list, entry for each cpu  [scputimes(user=12544.968749999998, system=19588.46875, idle=99475.578125, interrupt=94.90625, dpc=94.578125), scputimes(user=13804.453125, system=21443.296875, idle=96361.109375, interrupt=83.859375, dpc=83.453125), scputimes(user=16564.03125, system=25188.703125, idle=89856.125, interrupt=83.34375, dpc=128.03125), scputimes(user=19705.5625, system=30372.796875, idle=81530.5, interrupt=82.859375, dpc=213.578125)]
psutil.cpu_times_percent(interval=None, percpu=False)  # scputimes(user=14.2, system=22.4, idle=63.1, interrupt=0.1, dpc=0.1)
psutil.getloadavg()  # average system load in last 1, 5, and 15 minutes as a tuple e.g (0.22, 0.33, 0.35)

# ======================================================================================================================
# DISK
# ======================================================================================================================
psutil.disk_io_counters(perdisk=False, nowrap=True)  # sdiskio(read_count=1108853, write_count=5153040, read_bytes=26121326080, write_bytes=91932425216, read_time=1125, write_time=7416)
psutil.disk_usage('/')  # for combined drives -> sdiskusage(total=254721126400, used=216050003968, free=38671122432, percent=84.8)
psutil.disk_usage('C:/').total/2**30 #  460.08327865600586  total disk usage on C drive in GB for Windows, can provide full path
psutil.disk_partitions()  # [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260)]

# ======================================================================================================================
# MEMORY
# ======================================================================================================================
# Returns the Ram details
vm = psutil.virtual_memory()  # svmem(total=17026523136, available=8168816640, percent=52.0, used=8857706496, free=8168816640)
# total – total physical memory excluding swap.
# available – the memory that can be given instantly to processes without the system going into swap.
# used – memory used.
# free – memory not used at and is readily available
# active – memory currently in use or very recently used.
# inactive – memory that is marked as not used.
# buffers – cache data like file system metadata.
# cached – cached data
# shared – memory that may be accessed by multiple processes.

if psutil.WINDOWS:
    vm.total / 2 ** 30   # Returns total Ram in GB
else:
    vm.total / 10 ** 9   # Returns total Ram in GB for linux platforms

# This function provides details of swap memory statistics as a tuple
psutil.swap_memory()  # sswap(total=2550136832, used=1689100288, free=861036544, percent=66.2, sin=0, sout=0)
# total – total swap memory in bytes
# used – used swap memory in bytes
# free – free swap memory in bytes
# percent – the percentage usage that is calculated as (total – available) / total * 100
# sin – the number of bytes the system has swapped in from disk
# sout – the number of bytes the system has swapped out from disk

psutil.sys  # built-in module
psutil.test()

# USER         PID  %MEM     VSZ     RSS  NICE STATUS  START   TIME  CMDLINE
# SYSTEM         0   0.0   60.0K    8.0K        runni         10:17  System Idle P
# SYSTEM         4   0.0  200.0K  152.0K        runni         47:21  System
#              108   0.2   17.5M   75.2M        runni  Jul17  00:18  Registry
# orenb        144   0.4   69.0M  142.0M    32  runni  Jul17  01:44  C:\Program Fi
#              304   0.1   13.4M   33.4M        runni  Jul17  05:09  lsass.exe
#             6700   0.1    6.1M   34.1M        runni  Jul17  00:00  svchost.exe

psutil.threading  # <module 'threading' from 'C:\\Program Files\\Python39\\lib\\threading.py'>
psutil.time  # built-in module

# ======================================================================================================================
# Processes
# ======================================================================================================================
# Returning a sorted list of currently running processes
psutil.pids()   # [0, 4, 100, 448, 504, 508, 656, 680, 748, 752, …, 28344, 28368, 28504]
psutil.pid_exists(304)  # True
psutil.pid_exists(3)    # False
psutil.Process() # returns running process -> psutil.Process(pid=1200, name='python.exe', status='running', started='11:47:38')
psutil.pid_exists(pid=14136)  # returns bool, Used to check whether a certain process exists in the current process list
p = psutil.Process(pid=14136)  # returns specified process -> psutil.Process(pid=14136, name='OneDrive.exe', status='running', started='08:39:39')
p.memory_full_info() # pfullmem(rss=68947968, vms=21975040, num_page_faults=106768, peak_wset=86147072, wset=68947968, peak_paged_pool=574280, paged_pool=544696, peak_nonpaged_pool=186328, nonpaged_pool=49224, pagefile=21975040, peak_pagefile=45629440, private=21975040, uss=6225920)
p.memory_full_info().uss/(1024*1024) #  5.9296875 MB  - memory used by pid=14136
p.memory_percent()  # 0.40331286376575026  percent of RAM used

# Generator of processes which prevents the race condition for process stats
generator_of_processes = psutil.process_iter(attrs=None, ad_value=None)  # returns generator of processes
next(generator_of_processes)  # psutil.Process(pid=0, name='System Idle Process', status='running')

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

# Returns an generator yielding a WindowsService class instance
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

# ======================================================================================================================
# SYSTEM INFO
# ======================================================================================================================
# System boot time expressed in seconds since the epoch
bt = psutil.boot_time()  # e.g. 1658628770.5131664
dt.fromtimestamp(bt)  # converted to datetime datetime.datetime(2022, 7, 23, 22, 12, 50, 513166)
psutil.users()  # [suser(name='orenb', terminal=None, host=None, started=1658628767.0065024, pid=None)]
# user – It is the system name of the user.
# terminal – the tty of the user.
# host – the host name of the user.
# started – the creation time as a floating point number expressed in seconds since the epoch.
# pid – the PID of the login process.
# returns list of current users

psutil.version_info()  # returns version of psutil module e.g. (5, 9, 5)

# ======================================================================================================================
# SENSORS
# ======================================================================================================================
psutil.sensors_battery()  # Return battery information if installed else None.  e.g. sbattery(percent=95, secsleft=<BatteryTime.POWER_TIME_UNLIMITED: -2>, power_plugged=True)
     # - percent: battery power left as a percentage.
     # - secsleft: a rough approximation of how many seconds are left
     #             before the battery runs out of power. May be
     #             POWER_TIME_UNLIMITED or POWER_TIME_UNLIMITED.
     # - power_plugged: True if the AC power cable is connected

# ======================================================================================================================
# Network
# ======================================================================================================================
psutil.net_io_counters()   # snetio(bytes_sent=6941756107, bytes_recv=37212344367, packets_sent=10704514, packets_recv=19891531, errin=0, errout=0, dropin=0, dropout=0)
# returns details of network Input output statistics as a tuple
# bytes_sent – number of bytes sent
# bytes_recv – number of bytes received
# packets_sent – number of packets sent
# packets_recv – number of packets received
# errin – total number of errors while receiving
# errout – total number of errors while sending
# dropin – total number of incoming packets which were dropped
# dropout – total number of outgoing packets which were dropped

psutil.net_connections()  # e.g. [sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=<SocketKind.SOCK_DGRAM: 2>, laddr=addr(ip='::', port=58902), , …]
# returns list of socket connections of a system as a named tuples
# fd – the socket file descriptor.
# family – the socket family, either AF_INET, AF_INET6 or AF_UNIX.
# type – the socket type, either SOCK_STREAM, SOCK_DGRAM or SOCK_SEQPACKET.
# laddr – the local address as a (ip, port) named tuple
# raddr – the remote address as a (ip, port) named tuple
# status – represents the status of a TCP connection.
# pid – the PID of the process which opened the socket, if retrievable, else None.

psutil.net_if_addrs()  # e.g. {'Ethernet0': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='00-50-56-88-D2-2A', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address=X.X.X.X', netmask='255.255.252.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::1a63:d3b8:c7e0:cced', netmask=None, broadcast=None, ptp=None)], 'Loopback Pseudo-Interface 1': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='::1', netmask=None, broadcast=None, ptp=None)]}
                       # e.g  {'Local Area Connection* 3': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='62-6D-C7-C2-4D-C5', netmask=None, broadcast=None, ptp=None), ...
# returns addresses of each network interface card installed on the system
# family – the socket family, either AF_INET or AF_INET6
# address – the primary NIC address
# netmask – the netmask address
# broadcast – the broadcast address.
# ptp – “point to point” it is the destination address on a point to point interface.

psutil.net_if_stats() # e.g {'Bluetooth Network Connection': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=3, mtu=1500), 'Loopback Pseudo-Interface 1': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=1073, mtu=1500),  'Wi-Fi': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=505, mtu=1500),  'Local Area Connection* 3': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500),  'Local Area Connection* 4': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500)}
                      # e.g {'Ethernet0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=4294, mtu=1500, flags=''), 'Loopback Pseudo-Interface 1': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=1073, mtu=1500, flags='')}
# return information about each NIC (network interface card)
