# ======================================================================================================================
# 'shelve' module from the standard library, a serialization dictionary
# ======================================================================================================================
# https://docs.python.org/3/library/shelve.html
# The shelve module can be used as a simple persistent storage option for Python objects when a relational
# database is overkill. The shelf is accessed by keys, just as with a dictionary.
# The values are pickled and written to a database created and managed by anydbm
# shelve builds on top of pickle and implements a serialization dictionary where objects are pickled,
# but associated with a key. You can load your shelved data file and access your pickled objects via keys.



# Pickle example
import pickle
integers = [1, 2, 3, 4, 5]
pkl_file = r'.\myfiles\pickle-example.pkl'

# PICKLE
with open(pkl_file, 'wb') as pfile:
    pickle.dump(integers, pfile)

# UNPICKLE
with open(pkl_file, 'rb') as pfile:
    integers = pickle.load(pfile)
    print (integers)

# Shelve example
import os
import shelve
integers = [1, 2, 3, 4, 5]

shelf_store = os.path.join('myfiles','shelf-example')
# three files will be created
# myfiles/shelf-example.bak
# myfiles/shelf-example.dat
# myfiles/shelf-example.dir

# WRITE TO Shelf
with shelve.open(shelf_store, 'c') as shelf:
    shelf['ints'] = integers  # the list is pickled and associated by key 'ints'

# READ FROM Shelf
with shelve.open(shelf_store, 'r') as shelf:
    for key in shelf.keys():
        print(repr(key), repr(shelf[key]), key, shelf[key])


# Method	Description
# open()	open persistent dictionary object
# close()	synchronize and close persistent dictionary object.
# sync()	Write back all entries in the cache given that the shelf was opened with the writeback set to True.
# get()	    returns value associated with key
# items()	tuples list
# keys()	list of shelf keys
# pop()	    remove specified key and return the corresponding value.
# update()	update shelf from another dictionary/iterable
# values()	list of shelf values