# see https://medium.com/better-programming/context-managers-in-python-go-beyond-with-open-as-file-85a27e392114

# Context management - Using the 'with' operator


# ======================================================================================================================
# Method 1: using __exit__, __enter__ dunder methods
class Divide:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __enter__(self):
        print("Inside __enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Inside __exit__")
        print("Execution type:", exc_type)
        print("Execution value:", exc_value)
        print("Traceback:", traceback, '\n')
        return True   # <------ this is optional to prevent exceptions from crashing program

    def divide_by_zero(self):
        # causes ZeroDivisionError exception
        print(self.num1 / self.num2)

# ======================================================================================================================
# Method 2: Using the @contextmanager decorator  # can implement thread locking within the context manager
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

# ======================================================================================================================
# Sample Decorator
def invocation_log(func):
    def inner_func(*args, **kwargs):
        print(f'Before Calling {func.__name__}')
        return_val = func(*args, **kwargs)
        print(f'After Calling {func.__name__}')
    return inner_func

@invocation_log
def say_hello(name):
    print(f"Hello, {name}!")
# ======================================================================================================================



if __name__ == '__main__':

    with Divide(3, 1) as r:
        r.divide_by_zero()

    with Divide(3, 0) as r:
        r.divide_by_zero()


    say_hello('python')

    with my_context():
        print('test')

    with context_manager_example(5) as val:
        print(f'val={val}')  # returns 5
        print("Run operations with the context")

    # as of python 3.10 can use syntax below ...
    # with (open('output.log', 'w') as fout, open('input.csv') as fin):
    #     fout.write(fin.read())

