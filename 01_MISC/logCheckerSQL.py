################################################################################
### Program: logCheckerSQL.py to check content of log files
### Example of use from command prompt:
###     python emailer.py D:\...\SQLRUN_2018-04-02_22-54-26.log
### ARG1 = <path to log file>
### 04/03/18 - ONB - First Version 
################################################################################
import sys
#sys.argv = ['logchecker.py', 'D:\TSCLOG\SQLRUN_2018-04-02_22-54-26.log']
try:
    with open(sys.argv[1], 'r') as f_obj:
        lines_list = f_obj.readlines()
except IOError:
    print("Can't find file")
    sys.exit(1)
    
for line in lines_list:
    if line.find('INSERTED') > 0:     # line is a data line
        if (int(line.rsplit()[4]) > 0):  # 1 or more errors
            sys.exit(1)
################################################################################
