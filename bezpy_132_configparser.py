# The configparser module from Python's standard library defines functionality 
# for reading and writing configuration files as used by Microsoft Windows OS. 
# Such files usually have .INI extension.
# The INI file consists of sections, each led by a [section] header. 
# Between square brackets, we can put the section’s name. 
# Section is followed by key/value entries separated by = or : character. 
# It may include comments, prefixed by # or ; symbol. 
# 
# A sample INI file is shown below −

"""
 # this is a comment, put on seperate line
 ; this too is a comment, put on seperate line
[Section1]  # this also works 
key1:value1   
key2=value2  

[Settings]
StatusPort=6090
StatusRefresh=10

[FTP]
UserName=admin
Password=admin
"""

import configparser   # standard library

parser = configparser.ConfigParser()
parser.read(r'.\myfiles\test.ini')

parser.sections()             # ['Section1', 'Section2', 'Settings', 'FTP']
parser.options('Section1')    # ['key1', 'key2', 'key3']
parser.items('Section1')      # [('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]
parser['Section2']            # Section Object with dict type operations 'clear' 'getboolean', 'getfloat' 'getint'  'items' 'keys' 'name' 'parser' 'pop' 'popitem' 'setdefault' 'update' 'values'

parser.getboolean('Section2', 'BoolKey1')   # True
parser.getboolean('Section2', 'BoolKey2')   # False
parser.get('Section2', 'StringKey')         # 'this is my string'
parser.getint('Section2', 'IntKey')         # 42
parser.getfloat('Section2', 'IntKey')       # 42.0
parser.getfloat('Section2', 'FloatKey')     # 3.14
# parser.getint('Section2', 'FloatKey')     # ValueError: 


# Create ini file
parser = configparser.ConfigParser()
parser.add_section('Manager')
parser.set('Manager', 'Name', 'Ashok Kulkarni')
parser.set('Manager', 'email', 'ashok@gmail.com')

parser.has_section('Director')         # False - no such section
parser.has_option('Manager', 'Name')   # True - this option exists


fp = open(r'.\myfiles\test2.ini', 'w')
parser.write(fp)
fp.close()

# ======================================================================================================================
# ConfigParser Methods
# ======================================================================================================================
# sections()	    Return all the configuration section names.
# options()	        Return list of configuration options for the named section.
# items()	        return a list of tuples with (name, value) for each option in the section.

# has_section()	    Return whether the given section exists.
# has_option()	    Return whether the given option (section + item) exists in the given section.


# read()	        Read and parse the named configuration file.
# read_file()	    Read and parse one configuration file, given as a file object.
# read_string()	    Read configuration from a given string.
# read_dict()	    Read configuration from a dictionary. Keys are section names, values are dictionaries with keys and values that should be present in the section.

# get()	            Return a string value for the named option.
# getint()	        Like get(), but convert value to an integer.
# getfloat()	    Like get(), but convert value to a float.
# getboolean()	    Like get(), but convert value to a boolean. Returns False or True.

# remove_section()	Remove the given file section and all its options.
# remove_option()	Remove the given option from the given section.
# set()	            Set the given option.
# write()	        Write the configuration state in .ini format.
