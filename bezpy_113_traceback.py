# traceback from the standard library
# This module provides support for printing stack traces
# READ https://www.geeksforgeeks.org/traceback-in-python/


import sys
import traceback
  
# declaring array
A = [1, 2, 3, 4]
  
try:
    value = A[5]
      
except:
    traceback.print_exc()      # printing stack trace


# format_exc(limit = None, chain = True) : 
# This is like print_exc(limit) except it returns a string instead of printing to a file.


# Traceback (most recent call last):
#   File "c:/bezpy/bezpy/bezpy_113_traceback.py", line 13, in <module>
#     value = A[5]
# IndexError: list index out of range

try:
    3/0
except Exception as e:
    exc_type, exc_value, exc_tb = sys.exc_info()
    tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
    print(''.join(tb.format_exception_only()))



print("end of program") # this statement is to show that the program continues normally after the exception is handled


