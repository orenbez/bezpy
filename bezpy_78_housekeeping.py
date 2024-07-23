# Keep the most recent 'n' files in the directory of a given format
# pyinstaller housekeeping.py  will compile to exe file
# Usage: housekeeping.exe C\Temp\logs 20
# Designed to keep only a fixed amount of log files on web server
# e.g. C:\inetpub\logs\LogFiles\W3SVC1\u_ex210923.log
# e.g. C:\inetpub\logs\LogFiles\W3SVC1\u_ex211004.log
# e.g. C:\Users\Administrator\Documents\Navicat\MySQL\servers\EastCoast\ecusad\230916233000.psc
# e.g. C:\Users\Administrator\Documents\Navicat\MySQL\servers\EastCoast\ecusad\230916233000.psb


import os
import sys
import re
from pathlib import Path
from datetime import datetime as dt
# from time import time, mktime, strptime


def set_file_modification_time(filename, mtime):
    stat = os.stat(filename)
    atime = stat.st_atime
    os.utime(filename, times=(atime, mtime.timestamp()))


def check_args():
    if len(sys.argv) != 3:
        print('Format: housekeeping.exe <path> <keep_number>')
        sys.exit(1)
    elif not os.path.isdir(sys.argv[1]):
        print(f'Invalid directory {sys.argv[1]}')
        sys.exit(2)
    dir = sys.argv[1]
    os.chdir(dir)

def match_file(file):
    if re.search(r'^u_ex\d+\.log$', file) or re.search(r'^\d+\.ps[bc]$', file):
        return True
    else:
        return False

# For testing
def gen_files():
    for i in range(1,30):
        file_name = f'u_ex9988{str(i).zfill(2)}.log'
        Path(file_name).touch()
        # Set the modification time of myfile.txt to 1980-1-1, leave the access time intact
        set_file_modification_time(file_name, dt(1980, 1, 1, 23, i, 0))




if __name__ == '__main__':
    #sys.argv = ['housekeeping.py', r'C:\Temp\prac', '2']
    check_args()
    num_to_keep = int(sys.argv[2])
    files = [i for i in os.listdir() if match_file(i)]
    print(f'{len(files)} matched files: {files}. Keeping {num_to_keep} files')
    for file in sorted(files, key=lambda x: os.path.getmtime(x), reverse=True)[num_to_keep:]:
        os.remove(file)
        print(f'file: {file} has been deleted.')