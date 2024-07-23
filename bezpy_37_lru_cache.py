# memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the
# results of expensive function calls and returning the cached result when the same inputs occur again


# DONE: https://medium.com/better-programming/every-python-programmer-should-know-lru-cache-from-the-standard-library-8e6c20c6bc49
# LRU Cache - The Least Recently Used Cache Decorator
# @lru_cache is a decorator that will cache specific function calls and store the results for given parameters
# the inputs and outputs will be stored in a dictionary for the flow of the script
# Only use if the function input->output map is fixed/deterministic.  func(a) always gives (b), input value a must be hashable
# Only use if the object returned by the function is immutable otherwise you'll only be caching a reference to the object e.g. when returning a llst

# func.cache_info() displays how many hits / misses you had by repeating this function.
#                   a 'hit' means the function call was already performed
#                   and so you only needed to use the cache dictionary
# func.cach_clear() will empty the cache from memory
# when 'maxsize' is reached the least recently used mapping is replaced
# for some reason maxsize is set to a value which is a power of two. default value is 128 = 2 ** 7


# Syntax:
# @lru_cache(maxsize=128, typed=False)
#
# Parameters:
# maxsize:This parameter sets the size of the cache, the cache can store upto maxsize most recent function calls, if maxsize is set to None, the LRU feature will be disabled and the cache can grow without any limitations
# typed: # If typed is set to True, function arguments of different types will be cached separately. For example, f(3) and f(3.0) will be treated as distinct calls with distinct results and they will be stored in two separate entries in the cache



from functools import lru_cache   # parameter maxsize will limit
from functools import cache       # Simple lightweight unbounded cache, available from Python 3.9 onwards. for previous versions use lru_cache(maxsize=None) instead


from math import factorial
from time import time
# sys.getrecursionlimit()      # default is 1000
# sys.setrecursionlimit(5000)  # useful tool



# Manual Caching
def fib(n):
    """ returns the nth element of the sequence with manual caching """
    if n == 1 or n == 2:
        return 1
    elif n in fib_cache.keys():
        return fib_cache[n]
    else:
        x = fib(n-1) + fib(n-2)
        fib_cache[n] = x
        return x

@lru_cache(maxsize=1024)
def fib2(n):
    """ returns the nth element of the sequence with manual caching """
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


@lru_cache(maxsize=128)
def f1(n):
    return factorial(n)

# No caching this time
def f2(n):
    return factorial(n)

@cache  # Simple lightweight unbounded cache
def f3(n):
    return factorial(n)


def timeit(func, value):
    start = time()
    func(value)
    end = time()
    print(end - start)

if __name__ == '__main__':

    print('1st Round:')
    timeit(f1,10000)
    print(f1.cache_info())
    timeit(f2,10000)
    timeit(f3, 10000)

    print('2nd Round:')
    timeit(f1,10000)  #  this takes no time since f1(100000) has been cached
    print(f1.cache_info())
    timeit(f2,10000)
    timeit(f3, 10000)
    f1.cache_clear()


    # Manual Caching
    fib_cache = {}
    print(fib(100))

    # Using lru
    print(fib2(100))



# 1st Round:
# 0.26329660415649414
# CacheInfo(hits=0, misses=1, maxsize=128, currsize=1)
# 0.37100887298583984
# 2nd Round:
# 0.0
# CacheInfo(hits=1, misses=1, maxsize=128, currsize=1)
# 0.32114219665527344


# ======================================================================================================================
# @cached_property,  similar to @property but will execute the method only once and store in cache
# ======================================================================================================================
# from cached_property import cached_property   # before 3.8 requires `pip install cached_property`
from functools import cached_property           # as of 3.8  standard library
  
# A sample class
class Sample():
    def __init__(self, lst):
      self.long_list = lst

    @cached_property
    def find_sum(self):
        """find the sum of the given long list of integer values"""
        return (sum(self.long_list))
  
# s is an instance of the class sample
s = Sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s.find_sum  # 55
s.find_sum  # 55 - retrieves from cache
s.find_sum  # 55 - retrieves from cache