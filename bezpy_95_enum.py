# https://docs.python.org/3/library/enum.html
# https://www.geeksforgeeks.org/enum-in-python/

from enum import Enum, unique, IntEnum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

list(Color) # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]

c = Color.BLUE # initializing requires a value 1, 2 or 3

c.name  # returns 'BLUE'
c.value # returns 3

c._name_   # also returns 'BLUE'
c._value_  # also returns 3

# These 3 are all equal and can be compared
Color.BLUE     # <Color.BLUE: 3>  (Preferred)
Color(3)       # <Color.BLUE: 3>
Color['BLUE']  # <Color.BLUE: 3>

assert c == Color.BLUE
assert isinstance(Color.GREEN, Color)
type(Color.BLUE)  # <enum 'Color'>


# Class can be treated as a collection
for i in Color:
    print(i)
# Color.RED
# Color.GREEN
# Color.BLUE

# They are hashable
pen = {Color.RED : 'Red Pen',
       Color.BLUE : 'Blue Pen',
       Color.GREEN : 'Green Pen'}


# Enforce Uniqueness
@unique
class Mistake(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    #FOUR = 3   # ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE

list(Mistake) # [<Mistake.ONE: 1>, <Mistake.TWO: 2>, <Mistake.THREE: 3>]

# can use strings
class Test(Enum):
    ONE = 'ONE'
    TWO = 'TWO'
    THREE = 'THREE'

list(Test) # [<Test.ONE: 'ONE'>, <Test.TWO: 'TWO'>, <Test.THREE: 'THREE'>]

# Initialize with 'ONE', 'TWO', or 'THREE'
t = Test.ONE      # Preferred method
t = Test('ONE')   # Same as above
t = Test['ONE']   # Same as above
t.name   # 'ONE'
t.value  # 'ONE'


# Can only take int values
class Bounds(IntEnum):
    X = 10
    Y = 11
    Z = 12

list(Bounds)  # [<Bounds.X: 10>, <Bounds.Y: 11>, <Bounds.Z: 12>]


#  assign the numerical values automatically
class Language(Enum):
    Java = auto()
    Python = auto()
    HTML = auto()

list(Language)  # [<Language.Java: 1>, <Language.Python: 2>, <Language.HTML: 3>]