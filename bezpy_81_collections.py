# ======================================================================================================================
# the COLLECTIONS standard library
# ======================================================================================================================


# ======================================================================================================================
# OrderdDict added to the standard library in Python 3.1
# ======================================================================================================================
# Store each person's languages, keeping track of who was added first.
from collections import OrderedDict
# https://realpython.com/python-ordereddict/
# using an OrderedDict communicates your intention to rely on the order of items in your dictionary being preserved,
# both to human readers of your code and to the third-party libraries you call within it.

# Changed in version 3.7: Dictionary order is guaranteed to be in insertion order for built-in dict.
# This behavior was implementation detail of CPython from 3.6.

# Note for python 3.8 Dictionaries are now iterable in reversed insertion order using reversed()

fav_languages = OrderedDict()  # of type collections.OrderedDict
fav_languages['jen'] = ['python', 'ruby']
fav_languages['sarah'] = ['c']
fav_languages['edward'] = ['ruby', 'go']
fav_languages['phil'] = ['python', 'haskell', 'C++']

# Display the results, in the same order they were entered.  (I thiink dict does that too as of 3.7)
# >>> fav_languages
# OrderedDict([('jen', ['python', 'ruby']),
#              ('sarah', ['c']),
#              ('edward', ['ruby', 'go']),
#              ('phil', ['python', 'haskell', 'C++'])])


letters = OrderedDict(b=2, d=4, a=1, c=3) # initialize with values for keys 'a', 'b', 'c', 'd'

# 0. Using OrderedDict declares intention that order is important
# 1. since OrderedDict has a .__dict__ attribute you can add functionality and values to it.
# vars(OrderedDict()) -> {}
# vars(dict()) -> TypeError:  i.e. you can't do with 'dict' objects  ...
letters.value = 7
vars(letters)  # returns {'value': 7}
letters # returns OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)]) 

letters.sorted_keys = lambda: sorted(letters.keys())  # adding function to the class (can't do this with dict)
letters.sorted_keys()  # returns ['a', 'b', 'c', 'd']

# merge (|) and update (|=) dictionary operators work as of 3.9 like dict()
physicists = OrderedDict(newton="1642-1726", einstein="1879-1955")
physicists_1 = OrderedDict(newton="1642-1726/1727", hawking="1942-2018")
# physicists |= physicists_1  # UPDATE

biologists = OrderedDict(darwin="1809-1882", mendel="1822-1884")
# scientists = physicists | biologists # MERGE

# 2. Testing for Equality Between Dictionaries, only for OrderedDict does the equality require the order be the same
od1 = OrderedDict(a=1, b=2)
od2 = OrderedDict(b=2, a=1)
od1 == od2  # False

d1 = dict(a=1, b=2)
d2 = dict(b=2, a=1)
d1 == d2 # True

# 3. Enhanced .popitem()
od1.popitem(last=False)  # returns and removes first key-value pair. default is last=True,  feature not available for dict()

# 3. od.move_to_end(key[, last=True])  You can move a key to end or begining
od1.move_to_end("b", last=False)  # moves 'b' to begining of OrderedDict

# Note performance for OrderedDict is slower than dict and uses more memory than dict()

# ======================================================================================================================
# Counter
# ======================================================================================================================
from collections import Counter
ctr1 = Counter()   # fav color votes from multiple classrooms, Counter() will tally them
dict1 = {'blue': 1, 'green': 3, 'red': 4}
dict2 = {'blue': 2, 'red': 1, 'orange': 7}
ctr1.update(dict1)
ctr1.update(dict2)
ctr1.update(['blue', 'red', 'red'])
ctr1.subtract(['orange', 'orange'])  # removes from Counter,  Counter({'red': 7, 'orange': 5, 'blue': 4, 'green': 3})
ctr1.subtract({'brown': 2})  # can have -ve counts, Counter({'red': 7, 'orange': 5, 'blue': 4, 'green': 3, 'brown': -2})

ctr2 = Counter({'orange': 7, 'red': 5, 'blue': 3, 'green': 3})
ctr2['orange']  # returns 7
ctr2.most_common(2)  # returns [('orange', 7), ('red', 5)], the most common two elelments

ctr1 + ctr2   # ADD, returns Counter({'red': 12, 'orange': 12, 'blue': 7, 'green': 6})  ignores the -ve counts
ctr1 - ctr2   # SUBTRACT, returns Counter({'red': 2, 'blue': 1})  ignores the -ve counts
ctr1 & ctr2   # INTERSECT, returns Counter({'red': 5, 'orange': 5, 'blue': 3, 'green': 3})
ctr1 | ctr2   # UNION, returns Counter({'red': 7, 'orange': 7, 'blue': 4, 'green': 3})
ctr1.update(ctr2)    # Modifies ctr1 by adding counts
ctr1.subtract(ctr2)  # Modifies ctr1 by subtracting counts

c = Counter('which')                #  Counter({'h': 2, 'w': 1, 'i': 1, 'c': 1})
c = Counter(['w','h','i','c','h'])  #  Counter({'h': 2, 'w': 1, 'i': 1, 'c': 1})
c = Counter(cats=3, dogs=2)         #  Counter({'cats': 3, 'dogs': 2})
c.elements() # returns an iterator with all the elements flattened i.e. ['cats', 'cats', 'cats', 'dogs', 'dogs']

# inherits dict methods eg.  items, keys, values, get, setdefault
for i, j in ctr1.items():
    print(i, j)

# ======================================================================================================================
# namedtuple
# ======================================================================================================================
# Named tuples can be reuseable.
# note functools also has a namedtuple, not sure what difference is
# It is a factory function (creates objects), allows use of the dot operator to access values
from collections import namedtuple

Friend = namedtuple('Friend', 'birthday food color introvert')
Friend = namedtuple('Friend', ['birthday', 'food', 'color', 'introvert'])   # same as above
Kate = Friend('Feb', 'cake', 'pink', True)
Ben = Friend('Jan', 'fish', 'red', False)

Ben        # returns Friend(birthday='Jan', food='fish', color='red', introvert=False)
Ben.food   # returns 'fish'
# Ben.food = 'pizza'  # AttributeError: you can't modify the namedtuple
Ben[1]     # returns 'fish'
Ben._asdict  # returns OrderedDict([('birthday', 'Jan'), ('food', 'fish'), ('color', 'red'), ('introvert', False)])
Ben._fields  # ('birthday', 'food', 'color', 'introvert')


isinstance(Ben, tuple) and hasattr(Ben, '_fields')   # True, Ben is a namedtuple


Ben.count('red')  # returns 1
Ben.index('red')  # returns 2

Pete = Ben._replace(food='pizza')  # creates new object by replacing values in Ben
Dave = Friend._make(['Mar', 'beef', 'green', 'True'])  # alternate way to create object

# The alternative option to create a namedtuple is using typing.NamedTuple

# ======================================================================================================================
# deque
# ======================================================================================================================
# Queue FIFO - Double-ended Queue. removes from begining or end of list in constant time.
# Note a regular list will remove only from end at constant time but from begining at O(n) time
from collections import deque  # pronounced deck

q = deque('xyz')      # deque(['x', 'y', 'z'])
q.append('a')
q.append('b')
q.append('c')         # deque(['x', 'y', 'z', 'a', 'b', 'c'])
q.appendleft('d')     # deque(['d', 'x', 'y', 'z', 'a', 'b', 'c'])
q.pop()               # returns and removes 'c'
q.popleft()           # returns and removes 'd', deque(['x', 'y', 'z', 'a', 'b'])
q.extend([1, 2, 3])   # appends any iterable to end of queue
q.extendleft('456')   # appends any iterable to start of queue, deque(['6', '5', '4', 'x', 'y', 'z', 'a', 'b', 1, 2, 3])
q.rotate(-3)          # moves elements 3 positions to the left  deque(['x', 'y', 'z', 'a', 'b', 1, 2, 3, '6', '5', '4'])
q.rotate(1)           # moves elements 1 position to the right  deque(['4', 'x', 'y', 'z', 'a', 'b', 1, 2, 3, '6', '5'])


q = deque('hello', maxlen=5)   # will only allow 5 elements in deque
q.append('1')         # deque(['e', 'l', 'l', 'o', 1], maxlen=5)  romved the 'e' to append the '1'
q.maxlen              # returns the maxlen, note you can not modify

q = deque()           # Empty deque([])
q.extend('hello')
q.remove('e')         # removes first occurrence of that value
q.copy()              # returns a copy of the deque  deque(['h', 'l', 'l', 'o'])
q.count('l')          # counts occurrences of that element in your deque
q.index('o')          # returns index position of first occurrence of element
q.insert(3, 'a')      # insert element 'a' in index 3 position
q.reverse()           # reverses deque inplace
q.clear()             # Clears the deque


# ======================================================================================================================
# defaultdict
# ======================================================================================================================
# Use defaultdict to handle KeyError with a function
from collections import defaultdict

# Function to return a default values for a key that is not present
def def_value():
    return "Not Present"


# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
print(d["c"])  # returns "Not Present"  and sets d['c'] = "Not Present"


# ======================================================================================================================
# Queue
# ======================================================================================================================
# FIFO Queue   # this Class has thread lock features
from queue import Queue
q = Queue(maxsize=6)

q.empty()   # returns True
q.put(7)
q.put(8)
q.put(9)
q.full()   # returns False
q.queue    # returns list [7, 8, 9]
q.get()  # returns 7 from queue and removes
q.get()  # returns 8 from queue and removes
q.get()  # returns 9 from queue and removes
# q.get() # will loop forever as empty - must be crashed

q.maxsize # stores maxsize
q.qsize() # returns size of queue


# lifo Queue
from queue import LifoQueue
q = LifoQueue(maxsize=6)
q.put(7)
q.put(8)
q.put(9)
q.get() # returns and removes 9 from queue

# ======================================================================================================================