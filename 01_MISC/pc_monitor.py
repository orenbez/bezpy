# Investigate Remote desktop disconnects on Wang
import os
from time import sleep
from datetime import datetime as dt
from send_email import send

########################################################################################################################
### datestr4(): return a date_time string e.g. '2018-04-18 22:11:59'
########################################################################################################################
def datestr4():
    return dt.strftime(dt.now(), '%Y-%m-%d %H:%M:%S')

########################################################################################################################
### datestr1(): returns a date string e.g. '20180715'
########################################################################################################################
def datestr1():
    return dt.now().strftime('%Y%m%d')

########################################################################################################################
# Which process other than svchost.exe is LISTENING on port 3389
########################################################################################################################
def check_port():
    cmd1 = r'netstat -aon |find /i "LISTENING" |find "3389" > output.txt'
    os.system(cmd1)
    print(cmd1)

    with open('output.txt' , 'r') as op:
        lines = op.readlines()
        if not lines:  # NO PROCESS IS LISTENING
            with open(logfile, 'a') as log:
                log.write(f'{datestr4()} - Not LISTENING for 3389\n')
            #send('obezalely@tscinsurance.com', 'RMD not Listening on 3389', ' ', logfile)
        else:          # A PROCESS IS LISTENING
            for line in lines:
                pid = int(line.rstrip().split(' ')[-1])
                if pid != 2172:  # PROCESS IS NOT REMOTE DESKTOP
                    with open(logfile, 'a') as log:
                        log.write(f"{datestr4()}\n")
                    cmd2 = rf'tasklist /fi "pid eq {pid}" >> {logfile}'
                    os.system(cmd2)
                    print(cmd2)
                    send('obezalely@tscinsurance.com', 'Investigate Port Conflict', ' ', logfile)

            with open(logfile, 'a') as log:
                log.write(f"{datestr4()} - {line}\n")
    sleep(1)


def check_oren():
    cmd1 = r'netstat -aon |find /i "2172" |find /i "192.168.150.9" > output.txt'
    os.system(cmd1)
    print(cmd1)

    with open('output.txt' , 'r') as op:
        lines = op.readlines()
        if not lines:
            with open(logfile, 'a') as log:
                log.write(f'{datestr4()} - Oren not ESTABLISHED for 2172\n')
                send('obezalely@tscinsurance.com', 'RMD not Listening on 3389', ' ', logfile)
        else:
            with open(logfile, 'a') as log:
                log.write(f"{datestr4()} - {lines[0]}\n")
    sleep(1)

########################################################################################################################
### __main__:
########################################################################################################################
if __name__ == '__main__':
    logfile = f'log_{datestr1()}.txt'
    while True:
        check_port()
        check_oren()
        sleep(5)
########################################################################################################################
### End of __main__
########################################################################################################################