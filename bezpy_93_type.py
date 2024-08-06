# ======================================================================================================================
# Type Hinting or Annotation  -  Introduced in Python 3.0 and in the standard library since Python 3.5
# Does not give error/warning, only hints at data type
# Updated in python 3.9 & 3.10
# ======================================================================================================================
# https://peps.python.org/pep-0484/  PEP 484 – Type Hints
# ======================================================================================================================
# can use type checker tool 'pip install mypy'  (also see pytype, pyright, pyre)
# Run `mypy fileame.py` - will fail if you have typing issues
# ======================================================================================================================
# Type Alias	Built-in Type
# ======================================================================================================================
# List	        list       (see List vs list below)
# Tuple	        tuple      (see Tuple vs tuple below)
# Dict	        dict       (see Dict vs dict below)
# Set	        set        (see Set vs set below)
# FrozenSet	    frozenset
# Iterable      For any iterable collection.  e.g. list, tuple
# Sequence	    For list, tuple, and any other sequence like data type
# Mapping	    Includes, dict, set, frozenset, and any other mapping data type
# ByteString	bytes, bytearray, and memoryview types.
# NoReturn      return type for functions that are expected to raise an exception and not return a value or None
# ======================================================================================================================
# Tutorial: https://youtu.be/QORvB-_mbZ0
# ======================================================================================================================

import datetime
from decimal import Decimal
# ======================================================================================================================
# type hinting in variables that don't require type imports 
# ======================================================================================================================

# declare type, then initialize
x: int   
x = 5

# Primitives - declare & initialize
int_var: int = 5
float_var: float = 22/7
str_var: str = 'xxx'
bool_var: bool = True

# containers - declare & initialize
dict_var: dict = {1: 'one'}
list_var: list = ['1', '2']
set_var: set = {1, 2, 3}
tuple_var: tuple = (1, 2, 3)

# date - declare & initialize
date_var: datetime.datetime = datetime.datetime(2021, 1, 1, 3, 13, 44)
dt_var: datetime.date = datetime.date(2021, 1, 1)

# ======================================================================================================================
# type imports - List, Tuple, Dict, Set, ByteString
# ======================================================================================================================
from typing import List, Tuple, Dict, Set, ByteString

h: list = ['a', 'b', 'c']                 # not specifying contents of list
i: List[str] = ['a', 'b', 'c']            # list of strings, note List[str, str, str] is incorrect
j: tuple = (1, 2, 'abc')                  # not specifying contents of tuple
k: Tuple[int, int, str] = (1, 2, 'abc')   # specifying contents of tuple
l: Tuple[int, int, int] = (1, 2, 3)       # tuple of 3 ints, note Tuple[int] is incorrect
m: dict = {1: 'one'}                      # not specifying type of keys, values
n: Dict[int, str] = {1: 'one', 2: 'two'}  # specifying keys(int), values(str)
o: set = {1, 2, 3}                        # not specifying content type of set
p: Set[float] = {1.1, 2.2, 3.3}
q: ByteString = b'xxx'

# ======================================================================================================================
# type annotation in function parameters / return values
# ======================================================================================================================

# input & output type int
def add2(a: int, b: int) -> int:
    return a + b

# output type None
def add_numbers(num1: int, num2: int) -> None:
    print(num1 + num2)

# output type None is implicit
def bonus(base: int):
    print(f"Your Bonus is ${base*3}")

# can set default values in parameters and function variables
def f1(x: float = 3.14) -> bool:
    y: float = 0.1
    return x == y

# unspecified list type
def f2(x : list) -> list:
    pass


# list of specific types
from typing import List
# input: list of strings, output is  None
def greet_all(names: List[str]) -> None:
    for name in names:
        print("Hello", name)


# NEW TO 3.9, no longer need to import 'List' (capital-L), for a list of types  
# can just use 'list' and it is recognized

# Before 3.9
# def main(numbers: List[int]) -> None:
#   print(numbers)

# With 3.9
# def main(numbers: list[int]) -> None:
#   print(numbers)

# Note that list[int] or List[int] (before 3.9) is an example of a 'GenericAlias'

from typing import List, Tuple, Dict, Set
def f3(w: Set[int], x: List[str], y: Tuple[int, int, int], z: Dict[str, int]):
    pass

# ======================================================================================================================
# __name__
# ======================================================================================================================
d = datetime.date(24, 1, 1)

type(None)                # <class 'NoneType'>
type(None).__name__       # 'NoneType'
type(3)                   # <class 'int'>
type(3).__name__          #  'int'
type(d).__name__          # 'date'
type(type(3))             # <class 'type'>
type(type(3)).__name__    # 'type
# ======================================================================================================================
# _GenericAlias
# ======================================================================================================================
from typing import _GenericAlias
from typing import List, Tuple, Dict, Set, FrozenSet, Iterable, Sequence, Mapping, ByteString

isinstance(float, _GenericAlias)  # False
for type_alias in (List, Tuple, Dict, Set, FrozenSet, Iterable, Sequence, Mapping, ByteString):
    isinstance(type_alias, _GenericAlias)  # True for all above


# ======================================================================================================================
# Union - type hinting for alternative outputs
# ======================================================================================================================
from typing import Union
def bonus2(base: Union[int, float]):
    print(f"Your Bonus is ${base*3}")

# Version 3.10 improved syntax
# def bonus(base: int|float):
#     print(f"Your Bonus is ${base*3}")

# ======================================================================================================================
# custom classes type annotation
# =====================================================================================
from dataclasses import dataclass

@dataclass
class ClassOne:
    value1 : int
    pass

@dataclass
class ClassTwo:
    value1: ClassOne  # this is allowed since ClassOne was defined above
    pass


# Forward Referencing requires quotation marks since BinaryTree has not been defined yet
@dataclass
class BinaryTree:
    node: int
    left: 'BinaryTree'    
    right: 'BinaryTree'
    pass

@dataclass
class AnotherTree:
    left: BinaryTree   # this is allowed since defined above
    right: BinaryTree  # this is allowed since defined above

# ======================================================================================================================
# ClassVar - annotation to declare a class variable
# ======================================================================================================================
from typing import ClassVar
@dataclass
class Car:
    seats: ClassVar[int] = 4            # class variable
    passengers: ClassVar[List[str]]     # class variable
    color_code: int                     # instance variable 
    specs: List[str]                    # instance variable

# ======================================================================================================================
# Any - the catch-all data type
# ======================================================================================================================
from typing import Any
def f5(input: Any) -> Any:
    pass

# ======================================================================================================================
# Optional - type annotation means that 'x' can take a float or None
# ======================================================================================================================
from typing import Optional
def f6(x: Optional[float] = None):
    pass


x2 = Optional[int]   #  Created Type Alias (see Aliases below) == Union[int, NoneType]
x2                   #  returns typing.Union[int, NoneType]
x2.__origin__        #  returns typing.Union
x2.__args__          #  returns (<class 'int'>, <class 'NoneType'>)
isinstance(3, x2.__args__)       # True
isinstance(None, x2.__args__)    # True

# ======================================================================================================================
# Aliases - Custom type annotations
# ======================================================================================================================
x3 = List            # created Type alias
x3                   # returns typing.list
x3.__origin__        # returns <class 'list'>

# Type aliases
Vector = List[int]  # create Type Vector
Vector.__origin__   # returns <class 'list'>
def g4(x: Vector) -> Vector:
    pass

g4([1,2,3,4])  # this will pass 'mypy'


# ======================================================================================================================
# NewType - for user defined datatypes using NewType (not quite the same as aliases)
# ======================================================================================================================
from typing import NewType

# Create a new user type called 'Vector2'
Vector2 = NewType('Vector2', List[int])
# Vector2 is not equivalent to List[int], it is a subset of List[int] (see example below)

assert Vector2([1,2,3]) == [1,2,3]  # This passes, 


def g5(x: Vector2) -> None:
    pass

g5([1,2,3,4]) # will not give an error but will fail mypy since needs to be specifically of type Vector2, not just any List[int]
g5(Vector2([1,2,3])) # this would pass


dec_type = NewType('dec_type', List[Decimal])

def make_list(d: dec_type) -> dec_type:
    result = []
    for i in d:
        result.append(i + Decimal('0.1'))
    return result        

assert make_list([Decimal('1.1'), Decimal('1.2')]) == [Decimal('1.2'), Decimal('1.3')]

if hasattr(dec_type, '__supertype__'):
    type=dec_type.__supertype__

# dec_type == <function NewType.<locals>.new_type at 0x000001A9A3F9B318>
# type == typing.List[decimal.Decimal]


# ======================================================================================================================
# NoneType Alias
# ======================================================================================================================
NoneType = type(None)  # previously you would do 'from types import NoneType', but deprecated
nt: NoneType = None


# ======================================================================================================================
# MappingProxyType: a read only proxy for mapping objects e.g. the dict object.  Not sure why it is useful
# ======================================================================================================================
from types import MappingProxyType
d = {'a': 1, 'b': 2}
m = MappingProxyType(d)
m['a']


# ======================================================================================================================
# Callable - for a function that takes a function as a parameter
# ======================================================================================================================

# e.g. say your function takes two integers and returns an integer (like 'add2' above)
from typing import Callable

def f8(func: Callable[[int, int], int]) -> None:
    pass

# ======================================================================================================================
# Iterator
# ======================================================================================================================
from typing import Iterator
def iter(limit: int) -> Iterator[int]:
    for i in range(limit):
        yield i


# ======================================================================================================================
# get_type_hints - to return typing hints as a dictionary
# ======================================================================================================================
from typing import get_type_hints

def f9(x: int, y: int) -> int:
    pass

get_type_hints(f9)  # returns {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}


# ======================================================================================================================
# TypeVar 
# ======================================================================================================================
from typing import TypeVar
T = TypeVar('T')  # this is a generic type can take any type. Can set an upper bound eg. TypeVar('T', bound=<type>)

# this function is annotated such that the output must be the same 'generic type' as the input,  Any -> Any would be too generic
def g9(x: T) -> T:
    return x

# ==================================================
# Before 3.11
# ==================================================
from typing import TypeVar
TPerson = TypeVar('TPerson', bound='Person')

class Person:
    def update_name(self: TPerson, name: str) -> TPerson:
        self.name = name
        return self

# ==================================================
# After 3.11
# ==================================================
# from typing import Self
# class Person:
#     def update_name(self, name: str) -> Self:
#         self.name = name
#         return self
# this will work before 3.11 only if you add   'from __future__ import annotations' 

# ======================================================================================================================
# TypeVar with Generic - see https://rogulski.it/blog/python-typing-with-generic-typevar/
# ======================================================================================================================
from typing import TypeVar, Generic

TV = TypeVar('TV')

class Publisher(Generic[TV]):

    def publish(self, msg: TV):
        pass

p1 = Publisher[str]()  # Now TV must always by str
p1.publish('x')

q2 = Publisher[int]()  # Now TV must always by int
q2.publish(1)

# ======================================================================================================================
# Annotations
# ======================================================================================================================
# as of 3.9 from typing import Annotations


# ======================================================================================================================
# Type  see two uses below
# ======================================================================================================================
from typing import Type 

# example 1 - behaves like 'type' 
isinstance(int, type)  # returns True

data_type: Type
data_type = int

isinstance(data_type, Type)  # returns True
isinstance(data_type, type)  # This will also return True

# example for 2nd use of 'Type'
class Animal:
    def __init__(self, *, name: str):
        self.name = name

class Cat(Animal):
    pass

class Dog(Animal):
    pass


# input1 = the 'class' Animal or subclass, input2 = string,  
# Output = instance of class Animal (or subclass)
def make_animal(animal_class: Type[Animal], name: str) -> Animal:
    return animal_class(name=name)

animal = make_animal(Dog, "Kevin")   # will generate a Dog('Kevin')


# this function takes the string 'class' as an input
def another_fn(input: Type[str]):
    pass


# ======================================================================================================================
# typing.Annotated: as of python 3.9
# On its own Annotated does not do anything other than assigning extra information (metadata) to a reference.
# It is up to another code, which can be a library, framework or your own code,
# to interpret the metadata and make use of it. For example, FastAPI uses Annotated for data validation.
# Sphinx can use them for documenting acceptable argument types and return value types of functions.
# ======================================================================================================================
from typing import Annotated

# assign a to be the Annotation
a = Annotated[str, "this is just metadata"]
a.__metadata__  #  ('this is just metadata',)
a   # typing_extensions.Annotated[str, 'this is just metadata']

# assign b as an integer with an annotation
b: Annotated[str, "this is just metadata"] = 5


def func3(query: Annotated[str, "this is a querystring"]):
    pass




