# ======================================================================================================================
# Context management - Using the 'with' operator
# ======================================================================================================================
# see https://medium.com/better-programming/context-managers-in-python-go-beyond-with-open-as-file-85a27e392114
#
# ======================================================================================================================
# Method 1: using __exit__, __enter__ dunder methods
# ======================================================================================================================
class Divide:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __enter__(self):
        print("Inside __enter__")
        return self                # <- - - '__enter__' must return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Inside __exit__")
        print("Execution type:", exc_type)
        print("Execution value:", exc_value)
        print("Traceback:", traceback, '\n')
        return True   # <------ this is optional to prevent exceptions from crashing program

    def divide_by_num(self):
        # causes ZeroDivisionError when divisor is zero, will be handled in __exit__ however
        # and will not raise exception unless invoked explicitly.
        print(self.num1 / self.num2)


with Divide(3, 1) as r:
    r.divide_by_num()

# Inside __enter__
# 3.0
# Inside __exit__
# Execution type: None
# Execution value: None
# Traceback: None


with Divide(3, 0) as r:
    r.divide_by_zero()

# Inside __enter__
# Inside __exit__
# Execution type: <class 'ZeroDivisionError'>
# Execution value: division by zero
# Traceback: <traceback object at 0x000001BBA4BD4240>


# ======================================================================================================================
# Method 2: Using the @contextmanager decorator  # can implement thread locking within the context manager
# ======================================================================================================================
from contextlib import contextmanager   # BUILT-IN LIBRARY


# No parameters
@contextmanager
def my_context():
    print("Create the context")
    yield
    print("Destroy the context")


# With parameter
@contextmanager
def context_manager_example(x):
    print("Create the context")
    yield x
    print("Destroy the context")


with my_context():
    print('test')
# Create the context
# test
# Destroy the context


with context_manager_example(5) as val:
    print(f'val={val}')  # returns 5
    print("Run operations within context")

# Create the context
# val=5
# Run operations within context
# Destroy the context




