# Source https://snyk.io/blog/how-to-write-tests-in-python-using-doctest/
# built-in module 'doctest'

def prod(x, y):
    """
    This function returns the square of the input.
    :param a: int
    :return: int
    >>> prod(2, 3)
    6
    >>> prod(5, 7)
    35
    """
    return x * y

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # test the whole module run from command line
    #   `python bezpy_149_doctest.py`      (only indicates failures)
    #   `python bezpy_149_doctest.py -v`   (-v verbose)
    # without the main function, which invokes doctest.testmod(), we can still run from command line
    #   `python -m doctest -v bezpy_149_doctest.py`


# ==============================================
# OUTPUT
# ==============================================
# Trying:
#     prod(2, 3)
# Expecting:
#     6
# ok
# Trying:
#     prod(5, 7)
# Expecting:
#     35
# ok
# 1 items had no tests:
#     bezpy_149_doctest
# 1 items passed all tests:
#    2 tests in bezpy_149_doctest.prod
# 2 tests in 2 items.
# 2 passed and 0 failed.
# Test passed.


