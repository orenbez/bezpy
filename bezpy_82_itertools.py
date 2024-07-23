# https://medium.com/analytics-vidhya/itertools-library-with-examples-and-applications-6768ec5de177
import sys
from itertools import *

# https://docs.python.org/3/library/itertools.html
# ======================================================================================================================
# see bezpy_50_combinatorics.py
# ======================================================================================================================
# combinations(iterable, r)                   - Returns an r length subsequence of elements from the input iterable .
# combinations_with_replacement(iterable, r)  - Returns r length subsequences of elements from the input iterable allowing the individual elements to be repeated
# permutations(iterable, r=None)              - Returns successive r length permutations of elements in the iterable
# product(*iterables, repeat=1)               - Cartesian product of input iterables.  Equivalent to nested for-loops.
# ======================================================================================================================
# accumulate(iterable[, func])                - Returns iterator of accumulated sums or accumulated results of other binary functions
# chain(*iterables)                           - Returns iterator after chaining multiple iterators together
# compress(data, selectors)                   - Returns iterator over selected data
# count(start=0, step=1)                      - Returns an infinite iterator counter.  start=0 is default, step=1 is default
# cycle(iterable)                             - Returns looped iterator that will continuously cycel through values of object passed
# dropwhile(predicate_function, sequence)     - drops elements as long as the filter criteria is True then returns rest of container as iterator
# filterfalse(predicate_function, sequence)   - Returns iterator of items of sequence for which predicate_function(item) is False
# groupby()
# islice(iterable, start, stop[, step])       - return an iterator whose next() method returns selected values from an iterable, islice(iterable, stop) also works
# pairwise(iterable)                          - as of 3.10 returns iterator with each valued paired with it's adjacent value (see below)
# repeat(object[, times])                     - returns object (see below)
# starmap(function, iterable, /)              - Return an iterator whose values are returned from the function evaluated with an argument tuple taken from the given sequence. c.f. with map()
# takewhile(predicate, iterable, /)           - Return successive entries from an iterable as long as the predicate evaluates to true for each entry.
# tee(iterable, n=2, /)                       - Returns a tuple of n independent iterators.
# zip_longest(*iterables, fillvalue=None)     - Returns zip_longest object (iterator) zips elements even after the shortest collection is exhausted
# ======================================================================================================================

array1 = [1, 2, 3, 4, 5,]
array2 = ['a', 'b', 'c']
zip(array1, array2)  # iterator for [(1, 'a'), (2, 'b'), (3, 'c')]
zip_longest(array1, array2, fillvalue='x') # iterator for [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'x'), (5, 'x')]


i1 = iter([1, 2, 3])
i2 = iter([4, 5, 6])
i3 = chain(i1, i2)  # returns a chained iterator for [1, ... ,6]
i4 = chain.from_iterable([[1,2,3],[4,5,6],[7,8,9]]) # returns iterator after flattening the passed iterable i.e. [1, ..., 9]

permutations(range(3), 2) # iterator for [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
permutations(range(3))   # iterator for [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
combinations(range(3), 2) # iterator for [(0, 1), (0, 2), (1, 2)]
product((0, 1), (0, 1), (0, 1)) # iterator for  (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0)

# Can iterate forever
c = cycle([-1,1])
next(c) # -1
next(c) # 1
next(c) # -1


i = repeat(['a', 'b', 'c'])       # returns iterator next(i) returns ['a', 'b', 'c'] endlessly (DOES NOT CYCLE THROUGH [a,b,c]
i = repeat(['a', 'b', 'c'], 3)    # returns iterator next(i) returns ['a', 'b', 'c'] 3 times and then 'StopIteration' exception
assert ['a', 'b', 'c'] * 3 == ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
assert list(repeat(['a', 'b', 'c'], 3)) == [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]


accumulate([1, 2, 3, 4])      # returns iterator for [1, 3, 6, 10], where each term is accumulative sum of all previous
accumulate([1, 2, 3, 4], func=lambda x,y:x+y)  # same as above
accumulate([1, 2, 3, 4], func=lambda x,y:x*y) # iterator for [1, 2, 6, 24]
integers = count(start=0, step=1)  # iterator for [0, 1, 2, 3, 4, ... ] infinite count

squares  = (i**2 for i in integers)  # infinite generator expression of squares
sys.getsizeof(squares)  # 112 bytes is all the memory it needs for an infinite generator

for s in squares:
    print(s)
    if s > 100:
        squares.close() # stops the generator

dropwhile(lambda x: x<5, [1, 4, 6, 4, 1])  # returns iterator for [6, 4, 1]
filterfalse(lambda x: x%2, range(10))  # returns iterator for [0, 2, 4, 6, 8]


compress(['a', 'b', 'c', 'd'], [True, False, True, False])  # returns iterator of ['a', 'c'] which were selected
compress(['a', 'b', 'c', 'd'], [1, 0, 1, 0]) # same as above, evaluates truthyness of selector

# pairwise([1,2,3,4]) # returns iterator of [(1,2),(3,4)] pairing iterable into tuples of adjacent values  as of 3.10

i1, i2 = tee([1,2,3,4], 2)  # returns two identical iterators as a tuple each one is of [1 ,2, 3, 4]

# takewhile(predicate, iterable)
# will only take even numbers from the iterable
takewhile(lambda x: x % 2 == 0, [0, 2, 4, 7, 22, 34, 6, 67])  # returns iterator for [0, 2, 4, 22, 34, 6]


# islice(iterable, start, stop[, step])
islice([2, 4, 5, 7, 8, 10, 20], 1, 6, 2)  # returns iterator for  [4, 7, 10]

# islice(iterable, stop)
islice(range(20), 5)  # returns iterator for  [0, 1, 2, 3, 4]