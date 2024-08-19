# TRY THIS: https://medium.com/better-programming/5-pairs-of-magic-methods-in-python-you-should-know-f98f0e5356d6
# TRY THIS: https://towardsdatascience.com/how-to-be-fancy-with-python-part-2-70fab0a3e492?source=bookmarks---------64----------------------------
# TRY https://medium.com/swlh/welcome-to-python-meet-the-dunders-41026b2a7e36?source=bookmarks---------1----------------------------
# TRY https://betterprogramming.pub/advanced-python-concepts-257076fa8e35


# ======================================================================================================================
# monkeypatch
# ======================================================================================================================
# The term monkeypatch in python refers to dynamic modifications of a class or module at runtime, adding attributes or methods
# For instance, consider a class that has a method get_data. This method does an external lookup 
# (on a database or web API, for example), and various other methods in the class call it. However, in a unit test, 
# you don't want to depend on the external data source - so you dynamically replace the get_data method with a stub 
# that returns some fixed data. Because Python classes are mutable, and methods are just attributes of the class, 
# you can do this as much as you like - and, in fact, you can even replace classes and functions in a module in exactly the same way.
# e.g. 
# from SomeOtherProduct.SomeModule import SomeClass

# def speak(self):
#     return "ook ook eee eee eee!"

# SomeClass.speak = speak

# ======================================================================================================================
# objects are instances of classes, classes are themselves instances of metaclasses (see below)
# In object-oriented programming (OOP), a factory is an object for creating other objects
# In computer programming, 'cohesion' refers to the degree to which the elements inside a module/class belong together
# In software engineering, 'coupling' is the degree of interdependence between software modules
# Interface-based programming, also known as interface-based architecture, is an architectural pattern for implementing
#   modular programming at the component level, in an oop language which does not have a module system e.g. Java
#   To put it simply, an interface is a contract. This contract states the behavior of some component.  An interface is
#   an abstract type that defines the methods that need to be implemented by any objects that use the interface.
#   It defines the interaction between components that use the interface.  In python an interface is essentially
#   equivalent to an abstract class.  The distinction OOP Interface vs OOP Abstract Class is relevant for Java not Python.
#   Say for a example two objects implement an interface that require __len__ and __index__ functions.
# ======================================================================================================================

# __new__ Constructor: accepts cls as its first parameter, you actually don't have an instance yet, therefore no self exists at that moment, returns instance of the class after allocating memory
# __init__ Initializer: accepts self, called after __new__ and the instance is in place, so you can use self with it. __init__ must return None




class B:
    def __new__(cls, *args, **kwargs):   # CONSTRUCTOR - technically you are overriding object.__new__(cls)
        """handles object creation - called before initialisation"""
        print("Creating instance of the class")
        return super().__new__(cls)  # Equivalent to return object.__new__(cls) as you are inheriting from the 'object' base class

    def __init__(self, *args, **kwargs):  # INITIALIZER - technically you are overriding object.__init__()
        """handles object initialisation"""
        print("Init is called")

# The above class would be the same if __new__ and __init__ were used implicitly, under the hood.
# __new_ is called first by the class, returns and instance. That instance is passed to __init__

# The below sample would work the same ...
# class B:
#    pass

b = B()


# ======================================================================================================================
# The Singleton Class
# ======================================================================================================================
# in mathematics a singleton is a set with a single element
# in computing a singleton is a class that allows only one instance
# ======================================================================================================================
class Singleton:
    def __init__(self, cls):
        self._cls = cls

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@Singleton  # Only one instance of DBConnection can now be generated, protecting you from multiple instances
class DBConnection(object):
    def __init__(self):
        """Initialize your database connection here."""
        pass

    def __str__(self):
        return 'Database connection object'


x = DBConnection.instance()
y = DBConnection.instance()
print(id(x) == id(y), x is y)   # True True


# ======================================================================================================================
# Using __new__ to create a singleton class
# ======================================================================================================================

class Language:
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if cls._singleton == None:
            print('__new__ called creating an instance of the class')
            new_instance = super().__new__(cls)
            cls._singleton = new_instance
        return cls._singleton

    def __init__(self, lang, year):
        print('__init__ called initializing an instance of the class')
        self.lang = lang
        self.year = year


l1 = Language('French', 1991)
l2 = Language('Dutch', 1992)

print(f'{l1.lang=}')
print(f'{l1.year=}')
print(l1 is l2 is Language._singleton)

# __new__ called creating an instance of the class
# __init__ called initializing an instance of the class
# __init__ called initializing an instance of the class
# l1.lang='Dutch'
# l1.year=1992
# True

# ======================================================================================================================
# @dataclass introduced in python 3.7, for data oriented classes (as opposed to behavior oriented classes which focus on methods)
# https://docs.python.org/3/library/dataclasses.html
# With the @dataclass decorator you can use a Class like a dictionary so as to use the dot notation to retrieve values
# __init__ is auto-generated
# __repr__ is auto-generated, so print(Card) returns Card(rank='Q', suit='♠') which is prettier than normal classes which just return an address
# __eq__() is auto-generated, so card1 == card2 returns boolean
# the datatypes are equivalent to 'Type Hinting' and are not enforced
# The __post_init__ method is specific to the dataclasses library, because the __init__ method on dataclass classes is
# generated and overriding it would entirely defeat the purpose of generating it in the first place
# ======================================================================================================================

# Original implementation before dataclasses. These 3 methods are now auto-generated
# class Card1:
#
#     def __init__(self, rank: str, suit: str):
#         self.rank = rank
#         self.suit = suit
#
#     def __repr__(self):
#         return f'Rank = {self.rank}, Suit = {self.suit}'
#
#     def __eq__(self, card):
#         return self.rank == card.rank and self.suit == card.suit


from dataclasses import dataclass


@dataclass
class Card:
    rank: str   # this is an instance variable, without the decorator it would be a class variable
    suit: str   # this is an instance variable, without the decorator it would be a class variable


queen_of_spades = Card('Q', '♠')  # initialize instance  of  Card(rank='Q', suit='♠')
print(f'Your Card is: {queen_of_spades.rank} of {queen_of_spades.suit}')
# Your Card is: Q of ♠


# You can also set attributes immutable in dataclass via frozen=True
@dataclass(frozen=True)
class Transaction:
    sender: str
    receiver: str
    date: str
    amount: float

record = Transaction(sender="Tim", receiver="Fred", date="2020-06-08", amount=100.0)
# >>> record.sender='Pete'
# >>> dataclasses.FrozenInstanceError: cannot assign to field 'sender'

# The datatypes are not enforced. however if they are unknown you will need to make them a string e.g.
#  value : 'my_unknown_type'

# ======================================================================================================================
# dataclass introduced in python 3.7, before that you can install library 'attrs' for similar behavior
# ======================================================================================================================
@dataclass
class Person:
    name: str
    age: int

    @classmethod
    def generate_fred(cls):
        _dict = {'name': 'Fred', 'age': 15}
        return cls(**_dict)

p = Person.generate_fred()  # returns Person(name='Fred', age=15)     
# ===================================================================

from dataclasses import dataclass, field
# Note the default_factory must be a 0-argument function called to initialize a field's value
from random import choice
def factory_01():
    return choice([1, 2, 3])

@dataclass
class Member:
    name: str
    age: int
    iq: int = 100
    language1: str = 'English'
    language2: str = field(default='French')                  # set default value, like language1, did not need 'field()'
    language3: str = field(repr=False, default='Hebrew')      # set default value, like language2, but will not be represented in REPL or printout
    can_vote: bool = field(init=False)                        # don't set in __init__ so you can evaluate in __post_init__, or you can use this to force a default value and block intialization of the value
    group: str = field(default_factory=factory_01)            # this allows you to use a factory function
    email_addresses: list[str] = field(default_factory=list)  # for this default, we need field(), see explanation below

    def __post_init__(self):                        # this is run immediately after initialization of the other fields
        print('called __post_init__ method')
        self.can_vote = 18 <= self.age <= 70        # sets can_vote = True if conditions are met

m = Member('Jane Doe', 25)   # Member(name='Jane Doe', age=25, iq=100, language1='English', language2='French', can_vote=True, group=3, email_addresses=[])
m = Member(name='Jane Doe', age=25, iq=200, language2='Japanese', group=4)
Member('Jane Doe', 25, 23, group='Fred')   # Member(name='Jane Doe', age=25, iq=23, language1='English', language2='French', can_vote=True, group='Fred', email_addresses=[])

# Member(name='Jane Doe', age=25, can_vote=True) this will give TypeError as can_vote can not be initialized

# ======================================================================================================================
# problem with initializing with a mutable value. Python evaluates the default values when the script is interpreted at
# start of the run. see example below
# ======================================================================================================================
class Member3:
    def __init__(self, l: list[int] =[]):
        self.l = l

x = Member3()
y = Member3()

x.l.append(3)
# >>> x.l  # returns [3]
# >>> y.l  # returns [3]  --- should still be empty

# Solution is to use the default_factory
@dataclass
class Member4:
    l: list[int] = field(default_factory=list)

x = Member4()
y = Member4()

x.l.append(3)
# >>> x.l  # returns [3]
# >>> y.l  # returns []  --- worked !!!



from dataclasses import dataclass, field, asdict, astuple, is_dataclass


@dataclass(order=True)   # order=True  will now support the '>' and '<' operators by auto generating __lt__, __le__, __gt__, __ge__
class Person:
    first_name: str = "Ahmed"
    last_name: str = "Besbes"
    age: int = 30
    job: str = "Data Scientist"
    sort_index: int = field(init=False, repr=False)    # this helps define the sort order
    def __post_init__(self):
        self.sort_index = self.age

p1 = Person(age=30)
p2 = Person(age=20)

p1 > p2  # True


asdict(p1)    # {'first_name': 'Ahmed', 'last_name': 'Besbes', 'age': 30, 'job': 'Data Scientist', 'sort_index': 30}
astuple(p1)   # ('Ahmed', 'Besbes', 30, 'Data Scientist', 30)

is_dataclass(Person)  # True
is_dataclass(p1)      # True

# ======================================================================================================================

@dataclass(kw_only=True)   # as of 3.10, kw_only enforces intialization only with keywords, match_args=True allows for pattern matching (default setting)
class Person2:
    name: str
    age: int

# Person2('Fred', 12)  -- gives TypeError
Person2(name='Fred', age=12)

# ======================================================================================================================
class A:
    static_var = 'Jesus'  # static class variable belongs to all instances

    def __init__(self, name):
        self.name = name

    def foo(self):
        'This is a usual object method'
        print (f'name={self.name}')
        print(f'static_var={self.__class__.static_var}')  # can still access class variables this way
        print('executed foo()')
   
    @classmethod
    def class_foo(cls):
        'Can call by class or instance but will implicitly be called by class either way'
        print (f"cls.__name__={cls.__name__},  executed class_foo()")

    @staticmethod  # Treated as a normal function that was not called by class or instance
    def static_foo():
        'This is a static class method'
        print(f"Executing static_foo()")
 



a = A('John')   # Declare instance

a.foo()         # Call instance method
A.class_foo()   # Class method called by class but REQUIRES decorator @classmethod
a.class_foo()   # same as above, and will treat as if called by the class, not an instance
# ======================================================================================================================
a.static_foo()  # same as below whether called by class or instance but REQUIRES declaraion @staticmethod
A.static_foo()  # same as above whether called by class or instance
print (a.static_var, A.static_var)

# John executed foo()
# cls.__name=A,  executed class_foo()
# cls.__name=A,  executed class_foo()
# executing static_foo()
# executing static_foo()
# Jesus Jesus


a.__class__              # <class '__main__.A'>  i.e. <class 'A'>
a.__class__.static_var   # 'Jesus'
A.__class__              # <class 'type'>
A.static_var.__class__   # <class 'str'>
A.foo.__class__          # <class 'function'>



# ======================================================================================================================
# MRO (Method Resolution Order) denotes how Python or a programming language in general resolves a method or attribute
#     due to mro, python does not have an issue with the diamond problem. i.e. When an instance of Class W calls the
#     .go() method, it will be inherited from class Y,  not from class Z
# also see __mro_entries__
# ======================================================================================================================
#        X
#       /\
#      /  \
#     Y    Z
#     \   /
#      \ /
#       W
# ======================================================================================================================

class X:
     def bin(self):
         print(f"bin called in X")


class Y(X):
    def go(self):
        print(f"go called in Y")


class Z(X):
    def go(self):
        print(f"go called in Z")


class W(Y, Z): # Inherits from Y before Z
    def bin(self):
        super().bin() # this inherits from X through Y
        print(f"bin called in W")

    def bingo(self):
        self.bin()
        self.go()

# list base classes
W.__bases__ # (<class '__main__.Y'>, <class '__main__.Z'>)

w = W()

w.bingo()
# bin called in X
# bin called in W
# go called in Y

W.mro() # same as W.__mro__  # This prints the W-Class MRO
# (__main__.W, __main__.Y, __main__.Z, __main__.X, object)

# ======================================================================================================================
# Abstract Classes & Methods
# https://python.plainenglish.io/level-up-your-python-code-with-abstract-classes-7f7f6bdcbb5c
# ======================================================================================================================
# Abstract classes have no implementation but form a structure as a parent class for inheritance, they are never
# instantiated. They are just there to define a structure for the child (non-abstract concrete) classes
# A method that only has a declaration (with keyword 'pass') and not a definition is called an abstract method.
# A class that has an abstract method is called an abstract class.
# Python by default does not support abstract classes, but there is a module named abc that allows Python to create
# abstract methods and classes.
# Abstract factories group factories together and is a super factory class for those factories
# see https://en.wikipedia.org/wiki/Design_Patterns#Patterns_by_type
# ======================================================================================================================
from abc import ABC, abstractmethod  # built-in library

# 1. This is an abstract class which can not be instantiated itself
# 2. We do not know how to implement the methods for a generic animal.
# 3. We enforce any child obj module overrides all the methods in the parent abstract class


class Animal(ABC):
    @abstractmethod
    def get_sound(self) -> str:
        pass

    @abstractmethod
    def legs_number(self) -> int:
        pass


class Cat(Animal):
    def get_sound(self) -> str:
        return "Meow"

    def legs_number(self) -> int:
        return 4


class Monkey(Animal):
    def get_sound(self) -> str:
        return "Ooh"

    def legs_number(self) -> int:
        return 2


# a = Animal()  - this will give a 'TypeError'
c = Cat()
c.get_sound()
c.legs_number()
m = Monkey()
m.get_sound()
m.legs_number()


class C(ABC):
    @property
    @abstractmethod   # @abstractproperty deprecated in 3.3 use this instead
    def x(self):
        pass

    @x.setter
    @abstractmethod  # @abstractproperty deprecated in 3.3 use this instead
    def x(self, val):
        pass

    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod(arg):
        pass

# ======================================================================================================================
# Use @property so functions can be treated like a property
# @cached_property behaves in the same way but the value is cached after first evaluation  see bezpy_37_lru_cache.py
# ======================================================================================================================


from datetime import datetime as dt


class Book:
    def __init__(self, name, due_back):
        self.name = name
        self.due_back = due_back

    def is_overdue2(self):
        if self.due_back and dt.today() > self.due_back:
            return True
        return False

    @property
    def is_overdue(self):
        if self.due_back and dt.today() > self.due_back:
            return True
        return False


b = Book('Moby Dick', dt(2021, 2, 20))
b.is_overdue2()  # True,  This is a funcion
b.is_overdue     # True, Function is treated like a property


# ======================================================================================================================
class Counter:
    ct: int = 0


Counter.ct += 1  # does not need an instance to access/modify

# ======================================================================================================================
# operator module from the standard library
import operator
operator.add(1, 2)  # equivalent to the expression 1 + 2


# ======================================================================================================================
# __getitem__(key)
# dunder method for accessing indexed elements of a container or for defining a use for invoking square brackets
# on an instance. subscription/indexer with square brackets will call this dunder method in the class definition
# ======================================================================================================================
# --setitem(key, value)
# ======================================================================================================================
# dunder for setting indexed element of a container
# ======================================================================================================================
x = {'abc': 1}
x.__getitem__('abc')    # equivalent to  x['abc']

y = [1, 2, 3]
y.__getitem__(0)        # equivalent to y[0]
y.__setitem__(2, 4)     # equivalent to y[2] = 4

# ======================================================================================================================
# __class_getitem__(key)  this is the same for being invoked by a class
# ======================================================================================================================
# When defined on a class, __class_getitem__() is automatically a class method. As such, there is no need for it to be
# decorated with @classmethod when it is defined


class MyList:

    def __getitem__(self, index):
        return index + 1

    def __class_getitem__(cls, item):
        return f"{cls.__name__}[{item.__name__}]"    # this is used for type annotations - __class_getitem__


assert MyList()[0] == 1
assert MyList[int] == "MyList[int]"


# ======================================================================================================================
# metaclasses
# ======================================================================================================================
# A metaclass is a class whose instances are classes.
# Metaclasses, like regular classes, can define attributes and methods.
# They control the creation and structure of classes.
# Custom metaclasses often override the __new__ and __init__ methods to customize class creation.
#
# Usecases:
#   logging and profiling
#   interface checking
#   registering classes at creation time
#   automatically adding new methods
#   automatic property creation
#   proxies
#   automatic resource locking/synchronization.
# see https://www.youtube.com/watch?v=NAQEj-c2CI8&list=PLzMcBGfZo4-kwmIcMDdXSuy_wSqtU-xDP&index=3
# see https://python-course.eu/oop/metaclasses.php
# ======================================================================================================================


# ======================================================================================================================
# __getitem__(key)
# dunder method for accessing indexed elements of a container or for defining a use for invoking square brackets
# on an instance. subscription/indexer with square brackets will call this dunder method in the class definition
# ======================================================================================================================
# __setitem__(key, value)
# dunder for setting indexed element of a container
# ======================================================================================================================
x = {'abc': 1}
x.__getitem__('abc')  # equivalent to  x['abc']
y = [1, 2, 3]
y.__getitem__(0)  # equivalent to y[0]
y.__setitem__(2, 4)  # equivalent to y[2] = 4


class MyClass:
    def __init__(self, a):
        self.a = a
        self.d = {}

    def __getitem__(self, item):
        return self.d[item.upper()]
    def __setitem__(self, key, value):
        self.d[key.upper()] = value

c = MyClass(4)
c['ONE'] = 1  # invokes __setitem__
c.a  # returns 4
c['one']  # returns 1, invokes __getitem__