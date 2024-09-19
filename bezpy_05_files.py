import sys  #used for sys.exit() use echo %errorlevel%  or echo $? on Unix
import os
from time import sleep
from mylib.mymisc import boo      # function boo() will print an output marker to screen


# ============================================================================================================
# FILE INPUT OUTPUT.  note the 'with' operator will close file even if exception occurs in the code block
# ============================================================================================================
os.getcwd()   # Return the current working directory  e.g. C:\bezpy\bezpy

os.path.abspath(os.path.curdir) #alternative to getcwd()
os.chdir('..') # Changes current working directory (cwd) to the above directory  e.g. C:\bezpy
# os.chdir('../..') for two parent directories above
program_path = os.path.dirname(__file__)    # directory of your python file e.g C:\bezpy\bezpy
program_file = os.path.basename(__file__)   # python file name which is being executed

src = os.path.join(program_path, 'myfiles')
os.chdir(src) # Changes current working directory (cwd) to src

path = os.path.join(os.path.dirname(__file__), 'myfiles', 'file.txt')  # e.g 'c:\\bezpy\\bezpy\\myfiles\\file.txt'


#  './dir2/file'           RELATIVE PATH ON UNIX
#  '/dir1/dir2/file'       ABSOLUTE PATH ON UNIX

#  r'.\dir2\file           RELATIVE PATH ON WINDOWS
#  r'C:\dir1\dir2\file     ABSOLUTE PATH ON WINDOWS

# This should return full path as string 'C:\\Users\\obezalely\\OneDrive\\PYTHON\\myfiles\\output1.txt'
path = os.path.join(os.getcwd(), 'output1.txt')



try:        # if file not found will create file in that path as long as path exists
    # 'w' = WRITE, will create file if not present
    file_obj = open(path, 'w')  # ABSOLUTE PATH
    file_obj.write("This Will be line 1\n")
    file_obj.write("This Will be line 2")
    file_obj.flush() # flushes data to file immediately and doesn't wait for .close()
    file_obj.close() #NOTE: if you don't use the 'with' operator then you need to close manually
    
except IOError:
	print(f"Can't find path ... {path}")


# 'r' = READ is read only.  This is the DEFAULT and the 'r' is not required
os.chdir('..')
with open(r'myfiles\input.txt', 'r') as f_obj:  #RELATIVE PATH for some FUNCTIONS use .\myfiles\input.txt
    lines_list = f_obj.readlines()
    print ('lines_list:',lines_list)

for line in lines_list:
    print('A:',line)             #Includes the '\n' from each line in the file

for line in lines_list:
    print('B:', line.rstrip())   #rstrip() - strips the '\n' from each line in the file

with open(r'myfiles\input.txt', 'r') as f_obj:  #RELATIVE PATH
    whole_file = f_obj.read() # this time we read WHOLE FILE as a string
    print ('whole_file:',whole_file)
     
# ============================================================================================================
# simple loop through all lines - THIS IS THE EASIEST WAY
with open(r".\myfiles\input.txt", "r") as f:
    for line in f:   ## WILL NOT REACH THIS LINE IF FILE IS EMPTY, MAY NEED TO USE f.readlines() instead to check for empty file
        print(line.rstrip())

# generate line number with enumerate:
with open(r".\myfiles\input.txt", "r") as f:
    for line_number, line in enumerate(f, 1):
        print(line_number, line.rstrip())


# ============================================================================================================
# this only prints every other line. because each loop will read 'f' twice, once automatically,
# 2nd time with f.readline()
with open(r".\myfiles\input.txt", "r") as f:  # Options: errors='ignore', encoding="utf8"
    for _ in f:
        print (f.readline().rstrip())

# ============================================================================================================
with open(".\myfiles\input.txt", "r") as f:
    number_lines = len(f.readlines())
    f.seek(0) # resets file pointer to begining 'the zeroth' byte
    for _ in range(number_lines):
        print (f.readline().rstrip())

# ============================================================================================================
f = open(".\myfiles\input.txt", "r")
line = f.readline()  # read first line.      
while line:
    print(line, end='')
    line = f.readline()  # read next line    
# f.readline() returns empty string at end of file. NOTE: next(f) also returns the next line but raises StopIteration at end of file

# ============================================================================================================ 
# 'w' = WRITE, will create file if not present / overwrite if present
with open(r'myfiles\output2.txt', 'w') as f:
    f.write("This Will be OLD line 1\n")	
    f.write("This Will be OLD line 2\n")		
            
# 'a' = APPEND, will create file if not present / append if present by placing the pointer at end of file
with open('myfiles\output2.txt', 'a') as f:
    f.write("This Will be line 3\n")	
    f.write("This Will be line 4") # no next line 


f = open('myfiles\output2.txt')  # default is read in text mode (see below)
f.close() # need explicit close since no 'with' command was used

# as of python 3.10 can use syntax below ...
# with (open('output.log', 'w') as fout, open('input.csv') as fin):
#     fout.write(fin.read())


# f = open(file_name, 'r', encoding='utf-8') # Opens file stream in mode 'r' expecting unicode characters
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#    ========= =========================================================================================================
#    Character Mode
#    ========= =========================================================================================================
#    'r'       open for reading (default 'r' is not required)
#    'w'       open for writing, truncating the file first to the beginning if exists, creating new if doesn't
#    'wb'      open for writing in binary, truncating the file first to the beginning if exists, creating new if doesn't
#    'x'       create a new file and open it for writing, error if it exists
#    'a'       open for writing, appending to the end of the file if it exists, creates new file if doesn't exist
#    'a+'      open file for updating in text mode (reading and writing), will append if file exists or create otherwise
#    'ab'      open for writing in binary, appending to the end of the file if it exists, creates new file if doesn't exist
#    'ab+'     open for updating in binary (reading and writing), appending to the end of the file if it exists, creates new file if doesn't exist
#    'rb'      read in binary binary mode
#    't'       read in text mode ('t' is default)
#    'rt'      read in text mode ('t' is explicit here but not required)
#    'wb'      write in binary mode
#    'wb+'     updating in binary mode (reading or writing)
#    'wt'      write in text mode ('t' is explicit here but not required)
#    'r+'      open an 'existing' disk file for updating in text mode (reading and writing)
#    'U'       universal newline mode (deprecated)
#    ========= =========================================================================================================


# ======================================================================================================================
# FILE METHODS https://www.w3schools.com/python/python_ref_file.asp. Note there is also a readchar library (non-standard)
# ======================================================================================================================
# f.write(string)        # writes string to file  (note can also use the 'print' function to write to file
# f.writelines(list)     # writes list of lines to file
# f.read([n])            # reads next 'n' chars, from underlying buffer until we have n characters or we hit EOF
# f.read()               # reads the whole file
# f.readlines([n])       # reads list of next 'n' lines
# f.readline()           # reads the next line, and returns the line,   returns '' when reaches eof
# f.flush()              # flushes any cache stored with f.write() to the file, otherwise waits for f.close() before flushing
# f.close()	             # close file-stream
# f.closed               # returns boolean  True => file is closed
# f.readable()           # returns boolean  True => file is in read mode
# f.writable()           # returns boolean  True => file is write mode
# f.name                 # returns filename

# ======================================================================================================================
# THE FILE POINTER
# ======================================================================================================================
# f.seekable()               # returns bool, True if objects supports random access => tell, seek, truncate will work without error
# f.tell()                   # returns byte position of file pointer, can not be activated in loop that uses 'next' function
# f.seek(position[,origin])  # goes to file pointer position in bytes, seek(0) goes to the beginning
# f.truncate([size])         # truncate the file at the current pointer positing with f.truncate(),  or a specific byte position f.truncate(695)   
# Note can determine EOF if f.tell() has stopped incrementing with the next f.readline() command

# ======================================================================================================================
# Not sure about these functions
# ======================================================================================================================
# f.reconfigure(encoding=None, errors=None, newline=None, line_buffering=None, write_through=None)
                         # This performs a stream flusch and reconfigures the text stream
# f.isatty()             # Return whether this is an 'interactive' stream. ???
# f.fileno()             # Returns underlying file descriptor if one exists. ???  OSError is raised if the IO object does not use a file descriptor
# f.detach()             # Separate the underlying buffer from the TextIOBase and return it.
                         # After the underlying buffer has been detached, the TextIO is in an  unusable state.


# example for editing a file by replacing text ...
with open(r'.\myfiles\output2.txt','r+') as f:  # opened for read and/or write
    data = f.read()                     # reads entire file, pointer is at end
    f.seek(0)                           # places pointer at the beginning
    f.write(data.replace('OLD','NEW'))  # or use regex
    f.truncate()                        # places end-pointer at current pointer position.

# f.seek(8, 2) will advance 8 bytes from byte 2

# Edit file. insert arrow for every line starting with 'XXX'
f = open(r'.\myfiles\LoremIpsum.txt', 'r+')
count = 1 # initialize count
pointer = f.tell()  # stores pointer location before reading first line
line = f.readline()   # read first line
while line:
	if line.startswith('XXX'):
		f.seek(pointer)  # Moves to beginning of line
		f.write('-> ' + line) # edits line
	pointer = f.tell()  # stores pointer location before reading next line
	line = f.readline() # read next line
f.close()

# ======================================================================================================================
# FILE / DIRECTORY MANIPULATION
# ======================================================================================================================

# String quotes can be escaped with a backslash, but the backslash remains in the string;
# for example, r"\"" is a valid string literal consisting of two characters: a backslash and a double quote;
# r"\" is not a valid string literal (even a raw string cannot end in an odd number of backslashes).
# This is because 'r' tells the interpreter to include anything following backslash

# src = r'C:\OrenDocs\'  THIS IS INVALID use ...  src = r'C:\OrenDocs'
x = '\\n'  #first backslash escapes the 2nd. (new line is not interpreted)


src1 = r'C:\OrenDocs\PYTHON\myfiles'    # note don't end string with '\'  even for a RAW string
src2 = 'C:\\OrenDocs\\PYTHON\\myfiles'  # without raw string, using escape character
path = src2 + '\\' + 'input.txt'

# better
src = os.path.join(os.path.dirname(__file__), 'myfiles') 
path = os.path.join(os.path.dirname(__file__), 'myfiles', 'input.txt')



if(not os.path.exists(path)):
    print(f"{path} is an invalid path, please try again.")
    sys.exit()


# listdir
for file in os.listdir(src):    # loops through all files/directories in directory
    print(file)                 # file is a string of the file name

for file in os.listdir():      # loops through current working directory instead
    print(file)

# Deletes a single directory if path exists (known as LOOK-BEFORE-YOU-LEAP)
if os.path.exists(r'.\myfiles\folder_name'):
    os.rmdir(r'.\myfiles\folder_name')    # only works for an EMPTY DIRECTORY use shutil.rmtree(path) for non-empty

# Delete full path  recursively starting from 'myfiles'
if os.path.exists(r'.\myfiles\Data Science Projects\Project 1'):
    os.removedirs(r'.\myfiles\Data Science Projects\Project 1')

# Create a single folder
if not os.path.exists(r'.\myfiles\folder_name'):
    os.mkdir(r'.\myfiles\folder_name')
    # for linux platforms you can add parameter e.g. mode=511

# Creates a full path including all sub-directories
if not os.path.exists(r'.\myfiles\Data Science Projects\Project 1'):
    os.makedirs(r'.\myfiles\Data Science Projects\Project 1')  
    # can add parameter exist_ok=False to raise exception if target directory already exists
    # for linux platforms you can add parameter e.g. mode=511


# ======================================================================================================================
# os.access  - to test if the invoking user has the specified access to path
# ======================================================================================================================
# Syntax: os.access(path, mode)
# Mode:
# os.F_OK: Tests existence of the path.
# os.R_OK: Tests readability of the path.
# os.W_OK: Tests writability of the path.
# os.X_OK: Checks if path can be executed.
os.access(r'.\myfiles\file.txt', os.R_OK)  # returns True



# scandir returns an iterator of file objects
for file in os.scandir(src):    # loops through all files/directories in src
    print(f'Name: {file.name}, Path:{file.path}')
    # file is an object with values/ operations ....
    # 'file.is_dir()', 'file.is_file()', 'file.is_symlink()', 'file.name', 'file.path' = full path including file name
    # '.stat()  which returns meta-data ...
    # os.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=289334203,
    #                                        st_atime=1510341007, st_mtime=1390922866, st_ctime=1510341007)

# os.walk(path) will returns a generator for full directory tree
path = os.path.join(os.getcwd(),'myfiles')
for root, dirs, files in os.walk(path):
    print(f'ROOT:{root}')
    print(f'DIRS:{dirs}')
    print(f'FILE:{files}\n')


fullsourcepath = os.path.join(os.path.dirname(__file__), 'myfiles', 'output2.txt')
fulldestpath = os.path.join(os.path.dirname(__file__), 'myfiles', 'output3.txt')
fullsharepath = r'\\tsc-app12\Imageright Exports\Pomco\Shared Folders\Allstate Documents'


# Returns epoch time, see time module in bezPy03  you can use datetime library or time library to handle epoch time
mt = os.path.getmtime(fullsourcepath)   # last modified time
ct = os.path.getctime(fullsourcepath)   # created time
at = os.path.getatime(fullsourcepath)   # last access time
size = os.path.getsize(fullsourcepath)  # file size in bytes


# alternately also returns epoch time
mt = os.stat(fullsourcepath).st_mtime   # last modified time
ct = os.stat(fullsourcepath).st_ctime   # last created time
at = os.stat(fullsourcepath).st_atime   # last access time
size = os.stat(fullsourcepath).st_size  # file size in bytes


# Note: the 'stat' module from the standard library, defines constants and functions for interpreting the results
#       of os.stat(), os.fstat() and os.lstat()
# https://docs.python.org/3/library/stat.html



from time import mktime, strptime, ctime, time
from datetime import datetime as dt
ctime(mt) # 'Mon Aug 22 09:51:42 2022'  epoch_time -> string


# Set access time and modified time (must set both) based on epoch time values
atime= time()
time_struct = strptime('1/1/2017-13:12:59', '%m/%d/%Y-%H:%M:%S')  # converts string -> time.struct_time
mtime = mktime(time_struct) # time.struct_time ->  to epoch time
mtime = dt(2017, 1, 1, 13, 12, 59).timestamp()  # Datetime() -> Epoch Time
os.utime(fullsourcepath, times=(atime, mtime))  # manually setting the 'modifed time' for a file


# Set the modification time of myfile.txt to 1980-1-1, leave the access time intact
def set_file_modification_time(filename, mtime):
    """
    Set the modification time of a given filename to the given mtime.
    mtime must be a datetime object.
    """
    stat = os.stat(filename)
    atime = stat.st_atime
    os.utime(filename, times=(atime, mtime.timestamp()))


set_file_modification_time(fullsourcepath, dt(1980, 1, 1, 0, 0, 0))


# 1 unsigned byte can represent 0 to 255, i.e. '0b00000000' to '0b11111111'  note 2**8 = 256
# 1 signed byte uses first bit for sign and can represent -128 to 127

# Returns file size in bytes
# For Windows 1024 B = 2**10 b = 1 kB, 1024 kB = 1 MB   (binary  interpretation)
# Other OS    1000 B = 10**3 b = 1 kB, 1000 kB = 1 MB   (decimal interpretation)

# WINDOWS BINARY USE BASE-2
# kibi (kilobinary), mebi (megabinary), gibi (gigabinary), tebi (terabinary), exbi (exabinary), zebi (zettabinary), yobi (yottabinary)
# 1 KiB = 1024 bytes  = 2**10 B
# 1 MiB = 1024 KiB = 2**20 B = 1024 * 1024 bytes
# 1 GiB = 1024 MiB = 2**30 B = 1024 * 1024 * 1024 bytes
# 1 TiB = 1024 GiB = 2**40 B = 1024 * 1024 * 1024 * 1024 bytes
# 1 PiB = 1024 TiB = 2**50 B = 1024 * 1024 * 1024 * 1024 * 1024 bytes
# 1 EiB = 1024 PiB = 2**60 B = 1024 * 1024 * 1024 * 1024 * 1024 * 1024 bytes

# NON-WINDOWS USE BASE-10
# kilo, mega, giga, tera, peta, exa, zeta, yotta
# 1 Kb = 10**3 B = 1000 bytes 
# 1 Mb = 10**3 Kb = 10**6  B = 1000 * 1000 bytes 
# 1 Gb = 10**3 Mb = 10**9  B = 1000 * 1000 * 1000 bytes 
# 1 Tb = 10**3 Gb = 10**12 B = 1000 * 1000 * 1000 * 1000 bytes 
# 1 Pb = 10**3 Tb = 10**15 B = 1000 * 1000 * 1000 * 1000 * 1000 bytes 
# 1 Eb = 10**3 Pb = 10**18 B = 1000 * 1000 * 1000 * 1000 * 1000 x 1000 bytes 

import platform
one_kb = 2 ** 10 if platform.system() == 'Windows' else 10 ** 3
one_mb = 2 ** 20 if platform.system() == 'Windows' else 10 ** 6

# Note 'filesize' module was removed from the standard library, use os.path.getsize() instead
size_bytes = os.path.getsize(fullsourcepath)
size_kbytes = os.path.getsize(fullsourcepath) / one_kb
size_mbytes = os.path.getsize(fullsourcepath) / one_mb

# this MOVES AND RENAMES the file if the file exists and destination file doesn't exist
# otherwise you get FileExistsError.  Will not write over destination if already exists
if os.path.exists(fullsourcepath) and not os.path.exists(fulldestpath):
    os.rename(fullsourcepath,fulldestpath)  # for relative paths use dot as in  r'.\mydir\myfile'
	
# Check if file exist, then DELETE it if exists
if os.path.exists(fulldestpath):
    os.remove(fulldestpath)   # identilcal to os.unlink(path), unlink is the idomatic name for deleting files in unix
else:
    print("The file can not be removed as it does not exist")

# doesn't need full path, uses cwd (current working directory) or provide full path
os.path.isfile(fullsourcepath)   # bool
os.path.isdir(fullsourcepath)    # bool
os.path.exists(fullsourcepath)   # This returns true if fullpath is either a file or a directory

# join two or more paths with .join
os.path.join(r'C:\temp\s1', r'home\sub', r'x\y')   # 'C:\\temp\\s1\\home\\sub\\x\\y'


os.path.splitext(r'C:\temp\s1\filename.ext')   #  ('C:\\temp\\s1\\filename', '.ext')
os.path.split(r'C:\temp\s1\filename.ext')     #   ('C:\\temp\\s1', 'filename.ext')
# ======================================================================================================================
# shutil module:
# https://www.geeksforgeeks.org/shutil-module-in-python/
# https://docs.python.org/3/library/shutil.html
# Note:  don't think there is a built-in os function that copies files, would have to do an open() command for 'r' & 'w'
# ======================================================================================================================
# import shutil (built-in module)
# paths can be path-like objects or strings
# shutil.copyfile(src, dst, *, follow_symlinks=True)  # Copy data from src to dst in the most efficient way possible.
# shutil.copy(src, dst, *, follow_symlinks=True)      # Copies the file src to the file or directory dst. src=path to single file,  dst can be a full file_path or directory, also copies file permissions
# shutil.copy2(src, dst, *, follow_symlinks=True)     # Identical to copy() except that copy2() also attempts to preserve file metadata.
# shutil.copyfileobj(fsrc, fdst[, length])            # Copy the contents of the file-like object fsrc to the file-like object fdst.
# shutil.copymode(src, dst, *, follow_symlinks=True)  # Copy the permission bits from src to dst. The file contents, owner, and group are unaffected. src and dst are path-like objects or path names given as strings.
# shutil.copystat(src, dst, *, follow_symlinks=True)  # Copy the permission bits, last access time, last modification time, and flags from src to dst. On Linux, copystat() also copies the “extended attributes” where possible.
# shutil.ignore_patterns(*patterns)                   # This factory function creates a function that can be used as a callable for copytree()'s ignore argument, ignoring files and directories that match one of the glob-style patterns provided. See the example below.
# shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)  # Recursively copy an entire directory tree rooted at src to a directory named dst and return the destination directory. All intermediate directories needed to contain dst will also be created by default.
# shutil.rmtree(path, ignore_errors=False, onerror=None, *, onexc=None, dir_fd=None)  # Delete an entire directory tree; path must point to a directory (but not a symbolic link to a directory).
# shutil.move(src, dst, copy_function=copy2)   # Recursively move a file or directory (src) to another location (dst) and return the destination. # advantage over rename is that it doesn't throw exceptions
# shutil.disk_usage(path)                      # Return disk usage statistics about the given path as a named tuple with the attributes total, used and free, which are the amount of total, used and free space, in bytes. path may be a file or a directory.
# shutil.chown(path, user=None, group=None)    # Change owner user and/or group of the given path.
# shutil.which(cmd, mode=os.F_OK | os.X_OK, path=None)   # Return the path to an executable which would be run if the given cmd was called. If no cmd would be called, return None.
# shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])  # Create an archive file (such as zip or tar) and return its name.
# shutil.get_archive_formats()  # Return a list of supported formats for archiving. Each element of the returned sequence is a tuple (name, description).
# shutil.register_archive_format(name, function[, extra_args[, description]])   # Register an archiver for the format name.
# shutil.register_archive_format(name, function[, extra_args[, description]])   # Register an archiver for the format name.
# shutil.register_unpack_format(name, extensions, function[, extra_args[, description]])  # Registers an unpack format. name is the name of the format and extensions is a list of extensions corresponding to the format, like .zip for Zip files.
# shutil.unregister_unpack_format(name)  # Unregister an unpack format. name is the name of the format.
# shutil.get_unpack_formats()  # Return a list of all registered formats for unpacking. Each element of the returned sequence is a tuple (name, extensions, description)
# shutil.get_terminal_size(fallback=(columns, lines))  # Get the size of the terminal window.

# ┌──────────────────┬───────────────┬──────────────────┬──────────────┬───────────┐
# │     Function     │Copies metadata│Copies permissions│Can use buffer│Dest dir OK│
# ├──────────────────┼───────────────┼──────────────────┼──────────────┼───────────┤
# │shutil.copy       │      No       │        Yes       │    No        │    Yes    │
# │shutil.copy2      │      Yes      │        Yes       │    No        │    Yes    │
# │shutil.copyfile   │      No       │        No        │    No        │    No     │
# │shutil.copyfileobj│      No       │        No        │    Yes       │    No     │
# └──────────────────┴───────────────┴──────────────────┴──────────────┴───────────┘


# ======================================================================================================================
# 'pathlib' from the standard library  see https://docs.python.org/3/library/pathlib.html
# ======================================================================================================================
# https://realpython.com/python-pathlib/
# 'Path' is platform agnostic.  Will be WindowsPath only on windows and PosixPath on unix platforms
# ============================================================================================================
from pathlib import Path # stores full Path Object (for all platforms - not just windows) 
wp = Path.home() # WindowsPath('C:/Users/obezalely')  <class 'pathlib.WindowsPath'> 
wp = Path.cwd()  # WindowsPath('C:/Users/obezalely/OneDrive/PYTHON') <class 'pathlib.WindowsPath'>

# can use the windowsPath with standard functions but will return strings not Path object e.g.
os.walk(wp)
os.path.exists(wp)
os.path.join(wp, 'file.txt')


fp = Path(__file__)  # file path to this file  i.e 'C:\...\bezpy_05_files.py'
fp = Path(r'.\myfiles\subfolder\input.txt')        # WindowsPath('myfiles/subfolder/input.txt')
fp = Path('myfiles', 'subfolder', 'input.txt')     # As above

fp                      # returns WindowsPath('myfiles/subfolder/input.txt')
fp.is_absolute()        # returns False, path is a relative path
fp.absolute()           # returns WindowsPath('C:/Oren/06 Computing/06 25 Python/myfiles/subfolder/input.txt')


fp.parent               # returns WindowsPath('myfiles/subfolder'), parent directory
fp.parents[0]           # returns WindowsPath('myfiles/subfolder'), parent directory
fp.parents[1]           # returns WindowsPath('myfiles'), 2-directories up
fp.is_dir()             # returns bool
fp.is_file()            # returns bool
fp.exists()             # returns bool
# fp.mkdir()            # creates dir with the file path
# fp.relative_to(fp2)   # returns a patial path from fp2 parent onwards
fp.home()               # returns home path WindowsPath('C:/Users/orenb')
fp.cwd()                # returns current working directory
fp.name                 # returns 'input.txt'
fp.with_name('new.txt') # returns path with replaced name
fp.stem                 # returns 'input'
#fp.with_stem('new')    # returns path with replaced stem  New in version 3.9.
fp.suffix               # returns '.txt'
fp.suffixes             # will return A list of the path’s file extensions:  e.g. xxx.tar.gz -> ['tar', 'gz']
fp.with_suffix('.py')   # returns path and replaces suffix to .py
fp.with_suffix('')      # returns path and removes suffix
fp.as_posix()           # 'C:/Users/obezalely/OneDrive/PYTHON/myfiles/input.txt'  Returns a string representation of the path with forward slashes (/):
str(fp)                 # 'C:/Users/obezalely/OneDrive/PYTHON/myfiles/input.txt'
fp.parts                # Returns tuple e.g. ('myfiles', 'subfolder', 'input.txt')
'.'.join(fp.with_suffix('').parts)  # Converts filepath to dot notation

fp.read_text()                  #  Open -> Read -> Close
fp.read_bytes()                 #  Open in bytes -> Read -> Close
fp.write_text('hello')          #  Open -> Write -> Close  write_text(data, encoding=None, errors=None)
fp.write_bytes(b'\x48\x09\x40') #  open in bytes mode -> write -> close write_bytes(data)
f = fp.open(mode='w', buffering=-1, encoding=None, errors=None, newline=None)    # returns a regular file object
f.write('hello')
f.close()

fp = Path('C:/Oren/06 Computing/06 25 Python/myfiles/subfolder/input.txt')
fp.as_uri()   # returns 'file:///C:/Oren/06%20Computing/06%2025%20Python/myfiles/subfolder/input.txt', Only works for abosolute paths,


# Forward slash operator joins paths
fp = Path.home() / 'subdir' / 'newfile.txt' # WindowsPath('C:/.../subdir/newfile.txt')
fp = Path.home().joinpath('subdir', 'newfile.txt') # same as above
parent_dir = Path(__file__).parent    # parent of executing file  i.e.  /c/github
fp = Path(parent_dir / '..' / 'subdir')   # up one more dir and down to subdir i.e.  /c/subdir


Path(r'.\myfiles\touched.txt').touch()  # creates empty file

dirpath = Path(r'.\myfiles')
dirpath.iterdir()  # generator object of all files and subdirectories in dirpath (not recursively)
files0 = [f for f in dirpath.iterdir() if f.is_file()]  # list of path objects in dirpath (not recursively)
files1 = list(dirpath.glob("*.*"))       # Same as above
files2 = list(dirpath.glob("*.txt"))     # glob doesn't seem to take regex
files3 = list(dirpath.glob("**/*.txt"))  # all subdirectories
files4 = list(dirpath.rglob("*.txt"))    # recursive glob

# for unix
dirpath.resolve() # resolves sym links and eliminates .. components

# return the newest file in a directory
sorted(dirpath.iterdir(), key=os.path.getmtime)[-1]   # WindowsPath('myfiles/touched.txt')



# ============================================================================================================
# 'pathlib2' requires pip install pathlib2
# ============================================================================================================
# The goal of pathlib2 is to provide a backport of standard pathlib module which tracks the standard library module, 
# so all the newest features of the standard pathlib can be used also on older Python versions
# 
# 

# ============================================================================================================
# tempfile from the standard library
# ============================================================================================================
import tempfile
tempfile.gettempdir()    # returns the temp directory  'C:\\Users\\orenb\\AppData\\Local\\Temp'
tempfile.gettempdirb()   # returns the temp directory as byte string  b'C:\\Users\\orenb\\AppData\\Local\\Temp'

tempfile.gettempprefix()   # returns The default prefix for temporary directories as string. i.e. tmp
tempfile.gettempprefixb()

file = tempfile.TemporaryFile(dir='./')          # creates a temporary file in cwd, obj returned is a bytestream file object with a wrapper
file = tempfile.TemporaryFile()                  # creates a temporary file in the os temp directory
file = tempfile.TemporaryFile(delete=False)      # creates a temporary file which doesn't auto delete on close

# treat file as if you have opened a file stream with  `file = open(tmp_file_name, 'wb')`  all the FILE operators will work
file.write(b'hello world')
file.seek(0)   #  e.t.c.


file.name            # File Path: 'C:\\Users\\orenb\\AppData\\Local\\Temp\\tmpg0qwhxi2'
file.delete          # Delete attribute (bool) determines if auto delete on close
file.close()         # Close file

# NamedTemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True, *, errors=None)
named_file = tempfile.NamedTemporaryFile(prefix='xxx-', suffix='-zzz')  # you can control prefix & suffix
named_file.name                                # C:\\Users\\orenb\\AppData\\Local\\Temp\\xxx-kmxsn285-zzz
named_file.close()                             # Close file

sp_file = tempfile.SpooledTemporaryFile(max_size=10)  # Creating a temporary file to spool data into it
sp_file.close()

# TemporaryDirectory(suffix=None, prefix=None, dir=None)      # create a temporary directory object, must explicitly cleanup
temp_dir = tempfile.TemporaryDirectory()      # create a temporary directory
temp_dir.name         # e.g. 'C:\\Users\\orenb\\AppData\\Local\\Temp\\tmppg9b8_wx'
temp_dir.cleanup()    # deletes directory and contents

with tempfile.TemporaryDirectory() as temp_dir:  # this will invoke 'cleanup' on exit of context
     assert isinstance(temp_dir, str)   # within context manager,  temp_dir is a string not an object

# tempfile.mkdtemp(suffix=None, prefix=None, dir=None)      # create a temporary directory, but returns string, not directory object
temp_dir = tempfile.mkdtemp()   # returns directory path as string
os.rmdir(temp_dir)              # requires explicit removal - no cleanup method

# ============================================================================================================
# FILE SECURE TRANSFER - see bezpy_29_sftp.py
# ============================================================================================================

# ============================================================================================================
# ftplib module from the standard library for regular file transfer
# ============================================================================================================
from ftplib import FTP

def download(filename):
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    localfile.close()

def upload(filename):
    x = open(filename, 'rb')
    ftp.storbinary('STOR ' + filename, x)
    x.close()

try:
    ftp = FTP('ftp.bezalely.net')
    ftp.login(user='bezalely', passwd = 'Mashad$100')
except:
    print('Exit Program: Login failure')
    sys.exit(1)

os.chdir('myfiles')
ftp.cwd('//public_html//pytemp//')
upload('input.txt')  # os.getcwd() is the correct value so do not need path
ftp.quit()
print('FTP Successful')

# =====  USING GLOB WITH WILDCARDS--------------

# Without glob
import os
os.chdir('..')
file_paths = os.listdir("myfiles/")

jpgs = []
for file_path in file_paths:
  if file_path.endswith(".jpeg"):
    jpgs.append(file_path)

# With glob
from glob import glob
jpgs = glob("myfiles/*.jpg")        # returns list of jpegs  - USE WILD CARDS  '*' or '?' or [0-9]

# When recursive is set True, “**” followed by path separator('./**/') will match any files or directories.
glob('/home/geeks/Desktop/gfg/**/*.txt', recursive=True)  # matches all text files below /home/geeks/Desktop/gfg/


#  also  glob.iglob()  returns iterator instead of list


# sys.getdefaultencoding() returns the default encoding

def is_binary(file):
    '''Tests first char of file to see if it is binary'''
    TEXT_CHARS = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
    f = open(file, 'r')
    first_char = f.read(1)
    f.close()
    if bytes(first_char, 'utf-8') not in TEXT_CHARS:
        return True
    else:
        return False

# ======================================================================================================================
# The fileinput module from the standard library
# Used to iIterate over lines from multiple input streams
# https://docs.python.org/3/library/fileinput.html
# FileInput(files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)
# If an I/O error occurs during opening or reading a file, the IOError exception is raised
# ======================================================================================================================
import fileinput

for line in fileinput.input(files=r'.\myfiles\fileinput_test.txt', encoding="utf-8"):  # encoding parameter did not exist in previous versions
    print(line, end='')
# line1
# line2

for line in fileinput.input(files =('file1.txt', 'file2.txt')):
    print(line)   # will loop through multiple files


with fileinput.FileInput('file1.txt', inplace=True, backup='.bak') as f:
    for line in f:
        if f.isfirstline():
            print("FIRST LINE REPLACED\n", end='')
        else:
            print(line, end='')

# readline(self)
# filelineno(self)   - returns the line number in the current file
# filename(self)     - returns the filename of the line that has just been read (as str)
# fileno(self)       - returns
# isfirstline(self)  - returns True if the line just read is the first line of its file
# isstdin(self)      - returns True if the line was read from sys.stdin
# lineno(self)       - retruns the cumulative line number of the line that has just been read
# nextfile(self)     - close the current file so that the next iteration will read the first line from the next file,
#                    - Note: lines not read from the file will not count towards the cumulative line count;
#                    -       the filename is not changed until after the first line of the next file has been read.
# close(self)        - closes the sequence




# ======================================================================================================================
# io module from the standard library
# https://docs.python.org/3/library/io.html
# ======================================================================================================================
import io
f = io.StringIO("")  # creates empty text stream, initial cursor on the file starts at zero
f = io.StringIO("This is an in-memory text stream.")  # creates an initialized text stream initial cursor on the file starts at zero
f.read()     # reads the file from where pointer is and moves pointer to the end of the stream
f.write(" Welcome.")    # writes from where the pointer is.
f.seek(0)   # reset index to zero
f.getvalue()  # returns contents of the file irrespective of where the pointer is
f.isatty()       # This function Return True if the stream is interactive and False if the stream not is interactive
f.readable()     # This function return True if the file is readable and returns False if file is not readable.
f.writable()     # This function return True if the file supports writing and returns False if file does not support writing.
f.seekable()     # This function return True if the file supports random access and returns False if file does not support random access.
f.closed         #  This function return True if the file is closed and returns False if file is open.
f.close()        # close the file stream

# ======================================================================================================================
# linecache module form the standard library, provides a caching mechanism for line-oriented files
# https://docs.python.org/3/library/linecache.html
# ======================================================================================================================
import linecache
gfg = linecache.getline(r'.\myfiles\file.txt', 3)  # retrieve line 3 from the file

# 'filecmp' module from the standard library  provides a file comparison function.


# ======================================================================================================================
# Unix Groups - grp is part of standard library
# ======================================================================================================================
# import grp
# grp.getgrgid(4)  # returns info for 4th group from `getent group`
# grp.getgrnam('<unix-group-name>')  # returns info for specific group
# grp.getgrall()  # returns info for all groups

# INFO RETURNED:
# 0	gr_name	the name of the group
# 1	gr_passwd	the (encrypted) group password; often empty
# 2	gr_gid	the numerical group ID
# 3	gr_mem	all the group member’s user names