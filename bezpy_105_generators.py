# ======================================================================================================================
# GENERATORS (is a type of iterator that uses 'yield' keyword or is created with a generator expression
# ======================================================================================================================
# yield is used inside a function like a return statement. But yield returns a generated value.
# Generator is an iterator that generates one item at a time. A large list of value will take up a lot of memory.
# Generators are useful in this situation as it generates only one value at a time instead of storing all the
# values in memory.
#
# 1. Generators can use the 'next()' built-in function,
# 2. Returned iterators by generators are 'stateful' and can be looped through once without giving a StopIteration error
# 3. Generators can be converted to a list
# 4. Generators can be created with a generator expression or by using a generator function and the 'yield' keyword
# 5. Generators can be chained from one generator to the next


l = [2 ** x for x in range(5)]   # will produce a regular list (using list comprehension) [1, 2, 4, 8, 16]
g = (2 ** x for x in range(5))   # this is a 'genexp' (generator expression) will generate 1,2,4,8,16, g is of <class 'generator'>
first = next(g)                  # returns 1, by actually generating the first element
second = next(g)                 # returns 2, by actually generating the second element
third = next(g)                  # returns 4, by actually generating the third element
fourth = next(g)                 # returns 8, by actually generating the fourth element
fifth = next(g)                  # returns 16, by actually generating the fifth element
# sixth = next(g)                # this would raise the error 'StopIteration' as all values have been generated
next(g, 0)                       # this will prevent the error when iterations exhausted  and return default value of zero in this ca
g.close()                        # will take the generator to the end

# ======================================================================================================================

# same as above using the 'yield' keyword
def generate_nums():
    for i in range(5):
        yield 2 ** i  # yield will always produce a 'generator' type


g2 = generate_nums()  # is of <class 'generator'>
# NOTE: all interators can only loop once including generators
for j in g2:
    print(j)

g2 = generate_nums()  # refills the generator
list(g2)   # [1, 2, 4, 8, 16]


# ======================================================================================================================
# This is a Chained Generator
# ======================================================================================================================
g3 = (i + 1 for i in generate_nums())
list(g3)  # [2, 3, 5, 9, 17]

# ======================================================================================================================

def generator_function():
    yield 1  # will stop here and return the 1
    yield 2  # then will stop here and return the 2
    yield 3  # then will stop here and return the 3


for i in generator_function():
    print(i)
# Return
# 1
# 2
# 3

g3 = generate_nums()  # refills the generator
type(g3)  #  <class 'generator'>
to_list = list(g3)  # [1, 2, 4, 8, 16]

# ======================================================================================================================
# Generator example two
# ======================================================================================================================
def countdown(n):
    while n > 0:
        yield n  # This will return the value 'n' to the generator next function and then pause
        print('Resuming Generator')
        n -= 1


g = countdown(5)
next(g)  # Will execute countdown(5) and pause at the yield line returning the value of 5
next(g)  # this will resume the function by deducting one and stop at the next yield returning the value of 4

# ======================================================================================================================
# send()
# ======================================================================================================================
def gen_func():
    val = yield
    yield val * 10

g = gen_func()
next(g)    # prime the generator and goes to 1st yield
g.send(3)  # sends 3 to first yield and goes to 2nd yield  -- returns 30

# ======================================================================================================================
g = (x + 2 for x in range(4))  # -> [2, 3, 4, 5]

# when using a generator as an input argument, the brackets are not required
assert sum(x + 2 for x in range(4)) == sum((x + 2 for x in range(4))) == 14.