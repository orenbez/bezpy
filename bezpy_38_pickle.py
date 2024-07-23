# ======================================================================================================================
# 'pickle' module, from the standard library
# ======================================================================================================================
# primarily used in serializing and deserializing a Python object structure.
# In other words, it’s the process of converting any Python object into a byte stream to store it
# in a file/database, maintain program state across sessions, or transport data over the network.
# The pickled byte stream can be used to re-create the original object hierarchy by unpickling the stream.
# Some use convention of .pickle file extension some use .pkl
# pickle into type 'bytes' or 'bytearray'
# Note: sqlalchemy has type 'pickletype'
# Note: in pandas we can pickle a series or dataframe with s.to_pickle()  df.to_pickle()
# Pickling does not compress the data.  Use parquet (bezpy_140_parquet.py) to serialize & compress a series or dataframe
# Useful for sending data over sockets
# ========================FUNCTIONS=====================================================================================
# dump(object, fileName)      python object   -> serialized file
# load(file)                  serialized file -> python object

# dumps(object)               python object -> byte string  (serialization)
# loads(string)               byte string   -> python object  (deserialization)
# ======================================================================================================================
import pickle
import pandas as pd

# PICKLING A DICTIONARY TO OBJECT
d = {1:'a',2:'b'}  # dict object as an example
pickled_obj = pickle.dumps(d)  # pickles into bytes stream format  = b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00}\x94(K\x01\x8c\x01a\x94K\x02\x8c\x01b\x94u.'
d2 = pickle.loads(pickled_obj) # unpickled back to dictionary

# Errors for pickle.loads()
# 1. _pickle.UnpicklingError: unpickling stack underflow  (piclkled_obj is corrupt or ends unexpectedly)
# 2. EOFError: Ran out of input  (pickled_obj is being accessed by another process or simply empty e.g. >>> pickle.loads(b'') )


# PICKLING A DICTIONARY TO FILE
pickled_file =  open("./myfiles/dict.pkl","wb")
pickle.dump(d, pickled_file)  # pickles into byte stream file
pickled_file.close()

with open("./myfiles/dict.pkl","rb") as f:
	d3 = pickle.load(f)   # unpickles the file

# PICKLING A PANDAS SERIES TO FILE
# Series object Example with saving as a pickle file
s = pd.Series(data=[0,1,2,3,4,5])                 
s.to_pickle('./myfiles/series.pkl')
with open('./myfiles/series.pkl', 'rb') as f:
	s2 = pickle.load(f)

# PICKLING A DATAFRAME TO FILE
df = pd.DataFrame(data=[['Alex',10],['Fred',12],['Dave',14]])  # DataFrame object
df.to_pickle('./myfiles/dataframe.pkl')     # Saves as a pickle file
with open('./myfiles/dataframe.pkl', 'rb') as f:
	df2 = pickle.load(f) # unpickled


# see bezpy_111_shelve.py for persisting pickled objects