# !/usr/bin/python3
# the hash-bang is used by unix to recognize that script should be executed with python3, not used with windows """
# chmod +x file.py will make the file executable in unix
# ======================================================================================================================

""" Multi Line Comments are not really considered pythonic 
    as technically the string is not ignored as with a hash it is just not assigned to a variable """
# WARNING - Python does not like mixing TABS with SPACES for indentation, be consistent

# Cheat Sheet: https://overapi.com/python

# ======================================================================================================================
# IMPORTED MODULES - namespace conflicts
# ======================================================================================================================
from math import (sqrt,          # imports specific functions from standard 'math' library.
                  exp)           # Use brackets to go over multiple lines.
import os                         #used to retrieve environment variables but requires path os.function()
from sys import exit              #imports sys.exit() function, must be called using 'exit()' not 'sys.exit()'

# import mylib.mymath             #this would require the full path when you call it mylib.mymath.tripleMe(5)
# from mylib.mymath import *      #this doesn't require full path but may have namespace conflicts with function 
                                  #names in the current module and mylib.mymath. The full path can not be used in this case
                                  # for the function to be called so just a one word function name can be used more than once
                                  
from mylib.mymath import triple_me, add3_to_me #This imports two functions from the 'mymath' module (single script)
                                  #Best to import function list explicitly to avoid conflicts within namespace

from mylib.mymisc import boo      # function boo() will print an output marker to screen

# You can enter a path like this starting from your current directory ...
# from dir1.subdir.mymodule import *
# OR the path must be added to environment variable 'PYTHONPATH' just before execution OR the list sys.path at runtime

# import os as oper_sys  also works
# os.__file__ will give you path to the module you have imported.


# ======================================================================================================================
# USER DEFINED FUNCTIONS ...
# Function parameters are the names listed in the function's definition.
# Function arguments are the real values passed to the function.
# Functions are first-class objects in python, can be assigned, passed as arguments and compared
# ======================================================================================================================
def double_me (x):
    """User defined function"""   # this is the document string which apears with help(double_me)
    return 2 * x

d_me = lambda x: 2 * x
# ======================================================================================================================
# Lambda Expressions
# ======================================================================================================================
# lambda functions can have zero or more inputs, also known as anonymous functions as can be used without a name
# e.g. as a hook with the 'sort' functions key parameter  sort(key=lamba x: ...)
square = lambda x: x * x       # alternative function def in style of lamda calculus
sum_2_nums = lambda x, y: x + y
const = lambda : 1                   # always returns 1, no inputs
const = lambda *args, **kwargs: 1    # always returns 1, any inputs
const() # returns 1
l1 = lambda x, y=4: x + y             # sets default value for y
l2 = lambda a, b=2, *c, **d: [a, b, c, d]
l2(1, 2, 3, 4, x=1, y=2)    # [1, 2, (3, 4), {'x': 1, 'y': 2}]

# ======================================================================================================================
# MAIN CODE STARTS HERE ...
# ======================================================================================================================


# z = input("ENTER A VALUE:") # prints text to screen and waits for input
# print("you have inputed the value: ", z)

# variables and function names are case  sensitive
x = -1					        # determines types implicitly, x is an integer
print(exp(x))      		 	    # function defined in standard library
print(sqrt(4))      		 	# function defined in standard library
print(double_me(5))          	# function defined above
print(square(10))            	# function defined above (lamda format)
print(triple_me(5))          	# function defined in mymath.py (in the mylib directory)
print('hello','my','friend')    # the comma is replaced by a space in the output
print('hello'+'my'+'friend')    # the concatenation '+' has no spaces giving 'hellomyfriend'

if 'f' in 'foo': print('1'); print('2'); print('3') # Multiple instructions seperated by ';', but not pythonic

# this is a list, each element is a different types: int, float str, bool, complex, range, tuple, list, type, module
mixed_list = [5,3.1,11/3,11%3,11//3,"hello", 'hello', True, -1+2j, [0 ,1 ,2],(0 ,1 ,2),range(3), list(range(3)),
                                                                                 None, type(int),os,{'bad':0,'good':1}]
for i in mixed_list:
  print("\'" + str(i) + "\',  is of type:", type(i))   # THE 'type' FUNCTION

  
#RESULTS:
# '5',  is of type: <class 'int'>
# '3.1',  is of type: <class 'float'>  # not int like previous versions of python
# '3.6666666666666665',  is of type: <class 'float'>
# '2',  is of type: <class 'int'> # modulo division 11%3 = 2
# '3',  is of type: <class 'int'> # floor division
# 'hello',  is of type: <class 'str'>  # "hello" is same as 'hello'
# 'hello',  is of type: <class 'str'>
# 'True',  is of type: <class 'bool'>
# '(-1+2j)',  is of type: <class 'complex'>
# '[0, 1, 2]',  is of type: <class 'list'>
# '(0, 1, 2)',  is of type: <class 'tuple'>
# 'range(0, 3)',  is of type: <class 'range'> # range(3) is comparable to tuple (0,1,2)
# '[0, 1, 2]',  is of type: <class 'list'>
# 'None',  is of type: <class 'NoneType'> # None is a singleton
# '<class 'type'>',  is of type: <class 'type'> # 'type' is a type in it's own right
# '<module 'os' from 'C:\\Program Files\\Python37\\lib\\os.py'>',  is of type: <class 'module'>
# '{'bad': 0, 'good': 1}',  is of type: <class 'dict'>

# Multiple instructions in one line
x = 1; y = 2; z = 3

# These concatenations are the same  s1 - s4
s1 = 'xxx' + 'yyy'
s2 = 'xxx' 'yyy'
s3 = ('xxx'
      'yyy')
s4 = ('xxx' 'yyy') # this is a string
tuple5 = ('xxx', 'yyy') # this is a tuple
tuple6 =  'xxx','yyy' # this is also of type tuple
tuple7 = tuple(['xxx','yyy'])  # so is this
tuple8 = ('xxx',)  # this tuple with one entry must end with comma else will be interpreted as a string 'xxx'


my_bin_int = 0b010  # binary value,  print(my_bin_int) gives 2
bin(2) # returns '0b10'
my_oct_int = 0o642  # = 418
oct(418) # returns '0o642'
my_hex_int = 0xF3   # = 243
hex(243) # returns '0xf3'
my_exponent_float = -1.7e-6

# ======================================================================================================================
# Arithmetic Operators
# ======================================================================================================================
# +	  Addition	x + y	
# -	  Subtraction	x - y	
# *	  Multiplication	x * y	
# /	  Division	x / y	
# %	  Modulo Division	x % y  (also see built-in function divmod()
# //  Floor division	x // y (removes fraction)
# **  Exponentiation	x ** y
# ===============================================


# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# Note that sys.stderr will flush by default
# *objects - tuple unpacking of objects to print (see below)
# sep = ' ' - space is default sperator between objects
# end = '\n' - by default next line character is placed at end of line
print('xxx', 'yyy', sep='-', end='*')    # xxx-yyy*  '-' instead of ',' and '*' instead of '\n'
print('xxx', 'yyy', sep='\n', end='')    # will print each element on seperate line
# Can print to print(x, file=sys.stdout) # Standard Output which is default output text
# Can print to print(x, file=sys.stderr) # Standard Error which is error output text

# ======================================================================================================================
# type coercion functions examples ...  list(),int(), bool(), str()
# ======================================================================================================================
x = list(range(5)) # type coercion which generates list [0,1,2,3,4] which is now mutable
x = int('2') # string to int
x = bool('True') #string to bool
x = str(222) #int to string


# Python 3.6  allows underscores in python numeric types which will be ignored, may help to distinguish thousands
1_000_000 # = 1000000

# ======================================================================================================================
# decisions require indentation, not brackets, indentation must be consistent
# ======================================================================================================================
if type(x) == str:  # isinstance(x,str) is preferred syntax, see bezpy_04_builtins.py
  print ('x is a string')

a = 9
# one line "ternary" expressions
i = 5 if a > 7 else 0


# ======================================================================================================================
# IF/ELSE STATEMENTS
# IS EQUAL ==   ,   NOT EQUAL  !=
# ======================================================================================================================
x=2**9  # Two to the power of nine, equivalent to pow(2,9)
if x >= 0 and x < 10:
  digits = 1
elif x >= 10 and x < 100:
  digits = 2
elif x >= 100 and x < 1000:
  digits = 3
elif x >= 1000 and x < 10000:
  digits = 4
else: # i.e if none of the above
  digits = "too big" # more than 4
print ("Number of digits:",digits)   #this line will always execute  because not indented


# Continue on next line character '\', no comments following '\'
if x == 1 or \
   x == 2:
    print('success')

# alternative to above using brackets
if (x == 1 or
    x == 2):
    print('success')


# inline conditions
if x > 0 : print('bigger than zero')

# terneray operator 
print('bigger than zero') if x > 0 else print('less than or equal to zero')
sign = '+' if x > 0 else '-'

# negate the condition
condition = False
if not condition:
	print('condition is false')


# ======================================================================================================================
# LOOPING THROUGH LISTS
# ======================================================================================================================
for i in [2 , 4 , 6 , 8]:           #loops through the list
  print (i)                         #requires indentation

for i in range(5):   #print 0 to 4
  print (i)

for i in range(3,10):  #print 3 to 9
  print (i)

for i in range(10,0,-1): #equivalent to [10, 9, ..., 2, 1]  10->0 (excluding zero), the -1 is required
  print (i)

for i in range(10,0,-2): #equivalent to [10,8,6,4,2]  10->0 (excluding zero) decreases by two
  print (i)

for _ in range(3): # use underscore when you do not need to use the variable 'i'
  print ("hello")

# ======================================================================================================================
# triple quote strings can extend many lines
# ======================================================================================================================
print("""This will continue
        to this line""")

# ======================================================================================================================
# 'break' exits loop,  'continue' skips iteration  applies to 'for' or 'while' loops
# ======================================================================================================================
n = 0
while n < 15:
  n = n + 1
  if n == 7:
    continue
  elif n == 9:
    break
  print ("count:",n)


#  if vs while
# if condition_1 or condition_2:  This will not evaluate condition_2 if condition_1 passes
# while condition_1 or condition_2: both conditions will be evaluated

# ======================================================================================================================
# 'pass' keyword
# ======================================================================================================================
x = 5
if x == 7:
  print ("x == 7")
elif x == 5:
  pass   #python requires 'pass' here to do 'nothing', i.e. can't leave blank
print ("next")   #since not indented, this is not conditional

# Can also use ellipsis instead of pass
print(...)         # Ellipsis
print(type(...))   # <class 'ellipsis'>

# ======================================================================================================================
# end of while loop OR for loop 'else' command
# ======================================================================================================================
n =10
while n > 0:
  print (n)
  n = n - 1
  if n == 1:
      break
else:   # seems superfluous, but runs at end of while loop ONLY if completed without a break, also 'for' loop
  print ("loop completed without a break")


# ======================================================================================================================
# Walrus operator introduced in python 3.8 is unnecessary but can reduce syntax.  Assign and test equality together :=
# ======================================================================================================================
my_list = [1,2,3,4,5]
n = len(my_list)
if n > 3:
    print(n)
# Walrus operator saves the assignment line, but is confusing
#if (n := len(my_list)) > 3
#   print(n) # 5 


# ======================================================================================================================
# Assignment Operators in Python
# ======================================================================================================================
# =     Assign value of right side of expression to left side operand	x = y + z
# +=    Add and Assign: Add right side operand with left side operand and then assign to left operand	a += b
# -=    Subtract AND: Subtract right operand from left operand and then assign to left operand: True if both operands are equal	a -= b
# *=    Multiply AND: Multiply right operand with left operand and then assign to left operand	a *= b
# /=    Divide AND: Divide left operand with right operand and then assign to left operand	a /= b
# %=    Modulus AND: Takes modulus using left and right operands and assign result to left operand	a %= b
# //=   Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand	a //= b
# **=   Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand	a **= b
# &=    Performs Bitwise AND on operands and assign value to left operand	a &= b
# |=    Performs Bitwise OR on operands and assign value to left operand	a |= b
# ^=    Performs Bitwise xOR on operands and assign value to left operand	a ^= b
# >>=   Performs Bitwise right shift on operands and assign value to left operand	a >>= b
# <<=   Performs Bitwise left shift on operands and assign value to left operand	a <<= b


# ======================================================================================================================
# TUPLE METHODS https://www.w3schools.com/python/python_ref_tuple.asp
# ======================================================================================================================

t = ('a', 'b', 'c', 1, 2, 3, 1, False)
t.count(1)   # Returns 2  i.e. count for the value 1
t.index(1)   # Returns 3, index of first occurance of value 1
t.index(1,4) # Returns 6, index of first occurance of value 1 starting from position 4

# count(value, /) # Return number of occurrences of value.
# index(value, start=0, stop=9223372036854775807, /) #  Return first index of value.

t1 = (1, 2, 3)
t2 = t1  # t2 assigns the value of t1 not a reference to t1 since tuples are immutable


# ======================================================================================================================
# LISTS
# ======================================================================================================================
a = [19785 , "Jack" , "Davis", 35, 165.2 , "23 Wentworth Ave"]  # can access and rewrite elements a[0] to a[5]
print (a[4])  # returns 45.2
print (len(a))  # returns 6
print (a)  # prints out full list
x = a[2:5] # stores a[2],a[3],a[4] as new list1, this is 'slicing' which forms a sublist
print (x)


list1 = []  # empty list
list1 = list(range(20))  # [0,1,2,3,4,5 ...  18,19]

x = list1[0:15:2] # slices out elements 0 to 14 in intervals of two
r = list1[::-1]   # reverses the list
print(x)          # x = [0,2,4,6,8,10,12,14] = range(0,15,2)

list1 =  [5 ,6] + [7 ,8] + [9]   # Joining Lists
list1.append(10)          # appends to end of list [5,6,7,8,9,10]
list1.insert(0,3)        # inserts 3 at beginning of list1,  list1 =  [3,5,6,7,8,9,10]
list1.insert(1,4)         # inserts after list[0]  list =  [3,4,5,6,7,8,9,10]
z = list1.pop(4)          # deletes list[4] and assigns the value popped out to 'z',  list1 =  [3,4,5,6,8,9,10]
list1.pop()               # deletes last element ,         list1 =  [3,4,5,6,8,9,10]
list1.extend([1,2])       # joins list to end   list1 =  [3,4,5,6,8,9,1,2], same as  list1 + [1,2]
list1.sort()              # sorts elements alphabetically  [1,2,3,4,5,6,8,9]   modifies the list in-place and returns None
list1.sort(reverse=True)  # reverses list inplace AFTER sorting and return None
list1.reverse()           # reverses list inplace, without sorting, returns None

list2 = [-1,-8,-7]

list2.sort(key=abs, reverse=True)  # list2 is modified to [-8, -7, -1], 'key' determines the function that defines
                                   # the sorting algorithm.  in this case we will order by the ascending absolute
                                   # value of the integer. reverse=True will reverse the final order in the list

list3 = [('Fred', 7), ('Steve', 4), ('Anne', 9)]
list3.sort()  # Tuples sort by First value and then the 2nd value e.t.c
list3.sort(key=lambda x:x[1]) # This will sort by age

list3 = list2  # assigns list3 as a reference to list2 since lists are mutable

# WARNING: sorted() and reversed() are BUILT-IN functions not list functions see bezpy_04_builtins
sorted_list = sorted(list1, reverse=False)  # returns copy of the list BUT does not modify the list (reverse=False is the default)

# This reverses the order of the list, NOT IN reverse order
reversed_obj = reversed(list1)  # returns an iterator object of type 'list_reverseiterator'

list1.remove(8)       # removes first element that matches the number 8, also works with strings list=[1,2,3,4,5,6,9]
print(list1.count(8)) # counts how many number '8's are left in the list
del list1[-1]         # deletes last element list1=[1,2,3,4,5,6]
del list1[3:6]        # deletes the slice from list1, [1, 2, 3]
list1[3:6] = [7,8,9]  # inserts values in slice,  [1, 2, 3, 7, 8, 9]
list1[2:2] = ['a', 'b', 'c']   # inserts in the 2 position  [1, 2, 'a', 'b', 'c', 3, 7, 8, 9]


for i in range(0,len(list1)): #for each 'i' integer in range(0,5) - loops through range of integers
    print ('list1[' + str(i) + '] = ' + str(list1[i]))
list1.clear() # empties the list  list=[]

list1 = []
list2 = [2 , 4 , 6 , 8]
count = 0
for i in list2: #for each 'i' element/object of list2 - loops through list2
   list1.insert(count,i)
   print(list1)
   count = count + 1
if (list1 == list2):
  print ("lists are now the same")

if list1:  # if (list1 != []) 
    print('list1 is non empty')

index8 = list1.index(8) # = 3 which is the index for integer '8' in the list

while list1: # while list1 is not empty
    list1.pop()


# this prints duplicates in list so far
x = [1, 3, 5, 7, 9, 4, 1]
for i in range(len(x)):
    list_so_far = x[:i+1]
    current_element = x[i]
    if list_so_far.count(current_element) == 2:
        print(current_element)

# ======================================================================================================================
# LIST METHODS (complete list)
# https://www.w3schools.com/python/python_ref_list.asp
# ======================================================================================================================
# lst.append(val)      add item at end
# lst.clear()          remove all elements
# lst.copy()           returns shallow copy of the list
# lst.count(value)     counts number of occurences of 'value'
# lst.extend(seq)      add sequence of items at end
# lst.index(val)       returns first occurence of val, error if doesn't exist. Note that find() is a string function
# lst.insert(idx,val)  insert item at index
# lst.pop(idx)         value remove & return item at index idx (default last)
# lst.remove(val)      remove first item with value val
# lst.sort()           sort list in place, returns None.  Note call [1,3,2].sort() is of no use as the list is discarded
# lst.reverse()        reverse list in place, returns None
	
	
# ======================================================================================================================
# SETS are mutable, easiest way to handle duplicates
# elements within sets get hashed => quicker look up, note Python sets can only include hashable objects
# 5 in {SET}   # Lookup Time = O(1)
# 5 in [LIST]  # Lookup Time = O(n)
# ======================================================================================================================
x = set()  #creates empty set.  Note {} will be interpreted as empty dicionary
x = {5,3}
x.add(4)                    # x = {5,3,4}  Modifies x by adding SINGLE element but Returns None
y = {1,2,3}.union({5,3,4})  # Returns {1, 2, 3, 4, 5}

# | (UNION)
# & (INTERSECTION)
# - (DIFFERENCE)
# ^ (XOR = EXCLUSIVE OR = SYMMETRIC DIFFERENCE = UNION MINUS INTERSECTION)

# (INCLUSION RELATIONS)
# <   (IS PROPER SUBSET)
# <=  (IS SUBSET)
# >   (IS PROPER SUPERSET)
# >=  (IS SUPERSET)

x = {1, 2, 3, 4, 5} & {2,5,9} # {2, 5}
z = {1, 2, 3, 4, 5} - {5,11}  # {1, 2, 3, 4}  

s = [1,2,3,4,4]
s1 = set(s)   # removes the duplicate 4 from the list
s2 ={4,5,6}
s1 <= s2      # returns true if s1 is a subset of s2
s3 = {5,7}

x = s1.union(s2)    # Returns union of the sets but s1 is not modified
x = s1.union(s2,s3) # Returns s1 | s2 | s3
s1.update(s2)       # Equivalent to s1 = s1.union(s2) Updates s1 with the union of itself and others, returns None
s1 |= s2            # Same as above
s1 = s2.copy()      # set s1 is equivalent to s2
s1 = s2             # set s1 is a reference to s2  (same id value) since sets are mutable



def find_dupes(x: list) -> set:
    """Method to find duplicates in a list"""
    return set([i for i in x if x.count(i) > 1])

find_dupes([1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8])  #  {3, 5}



# ======================================================================================================================
# SET METHODS  https://www.w3schools.com/python/python_ref_set.asp
# ======================================================================================================================
# s1.add(7)                         # Add a SINGLE element to a s1. This has no effect if the element is already present.
# s1.clear()	                    # Removes all the elements from the set s1
# s1.copy()                         # Returns a shallow copy of a set


# s1.isdisjoint(s2)	                # Returns whether two sets has a intersection or not
# s1.issubset(s2)	                # Returns whether another set contains this set or not;  s1 <= s2
# s1.issuperset(s2)	                # Returns whether this set contains another set or not;  s2 >= s2

# s1.remove(6)                      # Remove an element from a set but raises KeyError if element is not a member
# s1.discard(6)                     # Same as above but does not raise error if the element is not present
# s1.pop()                          # Remove and Return an arbitrary set element. Raises KeyError if the set is empty.


# s1.difference(s2)	                    # Returns a set containing the difference between two or more sets; s1 - s2
# s1.difference_update(s2)	            # Removes the items in s1 that are also included in s2; s1 -= s2
# s1.intersection(s2)	                # Returns a set, that are the intersection of to other sets;  s1 & s2
# s1.intersection_update(s2)            # Removes the items S1 that are not present in s2;  s1 &= s2

# s1.symmetric_difference(s2)           # Returns a set with the symmetric differences of two sets; s1 ^ s2
# s1.symmetric_difference_update(s2)	# Inserts the symmetric differences from this set and another; s2 ^= s2
# s1.union(s2)	                        # Return a set containing the union of sets; s1 | s2
# s1.update(s2)	                        # Update the ENTIRE set s1 with the union of this set and others; s1 |= s2

   
# ======================================================================================================================
# STRINGS can be treated as tuples (immutable)  so length function works but insert doesn't
#         Note that strings are in Unicode by default for python 3.X
# ======================================================================================================================
x = ('a','2','c')
h = ['a','2','c']
y = "a2c"
z = "xxx"

# Since Immutable, can't assign character  z[0] = y, but can read z[0]

print("length of x =", len(x))  # len(x) = 3
print("length of y =", len(y))  # len(y) = 3
print(x == h) # False (different types)
print(y == h) # False (different types)
print(x[1] == y[1]) # True (both are chars not integers)
y = y + y  # gives "a2ca2c"  STRING CONCATENATION
y = 2*z    # gives "xxxxxx"  STRING CONCATENATION
#y = x + y gives runtime error since you can not concatenate different types



# ======================================================================================================================
# For mutable objects python passes by reference, immutable - passes by value, also true for equating objects
x = [1,2,3]
y = x  # this is a reference, so x and y have the same id() value

x = (1,2,3)
y = x # this is a copy, so x and y haved different id() value

def pass_param (x):            # Modifies the parameter passed
    return x.append("MODIFIED")

x = ['an', 'ordinary', 'list']
pass_param(x)    # passes x by Reference and modified it
pass_param(x[:]) # passes a copy of list x 'by Value' - no modification to list
#Note: for a copy of a dictionary/sets use dict(x) or x.copy(), set(x) or x.copy() NOT x[:]
y = x # y is a 2ndry reference to the list (x) which is mutable
y.append('Modified Again')  # this modifies 'x' and 'y' references to a specific id location

x = (1,2,3)
y = x  # this is a copy not a reference since (1,2,3) is immutable


# ======================================================================================================================

strg ='1234567890'
# Note: type ... help(str) in your R.E.P.L (python shell) for list of methods  and details for a string
#       type  dir(str) for plain list
print(strg[0])         #prints first digit '1'
print(strg[-1])        #prints last digit '0'
print(strg[1:5])       #prints digits '2345' i.e from 2nd digit until 6th
print(strg[5:-2])      #prints digits '678' i.e.from 6th digit until two from end
print(strg[:])         #prints full string  strg[:] is a copy of strg
print(strg[2:])        #prints from 3rd digit to end 34567890 equivalent to  str[2:len(str)]
print(strg[:5])        #prints from start until 6th digit 12345 equivalent to  str[0:5]

if '235' not in strg:
  print("can't find 235")
if '234' in strg:
  print("can find 234")


# Alternatively can use the find() function

if strg.find('235') > 0:
    print('found 235')


x = [12,23,34, 'hello']
print('hello' in x)
  

# ======================================================================================================================
# STRING METHODS / STRING FUNCTIONS
# https://www.tutorialspoint.com/python/python_strings.htm
# https://www.w3schools.com/python/python_ref_string.asp
# ======================================================================================================================
x = "s12A34z56a78c9HH0"   # similar to  ('s', '1', '2', ... , 'H', '0')


# s.find(str)   # function syntax:  str.find(str, beg=0, end=len(string))  FIRST Index if found and -1 otherwise
# s.index(str)  # function is the same but throws an error if substring not found
# s.rfind(str)  # find last substring
# s.rindex(str) # find last substring
# str in s      # returns bool True if substring present


x = "Elon is learning Python!"
print(x)
print(len(x)) # returns length of string
print (x.find("is"))    # returns 5
print (x.find("on",7))  # returns 21

print(x.capitalize()) # makes first char of string capital and rest lowercase
print(x.lower())  # all chars. lower
print(x.upper())  # all chars. upper
print(x.title())  # first char.of each word is capital


'xxx'.upper()       # returns 'XXX'
str.upper('xxx')    # same as above (see classes)
help('xxx'.upper)   # help on 'upper' function
help(str.upper)     # same as above 

x = "split to list"
y = x.split()    # returns list ['split','to','list'] (default seperator is the space char)
x = "split:to:list"
y = x.split(':') # returns list ['split','to','list']
z = ':'.join(y)  # joins list to a string using ':' as separator
print(z)         # "split:to:list"
print(x[::-1])   # reverse the string
string1 = "xxx is xxx is xxx is"
print (string1.replace("is", "was"))     # "xxx was xxx was xxx was"
print (string1.replace("is", "was", 2))  # "xxx was xxx was xxx is"  (only first two occurrences)


str1 = "w,e,l,c,o,m,e"
print(str1.split(',',2))    # splits two occurrence starting from left -> ['w', 'e', 'l,c,o,m,e']
print(str1.rsplit(',',2))   # splits two occurrence starting from right -> ['w,e,l,c,o', 'm', 'e']


# s.startswith(prefix[,start[,end]])
'aaabbbbbbb'.startswith('aaa')  # returns True
'aaabbbbbbb'.startswith('aaa',1,7)  # returns False
'aaabbbbbbb'[1:7].startswith('aaa') # same as above

# s.endswith(suffix[,start[,end]])
'aaabbbbbbb'.endswith('bbb') # returns True


# s.count(sub[,start[,end]])  # Counts occurences of substring 'sub'
# s.partition(sep)            # returns 3 element tuple (before, sep, after)
'aaa^^^ccc'.partition('^^^')  # Returns ('aaa', '^^^', 'ccc')

# s.index(sub[,start[,end]]) # RETURNS FIRST index, Error on Failure
# s.find(sub[,start[,end]])  # RETURNS FIRST index, -1 on Failure


# Use replace() to translate full strings, this works for keys of length '1' only
# these define a translation tables used to map individual characters.
char_map1 = str.maketrans('abc','def')               # 'a' -> 'd', 'b' -> 'e', 'c' -> 'f'
char_map2 = str.maketrans('abc','def','!"#$%&*?@^~') # same as above but third paramater all chars map to None or empty string
char_map3 = str.maketrans('','','!"#$%&*?@^~')       # here only the third parameter is important, all chars map to None
char_map4 = str.maketrans({'&': 'and', '@': 'at'})   # input is one dict which maps single chars to strings

'abc&@'.translate(char_map1)  # Returns 'def&@'
'abc&@'.translate(char_map2)  # Returns 'def'
'abc&@'.translate(char_map3)  # Returns 'abc'
'abc&@'.translate(char_map4)  # Returns 'abcandat'

#=========================================
# s.is…() tests on chars categories
#=========================================
# s.isalnum()
# s.isalpha()
# s.isascii()
# s.isspace()   # space chars only
# s.istitle()   # checks for title case
# s.isupper()
# s.islower()

# s.isprintable()
# s.isidentifier()

# s.isdecimal()
# s.isdigit()
# s.isnumeric()

#isnumeric vs isdigit vs isdecimal
str1 = '\u00B2'     #superscript of 2 -  only str1.isdecimal() = False
str2 = "3"          #digit - all 3 are True
str3 = '\u00BD'     #fractional value  only str3.isnumeric() = True


# s.expandtabs([tablength]) # REPLACES TABS WITH SPACES, DEFAULT TABLENGTH = 8 spaces
# s.upper()     # CONVERTS TO UPPER CASE
# s.lower()     # CONVERTS TO LOWER CASE 
# s.title()     # CONVERTS TO TITLE CASE
# s.swapcase()            # swaps case for each char in string
# s.casefold()            # Similar to lower() used for string comparisons, will convert more chars to lower than lower()
# s.capitalize()          # Convert to camel case
# s.center([width,fill])  # CENTER JUSTIFY
# s.ljust([width,fill])   # LEFT JUSTIFY
# s.rjust([width,fill])   # RIGHT JUSTIFY
# s.zfill([width])        # ZERO FILL FROM LEFT
# s.maketrans()           # Return a translation table (as a dict) usable for str.translate()  example above
# s.translate()           # Substitutes substrings based on translation table      example above
# s.partition()           # see example above 
# s.rpartition()          # not sure how differs from partition()
# s.format()              # see below
# s.format_map()          # Formats specified values in a string
# s.join(seq)     - joins list to a string using string 's' as separator
':'.join(['aaa','bbb','ccc']) # returns 'aaa:bbb:ccc'

# s.split([sep, max])     # splits string to list based on the provided seperator, default is ' ',  max number of splits
'aaa:bbb:ccc'.split(':')  # returns ['aaa', 'bbb', 'ccc']
# s.splitlines()          # returns a list of the lines in the string, breaking at line boundaries.
'xxx\nyyy'.splitlines()               # ['xxx', 'yyy']
'xxx\nyyy'.splitlines(keepends=True)  # ['xxx\n', 'yyy']

# s.rstrip([chars])  - removes trailing spaces or any specified string of [chars]
# s.lstrip([chars])  - removes leading spaces or any specified  string of  [chars]
# s.strip([chars]) - removes leading & trailing spaces or any specified  [chars]

# >>> x = 'abdceaaaa'
# >>> x.strip('a')
# 'bdce'

# >>> x = 'abababzzzababab'
# >>> x.strip('ab')  # removes any 'a' or 'b' characters from the lead and from the trail
# 'zzz'
# >>> x.strip('ba')  # order is unimportant, this is the same as above
# 'zzz'


# s.replace(old, new, count=-1) - where count is the max number of occurrences, string s is not modified
# s.removeprefix(prefix_string) # Python 3.9 will remove prefix and return string (not inplace)
# s.removeprefix(suffix_string) # Python 3.9 will remove suffix return string (not inplace)

# ======================================================================================================================
# ENCODE STRING->BYTES
# ======================================================================================================================
# bytes are sequences of 8-bit values, str are sequences of unicode
# each char of the byte-string can be represented by decimal integer 0-255  or hex integer 0x00 to 0xff
# - values for errors = {'strict','ignore','replace','xmlcharrefreplace'}  replaces - replaces errors with '?'
# - examples for encoding = {'utf-8', 'ascii', 'cp1026', 'cp949', 'shift_jis_2004', 'utf-16-le'}  # utf-8 is the default
s = 'H\t@'
e = s.encode('utf-8')  # b'H\t@', encode with utf-8 
e = s.encode(encoding='utf-8', errors='strict')  # b'H\t@', <class 'bytes'>,  note 'utf-8' is same encoding as 'utf8'
e = s.encode()        # b'H\t@', same as above as values are both default, <class 'bytes'>
e = bytes(s, 'utf-8') # b'H\t@',same as above, encoding is required, <class 'bytes'>
e = bytes([72,9,64])  # b'H\t@',same as above, <class 'bytes'>
e = b'H\t@'           # b'H\t@',same as above, of type bytes, encoding assummed to be utf-8, <class 'bytes'>
e = b'\x48\x09\x40'   # b'H\t@',same as above using hex values
f = bytearray(b'H\t@')           # returns array <class 'bytearray'> of 3 bytes
f = bytearray("H\t@",'utf-8')   # returns array <class 'bytearray'> of 3 bytes
f = bytearray([72,9,64])        # same as above
# f = bytearray(b'H\t@')        # requires an encoding, gives TypeError: 
e == f # returns True

# ======================================================================================================================
# bytes vs bytearray
# ======================================================================================================================
# bytes - immutable    .append() not allowed,   bytes([72,9,64]) + b'-'  returns new bytes object
# bytearray - mutable  bytearray([72,9,64]).append(22)  or bytearray([72,9,64]) + b'-'

# The bytes and bytearray are both iterable returning each bytes integer value
for byte in e:
    print(byte)
#
# 72
# 9
# 64

# ======================================================================================================================
# locale module from the standard library, provides support for localizing programs
# ======================================================================================================================
import locale
# get the preferred encoding for your local platform
locale.getpreferredencoding(False)  # on windows returns 'cp1252' i.e. Windows-1252 which is the preferred encoding
                                    # unix platforms returns 'utf-8'

# ======================================================================================================================
# DECODE BYTES->STRING
# ======================================================================================================================
e[0] # returns 72 which is the decimal value of the char 'H' = ord('H')
e[1] # returns 9 which is the decimal value of the char '\t' = ord('\t')
e.decode(encoding='utf-8', errors='strict') # returns 'H\t@' as string
e.decode()  # same as above as those are defaults


# bytes([128]).decode('ascii')  UnicodeDecodeError: 'ascii' codec can't decode byte 0x80 in position 0: ordinal not in range(128)
# bytes([128]).decode('utf-8')  UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte

# ascii == utf-8 for decoding int values 0-255 (some will have no decode value eg: 129)
# see https://www.ascii-code.com/  0-127 = ascii, 128-255 = extended ascii
for i in range(256):
    x_ascii = bytes([i]).decode('ascii', errors='ignore') # only decodes up to bytes([127]) in WINDOWS PLATFORM
    x_utf8 = bytes([i]).decode('utf-8', errors='ignore')  # only decodes up to bytes([127]) SAME AS ASCII on WINDOWS PLATFORM
    x_win = bytes([i]).decode('cp1252', errors='ignore')
    print(f"i={i}, ascii='{x_ascii}', char({i})='{chr(i)}', utf8='{x_utf8}', windows='{x_win}'")

# Also see built-in library codecs: This module provides support for encoding and decoding text strings.


# ======================================================================================================================
# ESCAPE CHARACTERS  also see bezpy_04_builtins.py
# ======================================================================================================================
print(0x48)    # prints the integer 72
print("\x48")  # prints H,  '\x48' is the Ascii code for 'H'
print(R"\x48") # 'R' or 'r' will ignore the esc. character (raw text)
print(r"\x48")


# \\	 Backslash (\)
# \'	 Single quote (')
# \"	 Double quote (")
# \a	 ASCII Bell (BEL) When sent to PRINTER emits gives sound nothing printed
# \b	 ASCII Backspace (BS) When sent to PRINTER - moves back one space
# \f	 ASCII Formfeed (FF = NEW PAGE CHAR FOR PRINTER ASCII(DEC: 12))
# \n	 ASCII Linefeed (LF) = historically would be like the typewriter going to begining of the line (not in use in many operating systems)
# \r	 ASCII Carriage Return (CR) - goes to next line (for most systems this is CR+LF) on screen
# \t	 ASCII Horizontal Tab (TAB)
# \v	 ASCII Vertical Tab (VT)  NOT USED TODAY
# \ooo	     character with octal value ooo, e.g. '\074' = '<'  (DEC = 60, note you can enter ALT+60 in word), "\101\102\103" -> 'ABC'
# \xhh	     character with hex value hh, e.g. '\x3c' -> '<' ,  '\xA3' -> '£', "\x41\x42\x43" -> 'ABC
# \uhhhh     character (Unicode) with 16-bit hex value e.g. print('\u00a3') Returns '£'
# \Uhhhhhhhh character (Unicode) with 32-bit hex value e.g. print('\u000000a3') Returns '£'

os.linesep  # returns the newline string.   Unix = '\n', Mac = '\n', Windows  = '\r\n'
# in Windows both a CR and LF are required to note the end of a line, whereas in Linux/UNIX a LF is only required
# to convert file types see here: https://kb.iu.edu/d/acux

print("xxx'xxx") # = 'xxx\'xxx'
print('yyy"yyy') # = 'yyy\"yyy'
print ('\xA3')   # = £ = ALT-0163 on WORD



# a = r"\"  NOT VALID - CAN'T END STRING WITH ODD NUMBER OF BACKSLASHES, the 'r' tells python to include whatever follows the \ so needs another character
a = r"\""   # This is not escaped
# b = "\"   NOT VALID - CAN'T END STRING WITH ODD NUMBER OF BACKSLASHES, the second quotation is escaped leaving the need for another "
b = "\""    # This is escaped 



# x = input()  # consider that ...  \n ...  is entered
# print (x)    # displays \\n since it is expected that you did not want to enter the escape char


# ======================================================================================================================
# OLD METHOD like C's printf()  ... format is used to format display output
# ======================================================================================================================
# %s insert string, 
# %d insert decimal values, 
# %f insert floating-point values 
str1 = "Name: %s, Age: %d, Weight: %.2f kg" % ('Zara', 21, 33.3)

# ======================================================================================================================
# NEW METHOD - mystr.format() is used to format display output
# ======================================================================================================================
str1 = "xxxx{}yyyy{}zzzz".format('DAVID',3)                  # 'xxxxDAVIDyyyy3zzzz' converts number 3 to a string  
str2 = "xxxx{0}yyyy{1}zzzz".format('DAVID',3)                # 'xxxxDAVIDyyyy3zzzz'  same as above
str3 = "xxxx{1}yyyy{0}zzzz".format('DAVID',3)                # 'xxxx3yyyyDAVIDzzzz'  switched output order
str4 = "xxxx{age}yyyy{name}zzzz".format(name='DAVID',age=3)  # 'xxxx3yyyyDAVIDzzzz' reference by keyword not by order

# ======================================================================================================================
# String Alignment with str.format()
# ======================================================================================================================
a, b = 3.16985, 698
str5 = "xxxx{:5.2f}yyyy{:4d}zzzz{:.1f}xxxx".format(a,b,a)     # 'xxxx 3.16yyyy 698zzzz3.2xxxx'  float & decimal formatting
str5 = f"xxxx{a:5.2f}yyyy{b:4d}zzzz{a:.1f}xxxx"               # same as above using f-strings

str6 = "xxxx{:<6d}yyyy{:^6d}zzzz{:>6d}xxxx".format(b,b,b)     # 'xxxx698   yyyy 698  zzzz   698xxxx' left / center / right justify
str7 = '${:,d}'.format(1000000)                               # '$1,000,000'
str8 = '${:10,d}'.format(1000000)                             # '$ 1,000,000'
str9 = '${:,.2f}'.format(1000000.789)                         # '$1,000,000.79'
str10 = '\xA3{:15,.2f}'.format(1000000.789)                   # '£   1,000,000.79'


#{SELECTION:FORMATTING!CONVERSION} for .format() function

# FORMATTING : fill char alignment sign mini width.precision~maxwidth type
# < > ^ = 0 at start for filling with 0
# integer: b binary, c char, d decimal (default), o octal, x or X hexa…
# float: e or E exponential, f or F fixed point, g or G appropriate (default), 
# string: s … % percent
# {:.2f}    = f (float), 2 digits after the decimal, rounded
# {:5.2f}   = f (float),   MIN 5 digits space filled (including decimal), 2 digits after the decimal, rounded
# {:<6d}    = d (integer), MIN 6 digits space filled, left justified
# {:10,d}   = d (integer), MIN 10 digits space filled, comma separate thousands
# {:15,.2f} = f (float),   MIN 15 digits space filled, comma separate thousands, two decimal places, rounded


# CONVERSION : s=readable text - converts value using str(), r=literal representation - converts using repr()
from math import pi
"{x!r}".format(x=pi)
"{x!s}".format(x=pi)

# see here https://docs.python.org/2/library/string.html#format-specification-mini-language

# ======================================================================================================================
# f-strings (format-string modifier) new to python 3.6
# ======================================================================================================================
one = 1000
two = 5000
f'{one},{two}'  # = '1000,5000'
f'{{{one},{two}}}' # = {'1000,5000'}  note that '{{' and '}}' escape the braces within an f-string
# can use in combination with raw strings order rf or fr both work
fstr2 = fr"Check directory D:\noo\{one}\{two}"

# New to Python 3.8
# print(f'{one = }')  # this will now display 'one = 1000', will preserve whatever spaces you use around the '=' sign

variable = 12345

print(f'---{variable:<10}---')      # Left-aligned: (<), 10-digit (10)
print(f'---{variable:^10}---')      # Center-aligned: (^), 10-digit (10)
print(f'---{variable:>10}---')      # Right-aligned (>), 10-digit (10)
print(f'---{variable:10}---')       # Same as above as right align is default
print(f'---{variable:010}---')      # Zero-Pad (0), 10-digit (10)
print(f'---{variable:10,d}---')     # 10-digit (10), Comma seperated (,), interger (d), right align is default
print(f'---{variable:10,.2f}---')   # 10-digit (10), Comma seperated (,), 2.d.p (.2), float (f)
print(f'---{variable:10,}---')      # 10-digit (10), right align is default, works for float or int
print(f'---{variable:<10.2e}---')   # left-aligned (<), 10-digit (10), 2.d.p (.2),  exponential (e)

# Note the 10 represents a MINIMAL width of 10-digits which include any commas or decimal points

# ---12345     ---
# ---  12345   ---
# ---     12345---
# ---     12345---
# ---0000012345---
# ---    12,345---
# --- 12,345.00---
# ---    12,345---
# ---1.23e+04  ---


# ======================================================================================================================
# is vs ==
# ======================================================================================================================
x = 7
y = 7

x == y  # True since holds same value
x is y  # not necessarily True as x and y could be different intances with different id()


x = [1,2,3]
x = y
x is y  # True, since y is a reference to x at the same id().  Comparison for 'is'  O(1),  quicker than x == y  O(n)

x = None
y = None  # reference to the same id()
x is None  # always correct to compare a None value with 'is' since None is a singleton and can only exists once in memory

# ===============================================
# Falsey Values  (all other values are Truthy)
# ===============================================
# Empty lists []
# Empty tuples ()
# Empty dictionaries {}
# Empty sets set()
# Empty strings ""
# Empty ranges range(0)
# Integer: 0
# Float: 0.0
# Complex: 0j
# None
# False

# ======================================================================================================================
# x or y:  if x is falsey then returns y. else returns x.  In general ...
# x or y or z: returns the first Truthy value otherwise returns the last value if all are Falsey
# ======================================================================================================================
7 or 8            # returns 7
7 or {}           # returns 7
None or {}        # returns {}
None or {} or 7   # returns 7
None or () or {}  # returns {}

x, y = 0, 7

x or y            # returns 7, the first truthy value
bool(x or y)      # True if either x or y are truthy, else False


# ======================================================================================================================
# x and y:  if x is falsey return x. else return y. In general ...
# x and y and z: returns the first Falsey value otherwise returns last value if all are Truthy
# ======================================================================================================================
9 and 2          # returns 2
None and 2       # returns None
None and {}      # returns None
7 and 8 and 9    # returns 9
7 and () and 9   # returns ()

x and y           # returns 0, the first falsey value
bool(x and y)     # False if either x or y are falsey, else True


# ======================================================================================================================
# DEEP COPY vs SHALLOW COPY (from the standard library)
# https://docs.python.org/3/library/copy.html
# ======================================================================================================================
from copy import copy, deepcopy
# copy(c)→ shallow copy of container
# deepcopy(c)→ deep copy of container

l = [1,2,3,4,5,6]
s = copy(l) # equivalent to S = L[:]
l[0] = 100  # this does not affect S as you have a copy,  S remains [1,2,3,4,5,6]

# but a shallow copy will use references for the sublists...
l = [[1,2,3],[4,5,6]]
s = copy(l)
l[0][0] = 100  # this does affect S as you have a copy,  S also becomes  [[100, 2, 3], [4, 5, 6]]

# solution is to use deepcopy which traverses downwards throughout the sublists and does a full copy, no references
l = [[1,2,3],[4,5,6]]
s = deepcopy(l)
l[0][0] = 100  # this doesn't affect S as you have a deepcopy,  S remains  [[1, 2, 3], [4, 5, 6]]


# ======================================================================================================================
# LIST COMPREHENSION 	quick way to generate lists  [expression - loop - condition] in style of functional programming
#                       You can loop over multiple containers and have multiple conditions
# ======================================================================================================================
x = []
for i in range(10):
    x.append(i ** 2)
#in one line you could also do this...
x = [i**2 for i in range(10)]  # x = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

i = 4     # this value remains for 'i' after the list comprehension
x = [i ** 2 for i in range(-5, 0)]  # 'i', the control variable of the list comp. does not shadow the global value
print(i)  # return 4,  does not return 0

even_numbers = [x for x in range(0, 10) if x % 2 == 0]
[x for x in dir(str) if x.startswith('is')] # all string functions beginging with 'is'

# multiple containers
x = ['a', 'b', 'c']
y = [1, 2, 3]
cartesian_set_product = [(i, j) for i in x for j in y]
# l = []
# for i in x:
#     for j in y:
#         l.append((i,j))

# multiple conditions
list_comp = [x for x in range(1,101) if x % 3 == 0 and x % 4 == 0]  # [12, 24, 36, 48, 60, 72, 84, 96]


# ======================================================================================================================
# SET COMPREHENSION
# ======================================================================================================================
myset = {x for x in [1,2,3]}


# ======================================================================================================================
# DICTIONARY COMPREHENSION
# ======================================================================================================================
names = ['dave', 'paul', 'fred']
ages = [4,5,6]
dict_comp1 = {names[i]:ages[i] for i in range(3)}


dict1 = {1:'a', 2:'b', 3:None}
dict_comp2 = {k:v for k, v in dict1.items() if v is not None}  # example using a filter based on 'value' v
dict_comp3 = dict((k, v) for k, v in dict1.items() if k < 3)   # example using dict and a filter based on 'key' k
assert dict_comp2 == dict_comp3

# ======================================================================================================================
# TUPLE, DICTIONARY & LIST UNPACKING see more in bezPy02_Exceptions.py
# ======================================================================================================================
t = (1, 10, 2)

print(t)   # (1, 10, 2)
print(*t)  # 1 10 2

r = range(*t) # equivalent to range(1, 10, 2) which gives (1, 3, 5, 7, 9)
# calling function(*t) will pass the tuple values as arguments
# note variable unpacked could also be a list

x, y, z = t  # sets x=1, y=10, z=2
x, _, z = t  # sets x=1, z=2


# concatenate tuples
x = 1, 2, 3
y = 5, 6, 7
z = x + (4,) + y      # z = (1, 2, 3, 4, 5, 6, 7)  NOTE: (4) is recognized as int, (4,) as a tuple
z = *x, 4, *y         # z = (1, 2, 3, 4, 5, 6, 7)

# print(*z)
# 1 2 3 4 5 6 7
# print(z)
# (1, 2, 3, 4, 5, 6, 7)

# one element tuple use comma
country = ('Australia')   # assigns country to a string
country = ('Australia',)  # assigns country to a one element tuple

a,b,_ = (1,2,3)  # ignores the last value
a,b,*_ = (1,2,3,4,5) # ignores all the last values


n = (1, 2, 3, 4, 5)
first_num, *middle_nums, last_num = n
# first_num = 1
# middle_nums = [2,3,4]
# last_num = 5

# Use underscore to indicate unwanted
n = (1, 2, 3, 4, 5)
first_num, *_, last_num = n
# first_num = 1
# last_num = 5


l1 = [1, 2, 3]
l2 = [5, 6, 7]
[*l1]   # [1, 2, 3]
(*l1,)  # (1, 2, 3)
[*l1, 4, *l2, 10]    #  [1, 2, 3, 4, 5, 6, 7, 10]
(*l1, 4, *l2, 10)   #   (1, 2, 3, 4, 5, 6, 7, 10)


style = {'bg':'white', 'fg':'black', 'font':'none 12 bold'}
# calling function(**style) will pass the dict values as keyword arguments 
# where  bg=white, fg=black e.t.c

d1 = {'a': 1, 'b': 2}
d2 = {'d': 4}

{**d1}                 # same as d1 = {'a': 1, 'b': 2}
{**d1, 'c': 3, **d2}   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d1 |  {'c': 3} | d2    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}   as of 3.9

# ======================================================================================================================
# VALUE ASSIGNMENT & SWAPPING (SHORT CUT)
# ======================================================================================================================
x, y = 5, 6   # is shorthand for ...
(x, y) = (5, 6)

# and is the same as ...
x = 5
y = 6

x, y = y, x  # swaps values so that x = 6 & y = 5, without using a 3rd variable


# ======================================================================================================================
# DICTIONARY  dicts are like associative arrays, maps, hashmaps, lookup tables
# see bezpy_81_collections.py for discussion on dict vs OrderedDict
# ======================================================================================================================
d = {'UserName':'davidj','Password':'eabcd','Index':4} # common way to assign dictionary
d2 = dict(a=3, b=4, k='v') # Keywords. equivalent to {'a': 3, 'b': 4, 'k': 'v'} but not very readable
d3 = dict([(3,"three"),(1,"one")]) # List of tuples. equivalent to {1:'one',3:'three'}
d4 = dict(zip(('a','b','c'),(1,2,3))) # zip function

# Note the key must be hashable/immutable.  so a list can not be a key as you can modify it.
d['Row']=44  # add to the dictionary
d['Col']=33

d['UserName']         # returns: davidj
print(d.keys())       # returns: dict_keys(['UserName', 'Password', 'Index' ... ])
print(d.values())     # returns: dict_values(['davidj', 'eabcd', 4 ... ])
print(d.items())      # returns: dict_items([('UserName', 'davidj'), ('Password', 'eabcd'), ('Index', 4), ...])

for i in d.keys():  # <class 'dict_keys'>  THIS IS ACTUALLY DEFAULT BEHAVIOR.  for i in d: will loop the keys
  print(i)

for i in d.values(): # <class 'dict_values'>
  print(i)

for k, v in d.items():  # <class 'dict_items'>
  print(k,"-->",v)

list1 = sorted(d.keys()) # returns keys alphabetically as list
# list1 = ['Col', 'Index', 'Password', 'Row', 'UserName'] 'x' is not modified

list2 = sorted(d.items()) # returns items alphabetically as list of tuples ordering by the key values
# list2 = [('Col', 33), ('Index', 4), ('Password', 'abcd'), ('Row', 44), ('UserName', 'davidj')]

# list3 = list(reversed(d.items()))
# list3 = [('Col', 33), ('Row', 44), ('Index', 4), ('Passxword', 'eabcd'), ('UserName', 'davidj')]

{'a':1,'b':2,'c':3}['c']  # this prints out the 3 (can use this for a switch statement)
{'c':1,'b':2,'c':3}['c']  # this is unpredictable as the keys are not mutually exclusive

# y = d['title'] this returns a KeyError as 'title' does not exist in the dictionary
y = d.get('title') # returns dictionary value or  None if KeyError, does not modify dictionary 'd'
y = d.get('title', 'Mr.') # returns dictionary value or  'Mr.' if for KeyErro, does not modify dictionary 'd' 
z = d.setdefault('title', 'Mr.') # same as get() but if None then  adds 'title':'Mr.' to dictionary and returns z = 'Mr.'
                                 # else just returns the existing value of the key in the dictionary

d = {1:'one', 2:'two'}
d2 = {3:'three', 4:'four'}

3 in d2.keys() # = True  (note  d2.has_key(3) has DEPRECATED, use 'in' operator instead
3 in d2        # = True  (ONLY CHECKS KEYS)
3 in d2.values() # = False
'three' in d2          # = False (ONLY CHECKS KEYS)
'three' in d2.values() # = True


# As alternative to 'in' operator you can use try/except
try:
    d[3]
except KeyError:
    print("No such Key")

# However 'get' and 'setdefault' are better to use
d.get(3, 'return this value if key is missing')
d.setdefault(4, 'set key to this value if key is missing')

d.update(d2) # Modifies d by appending dictionary d2's key-values pairs to dict d 'in-place'

d2.pop(3)    # removes key, value entry with key=3, returns value 'three'
# d2.pop(5)  # would give a KeyError
d.pop(5, 'Warning Message: 5 is not present in dictionary')  # Will not give key error if 5 is not a key


# =================================================================================
# DICTIONARY METHODS  # https://www.w3schools.com/python/python_ref_dictionary.asp
# =================================================================================
# del d[k]             # removes entry with key value
# len(dict)            # Gives the total length (number of items) in the dictionary.
# str(dict)            # Produces a printable string representation of a dictionary

# d.keys()             # returns a set-like object providing a view on D's keys
# d.values()           # returns an object providing a view on D's values
# d.items()            # returns a set-like object providing a view on D's keys & values

# del d[k]             # deletes key 'k' from dictionary and does not return any value, not even none
# d.pop(k[,v2])        # removes specified key, k, and returns associated v.   If key is not found, v2 is returned if suppled, otherwise KeyError is raised
# d.popitem()          # Returns tuple (k, v), remove and return some arbitrary (key, value) but raise KeyError if d is empty
# d.clear()            # clears all entries
# d.copy()             # Returns a shallow copy of dictionary dict
# d.get(key, default=None)        # For 'key', returns 'value' or 'default' if key not in dictionary
# d.setdefault(key, default=None) # Similar to get(), but will set dict[key]=default if key is not already in dict
# dict1.update(dict2)                # UPDATE in place - Adds dictionary dict2's key-values pairs to dict1, updating dict1 inplace with values in dict2 for the conflicting keys, returns None
# dict1 |= dict2                     # Same as above, as of python 3.9 updates can be performed with operator '|='
# d3 = {**d1, **d2}                  # MERGE of d1 & d2 to create a NEW dictionary, for conflicting keys, values in d2 are used
# dict3 = dict1 | dict2              # as of python 3.9 the merge operator can be used instead of dictionary unpacking above

x = ('key1', 'key2', 'key3')
d4 = dict.fromkeys(x, 5)  # Returns {'key1': 5, 'key2': 5, 'key3': 5}
d4 = dict.fromkeys(x)     # Returns {'key1': None, 'key2': None, 'key3': None}
# dict.fromkeys(iterable_of_keys,value)  # Returns dictionary with keys from list of keys and ALL values set to value  (all have the same value).
                                         # note that dict.fromkeys(keylist) will set ALL values to 'None'
# there is no dictionary reverse lookup function , you would need to loop through d.items() to find value and associated key

# ======================================================================================================================
# generate dictionary of keys/values with zip
# ======================================================================================================================
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict1 = {k:v for k, v in zip(keys, values)}

# ======================================================================================================================
# Remove duplicate dictionaries in a list
# ======================================================================================================================
# type dict is not hashable, elements of a set need to be hashable, so set(x) won't work, convert dict to tuple instead
def remove_dupes_from_dict(x):
    return [dict(t) for t in {tuple(d.items()) for d in x}]

x = [{'a': 1, 'b': 1}, {'a': 2, 'b': 2}, {'a': 1, 'b': 1}]
remove_dupes_from_dict(x)   #  [{'a': 1, 'b': 1}, {'a': 2, 'b': 2}]

# ======================================================================================================================
# Using Dictionaries for SWITCH function
# ======================================================================================================================
def switch(x):
    """ this acts as a switch function for discrete cases """
    return {'Sun': 1,'Mon': 2,'Tue':3,'Wed':4,'Thu':5,'Fri':6,'Sat':7}[x]
switch('Mon') # this returns 2 


def switch2(c):
    """ this acts as a switch function in other languages for cases within a range """
    return  { c < 0    : 'A',
            0 <= c < 1 : 'B',
            1 <= c < 2 : 'C',
            2 <= c < 3 : 'D',
            3 <= c     : 'E' }[True]
    
switch2(2.3) # returns 'D'

def switch3(x):
    """ this acts as a switch function in other languages for cases within a range """
    return  { \
        x in {1,2,3}   : 'A',
        x in {4,5,6}   : 'B',
        x > 6          : 'C',
       }[True]
    
switch3(5) # returns 'B'

def switch4(x):
    """ this acts as a switch function in other languages for cases within a range """
    return  {
        x in {1,2,3}   : 2*x,
        x in {4,5,6}   : 3*x,
        x > 6          : 20,
       }[True]

switch4(5) # returns 15

# see bezpy_92_radon.py  Reduce Cyclomatic Complexity

# ======================================================================================================================
# match, case keywords introduced in python 3.10   
# ======================================================================================================================
# def get_mood(day):
#     match day:
#         case 'Monday':
#             return 'Oh...'
#         case 'Thursday':
#             return 'Getting close!'
#         case 'Friday':
#             return 'Almost there!'
#         case 'Saturday' | 'Sunday':  # OR operator
#             return 'Weekend!!!'
#         case _:                      # default case with underscore
#             return 'Meh...'
#
# get_mood('Wednesday')
# >> 'Meh...'
#
#
#
# def alarm(item):
#     match item:
#         case [x, y] if x == y:
#             print(f'first value = second value and is {y}')
#         case [x, y]:
#             print(f'first value is {x}, second is {y}')
#         case [x, _, z]:
#             print(f'first value is {x}, third is {z}')
#         case[('a' | 'b') as first, _, _, _]:
#             print(f'first value is {first}')
#         case [a,b,c,d, *e]:
#             print(f'fifth value onwards {e}')
#
# alarm([1,2])
# >> first value is 1, second is 2
# alarm([1,2,3])
# >> first value is 1, third is 3
# alarm(['a', 1,2,3])
# >> first value is a
# alarm([1,2,3,4,5,6,7,8])
# >> fifth value onwards [5, 6, 7, 8]


# match is structural pattern matching, not a switch statement
# it matches by structure, not by value.
# So the first case will match any 2 item tuple
# def match_test(point: tuple):
#     match point:
#         case (x, y):
#             return (x+1, y+1)
#         case (100, 100):
#             return (x, y)
#
# match_test((100,100))  # Returns (101, 101) the first PATTERN is matched

# ======================================================================================================================
# zerofiller(): fills in house number with trailing zeros e.g. '14' -> '14000'
# ======================================================================================================================
def zerofiller(x):
    return { len(x) == 5 : x,
             len(x) == 4 : x + '0',
             len(x) == 3 : x + '00',
             len(x) == 2 : x + '000',
             len(x) == 1 : x + '0000'}[True]

# Note would use zfill string function

# ======================================================================================================================
# CLASSES CODE see mylib\bezpy_customer.py
# ======================================================================================================================
from mylib.bezpy_customer import Customer 	  #imports 'class Customer' from mylib\bezpy_customer.py

x = Customer('Jeff Knupp',"Bronze",1000.0, 85000)

# ======================================================================================================================
# CLASS INHERITANCE  see mylib\bezpy_parent_child.py
# ======================================================================================================================
from mylib.bezpy_parent_child import Parent, Child  #imports 'classes Parent & Child' from mylib\bezpy_parent_child.py

p = Parent('Papa')               # calls parent constructor 
c = Child('Fred', 2019)          # calls child & parent constructor

# ======================================================================================================================
# Remove unwanted final comma for single entry tuples
# ======================================================================================================================

def remove_final_comma(t: tuple) -> str:
    return '(' + ','.join([str(x) for x in t]) + ')'

t = (444, 555)
str(t)                  # '(444, 555)' < -- fine
remove_final_comma(t)   # '(444,555)'  < -- fine


t = (444,)   # single entry
str(t)                  # '(444,)'  < -- unwanted comma
remove_final_comma(t)   # '(444)'   < -- solution

# ======================================================================================================================
# String To Bool.  See python Notes doc for distutils common useage
# ======================================================================================================================
from distutils.util import strtobool

for value in ('False', 'false', 'F', 'f', '0'):
   assert strtobool(value) == 0

for value in ('True', 'true', 'T', 't', '1'):
   assert strtobool(value) == 1

