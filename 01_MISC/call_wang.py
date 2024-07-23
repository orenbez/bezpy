#!python3
########################################################################################################################
# Function: Procedure to test calling a Wang Cobol program and receiving a return value
# File Name: call_wang.py
# File Location: W:\TSCDIRECT\TSCDEV\ONBOBJ
# Notes:
#
# Version History:
# 09/27/2019 ONB 1st Version
#
#
########################################################################################################################

import subprocess

########################################################################################################################
###  CallProcess(cmd):
########################################################################################################################
def CallProcess(cmd):
    p = subprocess.Popen(cmd)
    p.wait()
    if p.returncode != 0:
        # print(p.stderr)
        print(f'Error 8: GETID failed, No data available for this policynumber: {cmd[-10:-2]}, car number {cmd[-1]}')
        sys.exit(8)



#############################################################################################################
### __main__:
#############################################################################################################
if __name__ == '__main__':

    cmd = "C:\\Acucorp\\Acucbl620\\AcuGT\\bin\\wrun32.exe D:\\TSCDIRECT\\TSCDEV\\ONBOBJ\\TESTPY arg1 arg2"
    CallProcess(cmd)
    returned_value = os.system(cmd)

