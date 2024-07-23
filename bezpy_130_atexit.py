# atexit is a module in python which contains two functions register() and unregister(). 
# The main role of this module is to perform clean up upon interpreter termination. 
# 
# Functions that are registered are automatically executed upon interpreter termination. 
# Except for the following cases:
#   1) Whenever a program is killed by a signal not handled by Python, 
#   2) when os._exit() is called, 
#   3) Python fatal internal error is detected

import sys
import os
import atexit  # from standard library

def hello1(name):
    print (f'hello {name}')

def hello2(name):
    print (f'hello {name}')


# Using register() as a decorator
@atexit.register
def goodbye():
    print("GoodBye.") 

 
# Using register() to register method
atexit.register(hello1, 'test1')
atexit.register(hello1, 'test2')
atexit.register(hello1, 'test3')

atexit.register(hello2, 'test4')
atexit.register(hello2, 'test5')
atexit.register(hello2, 'test6')
atexit.unregister(hello2) # unregisters the 'hello2' executions

# os._exit(1)  # will not invoke the registered functions
sys.exit(1)    # will invoke the registered functions

# OUTPUT:
# hello test3
# hello test2
# hello test1
# GoodBye.