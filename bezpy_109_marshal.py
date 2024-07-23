# ======================================================================================================================
# marshal module from the standard library, provides support for reading and writing marshalled Python objects.
# ======================================================================================================================
# https://docs.python.org/3/library/marshal.html
# The marshal module exists mainly to support reading and writing the “pseudo-compiled” code for Python modules
# of .pyc files. This module doesn’t support all Python object types.
# in general pickle should always be the preferred way to serialize Python objects.
# marshal exists primarily to support Python’s .pyc files for which marshal is faster.
# https://www.geeksforgeeks.org/marshal-internal-python-object-serialization/

# Python code to demonstrate de-serialization
import marshal

data = {12: 'twelve', 'feep': list('ciao'), 1.23: 4 + 5j, (1, 2, 3): u'wer'}
bytes = marshal.dumps(data)
redata = marshal.loads(bytes)
print(redata)

