# Very useful resource of algorithms

# https://the-algorithms.com/
# https://github.com/keon/algorithms
# requires pip install algorithms

# also see bezpy_49_sort_algorithms.py

from algorithms.sort import merge_sort
from algorithms.maths import prime_check

if __name__ == "__main__":
	merge_sort([1, 8, 3, 5, 6]) # [1, 3, 5, 6, 8]
	prime_check(7) # True