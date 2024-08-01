# ======================================================================================================================
# READ ME: https://python.plainenglish.io/improve-your-code-with-decorators-4fec033b99eb
# ======================================================================================================================
# In python functions are first-class objects and can ... 
# a) be assigned to a variable
# b) be taken as an input parameter of a function
# c) be returned from a function
# d) stored as dictionary values
# ======================================================================================================================
# 'Higher Order Functions' take first-class functions as parameters and/or return them. e.g map(), filter(), reduce()
# ======================================================================================================================
def compose(f, g, x):   # <--- first parameters are functions, last is a data type
    return f(g(x))
compose(print, len, 'string')

# ======================================================================================================================
# Assign function to a variable
# ======================================================================================================================
def greet(name):
    return "Hello " + name

greet_someone = greet  # Assign functions to variables (they are objects like anything else)
greet("John")  # Hello John
del greet # functions can be deleted (this one was reassigned so greet_someone() so still works)
greet_someone("John")  # Hello John,  same function call as greet("John") above

# ======================================================================================================================
#  Inner or nested function, limited to scope of the function
# ======================================================================================================================
def greet2(name):
    def get_message():
        return "Hello "
    result = get_message() + name
    return result

greet2("John") # Hello John, uses nested function

# ======================================================================================================================
# Functions can be passed as parameters to other functions. Known as high-order functions
# ======================================================================================================================
def call_func(func):
    other_name = "John"
    return func(other_name)  

call_func(greet_someone) # Hello John

# ======================================================================================================================
# Functions can be nested and return other functions
# ======================================================================================================================
def compose_greet_func1():
    def get_message():
        return "Hello there!"
    return get_message

greet4 = compose_greet_func1() # Functions can return other functions
greet4()  # 'Hello there!'

# ======================================================================================================================
# Inner functions have access to the enclosing scope, can modify enclosing scope variable with 'nonlocal' keyword
# ======================================================================================================================
def compose_greet_func2(name):
    def get_message():
        return "Hello there " + name + "!"
    return get_message


# ======================================================================================================================
# Decorators are callable objects which are used to modify functions or classes.
# Function decorators are functions which accept function references as arguments
# and adds a wrapper around them and returns the function with the wrapper as a new function.
# Note: You can decorate a function with more than one decorator
# ======================================================================================================================

# @function_decorator
# def func_name():
#     pass
#
# @class_decorator
# def ClassName:
#
#     @method_decorator   <-- not so common
#     def method_name():
#         ...

def our_decorator(func):
    def function_wrapper(x):  # <---- note decorator will only work for functions with a single parameter
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper


@our_decorator
def foo(x):  # foo is the decorated function
    print("Hi, foo has been called with " + str(x))

# our_decorator(foo)(4)       <----- this would have worked without the decorator syntax
# foo = our_decorator(foo)   <----- this would redefine foo without the decorator syntax
foo("xxx")

function_list = [len, str.isdigit, str.lower]  # functions can be stored in data structures

# ======================================================================================================================
# Sample Decorator
# ======================================================================================================================
def invocation_log(func):
    def inner_func(*args, **kwargs):
        print(f'Before Calling {func.__name__}')
        return_val = func(*args, **kwargs)
        print(f'After Calling {func.__name__}')
    return inner_func


@invocation_log
def say_hello(name):
    print(f"Hello, {name}!")

say_hello('David')
# Before Calling say_hello
# Hello, David!
# After Calling say_hello

# ======================================================================================================================
# Objects Can Behave Like Functions
# ======================================================================================================================
class Foo2:
    def __init__(self):
        print("__init__")
    def __call__(self):  #  allows you to execute an object as a function
        print("__call__")

x = Foo2() # returns __init__
x()        # returns __call__


class Foo3:
    def __init__(self, name):
        self.name = name

    def __call__(self, msg):  # allows you to execute an object as a function
        print(f'{self.name} says {msg}')


x = Foo3(name='Paul')  # initialize
x('hi')  # returns 'Paul says hi'

# func()  is equivalent to func.__call__()
func = lambda x, y: x + y
func(8, 9)  # 17
func.__call__(8, 9)  # 17

# ======================================================================================================================
# 'access modifiers' and 'name mangling'
# ======================================================================================================================
class Access:
    def __init__(self, a, b, c):
        self.public = a
        self._protected = b
        self.__private = c

v = Access('A', 'B', 'C')
v.public
v._protected
# v.__private   # would fail with ... AttributeError: 'Access' object has no attribute '__private'
v._Access__private  # <- - - this is 'name mangling' and will return 'C'


# ======================================================================================================================
# Timer decorator function 'measure_time' is more generic than our_decorator.
# It can handle functions with any number of arguments *args, *kwargs
# and functions that return a 'result'
# ======================================================================================================================
def measure_time(function):
    def wrapper(*args, **kwargs):
        import time
        print(f'Executing function: {function.__name__}')
        start = time.perf_counter()
        result = function(*args, **kwargs)
        print(f'Elapsed time: {time.perf_counter() - start} ms')
        return result
    return wrapper

@measure_time
def add(x, y):
    return x + y

add(2, 5) # This is decorated with measure_time
# Executing function: add
# Elapsed time: 1.7000000003264404e-06 ms
# 7

# Without decorator
def add2(x, y):
    return x + y

measure_time(add2)(2, 5)  # add2 is not decorated.  This would be equivalent to the above
# Executing function: add2
# Elapsed time: 1.700000005655511e-06 ms
# 7


# @measure_time()
# def add3(x, y):
#     return x + y


def validate_1_to_10(function):
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, int):
                raise ValueError('Only Integers Allowed')
            if not 1 <= i <= 10:
                raise ValueError('Value must be 1 to 10')
        result = function(*args, **kwargs)
        print(f'{function.__name__} was successful')
        return result
    return wrapper

@validate_1_to_10
def add3(x, y):
    return x + y

add3(3, 9)     # returns 12
# add3('3', 9)  will raise error
# add3(11, 9)   will raise error

# ======================================================================================================================
# Standard decorator syntax ...  can also use '@wraps for __doc__ and __name__ (see below)
# ======================================================================================================================
def decorator(function):
    def wrapper(*args, **kwargs):
        # Perform Before
        result = function(*args, **kwargs)
        # Perform After
        return result
    wrapper.__doc__ = function.__doc__               # update with the value of the decorated function (for doc string)
    wrapper.__name__ = function.__name__             # update with the value of the decorated function (important for pickling)
    wrapper.__qualname__ = function.__qualname__     # update with the value of the decorated function
    return wrapper

# ======================================================================================================================
# __doc__, __name__, __qualname__,
# ======================================================================================================================
class Example:
    def sample_method():
        """sample docstring"""
        pass
Example.sample_method.__doc__         #  'sample docstring'
Example.sample_method.__name__        #  sample_method
Example.sample_method.__qualname__    #  Example.sample_method






# ======================================================================================================================
# decorator with parameters  see https://www.pythontutorial.net/advanced-python/python-decorator-arguments/
# ======================================================================================================================
def meta_decorator(value):
    def decorator(function):
        def inner(arg):
            return function(arg) * value
        return inner
    return decorator


@meta_decorator(2)
def say_hi(x):
    return f'hi {x} '

say_hi('Tom')  # hi Tom hi Tom

# ======================================================================================================================
# @wraps updates the wrapper function to look like the decorated function by copying attributes 
# such as __name__, __doc__ (the docstring), etc.
# ======================================================================================================================
from functools import wraps

def repeat(times):
    """Call a function multiple times"""
    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorate


@repeat(3)
def say(message):
    """This is docstring for the say function"""
    print(message)

say('Hello')

# Output
# ------------------
# Hello
# Hello
# Hello

print(say.__name__)
print(say.__doc__)

# Output without @wraps
# ---------------------
# wrapper
# None

# Output with @wraps
# ---------------------
# say
# This is docstring for the say function

# ======================================================================================================================




@measure_time
def fib2(n):
    """ returns the nth element of the sequence with manual caching """
    if n == 1 or n == 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)


from math import factorial
@measure_time
def fib1(n):
    return factorial(n)

# ======================================================================================================================
# Decorators are executed bottom to top
# ======================================================================================================================


def make_bold(fn):
    return lambda : "<b>" + fn() + "</b>"

def make_italic(fn):
    return lambda : "<i>" + fn() + "</i>"

@make_bold      # <--invoked 2nd
@make_italic    # <--invoked 1st
def hello():
  return "hello world"

hello_html = hello()   # '<b><i>hello world</i></b>'

