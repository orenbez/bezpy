# ======================================================================================================================
# inspect from standard-library, provides an interface to the Python debugger, can evaluate object types
# ======================================================================================================================
# see also bezpy_156_pkgutil.py,  Standard Library module provides utilities for the import system, package support.
# see also bezpy_106_importlib.py,  Standard Library module provides the implementation to Python's import statement
# ======================================================================================================================

import inspect

# pprint([x for x in dir(inspect) if x.startswith('is')])
# 'isabstract',
#  'isasyncgen',
#  'isasyncgenfunction',
#  'isawaitable',
#  'isbuiltin',
#  'isclass',
#  'iscode',
#  'iscoroutine',
#  'iscoroutinefunction',
#  'isdatadescriptor',
#  'isframe',
#  'isfunction',
#  'isgenerator',
#  'isgeneratorfunction',
#  'isgetsetdescriptor',
#  'iskeyword',
#  'ismemberdescriptor',
#  'ismethod',
#  'ismethoddescriptor',
#  'ismethodwrapper',
#  'ismodule',
#  'isroutine',
#  'istraceback'

class A(object):
    def methd(self):
        pass

class B(A):
    pass
class C(B):
    pass

obj = A
inspect.isclass(obj)          # True - inspects object and returns bool

obj = A().methd
inspect.ismethod(obj)         # True - inspects object and returns bool
inspect.iscode(obj)           # False - inspects object and returns bool

import math
obj = math
inspect.ismodule(obj)         # True - inspects object and returns bool


def fn():
    pass

obj = fn
inspect.isfunction(obj)        # True - inspects object and returns bool

obj = sum                     # built-in function sum()
inspect.isbuiltin(obj)        # True - inspects object and returns bool


import math
inspect.getmembers(math)        # returns list of All the members of any module or object as list of tuples (name, obj)
# [ ... ('perm', <function math.perm(n, k=None, /)>),  ('pi', 3.141592653589793),  ('pow', <function math.pow(x, y, /)>), ... ]

import datetime
inspect.getmembers(object=datetime, predicate=inspect.isclass)  # returns only the 'class' members
# [('date', datetime.date),  ('datetime', datetime.datetime),  ('time', datetime.time),  ('timedelta', datetime.timedelta),  ('timezone', datetime.timezone),  ('tzinfo', datetime.tzinfo)]

inspect.getmembers(object=datetime, predicate=lambda x: not callable(x))  # non-callable members
inspect.getmembers(object=datetime, predicate=lambda x: x.__name__.startswith('ti') if inspect.isclass(x) else False)   # classes starting with ti
# [('time', <class 'datetime.time'>), ('timedelta', <class 'datetime.timedelta'>), ('timezone', <class 'datetime.timezone'>)]

inspect.signature(math.perm)    # returns signature object <Signature (n, k=None, /)>


# getsource(): returns the source code of a module, class, method, or a function

from dataclasses import dataclass
inspect.getsource(dataclass)      # returns any method librarysource code as a string. This will not work for built-in classes e.g. int


def fun(a, b):
    return a * b
inspect.getsource(fun)           # 'def fun(a, b):\n    return a * b\n'


# getmodule(): This method returns the module of a particular object
import collections
obj = inspect.getmodule(collections)    # <module 'collections' from 'C:\\Users\\orenb\\AppData\\Local\\Programs\\Python\\Python310\\lib\\collections\\__init__.py'>
obj is collections  # True

# stack(): This method helps in examining the interpreter stack or the order in which functions were called.
inspect.stack(context=1)          # Return a list of frame records for the caller’s stack
inspect.stack()                   # same as above

prev_frame = inspect.currentframe().f_back   # returns previous frame
filename, line_number, function_name, lines, index = inspect.getframeinfo(prev_frame)
inspect.getmodule(prev_frame)  # returns module of previous frame

# getdoc(): The getdoc() method returns the documentation of the argument in this method as a string.
inspect.getdoc(math.perm)  #  'Number of ways to choose k items from n items without repetition and with order ...

inspect.getmro(C)  # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
