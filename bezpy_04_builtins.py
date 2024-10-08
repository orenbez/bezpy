# ======================================================================================================================
# DEFINITIONS:
# ======================================================================================================================
# iterable:  object that you can loop, i.e. has built-in '__iter__' function.
#            In the loop iter() is invoked and an iterable created
#            Also can be indexed with '_getitem_' function, (e.g. list, tuple, string, set).
#            Iterating the collection or iterable uses 'Strict Evaluation'
#         
# iterator:  all iterable objects can be used to create an iterator which only stores one value at a time,
#            can be looped ONCE and the next value can be created with the 'next()' command.
#            Iterating with an 'iterator' or 'generator' uses 'lazy evaluation'
#
# generator: this is a type of iterator which is created by a genexp (generator expression) or by the 'yield'
#            keyword  (see bezpy_105_generators.py)
# ======================================================================================================================

# ======================================================================================================================
#     IMPORTED MODULES
# ======================================================================================================================
from mylib.mymisc import boo      # function boo() will print an output marker to screen
from sys import exit              # imports sys.exit() function, must be called using 'exit()' not 'sys.exit()'
# ======================================================================================================================


# ======================================================================================================================
# Version 3.10 has 77 built-in functions
# https://www.w3schools.com/python/python_ref_functions.asp
# https://www.programiz.com/python-programming/methods/built-in
# using the built-in functions can save processing time
# import builtins
# built_in_functions_list = dir(builtins)[dir(builtins).index('abs'):]
# builtins.abs(-7)  # this is the same as simply writing abs(-7)
# ======================================================================================================================
# abs(-5)	                     # Returns absolute value of a number, takes any object that implements __abs__, including custom classes
# aiter(async_iterable)          # Returns an AsyncIterator for an AsyncIterable object - NEW for 3.10  (see bezpy_20_asyncio.py)
# all([True, True, False])	     # Returns true when all elements in iterable/iterator are true
# anext()                        # Returns the next item from the async iterator - NEW for 3.10
# any([True, True, False])	     # Checks if any Element of an Iterable/Iterator is True
# ascii('⇒')	                 # Returns String Containing Printable Representation (escape chars unicode or hex) (see below)
# bin(7)	                     # converts integer to a string representing a binary number '0b111',  use int('0b111', 2) to convert back to integer
# bool(7)	                     # Coverts a Value to Boolean (see below)
# breakpoint()                   # added in 3.7.  stops code and allows you to use the shell (see below)
# bytearray("py",'utf-8')        # returns array <class 'bytearray'> of given byte size
# bytes("py",'utf-8')	         # returns immutable bytes object
# callable(boo)	                 # Checks if the Object is Callable like a function, class method, or a class
# chr(8704)	                     # Returns Character (a unicode string) from Integer unicode values 0 to 1114111 (see below)
# classmethod()	                 # Converts a function to a class method (used for factory methods) (see below), replaced with  Python decorator @classmethod.)
# compile(codeObj)               # Returns a Python code object  <class 'code'>
# complex(2,-3)	                 # Creates a Complex Number 2 - 3j
# copyright()                    # Displays copyright message
# credits()                      # Displays credits message
# delattr(obj, 'attr')           # Deletes Attribute From an object.  equivalent to `del obj.attr`   ...   (see bezpy01)
# dict([('x', 5), ('y', -5)])    # Creates a Dictionary
# dir(className)	             # Return Attributes of Object/Class. dir() returns list of all local variable names
# divmod(8, 3)	                 # Returns a Tuple of Quotient and Remainder e.g. quotient, remainder = divmod(8,3) which returns (2, 2)
# enumerate(iterable, start)     # Returns an iterator for an enumerate Object from a given start value, default start=zero
# eval('x + 1')	                 # Runs Python Code supplied as string (see below)
# exec()	                     # Executes Dynamically Created Program (see below)
# exit()                         # Used to exit shell
# filter( )                      # constructs iterator from elements which are true (see below)
# float('7.5')	                 # returns floating point number from number, string
# format()	                     # returns formatted representation of a value, not the same function as str.format()
# frozenset({1, 2, 3})	         # returns IMUTTABLE frozenset object from tuple or set. remember an obj of type set is mutable
# getattr(obj, attr[, default])  # returns value of named attribute of an object. Can set default value if attribute does not exist see below
# globals()	                     # returns dictionary of current global variables and values
# hasattr(obj, attr)	         # returns whether object has named attribute  (see bezpy01)
# hash('John Smith')	         # returns hash value (integer) of an object, (only applies to hashable/immutable objects) see bezpy_72_hashlib
# help()                         # Invokes the built-in Help System
# hex(12)	                     # Converts Integer to Hexadecimal
# id(obj)    	                 # Returns memory id of an Object as decimal
# input()	                     # reads from standard input
# int('222')	                 # returns integer from a string or from a float (rounds the value)
# isinstance(3, int)	         # Checks if a Object is an Instance of Class or instance of one of a tuple of classes
# issubclass(sub, parent)        # Checks if a Object is Subclass of a Class
# iter(('a', 'b', 'c'))          # returns iterator for an object of type tuple_iterator or iter(['a','b','c']) -> 'list_iterator' , or iter('xyz') -> str_iterator. They loop once
# len([1, 2, 3])	             # Returns Length of an Object, add __len__() to any custom class to customize the use of len(obj)
# license()                      # Displays history and license agreements of python
# list(('a', 'b', 'c'))          # Function	creates list in Python
# locals()	                     # returns dictionary of current local symbol table. useful in shell
# map(funcName,input_lst)        # Applies Function to an input list and returns an iterable 'map object' (see below)
# max([1, 7, 3, 9])	             # returns largest element
# memoryview()	                 # returns memory view of a byte or byte array
# min([1, 7, 3, 9])	             # returns smallest element of container
# next(i [, default])	         # Retrieves Next Element from generator/iterator i, returns the default value when exhausted e.g.  next(i, -1)
# object()	                     # Creates a Featureless Object of <class 'object'>
# oct(32)	                     # converts integer to octal
# open()	                     # Returns a File object, see bezpy_05_files.py
# ord('w')	                     # returns Unicode code point for Unicode character in decimal
# pow(3, 2)	                     # returns x to the power of y
# print('string to screen')      # Prints the Given Object, based on method sys.stdout.write()
# property()                     # returns the property attribute from the given getter, setter, and deleter.  (see below)
# quit()                         # Quit the shell
# range(1, 4)	                 # return sequence of integers between start and stop
# repr()	                     # returns printable string representation of an object (see below)
# reversed([9, 1, 4])	         # returns reversed iterator object of a any iterable object e.g list, tuple or string
# round(3.4567, 2)               # rounds a floating point number to n-decimal places, or to nearest integer if only one parameter (see below)
# set([1, 2, 3])	             # returns a Python set, set() returns an empty set
# setattr(obj, attr, value)      # sets value of an attribute of object  (see bezpy01)
# slice(1, 5, 2)	             # creates a slice object specified by range()
# sorted([1, 6, 2])	             # returns sorted list from a given iterable e.g 'list'.
# staticmethod()                 # converts any function to be a static method for a class, see below  (replaced with decorator @staticmethod)
# str(123)	                     # returns informal representation of an object as string
# sum([1, 2, 3])	             # Sums items of an Iterable / container (note use math.prod() for product of items
# super()	                     # Allow you to Refer Parent Class by super  see below()
# tuple([1, 2])                  # Function	Creates a Tuple from an iterable
# type('xxx')                    # returns Type of an Object
# vars(obj)                      # returns obj.__dict__ all attributes of an object in one dictionary
# zip([1, 2], ['a', 'b'])	     # returns an iterable of Tuples of type zip

# ======================================================================================================================
# abs() - predefined for number types, can customize for your own objects
# ======================================================================================================================
class AbsCustom:
    def __init__(self, x: str):
        self.x = x
    def __abs__(self):
        return self.x.lower()

abs(9)     # returns 9
abs(-3.1)  # returns 3.1
y = AbsCustom('HELLO')
abs(y)     # returns 'hello'

# ======================================================================================================================
# any() / all()  can take an iterable or an iterator
# ======================================================================================================================
x = [True, 0, 'abc']
any(x)  # returns 'True' if ANY value in iterable 'x' is True, else displays False
all(x)  # returns 'True' if ALL value in iterable 'x' is True, else displays False

# with list comprehensions ...
special_chars = [':', '/', ',']
x = "xxxxx/xxxxx"
any(char in x for char in special_chars)   # <--- doesn't require square brackets


x = [1, 3, 6]
assert all(isinstance(digit, int) for digit in x)  # all values are True


# ======================================================================================================================
# ascii() & chr() & ord()
# ======================================================================================================================
import unicodedata
# THE UNICODE POUND SIGN WITH CODE POINT = (U+00A3), UTF-8 encoding maps (U+00A3) to a two-byte sequence C2-A3.
unicodedata.name('£')  # 'POUND SIGN'
ascii('£')             #  RETURNS '\xa3' ASCII HEX VALUE since this is an ascii character
chr(163)               #  RETURNS '£'
chr(0xa3)              #  RETURNS '£'
ord('£')               #  RETURNS 163   DEC VALUE
'\N{POUND SIGN}'       #  RETURNS '£'   UNICODE DATA NAME
'\u00a3'               #  RETURNS '£'   UNICODE HEX VALUE
'\xa3'                 #  RETURNS '£'   ASCII HEX VALUE
# Note: if you type ALT + 0163 in Windows text editor will generate the pound sign but only works with the decimal code.  ord()
'£'.encode('utf-8') # b'\xc2\xa3' == bytes([194, 163])

# ======================================================================================================================
unicodedata.name('⇒')  # 'RIGHTWARDS DOUBLE ARROW'
implies = '⇒'
ascii('⇒')             # RETURNS UNICODE HEX VALUE'\u21D2' (since not in ascii range)
chr(8658)              # RETURNS '⇒'
chr(0x21d2)            # RETURNS '⇒'
ord('⇒')              # RETURNS INTERGER VALUE 8658
f'{implies!a}'         # RETURNS SAME AS ABOVE USING f-sttrings
'\u21D2'               # UNICODE for '⇒'
# No ascii hex since exceeds 255
'⇒'.encode('utf-8') # b'\xe2\x87\x92'

unicodedata.name('ϑ')    # 'GREEK THETA SYMBOL'
theta = 'ϑ'
ascii('ϑ')               # Returns '\u03D1' unicode hex
chr(977)                 # RETURNS GLYPH 'ϑ' based on dec value 977
chr(0x3d1)               # RETURNS GLYPH 'ϑ' based on hex value 977
ord('ϑ')                 # RETURNS 977 dec value
'\N{GREEK THETA SYMBOL}' # Returns 'ϑ' from the Unicode data name
'\u03D1'                 # 'ϑ' hex value
f'{theta!a}'             # Returns "'\\u03d1'"

ascii('&')      #  is within the ascii range so returns "'&'" not '\u0026'
chr(38)         # '&' DECIMAL VALUE
chr(0x26)       # '&' HEX VALUE
ord('&')        # 38  DECIMAL VALUE for '&'
'\N{AMPERSAND}' # Unicode data name
'\u0026'        # '&' UNICODE HEX
'\x26'          # '&' ASCII HEX

unicodedata.name('😀')   # 'GRINNING FACE'
ascii('😀')              # "'\\U0001f600'"
chr(128512)              # '😀'
chr(0x0001f600)          # '😀'
ord('😀')               # 128512
'\N{GRINNING FACE}'     # '😀'
'\U0001f600'            # '😀'  - note capital 'U'
# THERE IS NO \x   equivalent
'😀'.encode('utf-8') # b'\xf0\x9f\x98\x80' ==  bytes([240, 159, 152, 128])  Not sure how this encoding is working
# '😀'.encode('ascii') # UnicodeEncodeError: 'ascii' codec can't encode character '\U0001f600' in position 0: ordinal not in range(128)

unicodedata.name('💩') # 'PILE OF POO'

# ======================================================================================================================
# bool() - conversion to boolean, see bezpy_01_structures section 'Falsy Values'
# ======================================================================================================================
for i in [list(), tuple(), dict(), set(), range(0), '', 0, 0.0, 0j, None, False]:
    assert bool(i) == False

# everything else would return True, e.g. ...
bool(1)       # returns True
bool(2)       # returns True  (any int/float greater than one)
bool('hello') # returns True  (any non empty string)

# ======================================================================================================================
# float()  returns floating point number
# ======================================================================================================================
float('3.14')      # 3.14
float('inf')       # float representation of infinity
float('-inf')      # float representation of -ve infinity
float('1e-003')    # 0.001

# ======================================================================================================================
# callable() Checks if the Object is Callable like a function, class method, or a class
# ======================================================================================================================

class One:
    pass

def two():
    pass

def three():
    def inner():
        pass
    return inner  # <-- returns a function

four = lambda x: x + 1
five = 'hello'

callable(One)        # True
callable(two)        # True
callable(two())      # False
callable(three())    # True
callable(four)       # True
callable(five)       # False


# ======================================================================================================================
# classmethod() - Converts a method into a class method but is un-pythonic and has been replaced by @classmethod
# ======================================================================================================================

# UN-PYTHONIC
class OldPerson:
    age = 25
    def print_age(cls):  # This is a class method i.e. applies to the whole class and can access static variables
        print('The age is:', cls.age)

# create printAge class method
OldPerson.print_age = classmethod(OldPerson.print_age)
OldPerson.print_age()

# PYTHONIC
class NewPerson:
    age = 25
    @classmethod
    def print_age(cls):
        print('The age is:', cls.age)

NewPerson.print_age()

# Note: can use classmethod as a type of constructor or factory method to return a new instance ....
#       return cls(value1, value2)


# ======================================================================================================================
# staticmethod() - Converts a method into a static method but is un-pythonic and has been replaced by @staticmethod
# ======================================================================================================================
# UN-PYTHONIC - DO NOT USE
class OldMaths:
    # this method is static as it does not depend on an instance
    def add_numbers(x, y):
        return x + y

# create add_numbers static method
OldMaths.add_numbers = staticmethod(OldMaths.add_numbers)
print('The sum is:', OldMaths.add_numbers(5, 10))

# PYTHONIC WAY TO USE STATIC-METHODS
class NewMaths:
    @staticmethod
    def add_numbers(x, y):
        return x + y

print('The sum is:', NewMaths.add_numbers(5, 10))

# ======================================================================================================================
# eval()  - can evaluate a string expression but can not assign or modify a value
# ======================================================================================================================
x = '3'
y = '4'
func_name = 'add'
code = f'int({x}).__{func_name}__({y})'  # 'int(3).__add__(4)'
eval(code)   # returns 7

code = 'int({}).__{}__({})'.format(x, func_name, y)  # 'int(3).__add__(4)'


# ======================================================================================================================
# compile() / exec()
# ======================================================================================================================
code_in_string = """
a = 5
b = 6
print(a + b)
"""
code_object = compile(source=code_in_string, filename='sumstring.py', mode='exec')
exec(code_object)  # returns 11

code = 'x=1; x +=1; print(x)'
exec(code)   # eval(code) would fail

from datetime import *        # global scope namespace
name = 'David'                # local scope namespace
code_in_string = """
print(f'{name}, today is {date.today()}')
"""
allowed_globals = {'date': date}
allowed_locals = {'name': name}
exec(code_in_string, allowed_globals, allowed_locals)


# ======================================================================================================================
# frozenset() since this changes set to be immutable it can now be used as a key in dictionary
# ======================================================================================================================
{frozenset({1, 2, 3}): 'set_one'}      # works since frozenset returns hashable object
# {{1, 2, 3}: 'set_one'}               # TypeError unhashable type: 'set'


# ======================================================================================================================
# isinstance()
# ======================================================================================================================
isinstance(3, int)         # True
isinstance(int, type)      # True
isinstance(3, (str, int))  # True,  can verify instance is member of one of a tuple of classes

# ======================================================================================================================
# iter()  - looping through iterator.
# note can convert container to iterator if container has __iter__ method e.g. list, set, range, tuple
# then the iterator created will have a __next__ method
# ======================================================================================================================
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)  # convert to iterator - this is equivalent to mytuple.__iter__()

while True:
    try:
        next(myit)  # equivalent to myit.__next__()
    except StopIteration:
        print('done')
        break

myit = iter(mytuple)
while True:
    x = next(myit, -1)  # Returns -1 when iterations have exhausted
    if x == -1:
        break

# iter() invokes .__iter__() returns the iterator object itself.
# next() invokes .__next__() returns the next item in the sequence, can be invoked explicitly or by for loop

i = iter([1, 2, 3, 4])
list(i)  # Will convert iterator back to list [1,2,3,4], also tuple(i), set(i)

i = iter(['a', 'b', 'c', 'd'])
''.join(i)  # 'abcd'


# Define a custom class that can implement next() and iter()
class Nums:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    self.a += 1
    if self.a > 4:
        raise StopIteration
    return self.a

i = iter(Nums())
next(i)  # returns 2
next(i)  # returns 3
next(i)  # returns 4

for x in iter(Nums()):
    print(x)
# 2
# 3
# 4

# Create iterator from dictionary.
# NOTE. python dictionaries WILL record the order of data entry for the iterator since python 3.7.
d = {1:'one', 2:'two'}
x = iter(d.items())
next(x) # returns first item in dictionary as tuple (1, 'one')

# ======================================================================================================================
# filter(filter_function, collectible) returns a iterator filter object,
#                                      the collectible is filtered through a filter function
# ======================================================================================================================
# the filter_function must be a 'Predicate Function' that will return a boolean

# function that filters vowels only and returns boolean
def filter_vowels(x):
    if x in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False
    
result = filter(filter_vowels, ['a', 'b', 'd', 'e', 'i', 'j', 'o'])

# you can now loop through the filter object e.g. for r in result ...  or convert to list, or use next()

# 2nd example filter out the under 18s
ages = [5, 12, 17, 18, 24, 32] # iterable

def filter_function(x):  # the filter function
  if x < 18:
    return False
  else:
    return True

adults = filter(filter_function, ages)  # return type is a filter object

# Using a lambda function to get an interable subset of my_list divisible by 13
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]
result = filter(lambda x: x % 13 == 0, my_list)

# Passing 'None' will filter all falsey objects from the collectible where bool(i) == False
anylist = [0, None, "", 0j, [], (), False, 0.0]
result = filter(None, anylist)  # This filters ALL of the values in anylist as they are all 'falsey'   

  
# ======================================================================================================================
# map() returns an iterator, you can loop, use next() command, or convert to list
# ======================================================================================================================
def calc_square(n):
  return n**2
numbers = (1, 2, 3, 4)
result1 = list(map(calc_square, numbers))     # [1, 8, 27, 64]
result2 = list(map(lambda x: x**2, numbers))  # same result using lambda notation

first_name = ["Keith", "Elizabeth","Alex","William"]
last_name = ["Philip", "Brown", "Smith", "Oliver"]
m = map(lambda x, y:x + " " + y, first_name, last_name)
list(m)  # ['Keith Philip', 'Elizabeth Brown', 'Alex Smith', 'William Oliver']

columns = "xxx, yyy,zzz"
list(map(lambda x: x.strip(), columns.split(',')))     # ['xxx', 'yyy', 'zzz']   <- THIS IS MORE EFFICIENT
[col.strip() for col in columns.split(',')]            # ['xxx', 'yyy', 'zzz']   <- THIS IS MORE READABLE


# ======================================================================================================================
# property()  Set property to use getter, setter and delete methods,
# ======================================================================================================================
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # This is not a 'Class' Variable, but 'name' is now unique for each instance
    # last parameter is the doc-string for the attribute
    name = property(get_name, set_name, del_name, 'Name property')

p = Person('Adam')
print(p.name)     # this will now be equivalent to p.get_name()
p.name = 'John'   # this will now be equivalent to p.set_name('John')
del p.name        # this will now be equivalent to p.del_name()

# The Pythonic Way to use this feature...  https://betterprogramming.pub/python-property-decorators-e370c39c7796
class Person2:
    def __init__(self, name):
        self._name = name

    @property  # getter function
    def name(self):
        print('Getting name')
        return self._name

    @name.setter  # called when setting '_name'
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter # called when deleting '_name'
    def name(self):
        print('Deleting name')
        del self._name

p = Person2('Adam')
print(p.name)     # this will now be equivalent to p.get_name()
print(p._name)    # same as above
p.name = 'John'   # this will now be equivalent to p.set_name('John')
del p.name        # this will now be equivalent to p.del_name()

# What is @name.getter for?



# Note: __xxx__() are known as  magic methods or dunder methods
x = object()  # an instance of type 'object' from which all other objects inherit
type(x) #  <class 'object'>


# ======================================================================================================================
# super()
# ======================================================================================================================
# Note: keyword 'object' no longer required for the base class, only need to declare 'class Mammal:'
#       Base class is already implicitly inheriting from Class 'object'

# Base Class
class Mammal(object):
    def __init__(self, name):
        self.name = name
        print(f'{self.name} is a warm-blooded mammal.')

    def description(self):
        print(f'{self.name} is a mammal')

# Subclass
class Dog(Mammal):
    def __init__(self, num_legs):
        self.num_legs = num_legs
        print(f'Your dog has {self.num_legs} legs.')
        super().__init__('Rover')  # Instead of Mammal.__init__(self, 'Rover')
        print(f"Only now you can access {self.name}'s name")

    def description(self):
        print(f'{self.name} is a dog')

    def call_both(self):
        self.description()
        super().description()

d1 = Dog(4)
# Your dog has 4 legs.
# Rover is a warm-blooded mammal.
# Only now you can access Rover's name

d1.call_both()
# Rover is a dog
# Rover is a mammal

isinstance(d1, Dog)       # True
issubclass(Dog, Mammal)   # True
d1.name                   # returns 'Rover'
getattr(d1, 'name')       # same as d1.name above, useful when you have atrribute as a string, or to perform loops e.g  for attr in ['name','age','height']
hasattr(d1, 'name')       # bool returns true
d1.num_legs               # returns 4
getattr(d1, 'num_legs')   # same as above
getattr(d1, 'color', 'unknown')  # returns the default value 'unknown' as the color attribute has not been set
setattr(d1, 'color', 'brown')    # sets the attribute 'color'  even though it doesn't yet exist
delattr(d1, 'num_legs')          # deletes the attribute

# ======================================================================================================================
# max(collectible[, key]) - 'key' provides a function to customize the definition of max
# ======================================================================================================================
max(2, 4, 1)    # returns 4
max([2, 4, 1])  # returns 4
max([2, 4, 1], [3, 1, 1])  # returns [3,1,1] since first item is largest
max([(1, 4), (2,  2)], key=lambda x: x[0] + x[1])  # (1,4) returned as the sum of the tuple digits is the max

# Calcuate most frequent element in a list
nums = [2, 2, 6, 2, 2, 3, 4, 2, 113, 2, 1]
max(set(nums), key=nums.count) # returns 2

d = {'a': 1, 'b': 2, 'c': 3}
max(d, key=lambda k: d[k])  # returns 'c'

# ======================================================================================================================
# min(collectible[, key]) - 'key' provides a function to customize the order
# ======================================================================================================================
min(2, 4, 1)    # returns 1
min([2, 4, 1])  # returns 1
min([(1, 4), (2, 2)], key=lambda x: x[0] + x[1])  # (2, 2) returned as the sum of the tuple digits is the min


# ======================================================================================================================
# sorted() - returns a list. ascends the elements in the collection, returns copy of list that is sorted.
#            Does not affect original list (not inplace).
#            Can work with tuples, sets too unlike the 'sort' list method which is only for lists
#            reverse=True for descending order
#            both list.sort() and sorted python uses O(n * Log n) Tim Sort Algorithm
#            but list.sort() is in-place and is therefore more memory efficient than sorted()
# ======================================================================================================================
sorted([2,5,1])        # [1, 2, 5]
sorted(['c','d','a'])  # ['a','b','c']
sorted(['ab','aa'])    # ['aa', 'ab']
sorted('hello')        # ['e', 'h', 'l', 'l', 'o']  - treated the string as a list
sorted((2, 5, 1))      # [1, 2, 5]
sorted([2, 5, 1], reverse=True) # [5, 2, 1]
sorted([-5, -2, -7], key=abs) # [-2, -5, -7] 'key' provides the category of order. i.e. put in order of absolute value
sorted([(1, 4), (2, 2)], key=lambda x: x[0] + x[1])  # [(2, 2), (1, 4)] put in ascending order for sum of tuple digits

# ======================================================================================================================
# reversed() -  returns an ITERATOR - reverses the order of the collectible - NOT in DESCENDING ORDER -
# ======================================================================================================================
t = ('P', 'y', 't', 'h', 'o', 'n') # this is a tuple
r = reversed(t) # this is an iterator <class 'reversed'>
l = list(reversed(t))  # this is now a list

# ======================================================================================================================
# slice()
# ======================================================================================================================
py_string = 'Python'
# slice(stop)                    equivalent to  [:stop]
# slice(start, stop)             equivalent to  [start:stop]
# slice(start, stop, step)       equivalent to  [start:stop:step]

py_string[slice(3)]            # Returns 'pyt' = py_string[:3]
py_string[slice(-1, -4, -1)]   # Returns 'noh' = py_string[-1:-4:-1]
py_string[slice(4, 1, -1)]     # Returns '' = py_string[4:1:-1] syntax is not understood
py_string[slice(4, 1)]         # Returns '' = py_string[4:1] syntax is not understood

# ======================================================================================================================
# format(value, format_spec='')  - not the same as str.format()
# ======================================================================================================================
# [[fill]align][sign][#][0][width][,][.precision][type]
# fill: (any character) the padding character.
# align: It is an option to specify the alignment of the output string.
    # "<": left-alignment specifier
    # ">": right-alignment specifier
    # "^": center-alignment specifier
    # "=": justified specifier
# sign: This determines the use of signs for the output.
    # "+": Positive numbers have a "+" sign and negative numbers have a "-" sign.
    # "-": Negative numbers have a "-" sign.
    # " " (space): Positive numbers are preceded by a space and negative numbers are preceded by a "-" sign.
# "#": This specifies that the return value should have a type indication for numbers. For example, hexadecimal numbers should have a "0x" prefix added to them.
# "0": This specifies that the output should be sign aware and padded with 0's for consistent output.
# width: (integer) Specifies the full width of the return value.
# ",": Specifies that the return value should have commas as a thousand separator.
# .precision: (integer) determines the number of characters after the decimal point.
# type: This Specifies the output type. The types are of three types:
    # String: Use an "s" or nothing at all to specify a string.
    # Integer: d (decimal), b (binary), o (octal), x (hexadecimal with lowercase characters), X (hexadecimal with uppercase characters), c (character)
    # Floating point: f (lowercase fixed point), F (uppercase fixed point), e (exponent using "e" as separator), E (exponent using "E" as separator), g (lowercase general format), G (uppercase general format), % (percentage)

# ======================================================================================================================
format(1000, '.3f')           # Float '1000.000'
format(1000, 'b')             # Binary  '1111101000'
format(4453, "*>+10,d")       # Decimal '****+4,453'
format(933.3629, "0^-9.2f")   # Float '0933.3600'

# Using format() by Overriding __format__()
class Car:
    def __format__(self, format):
        if(format == 'colour'):
           return 'Red'
        return 'None'

format(Car(), "colour")



# ======================================================================================================================
# enumerate & zip classes - help to pair up list entries
# Can start the counter at any value, default is zero enumerate(iterable, start=0)
# ======================================================================================================================
the_list = ['a','b','c']
enum1 = enumerate(the_list) # produces an enumerated (iterable) data type 'enumerate' (NOT A LIST OF TUPLES)
for i, j in enum1:               # [(0, 'a'), (1, 'b'), (2, 'c')]
  print(i, " ---> ", j)          # Only prints once and behaves like an iterator.
                                 # You can loop once or use next(enum1)

# it is clearer syntax to loop over an enumerate object than to loop over range(len(the_list))

zip1 = zip(['x','y','z'],['a','b','c'])  # produces a iterable, zipped data type (NOT A LIST OF TUPLES)
for i, j in zip1:                        # similar to [('x','a'), ('y', 'b'), ('z', 'c')]
  print(i, " ---> ", j)                  # but can't be indexed e.g. z[0] will give error


# strict flag introduced in version 3.10
x = ['a','b','c']
y = [1, 2, 3, 4]
z = zip(x, y)  # this will drop y[3] = 4  value and only zip 'a','b','c' -> 1 ,2 ,3
# z = zip(x, y, strict=True)  # this will throw an error as of python 3.10 as len(x) and len(y) must be equal --??? not raising error


# better to use Numpy Library but this works
array = []
array1 = [1, 5, 2]
array2 = [3, 4, 6]
for f, b in zip(array1, array2):
    res = f * b
    array.append(res)



# ======================================================================================================================
# str() vs repr() vs eval()
# ======================================================================================================================
import datetime
today = datetime.datetime.now()
a = datetime.datetime.now()  # datetime.datetime(2018, 12, 5, 16, 21, 40, 137132)   creates and object
b = repr(a)                  # 'datetime.datetime(2018, 12, 5, 16, 21, 40, 137132)', used in the REPL shell, calls the __repr__ dunder for the object
c = eval(b)                  # datetime.datetime(2018, 12, 5, 16, 21, 40, 137132)    returns an object
d = str(a)                   # often nicer representation '2018-12-05 16:21:40.137132', used by the print command, calls the __str__ dunder for the object
e = f'{a!r}'                 # same as repr(a) using f-strings
assert(c == a)               # this is True
assert(b == e)               # this is True



repr(today)        # this is equivalent in REPL to the python shell output 
                   # the python shell will use this built-in-function to display the variable object as a string
                   # when you type ... >>> today
                   # today.__repr__() would therefore give the same result
                   # returns string 'datetime(2018, 12, 5, 16, 8, 3, 854132)'
                   # repr() is mainly used for debugging and development
                   # repr’s goal is to be unambiguous
                   # override __repr__ in your class to define its behavior


str(today)         # this is equivalent to today.__str__() which gives a more user-friendly representation of
                   # the date object
                   # returns string  '2018-12-05 16:08:03.854132'
                   # str() is used for creating output for end user
                   # str's goal is to be readable.
                   # override __str__ in your class to define its behavior


today = 'datetime.datetime(2018, 12, 5, 16, 8, 3, 854132)'
eval(today)        # this returns the actual datetime object
                   # returns object datetime.datetime(2018, 12, 5, 16, 8, 3, 854132)
													   
# ======================================================================================================================
# boolean operators
# ======================================================================================================================
a = True
b = False
a | b    # boolean OR
a or b   # boolean OR
a & b    # boolean AND
a and b  # boolean AND
a ^ b    # boolean XOR
not a    # boolean negation

# ======================================================================================================================
# Integer sizes (no current limit with python-3)
# ======================================================================================================================
# if 'i' is a 32-bit signed integer
# =>  -2**31 <= i <= 2**31 - 1 ( = 0b11111111111111111111111111111111 31 ones ) and one for the sign

# if 'i' is a 32-bit unsigned integer
# =>     0 <= i <= 2**32 - 1  ( = 0b11111111111111111111111111111111 32 ones )

# if 'i' is a 64-bit signed integer
# =>  -2**63 <= i <= 2**63 - 1 

# if 'i' is a 64-bit unsigned integer
# =>     0 <= i <= 2**64 - 1  

# ======================================================================================================================
# bitwise operators on binary numbers (used in embedded programming, systems programming, and networking)
# ======================================================================================================================
a = 0b00111100    # 60 = 00111100 
b = 0b00001101    # 13 = 00001101 

# & Binary AND
c = a & b        # 12 = 00001100
print(bin(c))    #        0b1100

# | Binary OR
c = a | b        # 61 = 00111101 
print(bin(c))    #      0b111101

# ^ Binary XOR (exclusive OR)
c = a ^ b        # 49 = 00110001
print(bin(c))    #      0b110001

# 2's complement is a binary system that allows for the representation of +ve and -ve numbers
# in 2's complement we change a +ve number to its negative by operation of 'flip bits add one'
# the python '~' Negation operator uses Binary 2's Complement

# (warning: numbers are not regular binary they are 2's complement)
# e.g  7 = 0111 (flip digits) -> 1000 (add one) -> 1001 = -7
# Here are some 4-Bit 2's complement numbers ...

# ===============================
# DEC   4-BIT 2's Complement
# ===============================
# -8	1000
# -7	1001
# -6	1010
# -5	1011
# -4	1100
# -3	1101
# -2	1110
# -1	1111
# 0	    0000
# 1	    0001
# 2	    0010
# 3	    0011
# 4	    0100
# 5	    0101
# 6	    0110
# 7	    0111
# https://www.exploringbinary.com/twos-complement-converter/

# now consider regular 4-digit binary number 0101 so to negate it we want 1010
# well 1010 in (2's complement 4-bit binary) = -6 (see chart above)

# so in python ...
x = 0b0101 # stores the decimal  5
y = ~x     # stores the decimal -6 which is represented by 1010 in two's complement

# in python the '~' operator effectively adds one and then multiplies by -1 to the decimal value
# '~' will generate an integer which in 2's complement format would be the negation of the original binary number

a = 0b00111100   # 60 = 00111100
c = ~a           # = -61  = 11000011 (in 8-digit 2's Complement format)
print(bin(c))    # is not useful, gives you -0b111101 (binary regular) = -61 (integer) = 11000011 (8-bit 2's complement)

# a << n --> Binary Left Shift (n) digits and replace with zeroes
c = a << 2       # 240 = 11110000  shifted 2 digits to the left
print(bin(c))

# a >> n --> Binary Right Shift (n) digits and replace with zeroes
c = a >> 2       # 15 = 00001111    shifted 2 digits to the right
print(bin(c))


# python 3.10 introduces bit_count()
# x = 102
# x.bit_count() # returns 4 representing number of '1's in the binary form of integer 102 = 01100110  i.e. 4 x '1' bits


# ======================================================================================================================
# dir() returns list of all local variable names, function names, class names
for name in dir():
    print(name)

# in the global scope these are equivalent sets
s1 = set(dir())
s2 = set(locals().keys())
s3 = set(globals().keys())
# ======================================================================================================================

# ======================================================================================================================
# breakpoint() - shell debugger - full list of commands: https://docs.python.org/3/library/pdb.html#debugger-commands
# ======================================================================================================================
# (Pdb) >? help    # help will list the commands,
# Documented commands (type help <topic>):
# ======================================================================================================================
# EOF    c          d        h         list      q        rv       undisplay
# a      cl         debug    help      ll        quit     s        unt
# alias  clear      disable  ignore    longlist  r        source   until
# args   commands   display  interact  n         restart  step     up
# b      condition  down     j         next      return   tbreak   w
# break  cont       enable   jump      p         retval   u        whatis
# bt     continue   exit     l         pp        run      unalias  where
# (Pdb) >? help c   # gives you help on the 'c' command
# c(ont(inue))
#         Continue execution, only stop when a breakpoint is encountered.
# ======================================================================================================================
# n = next = go to next line (steps over functions) 
# s = step = step into function
# r = return = step out of function
# c = continue = continue to next breakpoint
# l = list = display code near the breakpoint
# ll = longlist = display more code near breakpoint
# w = where = show the stack 
# h = help = display commands 
# exit = quit debugger and end program
# b 231 = break 231 = sets breakpoint at line 231 (can check line numbers with 'list'
# b = break = lists current breakpoints (not including the physical ones in the code - breakpoint())
# c = clear = clears current breakpoints (not including the physical ones in the code - breakpoint())
# p = print value
# pp = pretty print a dictionary
# restart = restart the program
# ======================================================================================================================


round(1.267, 2)  # Returns 1.27 as expected
# ======================================================================================================================
# School textbook rounding methods rounds up i.e x.5 -> x + 1
# but round() uses the "rounding half to even strategy" or "Bankers’ rounding" where the function rounds towards the
# neareast even integer ... e.g.
# 1.5 & 2.5 both round to 2.0
# -0.5 & 0.5 both round to 0.0
# -2.5 & -1.5 both round to -2.0
# For the traditional rounding function use round2()
# see https://www.quora.com/Why-does-rounding-0-5-create-so-many-problems
# ======================================================================================================================
round2 = lambda x,y=None: round(x + 0.0000001,y)
round(0.5)  # = 0
round2(0.5) # = 1
round(1.5)  # = 2
round2(1.5) # = 2

# Returns the last 3-digits of an integer  e.g 1234->234
last3 = lambda x: x-(1000*(x//1000))
last3(1234) # Returns 234

# ======================================================================================================================
# reduce() - Demoted in python 3, was originally a built-in function.
#            to be honest it is more readable to use loops instead
#            The function returns a single result of the nested value
# ======================================================================================================================
from functools import reduce

# reduce(function(f), list(l)) computes the nested value ... f(f(f(l[0],l[1]),l[2]),l[3])
# i.e. performs function on first two terms f(l[0],l[1])
# and then function on the result of that and the third term,  e.t.c.

sum_list = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  #  i.e. ((((1+2)+3)+4)+5) equivalent to sum([1,2,3,4,5])
prod_list = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]) # ((((1*2)*3)*4)*5)
           
# Return the largest number by comparing first two and keeping the largest, comparing that with 3rd term ...e.t.c.
arr_num = [110, 569, 784, 377, 900, 126]
largest_num = reduce(lambda x, y: x if x > y else y, arr_num)
print(largest_num)

# other functools
# functools.lru_cache        see bezpy_37_lru_cache.py
# functools.singledispatch:  see bezpy_118_singledispatch.py
# functools.partial:         see bezpy_126_partial.py

# ======================================================================================================================
# int(str, base=n) Converts to integer base 10. All below examples, return 17
# ======================================================================================================================
int('17')               # = 17, treated as base 10
int('17', 0)            # = 17, treated as base 10
int('17', base=10)      # = 17, treated as base 10

int('10001', base=2)    # = 17, treated as base 2 
int('0b10001', base=2)  # = 17, treated as base 2
int(0b10001)            # = 17, treated as base 2

int('101', 4)           # = 17, converts 101 in base=4  to decimal integer

int('21', base=8)       # = 17, treated as oct
int('0o21', base=8)     # = 17, treated as oct
int(0o21)               # = 17, treated as oct

int('11', base=16)      # = 17, treated as hex
int('0x11', base=16)    # = 17, treated as hex
int(0x11)               # = 17, treated as hex


int(3.14)    # = 3
int(True)    # = 1
int(False)   # = 0

# ======================================================================================================================
# memoryview() - memory view of a byte or byte array
# ======================================================================================================================
mv = memoryview(b'abc')
mv[0]  # returns 97, integer representing 'a'

# ======================================================================================================================
# object() - returns empty object of type object
# ======================================================================================================================
empty_object = object()

# ======================================================================================================================
# pow(index, power[, modulo])  - optional 3rd parameter for modulo division of the result
# ======================================================================================================================
pow(3, 2)        # = 3 ** 2 = 9
pow(3, 2, 4)     # = 3 ** 2 % 4

# ======================================================================================================================
# sum(iterable[, start])
# ======================================================================================================================
sum([1,2,3], start=5)   # returns 11 = 5 + 1 + 2 + 3

# ======================================================================================================================
# tuple(iterable)
# ======================================================================================================================
tuple(['a', 'b', 'c'])        # ('a', 'b', 'c')
tuple('abc')                  # ('a', 'b', 'c')
tuple([['a'], ['b'], ['c']])  # (['a'], ['b'], ['c'])


# ======================================================================================================================
# The Context Manager 'with' statement  require __enter__() and __exit__() defined in the object methods
#                            which determine how it is used.
# ======================================================================================================================

# note you can use the library 'dis' (disassemble) to convert a function to machine instructions

# I think these libraries are used for parsing python code ...
# built-in library symbol: This module provides support for Python symbol constants e.g. symbol.del_stmt == 276
# built-in library token: This module provides support for Python token constants e.g. token.COMMA == 12
# built-in library syslog: This module is for an interface to Unix
