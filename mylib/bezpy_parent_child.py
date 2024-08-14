# ======================================================================================================================
# Polymorphism = having many forms (e.g. len function name being used by different parameters)
# ======================================================================================================================
# Inheritance as in Parent->Child
# ======================================================================================================================
# Multiple inheritance is a feature of some object-oriented computer programming languages in which an object or class
#                      can inherit characteristics and features from more than one parent object or parent class.
# ======================================================================================================================
# Single inheritance, where an object or class may only inherit from one particular object or class.
# ======================================================================================================================

class Parent:           # define parent class
    parent_attr = 100    # static or class variable

    def __init__(self, name):
        print("Calling parent constructor")
        self.name = name

    @staticmethod
    def parent_method():
        print('Calling parent method')

    @classmethod
    def set_attribute(cls, attr):
        cls.parent_attr = attr  # Will reassign parent_attr

    @classmethod
    def get_attribute(cls):
        print("Parent attribute :", cls.parent_attr)


class Child(Parent):  # define child class of parent
    child_attr = 'silly'  # static variable
   
    def __init__(self, name, year):
        print("Calling child constructor")
        super().__init__(name)  # invokes parent constructor, equivalent to Parent.__init(self,name)
        self.graduation_year = year

    @staticmethod
    def child_method():
        print('Calling child method')

    @classmethod
    def set_attribute(cls, attr):  # OVERRIDES parent method
        cls.child_attr = attr     # Will reassign 'child_attr' static class variable

    def welcome(self):
        print("Welcome", self.name, "to the class of", self.graduation_year)

    @classmethod
    def get_attribute(cls):  # OVERRIDES parent method
        print("Child attribute :", cls.child_attr)


class Child2(Parent):  # define child class of parent
    child_attr = 'silly2'  # static variable


if __name__ == '__main__':

    p = Parent('Papa')       # calls parent constructor
    c = Child('Fred', 2019)  # calls child & parent constructor

    c.child_method()  # child calls its method
    c.parent_method()  # calls parent's method as not defined for child
    c.set_attribute('billy')  # call child's method (parent is overrided)  child_attr assigned for the class
    c.get_attribute()  # Call Child's method  (parent is overrided)

    print(issubclass(Child, Parent))  # boolean function returns true if the given subclass sub is indeed a subclass of the superclass sup.
    [x.__name__ for x in Parent.__subclasses__()]      # returns all the children  ['Child', 'Child2']

    print(isinstance(c, Child))  # boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class

    c.welcome()             # Welcome Fred to the class of 2019
    c.new_attr = 6          # assigns a new attribute not part of Class Child
    print(c)                # returns the default __str__() method = <__main__.Child object at 0x00000263763756D0>
                            # note that 0x00000263763756D0 is the hex value for what id(c) would return
    print(id(c))            # returns 2626208356048


class Elon:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'x={self.x}, y={self.y}'

    def __eq__(self, b):
        return self.x == b.x and self.y == b.y

a = Elon(1, 3)
b = Elon(1, 3)
a == b   #  True

# ======================================================================================================================
# Base Overloading Magic / Dunder Methods within a class (overrided the defualt functions)
# Full list here: https://docs.python.org/3/reference/datamodel.html
# ======================================================================================================================
# __del__(self)                 Destructor, deletes an object Sample Call : del obj
# __repr__(self)                Evaluable string representation Sample Call : repr(obj) -- see below __repr__ vs __str__
# __str__(self)                 Printable string representation Sample Call : str(obj)  -- see below __repr__ vs __str__
# __cmp__ (self, x)             Object comparison Sample Call : cmp(obj, x)
# __and__(self, x)              Addition overloading of two objects Sample Call: add(a,b)  OR 'a + b'
# __new__()                     Constructor Method: actually constructs the instance of the class, allocates memory, and returns new instance. Is invoked before the __init__ method
# __init__ (self [,args...])    Initializer (with any optional arguments) Sample Call : obj = className(args)
# __eq__()                      Equal Method for equality (==)
# __contains__(self, i):        Returns boolean,   This will allow you to use the 'in' keyword
# __sub__                       for subtraction(-)
# __mul__                       for multiplication(*)
# __truediv__                   for division(/)
# __lt__                        for less than(<)
# __gt__                        for greater than(>)
# __le__                        for less than or equal to (≤)
# __ge__                        for greater than or equal to (≥)
# __setattr__                   to control attributes upon set
# __delattr__                   to control attributes upon delete
# __doc__                       stores the doc string
# __bool__                      to define truthiness of the class instance
# __getitem__                   to implement slicing/indexing
# __setitem__                   for setting indexed element of a container
# __call__(self)                to execute an object as a function
# __class_getitem__             to implement [] on a class-level

# ======================================================================================================================
# __repr__ vs __str__
# ======================================================================================================================
#
# for an object x:
#     if only __repr__ defined  -> uses for >>> x, >>> str(x), >>> repr(x), >>> print(x)
#     if only __str__ defined   -> uses only for >>> str(x) and >>> print(x)
#     if both are defined       -> >>> str(x) and >>> print(x) uses __str__, >>> x and >>> repr(x) uses __repr__

# note, you can add __repr__ = __str__  to bottom of class

# ======================================================================================================================
# New decorator '@override' for python 3.13
# When the type checker sees that our method is being decorated with @override, it will treat it as a type error if we
# change or remove the method from the parent class.
# ======================================================================================================================
# from typing import override
#
# class Car:
#     def fill_gas(self, gas: str) -> bool: ...
#
# class DieselCar(Car):
#     # override this method from parent class
#     @override
#     def fill_gas(self, gas: str) -> bool:
#         print("I only run on diesel")
#
# class PetrolCar(Car):
#     # override this method from parent class
#     @override
#     def fill_gas(self, gas: str) -> bool:
#         print("I only run on petrol")