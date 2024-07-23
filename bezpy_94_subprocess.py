# Spawn concurrent process to execute an exernal command from the command line
import os
import sys
# ============================================================================================================
# METHOD 1:  os.popen()  -  NOT PREFERRED
# ============================================================================================================
os.popen('dir')
stdout = os.popen("echo Hello World").read() #execute and receive text response from stdout
# for powershell command 'gci .'  use ...  cmd = "powershell; gci . "
# e.g. cmd = '''powershell; "Test-Connection yahoo.com -Count 1  | Select-Object Address, StatusCode, ResponseTime, BufferSize"'''


# ============================================================================================================
# METHOD 2: os.system()  -  NOT PREFERRED
# ============================================================================================================
return_value = os.system('"echo Hello World"')
cmd = "python --version"
returned_value = os.system(cmd)  # returns the exit code in unix
print(f'{returned_value}')
# for powershell command 'gci .'  use ...  cmd = "powershell; gci . "


def clear():
    """can clear DOS o/p screen with clear() command in the code """
    os.system( 'cls' )


# READ: https://www.datacamp.com/tutorial/python-subprocess

# ============================================================================================================
# METHOD 3: subprocess.run()  
# The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, 
# and obtain their return codes. subprocess.run() executes a command and waits for it to finish
# Note: better to use subprocess.run() over subprocess.call, which uses an older API
# ============================================================================================================

import sys
import subprocess


# subprocess.run('dir') on windows you require shell=True
subprocess.run('dir', shell=True)  


r = subprocess.run([sys.executable, "-c", "print('test')"], capture_output=True, text=True, check=False, timeout=10)
# subprocess.run returns object subprocess.CompletedProcess
# sys.executable - gives path to python.exe
# capture_output=True - output is captured to stdout & stderr by returned object and not displayed to screen, alternatively use stdout=subprocess.PIPE, stderr=subprocess.PIPE
# text=True - sets output as text, default is a bytestring
# encoding=’UTF-8′ -  (as alternative to above, sets output to UTF-8, default is binary)
# check=True - subprocess.CalledProcessError exception raised if the external program returns a non-zero exit code
# shell=True - allows you to enter commands just as if you were entering them in a Bash compatible shell as one string not as a list
# timeout=10 - will raise error subprocess.TimeoutExpired if the 10 secs expires
# input=     - use input argument to redirect standard input to the command equivalent of '<'. eg. redirect the output of previous command

r.args        # ['C:\\venv37\\Scripts\\python.exe', '-c', "print('test')"]
r.returncode  # = 0  i.e. success
r.stdout      #  = 'test\n'
r.stderr      # ''  will be empty string unless return code != 0
r.check_returncode() # Raise CalledProcessError if the exit code is non-zero  (same as check=True)


# ============================================================================================================
# METHOD 3: subprocess.Popen() - spawns a subprocess concurrently
# ============================================================================================================
# The main difference is that subprocess.run() executes a command and waits for it to finish, 
# subprocess.Popen you can continue doing your stuff while the process finishes and then just repeatedly call 
# subprocess.communicate yourself to pass and receive data to your process.
# Note that, what subprocess.run is actually doing is invoking for you the Popen and communicate, 
# so you don't need to make a loop to pass/receive data nor wait for the process to finish.



# Send output and error to NULL instead of the shell
# process = subprocess.Popen([r'C:\path\to\app.exe', 'arg1', '--flag', 'arg'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
# process.wait() # Waits for subprocess to complete 



# subprocess.PIPE will send the output to return value of process.commnuicate(), could also use capture_output=True
# process = subprocess.Popen([r'C:\path\to\app.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# stdout, stderr = process.communicate()  # This will block until process completes


# When using Popen, you can additionally use terminate(), kill() and send_signal() for more interactions with the process.

# send stdout to a file
with open('log.txt', 'w') as logfile:
    c = subprocess.Popen(['dir', '/B'], stdout=logfile, shell=True)



p = subprocess.Popen(['python', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)  # if you need full path use sys.executable instead of 'python'
return_value = p.wait()   # wait for subprocess to complete,  should return 0
p.args #  ['python', '--version']
p.returncode # should be 0,  same value as return_value
p.stdout.read()     # Standard output
if return_value != 0:
    print(p.stderr.read())  # standard error

from subprocess import check_output
# returns stdout directly using Popen
def get_version(): 
    stdout = check_output(['python', '--version'], text=True) # 'Python 3.10.1\n'
    return stdout[:stdout.find('.')] # Python 3
# p = subprocess.Popen(['powershell.exe', 'C:\\Temp\\test.ps1'], stdout=sys.stdout)   EXECUTE POWERSHELL SCRIPT


#subprocess.Popen(r'explorer /select,r"C:\temp"')     # Will Open Windows Explorer
#subprocess.call("explorer C:\\temp", shell=False)    # Will Open Windows Explorer (part of the old api) returns the returncode
#subprocess.run("explorer C:\\temp", shell=False)     # preferred to above, returns object which includes the returncode
#os.system('start %windir%\explorer.exe "C:\T1"')     # Will Open Windows Explorer
#os.startfile(r'.\myfiles\test.txt')                  # Will Open the txt file in windows
#os.startfile(r'.\myfiles\test.txt', 'open')          # Same as above
#os.startfile(r'.\myfiles\test.txt', 'print')         # will print file to the default printer



# You can install the 'sh' library as an alternative to os.subprocess
# https://pypi.org/project/sh/
# pip install sh
# import sh

# Run any command in $PATH...
# print(sh.ls('-la'))
