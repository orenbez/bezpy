# Try this: https://medium.com/better-programming/avoid-these-5-mistakes-when-handling-exceptions-in-python-645f0ce92c92
# Function Arguments, Error Handling, Command line Agruments, 'global' keyword, 'nonlocal' keyword,
# Recursive Vs Iterative, Environment Variables, XML

import sys
import os
from mylib.mymisc import boo      # function boo() will print an output marker to screen


#  when importing this file as a module, __name__ takes the value of the module name, else __name__='__main__'
if __name__ == '__main__':
    print("this will only print when you run 'bezpy_02_exceptions.py' as a script")


# ======================================================================================================================
# POSITIONAL vs KEYWORD 
# ======================================================================================================================
def pet_name(name, pet):
    print('my pet', name, 'is a', pet)

pet_name('fred', 'dog')            # positional arguments
pet_name(name='fred', pet='dog')   # keyword arguments
pet_name(pet='dog',name='fred')    # keyword arguments don't have to be ordered
#  pet_name(name='fred', 'dog')    # positional arguments can not follow keyword arguments

# ======================================================================================================================
# operators '/' to distinguish positional only parameters that come before '/'  i.e. a & b
# operators '*' to distinguish keyword only parameters that follow '*' (introduced in python 3.8)  i.e. e & f
# the function definition will confirm the 'signature' of the function.  i.e. the correct number / type of parameters
# ======================================================================================================================
def f1(p1, p2, /):  # only accepts positional arguments
    pass


def f2(*, k1, k2):  # only accepts keyword arguments
    pass


def f3(p1, p2, /, a1, *, k1, k2):    # a1 can be positional or keyword
    pass

def my_func(a, b, /, c, d, *, e, f):   # c & d have no restrictions, except a positional arg can not follow keyword arg
    return a+b+c+d+e+f

# my_func(1, 2, 3, 4, 5, 6)           # invalid as e and f are keyword-only
# my_func(a=1, b=2, 3, 4, e=5, f=6)   # invalid as a and b are position-only
# my_func(1, 2, c=3, 4, e=5, f=6)     # SyntaxError: positional argument follows keyword argument
my_func(1, 2, c=3, d=4, e=5, f=6)     # returns 21
my_func(1, 2, 3, d=4, e=5, f=6)       # returns 21


# ======================================================================================================================
# DEFUALT VALUES vs  OPTIONAL ARGUMENTS  (MUST BE AT END)
# ======================================================================================================================
def pet_name2(name, pet='dog', height=14, color=None):
    print('my pet', name, 'is a', pet)
    print('who is', height, 'inches tall')
    if color:  # equivalent to ..... if color != None
        print(name, 'is', color)

pet_name2('fred')  # defaults to dog, 14 inches
pet_name2('pete', 'cat', )  # defaults to cat, 14 inches
pet_name2('henry','monkey',24)
pet_name2('rover','rabit',7, 'white')

# default parameters are created only once on startup when function definition is read, not every time on execution
# So be careful when using mutable values as defaults.  The function will remember the value for each call
def mutable_default(val=[]):
    val.append(1)
    print(val)

mutable_default([7,3,4])  # [7, 3, 4, 1]
mutable_default()         # [1]
mutable_default()         # [1, 1]
mutable_default()         # [1, 1, 1]

def alt_default(val=None):
    if not val:
        val = []
    val.append(1)
    print(val)

def alt2_default(val=tuple()):
    val = list(val)
    val.append(1)
    print(val)


# ======================================================================================================================
# arbitrary number of arguments
# ======================================================================================================================
def mypets(animal, *names):
    print(f"these are my {animal}'s  names: ")
    assert isinstance(names, tuple)  # 'names' is treated now as an ordinary tuple
    for x in names:
        print (x)
mypets('hamsters', 'peanut')
mypets('dogs', 'fred', 'rover', 'butch')

# would also work without packing but not as clear
def mypets2(animal, name_tuple):
    print(f"these are my {animal}'s  names: ")
    for x in name_tuple: #'names' is treated now as an ordinary tuple
        print (x)

# ======================================================================================================================
# arbitrary number of keyword arguments (used for dictionaries)
# ======================================================================================================================
def createdict(name, **animals):
    mydict = {'owner':name}
    assert isinstance(animals, dict)  # 'animals' is treated now as an ordinary dict
    print (animals)
    mydict |= animals
    return mydict

x = createdict('oren', hamster='peanut', dog='rover')  # {'owner': 'oren', 'hamster': 'peanut', 'dog': 'rover'}
y = createdict ('elon', elephant='eli')  # {'owner': 'elon', 'elephant': 'eli'}


def args_test(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))

args_test('arg1', 'arg2', 'arg3', k1='v1', k2='v2', k3='v3')
## RETURNS:
# ('arg1', 'arg2', 'arg3') <class 'tuple'>
# {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'} <class 'dict'>    

x = ('arg1','arg2','arg3')
y = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
args_test(*x, **y)
# RETURNS SAME AS ABOVE


# ======================================================================================================================
# RECURSIVE VS ITERATIVE FUNCTION EXAMPLE
# ======================================================================================================================
# Fibonacci Sequence starting with 1,1, =  1,1,2,3,5,8,13
# fib(n) = fib(n-1) + fib(n-2)
# fib(1) = 1
# fib(2) = 1
# ======================================================================================================================
def fib(n):
    """ returns the nth element of the sequence """
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    """ returns the nth element of the sequence """    
    if n == 1 or n == 2:
        return 1
    else: 
        x = [1,1]
        for i in range(1,n-1):
            x.append(x[i] + x[i-1])
        return x[-1]

print(fib(15), fib2(15))

# ======================================================================================================================
# ERROR HANDLING - safer to specify the exception.  'except:' will catch-all-exceptions
#                  running with the try / except clause will explicitly display your error to screen
# ======================================================================================================================
# FULL LIST OF EXCEPTIONS/ERRORS: https://docs.python.org/3/library/exceptions.html  (bottom of page)

num_tickets = 3
#num_tickets = input("How many tickets do you need? ")
try:
    num_tickets = int(num_tickets)
except ValueError: # "except:" will catch all errors and NOT stop
    print("Entry invalid, please try again.") # if you entered a char instead.
else:  # the try was successful. Better to reduce the content in 'try' and move it to here. You can even
       # return a value here and the 'finally clause will still be executed afterwards
    print('this is printed only if success')
finally:
    print('this will always get printed')
    # if the 'try' fails,  'finally' will be executed before the exception is handled
    # if the 'try' passes, 'finally' will be executed after the 'else' statement
    # Note as of python 3.8: 'continue' can now be used in the finally clause (not sure why I would use it!!)

# ======================================================================================================================
# 'try' & 'finally' combination. Will not handle the exception, only allows 'finally' to perform before failing
# ======================================================================================================================
# all exceptions will fail silently and the finally will execute in all scenarios
# try:
#     Database Query
# finally:   # <---- will execute in all scenarios, even if the try is successful
#     Close database connections


# ======================================================================================================================
# 'try' 'except' 'finally' combination
# ======================================================================================================================
# this generates runtime error but will print out the 'finally' statement BEFORE stopping
# try:
#     x = 5/0
# except ZeroDivisionError:     # <---- will only execute on a failed 'try'
#     raise ZeroDivisionError
# finally:
#    print('PROGRAM STOPPED BECAUSE OF ZeroDivisionError')    # <---- this will print before error is raised


# ======================================================================================================================
# 'try' & 'except' combination
# ======================================================================================================================
path = r'C:\OrenDocs\no-such-path\output1.txt'
try:
    file_obj = open(path, 'w') #the file path doesn't exist
except FileNotFoundError:
    print(f'{path} is not there!!!!!') # this will fail silently

try:
    file_obj = open(r'C:\OrenDocs\no-such-path\output1.txt', 'w')   # the file path doesn't exist
except Exception as e:
    print(e, type(e))  # [Errno 2] No such file or directory: 'C:\\OrenDocs\\no-such-path\\output1.txt' <class 'FileNotFoundError'>


# Note errno constants from the standard library
# https://docs.python.org/3/library/errno.html

# Log exception first
number = 0
# try:
#     3/number
# except Exception as e:
#     logging.error()  or logging.exception(f'EXCEPTION OCCURED {e}')
#     raise e   #  will raise exception "ZeroDivisionError: division by zero" only after logging is performed

#  e.args     # ('division by zero',)
#  e.args[0]  # 'division by zero'


# try:
#     3/number
# except ZeroDivisionError:
#     raise ZeroDivisionError(f'You can not divide by {number}')   # allows for personalized message

# Custom Made Exception
class InvalidDataError(Exception):
    pass

# try:
#     3/number
# except Exception as e:
#     raise InvalidDataError from e    # this sets the e.__cause__ value
#     raise InvalidDataError("exception message goes here")    # InvalidDataError: exception message goes here

# except (Exception1, Exception2) as e    # you can combine check for multiple exceptions


# ======================================================================================================================
class DataError(Exception):
    def __init__(self, missing):
        self.missing = missing

#raise DataError('data is missing')   # DataError: data is missing


# class MyException(Exception):
#    __note__ = 'this is my note'  # as of 3.11 the 'BaseException' class has a class attribute __note__

# raise MyException('exception message') # MyException: exception message
# From 3.11 can use 'ExceptionGroup'  to raise multiple exceptions at once see https://peps.python.org/pep-0654/
# and new keyword 'except*' to handle them


# ======================================================================================================================
# EAFP (Easier to Ask Forgiveness than Permission)  vs.  LBYL (Look Before Your Leap)
# ======================================================================================================================
def eafp_divide_ten_by(number):
    try:
        print(f'10 divided by {number} is {10 / number}.')
    except ZeroDivisionError:
        print("You can't divide zero.")
    except TypeError:
        print("You can only divide a number.")
    except Exception as e:  # Catch any other exception
        print(e, type(e))

def lbyl_divide_ten_by(number):
    if isinstance(number, int) or isinstance(number, float):
        if number == 0:
            print("You can't divide zero.")
        else:
            print(f'10 divided by {number} is {10 / number}.')
    else:
        print("You can only divide a number.")


# To return all subclasses of the BaseException class
BaseException.__subclasses__()  #  [Exception, GeneratorExit, SystemExit, KeyboardInterrupt, exceptiongroup.BaseExceptionGroup, asyncio.exceptions.CancelledError]

# To return all subclasses of the Exception class
Exception.__subclasses__()  #  [<class 'TypeError'>, <class 'StopAsyncIteration'>, <class 'StopIteration'>, <class 'ImportError'>, <class 'OSError'>, <class 'EOFError'>, <class 'RuntimeError'>, <class 'NameError'>, <class 'AttributeError'>, <class 'SyntaxError'>, <class 'LookupError'>, <class 'ValueError'>, <class 'AssertionError'>, <class 'ArithmeticError'>, <class 'SystemError'>, <class 'ReferenceError'>, <class 'MemoryError'>, <class 'BufferError'>, <class 'Warning'>, <class '_pydev_bundle._pydev_getopt.GetoptError'>, <class 'socket._GiveupOnSendfile'>, <class 're.error'>, <class 'sre_parse.Verbose'>, <class 'locale.Error'>, <class 'tokenize.TokenError'>, <class 'tokenize.StopTokenizing'>, <class 'copy.Error'>, <class 'warnings._OptionError'>, <class 'inspect.ClassFoundException'>, <class 'inspect.EndOfBlock'>, <class '_shaded_ply.lex.LexError'>, <class 'struct.error'>, <class 'binascii.Incomplete'>, <class '_shaded_ply.yacc.YaccError'>, <class '_shaded_thriftpy.parser.exc.ThriftParserError'>, <class 'subprocess.SubprocessError'>, <class '_shaded_thriftpy.thrift.TException'>, <class '_queue.Empty'>, <class 'queue.Full'>, <class 'email.errors.MessageError'>, <class 'uu.Error'>, <class 'http.client.HTTPException'>, <class 'xml.parsers.expat.ExpatError'>, <class 'zlib.error'>, <class 'xmlrpc.client.Error'>, <class '_lzma.LZMAError'>, <class 'shutil.RegistryError'>, <class 'shutil._GiveupOnFastCopy'>, <class 'pydoc.ErrorDuringImport'>, <class 'ctypes.ArgumentError'>, <class '_ctypes.COMError'>, <class '_pydevd_bundle.pydevd_resolver.UnableToResolveVariableException'>, <class '_pickle.PickleError'>, <class 'pickle._Stop'>, <class 'zipfile.BadZipFile'>, <class 'zipfile.LargeZipFile'>, <class 'pkg_resources._vendor.backports.tarfile.TarError'>, <class 'pkg_resources.extern.packaging._tokenizer.ParserSyntaxError'>, <class 'pkg_resources.ResolutionError'>, <class '_pydevd_bundle.pydevd_vars.ExceedingArrayDimensionsException'>]
[x.__name__ for x in Exception.__subclasses__()]   # ['TypeError', 'StopAsyncIteration', 'StopIteration', 'ImportError', 'OSError', 'EOFError', 'RuntimeError', 'NameError', 'AttributeError', 'SyntaxError', 'LookupError', 'ValueError', 'AssertionError', 'ArithmeticError', 'SystemError', 'ReferenceError', 'MemoryError', 'BufferError', 'Warning', 'GetoptError', '_GiveupOnSendfile', 'error', 'Verbose', 'Error', 'TokenError', 'StopTokenizing', 'Error', '_OptionError', 'ClassFoundException', 'EndOfBlock', 'LexError', 'error', 'Incomplete', 'YaccError', 'ThriftParserError', 'SubprocessError', 'TException', 'Empty', 'Full', 'MessageError', 'Error', 'HTTPException', 'ExpatError', 'error', 'Error', 'LZMAError', 'RegistryError', '_GiveupOnFastCopy', 'ErrorDuringImport', 'ArgumentError', 'COMError', 'UnableToResolveVariableException', 'PickleError', '_Stop', 'BadZipFile', 'LargeZipFile', 'TarError', 'ParserSyntaxError', 'ResolutionError', 'ExceedingArrayDimensionsException']
[x.__name__ for x in ArithmeticError.__subclasses__()]   # ['FloatingPointError', 'OverflowError', 'ZeroDivisionError', 'DecimalException']



# ======================================================================================================================
# 'raise' & 'assert' keywords
# ======================================================================================================================

a = 4  # the 'assert' keyword is used for debugging - checking conditions
       # "assert a == 5 " raises an 'AssertionError:' if condition is False 
assert a == 4  , "this will be the error message that displays after 'AssertionError:"

# you can also use the 'raise' keyword for which an error of your choice is raised if the condition is True
if a == 5:
    raise AssertionError('your condition is True')
# raise Exception('message')   # this is a generic exception

# >>> __debug__   # this returns True,  when running with flag  `python -O yourscript.py`  __debug__ returns False and
#                 # the assert lines are ignored


# ======================================================================================================================
# Modified 'mutable' objects will keep their original id, but 'immutable' objects will be re-assigned another id
#   so passing a mutable object as an argument will always be 'Pass by Reference', unless you pass a copy
# ======================================================================================================================
def change_mutable(x=[]):
    x.append(5)
    print(x, id(x))

my_list = [1,2,3,4]
print(my_list, id(my_list))
change_mutable(my_list)     # Passes the actual list by reference, Id is maintained.
print(my_list, id(my_list))
change_mutable(my_list[:])  # This passes a copy, NEW id is assigned
print(my_list, id(my_list))
change_mutable()    # The argument is missing, will default to an empty list


# General Scope rule for functions in python LEGB (Local, Enclosing, Global and Built-in)
# 1) Local Scope is checked first
# 2) Enclosing Scope (for nested functions)
# 3) Global Scope
# 4) Built-in Scope (loaded when an interpreter is launched, e.g. print function)

# ======================================================================================================================
# For immutable objects, NEED the 'global' keyword to 'Pass by Reference' so as to modify the actual global value
# Note: technically a global variable needs only be declared in a function if the function is MODIFYING the value,
#      to simply ACCESS the value it is not necessary to identify as global in that function
# ======================================================================================================================
def p1():  # WARNING You can't pass the parameter to the function with p(x) as it will give error since you declared variable as global
    global x  # not required if you are just accessing the variable
    print(x)
    x = 7   # declared  global since you are modifying a variable defined in the global namespace

x = 5
p1()
print(x)
# Output
# 5
# 7


# ============================================================================================================
# Immutable object Access only   PASS BY VALUE  does not require global declaration
# ============================================================================================================
def p2():
    print(x)  # will access the global value for read only, can not reassign. doesn't require 'global' declaration

x = 5
p2()
print(x)
# Output
# 5

# ============================================================================================================
# Immutable object PASS BY VALUE  will not modify the original x in the global scope
# ============================================================================================================
def p3(z):
    z = z + 2
    
x = 5
print(x)
p3(x)
print(x)
# Output
# 5
# 5

# =====================================================================
#  Mutable objects get modified when passed   PASS BY REFERENCE
# =====================================================================
def p4(z):
    z.append(9)
    
x = [5]
print(x)
p4(x)
print(x)
# Output
# [5]
# [5, 9]

# ========================================================================================
#  Mutable objects don't even need to be passed don't need global declaration to be modified
# ========================================================================================
def p5():
    x.append(9)
    
x = [5]
print(x)
p5()
print(x)
# Output same as above
#[5]
#[5, 9]

# ============================================================================================================
def f1(): # prints the current value in the global scope (Access allowed without 'global' declaration)
    print('id(gl): ',id(gl), '; Value:', gl)  # gl has the same id as you have accessed the global scope value

def f2(): # prints the locally defined value - does not modify the value in the global scope
    gl = 200  # this 'gl' has a new id, but only for the local scope
    print('id(gl): ',id(gl), '; Value:', gl)

def f3():
    global gl   # this will give the function access to MODIFY the already existing global
    gl = 300    # since you are reassigning a global immutable object the id changes at this line.
    global gl2  # from this line onwards gl2 can be accessed globally too, not defined until now
    gl2 = 400
    print('id(gl2):',id(gl2), '; Value:', gl2) 

def f4(): # prints the current value in the global scope
    print('id(gl2):',id(gl2), '; Value:', gl2) 

def f5(gl3): # prints the locally defined value
    gl3 = gl3 + 1 # does not modify the value in the global scope 
    print('id(gl3): ',id(gl3), '; Value:', gl3)

gl = 100 # Assigned in the Global scope, automatically has global access
print('id(gl): ',id(gl), '; Value:', gl)
      # id(gl):  1271084242384 ; Value: 100
f1()  # id(gl):  1271084242384 ; Value: 100
f2()  # id(gl):  1271084245648 ; Value: 200
f1()  # id(gl):  1271084242384 ; Value: 100
f3()  # id(gl2): 1271141210992 ; Value: 400
f1()  # id(gl):  1271141210000 ; Value: 300
f4()  # id(gl2): 1271141210992 ; Value: 400

gl3 = 300  # Assigned in the Global scope, automatically has global access
print('id(gl3): ',id(gl3), '; Value:', gl3)  # id(gl3):  1271141210000 ; Value: 300
f5(gl3)                                      # id(gl3):  1271141211888 ; Value: 301
print('id(gl3): ',id(gl3), '; Value:', gl3)  # id(gl3):  1271141210000 ; Value: 300

# ======================================================================================================================
# using the 'nonlocal' keyword is similar to 'global' but used for nested functions 
# ======================================================================================================================
def outer_function():  # outer or enclosing function
    a = 500
    b = 600
    def inner_function():  # inner or nested function
        nonlocal a  # now we can modify 'a' for the scope of the outer function - only works for NESTED function
        global b    # this doesn't help within the scope of the outer function - only the global scope
        a = 100
        b = 200
        print("Inner function: ",a)  # 100
        print("Inner function: ",b)  # 200
    inner_function()
    print("Outer function: ",a)      # 100
    print("Outer function: ",b)      # 600 
outer_function()
# print("Outer function: ",a)      # this would raise an error - not defined in the global scope
print("Global Scope:   ",b)        # 200 

# ======================================================================================================================
# Python Closure Function has 3 properties, can be used as the 'key' in the list.sort() method
# ======================================================================================================================
# 1. We must have a nested function
# 2. The nested function must refer to a value defined in the enclosing function.
# 3. The enclosing function must return the nested function.
def closure_function(msg):
    # This is the outer enclosing function
    def printer():
        # This is the nested function
        print(msg)
    return printer  # returns the nested function

def init_count():
    """
    demonstrates how a closure can modify the outerscope count and maintain the value.  The closure allows you to
    capture the variables from the outer function and use them again even after the function has been exited.
    """
    count = 0
    def add(amount):
        nonlocal count
        count += amount
        print(count)

    return add

x = init_count()   # the closure is created and bound to the function 'x'
x(1)  # returns 1
x(1)  # returns 2
x(1)  # returns 3


def inner_2():
    global b   # 'b' can be set here and used in outer_2
    print(b)   # this will access the b defined in outer_2
    b = 200    # will modify the global b


def outer_2():
    global b
    b = 500
    inner_2() # this will access b
    print(b)  # this prints the 200
    
outer_2()

# ======================================================================================================================
# PASSING ARGUMENTS TO THE COMMAND LINE see bezpy_08_arparse.py for a more formal method
# ======================================================================================================================
# Example use from command line....
# $python>: python main2.py foo bar "name='david jones'" age=23

# This is Equivalent to passing the above from the command line
sys.argv = ['C:/Users/orenb/OneDrive/PYTHON/bezpy_02_exceptions.py', 'foo', 'bar', "name='david jones'", "age=23"]

if len(sys.argv) > 0:
    print (sys.argv[0]) # C:\...PATH...\main2.py (DEFAULT ARGUMENT)
if len(sys.argv) > 1:
    print (sys.argv[1]) # foo (FIRST ARGUMENT)
if len(sys.argv) > 2:
    print (sys.argv[2]) # bar (2ND ARGUMENT)
if len(sys.argv) > 3:
    print (sys.argv[3]) # name='david jones'
if len(sys.argv) > 4:
    print (sys.argv[4]) # age=23

kwargs = {}  # to upload the keyword arguments to a dictionary
# Note "xxx=yyy".split('=')[0] ='xxx', "xxx=yyy".split(':')[1] = 'yyy'
for x in sys.argv[3:]:
    key = x.split('=')[0]
    value = x.split('=')[1]
    kwargs[key] = value
for k, v in kwargs.items():
    print('keyword argument: {}-->{}'.format(k, v))

# ======================================================================================================================
# Environment Variables  CAN ONLY BE TYPE STRING
# ======================================================================================================================
# set MYENVIRONVAR="Whatever I choose"  -- this sets env. variable in msdos
# echo %MYENVIRONVAR%                   -- this returns "Whatever I choose" in msdos
# set                                   -- this displays all environment variables in msdos

import os
os.environ                                        # returns all env. variables as a environ dictionary environ({'X': '1'})
os.environ.copy()                                 # returns all env. variables as a dictionary {'X': '1'}

os.environ['PYTHONPATH'] = 'C:\\dir;C:\\dir2'     # sets environment variable.  WARNING: this is too late at runtime to be added to sys.path
os.environ['USERNAME']  	                      # return environment variable but KeyError if not found
os.environ.get('COMPUTERNAME')                    # like dictionary returns None if not present
os.environ.get('MYVAR','FRED')                    # can set a default value for z (not the env. variable)
os.getenv('MYVAR', default='Fred')                # same as environ.get
os.environ['VAR2'] = 'FREDDY'                     # sets environment variable but only for the shell the program is running in
#environ.putenv('VAR2','FREDDY')                  # ???this doesn't seem to do anything???

list(os.environ.keys())                           # ['PYTHONPATH', 'USERNAME']
list(os.environ.values())                         # ['C:\\dir;C:\\dir2', 'FRED']
list(os.environ.items())                          # [('PYTHONPATH', 'C:\\dir;C:\\dir2'), ('USERNAME', 'FRED')]
os.environ.clear()                                # clears all env. variables from this executing shell
os.environ.setdefault('XXX', 'y')                 # returns env. variable 'XXX' but if doesn't exist, sets it and  returns 'y' same as dict.setdefault()



os.environ.pop(key, default='xxx')                # remove specified key and return the corresponding value or default if doesn't exist
os.environ.popitem()                              # ('ALLUSERSPROFILE', 'C:\\ProgramData')  removes random key-value and returns the pair

# os.environ.unsetenv
# os.environ.decodekey
# os.environ.decodevalue
# os.environ.encodekey
# os.environ.encodevalue


# Method 1
# Here is an example with running file poo.py …
# $> python -W ignore poo.py   # This is equivalent too ...


# Method 2 Windows
# $> SET PYTHONWARNINGS=ignore
# $> ECHO %PYTHONWARNING%  ... to check value
# $> python poo.py

# Method 3 - set at top of the page before importing libraries that issue warnings
# from os import environ
# environ['PYTHONWARNINGS'] = ignore


# These values below can be set by the shell before executing the program.  'x' just means set to any value
# PYTHONCASEOK=x:            Forces Python to ignore case when parsing import statements. This is a Windows-only environment variable.
# PYTHONDEBUG=x:             Performs the same task as the -d option.
# PYTHONDONTWRITEBYTECODE=x: Performs the same task as the -B option.
# PYTHONFAULTHANDLER=x:      Forces Python to dump the Python traceback (list of calls that led to an error) on fatal errors.
# PYTHONHASHSEED=arg:        Determines the seed value used to generate hash values from various kinds of data. When this variable is set to random, Python uses a random value to seed the hashes of str, bytes, and datetime objects. The valid integer range is 0 to 4294967295. Use a specific seed value to obtain predictable hash values for testing purposes.
# PYTHONHOME=arg:            Defines the default search path that Python uses to look for modules.
# PYTHONINSPECT=x:           Performs the same task as the -i option.
# PYTHONIOENCODING=arg:      Specifies the encoding[:errors] (such as utf-8) used for the stdin, stdout, and stderr devices.
# PYTHONNOUSERSITE:          Performs the same task as the -s option.
# PYTHONOPTIMIZE=x:          Performs the same task as the -O option.
# PYTHONPATH=arg:            Provides a semicolon (;) separated list of directories to search for modules. This value is inserted in the sys.path variable in Python. see 'Python Notes Google Docs'
# PYTHONSTARTUP=arg:         Defines the name of a file to execute when Python starts. There is no default value for this environment variable.
# PYTHONUNBUFFERED=x:        Performs the same task as the -u option.
# PYTHONVERBOSE=x:           Performs the same task as the -v option.
# PYTHONWARNINGS=arg:        Performs the same task as the -W option. arg=ignore (to suppress warnings) or arg=default (to reinstate warnings)


# ======================================================================================================================
# https://docs.python.org/3/library/sysconfig.html
# `python -m sysconfig`  this will display all the results
# ======================================================================================================================
import sysconfig   # from standard library
sysconfig.get_config_vars()     # returns all environment variables as dictionary
sysconfig.get_config_var('py_version')  # '3.10.0'  returns named environment variable
sysconfig.get_platform()  # returns a string that identifies the current platform  'win-amd64'
# sysconfig.expand_makefile_vars(s, vars)
sysconfig.get_config_h_filename()   # 'C:\\Users\\orenb\\AppData\\Local\\Programs\\Python\\Python310\\Include\\pyconfig.h'
sysconfig.get_makefile_filename()   # 'C:\\Users\\orenb\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\config\\Makefile'

sysconfig.get_path_names()    # This function returns a tuple containing all path names currently supported in sysconfig.
    # ('stdlib', 'platstdlib', 'purelib', 'platlib', 'include', 'scripts', 'data')
    # stdlib	    directory containing the standard Python library files that are not platform-specific.
    # platstdlib	directory containing the standard Python library files that are platform-specific.
    # platlib	    directory for site-specific, platform-specific files.
    # purelib	    directory for site-specific, non-platform-specific files.
    # include	    directory for non-platform-specific header files.
    # platinclude	directory for platform-specific header files.
    # scripts	    directory for script files.
    # data	        directory for data files.

sysconfig.get_path('include')  # 'C:\\Users\\orenb\\AppData\\Local\\Programs\\Python\\Python310\\Include'


# sysconfig.get_paths(scheme, vars, expand)
# sysconfig.get_preferred_scheme(key)
sysconfig.get_python_version()  # returns the MAJOR.MINOR Python version number as a string.

sysconfig.get_default_scheme()  # 'nt'
sysconfig.get_scheme_names()    # ('nt', 'nt_user', 'osx_framework_user', 'posix_home', 'posix_prefix', 'posix_user')
# Python uses an installation scheme that differs depending on the platform and on the installation options. Following schemes are currently supported:
# posix_prefix	scheme for Posix platforms like Linux or Mac OS X.
# posix_home	scheme for Posix platforms used when a home option is used upon installation.
# posix_user	scheme for Posix platforms used when a component is installed through Distutils and the user option is used.
# nt	        scheme for NT platforms like Windows.
# nt_user	    scheme for NT platforms, when the user option is used

# sysconfig.is_python_build(check_home)
# sysconfig.parse_config_h(fp, vars)
# sysconfig.realpath(path, strict=false)


# ======================================================================================================================
# METHOD 1: dotenv
# ======================================================================================================================
# load environment variables with dotenv library from a '.env' file  (good for storing passwords)
from dotenv import load_dotenv, find_dotenv  # requires pip install python-dotenv
# create '.env' file using dos command: type nul > .env

load_dotenv(dotenv_path=r'C:\Users\orenb\OneDrive\PYTHON\myfiles\.env') # put path to .env file if not in current directory else dotenv_path='.\.env'
# load_dotenv() # loads .env file from local directory
# load_dotenv(find_dotenv())  # can find your .env file
print(os.environ.get('SECRET_KEY'))

# ======================================================================================================================
# METHOD 2: python-decouple
# ======================================================================================================================
# 'DASHBOARD_RENEWAL_EMAILS' is listed in the .env file
# from decouple import Csv, config
# DASHBOARD_RENEWAL_EMAILS = config('DASHBOARD_RENEWAL_EMAILS', cast=Csv())

# ======================================================================================================================
# METHOD 3: python-environ  (not the built-in os.environ)
# ======================================================================================================================
# More commonly use pip install python-environ
# Fill os.environ with .env file variables
import environ
env = environ.Env()

#  see https://django-environ.readthedocs.io/en/latest/

#------------------------------------
import warnings # used to issue warnings
warnings.warn("this is oren's warning")
#------------------------------------

# ======================================================================================================================
# pythonic way to restart a main script mid-code
# ======================================================================================================================
# if __name__ == '__main__':
#    while True:
#        ...
#		if (condition to restart):
#            continue
#            ...
#	 break
# ======================================================================================================================

#=======================================================================================================================
#   sys.intern() interning values can optimize comparison performance and save memory
#                useful for interned dictionary keys
#=======================================================================================================================
x = sys.intern('hello this is a full sentance.')
y = sys.intern('hello this is a full sentance.')
print(id(x))
print(id(y))   # prints same id as above which saves memory

print(x == y)  # True since same value
print(x is y)  # True since same memory location, quicker than string comparison

# in previous versions python automatically interned strings upto 20 chars,
# Since python 3.7 this was extended to 4096 chars but not if there are spaces
# So best to EXPLICITY intern your strings

a = 'Y'*4096
b = 'Y'*4096
print(a is b)  # True

c = 'Y'*4097
d = 'Y'*4097
print(c is b) # False

x = 'aaa bbb'
y = 'aaa bbb'
x is y # False

c = sys.intern('z'*4097)
d = sys.intern('z'*4097)
