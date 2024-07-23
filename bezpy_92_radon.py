# ======================================================================================================================
# Radon is a program that measures Python metrics ( complexity and number of lines). https://github.com/rubik/radon
# Requires 'pip install radon'
# ======================================================================================================================
# https://linuxtut.com/en/5010aaa6808b7290d68d/
# https://realpython.com/python-refactoring/
# https://radon.readthedocs.io/en/latest/intro.html
# ======================================================================================================================
# Cyclomatic Complexity increases as the number of control statements increases
# This corresponds to the number of decisions a block of code contains plus 1. This number (also called McCabe number)
# and is equal to the number of linearly independent paths through the code. This number can be used as a guide when
# testing conditional logic in blocks.
# ======================================================================================================================
# radon cc -s file_name.py   # cc=Cyclomatic Complexity
# ======================================================================================================================
# Option	        Description
# -s, --show	    Display Cyclomatic Complexity.
# -n, --min	        Set the minimum rank to display. Specify A to F after this argument
# -x, --max	        Set the maximum rank to be displayed. Specify A to F after this argument
# -a, --average	    Display the average of Cyclomatic Complexity at the end. This average is-n or-Affected by x filter
# --total-average	Receive the average of all data-Unlike a, it is not affected by the filter
# -e, --exclude	    Specify the path of the file to be excluded from analysis separated by commas
# -i, --ignore	    Specify directories to ignore, separated by commas. Do not check under ignored directories
# -o, --order	    Specify the sort order. (SCORE complexity order/LINES by number of lines/ALPHA block name order)
# -j, --json	    Output the result in JSON
# --no-assert	    Assert when calculating complexity()Instructions do not count
# ======================================================================================================================
# Output Example: F 4:0 main - B (6)
# ======================================================================================================================
# F means function, main is the name of the function, 4:0 is the line:column the function starts on.
# B is the rating from A to F. A is the best grade, meaning the least complexity.
# The number in parentheses, 6, is the cyclomatic complexity of the code.


# F=Function
# M=Method
# C=Class
# ======================================================================================================================
# CC-value	Rank	risk
# 1 - 5	    A	    low -Simple block
# 6 - 10	B	    low -Well-structured and stable block
# 11 - 20	C	    moderate -A little complicated block
# 21 - 30	D	    more than moderate -More complex blocks
# 31 - 40	E	    high -Complex blocks, alarming
# 41+	    F	    very high -Unstable blocks that are error prone
# ======================================================================================================================


# ======================================================================================================================
# Halstead complexity metrics relate to the size of a program’s codebase, in simple terms The effort of your
# application is highest if you use a lot of operators and unique operands.
# The effort of your application is lower if you use a few operators and fewer variables.
# ======================================================================================================================
# Operands are values and names of variables.
# Operators are all of the built-in keywords, like if, else, for or while.
# Length (N) is the number of operators plus the number of operands in your program.
# Vocabulary (h) is the number of unique operators plus the number of unique operands in your a program.
# Volume (V) represents a product of the length and the vocabulary.
# Difficulty (D) represents a product of half the unique operands and the reuse of operands.
# Effort (E) is the overall metric that is a product of volume and difficulty.
# ======================================================================================================================
# radon hal file_name.py
# Output Example:
# h1: 3
# h2: 6
# N1: 3
# N2: 6
# vocabulary: 9
# length: 9
# calculated_length: 20.264662506490406
# volume: 28.529325012980813
# difficulty: 1.5
# effort: 42.793987519471216
# time: 2.377443751081734
# bugs: 0.009509775004326938
# ======================================================================================================================


# ======================================================================================================================

# ======================================================================================================================
# Maintainability Index is a software metric which measures how maintainable (easy to support and change) the source
# code is. The maintainability index is calculated as a factored formula consisting of SLOC (Source Lines Of Code),
# Cyclomatic Complexity and Halstead volume.
# ======================================================================================================================
# radon mi -s file_name.py   #mi=Maintainability Index
# ======================================================================================================================
# Option	    Description
# -s, --show	Display Maintainability Index.
# -e, --exclude	Specify the path of the file to be excluded from analysis separated by commas
# -i, --ignore	Specify directories to ignore, separated by commas. Do not check under ignored directories
# -m, --multi	Do not count multi-line strings as comments
# ======================================================================================================================
# Output Example: file_Name.py - A (58.76)
# ======================================================================================================================
# MI score	    Rank	Maintainability
# 100 - 20	    A	    Very Maintainable
# 19 - 10	    B	    Medium
# 9 - 0	        C	    Very low
# ======================================================================================================================



# =================================================================================
# Example of dictionary use to reduce Cyclomatic Complexity
# =================================================================================

def do_create():
    print(1)

def do_activate():
    print(2)

def do_delete():
    print(3)

# Method 1: CC VALUE = 3
def perform_action(action):
    if action == 'create':
        do_create()
    elif action == 'delete':
        do_delete()
    else:
        do_create()

# Method 1: CC VALUE = 1
def perform_action2(action):
    ACTION_MAPPING = {"create": do_create,
                      "activate": do_activate,
                      "delete": do_delete,}
    handler = ACTION_MAPPING.get(action)
    handler()


# CC = 3
def test1():
    if 1 == 1 and 2 == 2:  
        print('hey')
# CC = 3
def test2():
    if 1==1:
        if 2==2:
            print('hey')


def convert(x):
    '''handles one of three data types else returns the original object'''
    def do_int(a):
        pass

    def do_float(c):
        pass

    def do_complex(b):
        pass

    # WARNING:  "isinstance(x, int) : do_int(x)," wouldn't work because python will attempt to evaluate do_int(x) every time
    #           even when isinstance(x, int) == False, so must use "isinstance(x, int) : do_int," instead

    handler = {isinstance(x, int) : do_int,    
               isinstance(x, float): do_float,
               isinstance(x, complex): do_complex}.get(True)

    if handler:
        return handler(x)
    return x


if __name__ == '__main__':
    perform_action('create')
    perform_action2('activate')


# ========================================================================================