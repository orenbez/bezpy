# TRY THIS https://towardsdatascience.com/pandas-tips-i-wish-i-knew-before-ef4ea6a39e1a
# TRY THIS https://towardsdatascience.com/the-top-five-most-useful-commands-in-pandas-4390d4e165a5
# https://towardsdatascience.com/pandas-analytics-server-d9abceec888b
# https://towardsdatascience.com/reordering-pandas-dataframe-columns-thumbs-down-on-standard-solutions-1ff0bc2941d5
# https://towardsdatascience.com/top-5-functions-for-exploratory-data-analysis-with-pandas-7b3cbe1a1566
# https://towardsdatascience.com/20-pandas-functions-that-will-boost-your-data-analysis-process-f5dfdb2f9e05
# ======================================================================================================================
# IMPORTED MODULES - Note need to install 'xlrd', 'pyarrow', 'openpyxl
# import pandas_datareader.data as web
# see https://www.tutorialspoint.com/python_pandas/python_pandas_quick_guide.htm
#
# see https://www.tutorialspoint.com/python_pandas/
# python -m pip install --upgrade --pre pandas==1.0.0rc0
from decimal import Decimal
from datetime import timedelta as td
from datetime import datetime as dt
from datetime import date
import sys
from time import time

import pandas as pd
import pandasql as ps
import numpy as np

# ======================================================================================================================
# Pandas Series: one-dimensional array, indexed.  IMPORTANT as Columns of multi-dim arrays are reduced to a series
# ======================================================================================================================
# Homogeneous data (NOTE can be type object but that is slow), Size Immutable, Values of Data Mutable
# 'Size Immutable' => fixed length, no append function to add or to remove elements
# Constructor: pandas.Series(data, index, dtype, copy)
# Note default indexing is 0,1,2,3,4....
# dtype = datatype, If None, data type will be inferred, if mixed data types 'Object' is assumed

# ======================================================================================================================
# Pandas Series Functions:
# ======================================================================================================================
# s.abs()            Returns absolute values as series
# s.mod()            Return Modulo of series, e.g. s.mod(3)
# s.describe()       Returns analysis of column based on whether the columns is numerical or
# s.unique()         Returns numpy array of unique values
# s.nunique()        Returns number of unique values
# s.value_counts()   Returns count of each unique value, normalize=True will give you percentages
# s.sum()            Sum of all values
# s.prod()           Product of all values, same as s.product()
# s.head()           Displays top values (default is five values) use head(n) for diff number of values
# s.tail()           Displays last values (default is five values) use tail(n) for diff number of values
# s.sample()         Displays sample values (default is 1 value) use sample(n) for diff number of values
# s.values           Converts to np array
# s.compare(s2)      Compare to another Series and show the differences.
# s.to_csv()         Writes to CSV
# s.to_dict()        Converts Series to dictionary pd.Series([0,1,2], index=['a','b','c']) -> {'a': 0, 'b': 1, 'c': 2}
# s.to_excel()
# s.to_json()        Series to Json pd.Series([0,1,2], index=['a','b','c']) ->  '{"a":0,"b":1,"c":2}'
# s.to_list()        Converts series to list but can also use to convert index to list
# s.to_markdown()    Converts to printable md format
# s.to_numpy()       Converts to array (also s.values)
# s.to_period()      Convert Series from DatetimeIndex to PeriodIndex.
# s.to_pickle()      Converts to pickle file
# s.to_sql()         Writes to database see bezpy_13_SqlAlchemy.py
# s.to_timestamp()   Converts string-> timestamp
# s.pct_change()     Change from previous value
# s.std()            Standard Deviation
# s.kurt()           Kertosis value, same as s.kertosis()
# s.sort_values()    by=['colB', 'colC'], ascending=False, na_position='last' (nulls last), inplace=True
# s.sort_index()     Sort by the index
# s.mean()           Mean value
# s.median()         Median value
# s.memory_usage()  # bytes consumed by series, index=False (excludes index which is default), deep=True (introspect the data deeply by interrogating `object` dtypes for system-level memory consumption, and include it in the returned value)
# s.min()           # Min value of series
# s.max()           # Max value of series
# s.nlargest(3)     # Largest 3 values
# s.nsmallest(3)    # Smallest 3 values
# s.mode()          # Most frequent
# s.quantile()      # s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9]), s.quantile(.25, interpolation='linear') = 3  (i.e. 25% of the data is below this point)
# s.idxmax()        # returns index value for the max value of the group
# s.idxmin()        # returns index value for the min value of the group
# s.replace()       # replaces values in series, not only for strings.
# s.map()           # Map elements of array with dictionary  e.g. s.map({0: 'Zero', 1: 'One'}) operate on one element at time, returns NaN for the rest
                    # .map() is for substitutions .apply() , .transform() used for function mapping
# s.transform()     # Similar to apply but works with function, a string function, a list of functions, and a dict
# s.apply()         # Similar to transform e.g. s.apply(lambda x: x+1)  but use with functions only, also use for df, also operate on one element at time, suited for more complex mappings
# s.isnull()        # Returns bool series where null=True
# s.isna()          # Same as isnull
# s.fillna(value)   # Fills all null values with give value
# s.notnull()       # Returns bool series where null=False
# s.notna()         # Same as notnull
# s.add(s2)         # Sums entries of s1 to those of s2
# s.argmin()        # Returns argument which gives smallest value
# s.idxmin()        # Returns argument which gives smallest value (same as above)
# s.argmax()        # Returns argument which gives smallest value
# s.idxmax()        # Returns argument which gives smallest value (same as above)
# s.argsort()       # Returns series of entries in sorted order
# s.at()            # see below
# s.loc()           # see below
# s.iloc()          # see below
# s.index           # Returns index array,  same as s.axes
# s.keys()          # Returns index array
# s.all()           # Returns True if all entries in series has bool value of True
# s.any()           # Returns True if any entry in series has bool value of True
# s.append(s2)      # appends s2 to s.  Returning a new series since 's' is immutable
# s.astype()        # Used for conversions of entries (see below). Parameters copy=True returns copy, copy=False, modifies in-place, Specifies whether to return a copy (True), errors='raise' or 'ignore'
# s.equals(s1)      # Returns True if series s is equal to s1, and dtypes are identical  (ALSO USE FOR DATAFRAMES)
# s.eq(s1)          # Returns series of booleans comparing each value
# s.copy()          # creates a copy of the series
# s.clip(lower=0, upper=1)  # Sets values outside of limits to minimal/maximal values
# s.diff()                  # Generates a series of differences between value with previous value
# s.where(s<3, other=4)     # Returns series which satisfy condition, else populates with 'other' value
# s.dtype                   # returns dtype of the data, e.g dtype('O')  for 'Object' type, dtype('int64') for integer
# s.dtypes                  # for a series, same as above, for df - shows dtype for each column

s = pd.Series(data=[0,1,2,3,4,5], index=['a','b','c','d','e','f'], dtype='float64') # dtype is coerced as 'float64'
s = pd.Series([0,1,2,3,4,5], index=['a','b','c','d','e','f'])  # dtype is automatically inferred as 'int64'
s = pd.Series(data=[0,1,2], dtype='int64')
# 0    0
# 1    1
# 2    2
# dtype: int64

# interpolation : {‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # => 9 buckets between 1st and last digit
s.quantile(0, interpolation='linear')      # 1
s.quantile(0.25, interpolation='linear')   # =3.25, (9*0.25=2.25 => 1/4 way along in 2nd bucket between digit '2' & '3'
s.quantile(0.25, interpolation='midpoint') # =3.5   (midpoint between digit '2' & '3'
s.quantile()      # = 5.5, default is 0.5 i.e 50% quartile
s.quantile(0.5)   # = 5, default is 0.5  (same as above)  you are 1/2 way between 4th & 5th digit
s.quantile(0.75, interpolation='linear')  # 7.75
s.quantile(1, interpolation='linear')     # 10.0


s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) # => 10 buckets between 1 & 11
s.quantile(0, interpolation='linear')     # = 1  (before 1st bucket
s.quantile(0.25, interpolation='linear')  # = 3.5  (10 * 0.25= 2.5 => 1/2 way between '3' & '4'
s.quantile(0.5, interpolation='linear')   # = 6.0
s.quantile(0.75, interpolation='linear')  # = 8.5
s.quantile(1, interpolation='linear')     # = 11

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8])
s.quantile([.25, .50, 0.75], interpolation='midpoint')
# 0.25    2.5
# 0.50    4.5
# 0.75    6.5
# dtype: float64

s.astype('float64')  # converts to dtype='float64'
# 0    0.0
# 1    1.0
# 2    2.0
# dtype: float64


# The Replace Function
# replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad')
# to_replace : the values that need replacing
# value : the value to replace with
# method : {'pad', 'ffill', 'bfill', `None`} used insted of 'value' e.g. 'bfill' is backfill the same value as the one ahead

s.replace(to_replace=0, value=1, inplace=True)  # replaces zeros with ones and modifies s inplace
s.replace([0,1,2], [11,12,13])  # Replace any of values in first list with corresponding in second list
s.replace({0:11, 1:12, 2:13})  # same as above using dictionary
s = pd.Series(data=['bad', 'foo', 'bat'])
# s.replace(to_replace='^b.d$', value='bod', regex=True) # Currently gives error TypeError: 'NoneType' object is not callable
# 0    new
# 1    foo
# 2    new
# dtype: object

s.memory_usage(deep=True)  # returns 308, total memory used in RAM = 308 bytes, with deep=True the memory footprint of object dtype columns is calculated too


s.index     #  Index(['a', 'b', 'c', 'd', 'e', 'f'], dtype='object')
s.values    #  array([0, 1, 2, 3, 4, 5], dtype=int64)
s  # RETURNS: COL1 = index, COL2 = values
# a    0
# b    1
# c    2
# d    3
# e    4
# f    5
# dtype: int64

s = pd.Series(data=[0, 1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e', 'f'], dtype='int64')
# ======================================================================================================================
s.iloc[4]    # returns 5th element, ALWAYS WORKS
s[4]         # same as above, BUT DON'T USE.

s.loc['e']   # returns 5th element, ALWAYS WORKS.  (if multiple elements have index 'e', will return a series of those elements
s['e']       # same as above BUT DON'T USE.

s.iloc[0:2]  # returns first two elements (slicing)
s[0:2]       # same as above, BUT DON'T USE. only works when index are string chars not integers

s.iloc[[0, 2]]    # returns subset series of elements 0 and 2 supplied as list [0, 2],
s[[0, 2]]         # same as above, this works since the index are string characters
# a    0
# c    2
# dtype: int64

s[s>3] #this slices the list to all values greater than 3
# 4    4
# 5    5

s.where(s>3)
# 0    NaN
# 1    NaN
# 2    NaN
# 3    NaN
# 4    4.0


s = pd.Series([0,1,2,3,4,5], index=[9,10,11,12,13,14])
s.loc[9] # returns first element
s.iloc[0]  # returns first element
#s[0] # this would give an error as the index are integers and zero is not in the range 

# ======================================================================================================================
#  string series with default index 0,1,2
# ======================================================================================================================
s2 = pd.Series(['aaa ','bbb ','ccc '])
# 0    aaa
# 1    bbb
# 2    ccc
# dtype: object


# pandas.Series.str functions

s2.str.upper()       # performs string operation on the entire series and returns
s2 = s2.str.upper()  # modifies s2
s2.str.rstrip().str.upper()  # combines string operations
# 0    AAA
# 1    BBB
# 2    CCC
# dtype: object

s2.str.rstrip().str.upper()[:2]  # returns first two elements of the series
s2.str.rstrip().str.upper().iloc[:2] # same as above but less confusing
# 0    AAA
# 1    BBB
# dtype: object

s2.str.rstrip().str.upper().str[:2] # slices first two chars from every element
# 0   AA
# 1   BB
# 2   CC
# dtype: object

# pandas.Series.str.slice function -- WARNING not exactly the same as the slice() function
s2.str.rstrip().str.upper().str.slice(stop=2)  # same as above command

# pandas.Series.str.split(pattern, max_no, expand=True/False)
s2 = pd.Series(['aaa:bbb','ccc:ddd','eee:fff'])
s2.str.split(':')
# 0    [aaa, bbb]
# 1    [ccc, ddd]
# 2    [eee, fff]
# dtype: object

s2.str.split(':', expand=True)     # returns dataframe
#      0    1
# 0  aaa  bbb
# 1  ccc  ddd
# 2  eee  fff

s = pd.Series(['line to be wrapped', 'another line to be wrapped'])
s.str.wrap(4)   # adds next-line to each element every 4 chars and after every space
# 0               line\nto\nbe w\nrapp\ned
# 1    anot\nher\nline\nto\nbe w\nrapp\ned

s2.map(lambda x: str(x).rstrip()) # convert to string and then do rstrip on each element of series
s2.map(lambda x: str(x)[:2])      # convert to string and retreive first two chars of each element
s2.apply(lambda x: str(x)[:2])    # same as above, apply is suited to more complex operations and aggregation

# Can Use a dictionary to map each field (doesn't work for the built-in python 'map')
s.map({0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five'})

# verify if one s2 is a subset of s1 
s1 = pd.Series([0, 1, 2, 3, 4, 5])
s2 = pd.Series([2, 5, 6])
s2.isin(s1)                   # Checks values in Series S1 and returns Which S2 Values have a match
s2.isin([0, 1, 2, 3, 4, 5])   # Same as above but uses a list
# 0     True
# 1     True
# 2    False
# dtype: bool

s2[s2.isin(s1) == False]  # Values for s2 which are not in s1
# 2    6
# dtype: int64

s2.isin([6])  # To Check a single element you still need a list container
#0    False
#1    False
#2     True   # only the last element has a match with integer 6
#dtype: bool

# ======================================================================================================================
# converting dict to Series, keys become the series index, data type becomes 'object'
# ======================================================================================================================
d = {'name' : 'IBM', 'date' : '2010-09-08', 'shares' : 100, 'price' : 10.2}
s = pd.Series(d)
# name             IBM
# date      2010-09-08
# shares           100
# price           10.2
# dtype: object


# ======================================================================================================================
# IMPORTANT!!!! THERE ARE 4 WAYS TO ACCESS SERIES DATA.  1 & 3 will always work
# ======================================================================================================================
s.iloc[0]        # 1. returns first data 'IBM' - dataframe index number location, THIS ALWAYS WORKS
s[0]             # 2. returns first data 'IBM' - works like indexing a list, ONLY WORKS for String index
s.loc['name']    # 3. returns first data 'IBM' - dataframe index name location
s['name']        # 4. returns first data 'IBM' - works like accessing value in python dict ONLY WORKS for String index

s.iat[0] = 'IBM2'
s.at['shares'] = 150  # modifies value
s.at['change'] =.03   # adds new field

# INDEX           DATA
# name             IBM2
# date      2010-09-08
# shares           100
# price           10.2
# dtype: object

# ======================================================================================================================
# Recognized Data Types for a series or DataFrame column
# ======================================================================================================================
# There are confusingly similar type of dtypes e.g. bool, boolean, int64, Int64
# Pandas {'boolean', 'category', 'interval', 'string', 'UInt8', 'UInt16', 'UInt32', 'UInt64', 'Int8', 'Int16', 'Int32', 'Int64', 'Float32', 'Float64', 'datetime64[ns]', 'object'}  
# Numpy  {'int8', 'int16', 'int32', 'int64', 'float32', 'float64', 'datetime64', ...} full list below
# Python {'bool', 'int', 'float', 'str'},  
# some python types are mapped to pandas or numpy data types  float->float64, int->int32

# Full list of Python data types ... 
pandas_dtypes = [i for i in dir(pd) if i.endswith('Dtype')]
['BooleanDtype', 'CategoricalDtype', 'DatetimeTZDtype', 'Float32Dtype', 'Float64Dtype', 'Int16Dtype', 'Int32Dtype', 
'Int64Dtype', 'Int8Dtype', 'IntervalDtype', 'PeriodDtype', 'SparseDtype', 'StringDtype', 'UInt16Dtype', 'UInt32Dtype', 
'UInt64Dtype', 'UInt8Dtype']
pd.Int64Dtype.name  # 'Int64'  e.g. dtype='Int64'
pd.Int64Dtype()     # can be used the same as 'Int64'  e.g.  dtype=pd.Int64Dtype()
pd.Int64Dtype.type  # <class 'numpy.int64'>

# ======================================================================================================================
# Full Numpy Datatype List. eg pd.Series([0,1,2,3,4,5], dtype='uint64') will be recognized
# ======================================================================================================================
# Data          Type	Description
# ----------------------------------------------------------------------------------------------------------------------
# bool_	        Boolean (True or False) stored as a byte
# int_	        Default integer type (same as C long; normally either int64 or int32)
# intc	        Identical to C int (normally int32 or int64)
# intp	        Integer used for indexing (same as C ssize_t; normally either int32 or int64)
# int8	        Byte (-128 to 127)
# int16	        Integer (-32768 to 32767)
# int32	        Integer (-2147483648 to 2147483647)
# int64	        Integer (-9223372036854775808 to 9223372036854775807)
# uint8	        Unsigned integer (0 to 255)
# uint16	    Unsigned integer (0 to 65535)
# uint32	    Unsigned integer (0 to 4294967295)
# uint64	    Unsigned integer (0 to 18446744073709551615)
# float_	    Shorthand for float64.
# float16	    Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
# float32	    Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
# float64	    Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
# complex_	    Shorthand for complex128.
# complex64	    Complex number, represented by two 32-bit floats
# complex128	Complex number, represented by two 64-bit floats
# object_       Object

# e.g.  df['COL2'].dtype == numpy.object_

# ======================================================================================================================
s1 = pd.Series([0, 1, 2, None], dtype=bool)     # regular python bool which coerces values to boolean, bool(None) = False
s2 = pd.Series([0, 1, 0, pd.NA], dtype='boolean') # new pandas 1.0.0 dtype, allows null values with pd.NA
s3 = pd.Series(['aaa', 'bbb', 'ccc', 'ddd'], dtype='string')    # new string dtype for pandas 1.0.0 (previously used dtype=object)
s4 = pd.Series([1, 2, 3, 4], dtype='int64')              # Numpy datatype, could also do dtype=np.int64
s5 = pd.Series([1, 2, 3, pd.NA], dtype='Int64')         # Pandas datatype is more flexible, can take the pandas null value
s6 = pd.Series([1.0, 2, 3, 4.1], dtype='float64')       # Numpy datatype, could also do dtype=np.float64
s7 = pd.Series(data=[dt(2000,1,1), dt(2000,1,2), dt(2000,1,3), dt(2000,1,4)],  dtype='datetime64[ns]')  # Pandas TimeStamp c.f. Numpy datetime64 e.g. np.datetime64('2000-01-01')

pd.Series(['1.2', '1.3'], dtype='str')  # will construct dtype=object
pd.Series([1.2, 1.3], dtype=str)        # python str type, will coerce values to string but will be dtype=object
pd.Series([1.2, 1.3], dtype='str')      # same as above
pd.Series([1.2, 1.3], dtype='string')   # dtype is now Pandas StringDtype

pd.Series(['M', 'F', 'F', 'F', 'M', 'F'], dtype='category')   # Memory-efficient array for string values with many repeated values.

pd.Series(['M', 'F', 'F', 'F', 'M', 'F'], dtype='object').memory_usage(deep=True)      # returns 476
pd.Series(['M', 'F', 'F', 'F', 'M', 'F'], dtype='string').memory_usage(deep=True)      # returns 476, treated as above
pd.Series(['M', 'F', 'F', 'F', 'M', 'F'], dtype='category').memory_usage(deep=True)    # returns 358, save memory as declared 'category' type


# ======================================================================================================================
# Null Types  
# ======================================================================================================================
# None            (python)
# float('nan')    (python float - not a number)
# Decimal('NaN')  (decimal type - not a number)
# np.nan          (numpy not a number)
# pd.NaT          (pandas timestamp null)
# pd.NA           (new pandas generic null value)

isinstance(pd.NA, pd._libs.missing.NAType)  # True
isinstance(pd.NaT, pd._libs.NaTType)        # True


pd.Series([1, 2, np.nan])     # casts as float type since you have missing value np.nan
# 0    1.0
# 1    2.0
# 2    NaN
# dtype: float64

pd.Series([1, 2, pd.NA])       # null-type introduced in pandas 1.0.0  Jan 2020  null type pd.NA
# 0       1
# 1       2
# 2    <NA>
# dtype: object

pd.Series([None, float('nan'), Decimal('NaN'), np.nan, pd.NaT, pd.NA, ''], dtype='string')  # all converted to pd.NA except for the empty string
# 0    <NA>
# 1    <NA>
# 2    <NA>
# 3    <NA>
# 4    <NA>
# 5    <NA>
# 6
# dtype: string

pds = pd.Series([None, float('nan'), np.nan], dtype='float64')   # all will convert to np.nan
# 0   NaN
# 1   NaN
# 2   NaN
# dtype: float64

np.isnan(pds.iloc[0])  # True
pd.isna(pds.iloc[0])   # True   (same method as pd.isnull())
pds.iloc[0] is np.nan  # returns False even though it is np.nan 

# ======================================================================================================================
# Pandas DataFrame: two-dimensional array
# ======================================================================================================================
# Potentially each column is of a different type (Heterogeneous data)
# Size – Mutable
# Data Mutable
# Labeled axes (rows and columns)
# Can Perform Arithmetic operations on rows and columns
# Constructor: pandas.DataFrame(data, index, columns, dtype, copy)
# data  - ndarray, series, map, lists, dict, constants and also another DataFrame.
# index - For the row labels, default 0,1,2,3,...
# columns - For column labels, default 0,1,2,3,...
# dtype - Data type of each column, CAN ONLY SET ONE TYPE FOR ALL COLUMNS USING THIS PARAMETER
# copy - True for copying of data, default is False

## if you get a SettingWithCopyWarning :https://www.dataquest.io/blog/settingwithcopywarning/
## Then you are probably trying to modify a 'View' instead of a 'Copy'


# ======================================================================================================================
# TYPE 1: NESTED LIST -> DATAFRAME
# ======================================================================================================================
# NOTE THAT pd.DataFrame.from_records(data) is the same as pd.DataFrame(data)
# ======================================================================================================================
df1 = pd.DataFrame(data=[['Alex',10],['Fred',12],['Dave',13]], index =['a','b','c'], columns=['Name','Age'])


# RETURNS: COL1 = INDEX, COL2 = Name, COL3 = Age
#    Name  Age
# a  Alex   10
# b  Fred   12
# c  Dave   13

df1.dtypes
# Name    object
# Age      int64
# dtype: object


# The BEST way to set datatypes is like this ...  Can not do it during initialization line
df1 = df1.astype({'Name': 'string', 'Age': 'int32'})
# df1.dtypes
# Name    string
# Age      int32
# dtype: object


# ======================================================================================================================
# TYPE 2: LIST OF TUPLES -> DATAFRAME
# ======================================================================================================================
data = [(3, 'a'), (2, 'b'), (1, 'c')]
pd.DataFrame(data)   # or pd.DataFrame.from_records(data) 
# note that the columns will be defaulted to ‘0’, ‘1’, ‘2’, … if they are not set

# ======================================================================================================================
# TYPE 3: DICTIONARY -> DATAFRAME  (keys become columns, Values  column data
# ======================================================================================================================
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],
        'Age': [28,34,29,42]}
index = ['row0', 'row1', 'row2', 'row4']
pd.DataFrame(data, index=index)
#       Name  Age
# row0  Tom    28
# row1  Jack   34
# row2  Steve  29
# row4  Ricky  42


index = [10, 20, 30, 40]
df2 = pd.DataFrame(data, index=index)
#      Name  Age
# 10    Tom   28
# 20   Jack   34
# 30  Steve   29
# 40  Ricky   42

#  Read From Dictionary of ROWS using from_dict()
pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]), orient='columns')   # DEFAULT is orient='columns'
#    A  B
# 0  1  4
# 1  2  5
# 2  3  6

pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]), orient='index', columns=['one', 'two', 'three'])
#    one  two  three
# A    1    2      3
# B    4    5      6


# ======================================================================================================================
# TYPE 4: Lists[dict] -> DATAFRAME, not very efficient as columns repeated
# ======================================================================================================================
data = [{'COL1': 1, 'COL2': 2, 'COL3': 3},
        {'COL1': 5, 'COL2': 6, 'COL3': 7}, 
        {'COL1': 9, 'COL2': 10, 'COL3': 11}]
df3 = pd.DataFrame(data)
#    COL1  COL2  COL3
# 0     1     2     3
# 1     5     6     7
# 2     9    10    11


# ======================================================================================================================
# TYPE 5: np.array -> DATAFRAME
# ======================================================================================================================
# i4 = integer 4 bytes, U1 unicode string 1 byte
data = np.array([(3, 'a'), (2, 'b'), (1, 'c')], dtype=[('col_1', 'i4'), ('col_2', 'U1')])
pd.DataFrame(data)
#    col_1 col_2
# 0      3     a
# 1      2     b
# 2      1     c


# ======================================================================================================================
# TYPE 6: EXCEL->DATA FRAME
# ======================================================================================================================
df4 = pd.read_excel(r'myfiles\data.xlsx', sheet_name='Sheet1', skiprows=0, usecols='A:C', dtype=object)
#  COL1 COL2 COL3
#0    1    2    3
#1    4    5    6
#2    7    8    9


# For a single sheet
df4 = pd.read_excel(io=r'myfiles\data.xlsx',
                    sheet_name='Sheet2',
                    skiprows=1,
                    usecols='A:B',
                    na_values=['<NA>', 'N/A', 'NA', 'NULL'],
                    dtype={'COL1': 'Int32','COL2': 'string'})

# read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None,
#            squeeze=False, dtype: 'DtypeArg | None' = None, engine=None, converters=None, true_values=None,
#            false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True,
#            verbose=False, parse_dates=False, date_parser=None, thousands=None, comment=None, skipfooter=0,
#            convert_float=None, mangle_dupe_cols=True, storage_options: 'StorageOptions' = None)

# io=string pathname of excel file
# sheet_name=sheet name or number (0 is first sheet), if you provide a list the response is a dictionary of dataframes
# header=None => no header row,  0 => the first row is the header row (this is the default)
# names=None is default else provide a list of column names for the dataframe
# index_col=None is default, else provide column to be used for the row indices
# usecols=integer or list of integers for the colums to import to df or use a string e.g. "A:C,F,G" includes cols A,B,C,F,G
# skiprows=default is 0, else provide integer of number of rows from the top to skip
# dtype E.g. dtype='str' (for all columns) or  dtype={'col_a': np.float64, 'col_b': np.int32}
# converters = {'col_a': custom_function1, 'col_b': custom_function2}  # can define your own custom functions to convert column data
# na_values= additional strings list or single string to be recognized as Null value


# pd.ExcelFile(path_or_buffer, engine=None, storage_options: 'StorageOptions' = None) -- seems to invoke read_excel()
# Creates object for ALL Sheets in workbook.
ex_file = pd.ExcelFile(r'myfiles\data.xlsx')
ex_file.engine  # 'openpyxl'
ex_file.sheet_names   # ['Sheet1', 'Sheet2']
ex_file.book   #  <openpyxl.workbook.workbook.Workbook object at 0x000001ECDB842110>
ex_file.parse(sheet_name='Sheet2', header=1)  # returns dataframe for 'Sheet2'

# ======================================================================================================================
# TYPE 7: SERIES DICTIONARY -> DATAFRAME  (preserves datatype for each column)
# ======================================================================================================================
df5 = pd.DataFrame(data={'c1':s1,'c2':s2,'c3':s3,'c4':s4,'c5':s5,'c6':s6,'c7':s7})
df5.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   c1      4 non-null      bool
#  1   c2      3 non-null      boolean
#  2   c3      4 non-null      string
#  3   c4      4 non-null      int64
#  4   c5      3 non-null      Int64
#  5   c6      4 non-null      float64
#  6   c7      4 non-null      datetime64[ns]
# dtypes: Int64(1), bool(1), boolean(1), datetime64[ns](1), float64(1), int64(1), string(1)
# memory usage: 302.0 bytes


# With this method you can set dtypes for each column ...
df5 = pd.DataFrame({'A':pd.Series([1,2,3], dtype='str'),
                    'B':pd.Series([4,5,6], dtype='int'),
                    'C':pd.Series([7,8,9], dtype='float')})

d = {'Name': pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack', 'Lee','David','Gasper','Betina','Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
df = pd.DataFrame(d)


# ======================================================================================================================
# TYPE 8: CSV FILE -> DATAFRAME
# ======================================================================================================================
df6 = pd.read_csv('myfiles\\titles.csv', index_col=None, sep=',', skiprows=None, encoding='utf-8')
     # sep='\t'  e.g. tab seperator
     # index_col = None : there is no index,  otherwise index_col = 'date' use the 'date column as index
     # usecols=[‘col1’, ‘col2’, …],   ... to select columns
     # iterator=True
     # skiprows=100, ... rows to skip
     # nrows=100,    ... rows to select
     # low_memory=False
     # parse_dates=['date_col1', 'date_col2',  will parse the date columns into type datetime64[ns]
     # see date_parser=
     # na_value = [9999, "?"]   ... represent both of these values in the data as NaN
     # true_values = ['Yes'],  ... converts string value 'Yes' to True
     # false_values = ['No']   ... converts string value 'No' to False
     # dtype={‘col1’: string, ‘col2’: int, …}  or dtype='string'  (works for all columns) <-----  Only working since pandas 1.1.0

# exception is raised pandas.errors.EmptyDataError for read_csv when empty data or header is encountered

# ======================================================================================================================
# TYPE 9:  list of DataClass objects
# ======================================================================================================================
from dataclasses import dataclass

@dataclass
class Point:
    x_loc: int
    y_loc: int

points = [Point(1, 2), Point(4, 5), Point(3, 7)]

pd.DataFrame(points)
#    x_loc  y_loc
# 0      1      2
# 1      4      5
# 2      3      7
# ======================================================================================================================

df = df1

df['Name'] # returns the name column as a data series
# df.loc['Name'] # returns error as 'Name' is not in index

# if you have labeled the columns - you can not access by the number so ..
# df[0]  gives an error as you have named the columns


# set column as index
df = df.set_index('Name')  # sets the 'Name' Column as the index column
# Note that df.set_index('Name',inplace=True) will modify df itself and not
# return a dataframe to assign


df.loc['Alex']  # returns Age 10
# Age    10
# Name: Alex, dtype: int64


df.reset_index(inplace=True) #moves 'Name' back as a column and resets the index to 0,1,2,...

df = pd.DataFrame(data=[['Alex',10], ['Fred',12], ['Dave',13], ['Pete',16], ['Bill',9], ['Paul',14]])
# ======================================================================================================================
# Defaulted index and column
# ======================================================================================================================
#       0   1
# 0  Alex  10
# 1  Fred  12
# 2  Dave  13
# 3  Pete  16
# 4  Bill   9
# 5  Paul  14

df[0]               # returns first column
df[[0,1]]           # returns both columns as a dataframe- you provided list [0,1]
df.iloc[0]          # returns first row as a SERIES
df.iloc[[0]]        # returns first row as a DATAFRAME
df.iloc[[0,1,2]]    # dataframe of first three rows, df.iloc[0,1,2] returns error Too many indexers
df.loc[0]           # also returns first row, as it is indexed as 0

df.iloc[range(2,5)]  # returns rows 2 to 4 as a dataframe
df.iloc[2:5]         # same as above
df.iloc[[2,3,4]]     # same as above

# Reference to df Method 1
df_ref = df    # note that df_ref is just another name for df, they are the same
df_ref is df   # returns True, modify one and you change the other

# Reference to df Method 2
df_ref = df.copy(deep=False)  # returns reference to df
df_ref is df   # returns false for some reason but is still a reference to df


# Copy of df
df_copy = pd.DataFrame(df, copy=True)
df_copy = df.copy()   # same as above
df_copy is df         # returns False
df_copy.equals(df)    # returns True

df_copy == df         # returns DataFrame with boolean fields
df_copy.eq(df)        # same as above
#       0     1
# 0  True  True
# 1  True  True
# 2  True  True
# 3  True  True
# 4  True  True
# 5  True  True


df2
#      Name  Age
# 10    Tom   28
# 20   Jack   34
# 30  Steve   29
# 40  Ricky   42

# .iat[] / at[] are 'scalar access locators' for specific scalar elements only  (follows column df[COL].iat[x])
# .iloc[] / loc[] are location executors that can be used for scalars or for series

# Note that the index numbers are still 0,1,2,3 w.r.t.  .iat[] or .iloc[]
# Note that the index values are 10,20,30,40   w.r.t.   .at[]  or .loc[]

df2.iloc[0]  # returns first row as pandas series
df2.loc[10]  # returns first row as pandas series
df2['Name']  # returns first column as pandas series
# df2[0] this returns error as columns have names


#df2.at[10]  # returns error, .at[] ONLY follows column to specify a single element,
# can not return a series like loc but is FASTER when looping through a series
df2['Name'].at[10]  #  Returns Tom
df2['Name'].iat[0]  #  Returns Tom


# Change Tom's Name to Fred
df2['Name'].at[10] = 'Fred'
df2['Name'].iat[0] = 'Fred'

# IMPORTANT NOTE:
# BEST TO USE .at[] for assigning a value
#         USE .iloc[], .loc[] only to retrieve
#  df2['Name'].loc[10] = 'Fred' this would issue a Warning
#  df2['Name'].iloc[0] = 'John' this would issue a Warning
#  pd.options.mode.chained_assignment = None  # suppress warnings but this is a last resort!!!!

# NOTE:
df2['Age'] # returns age column as a panda series, index is 10,...,40

# INDEX DATA
# 10    28 <---- first row of data
# 20    34
# 30    29
# 40    42
# Name: Age, dtype: int64

# display first Age on list

df2['Age'][10]      # returns 28 - as above
df2['Age'].at[10]   # returns 28 - better to keep .at[] for writing only not reading
df2['Age'].iat[0]   # returns 28 - better to keep .at[] for writing only not reading
df2['Age'].loc[10]  # returns 28 -  df2[COL].loc[ROW]
df2['Age'].iloc[0]  # returns 28 - using the integer index not the official index
#df2['Age'][0]      # returns error as rows are not integer indexed 0,1,2, .... 


df2.iloc[0] # returns 1st row of data as series,  index = ['Name','Age']
df2.loc[10] # returns 1st row of data as series,  index = ['Name','Age']

#INDEX    DATA
# Name    Fred
# Age       28    <------2nd row of data
# Name: 10, dtype: object


# NOW WE CAN USE MULTIPLE WAYS TO ACCESS SERIES DATA returned by  df2.iloc[] or df2.loc[]
df2.iloc[0]['Age']         # returns 28
df2.iloc[0].loc['Age']     # returns 28

df2.iloc[0][1]             # returns 28
df2.iloc[0].iloc[1]        # returns 28
df2.iloc[0, 1]             # returns 28

df2.loc[10].iloc[1]        # returns 28
df2.loc[10][1]             # returns 28

df2.loc[10]['Age']         # returns 28
df2.loc[10, 'Age']         # returns 28
df2.loc[10].loc['Age']     # returns 28



# ======================================================================================================================
# Lookup Steve's Age
# ======================================================================================================================

# METHOD 1 ... convert to python series
s = pd.Series(list(df2['Age']), index = list(df2['Name']))
ans = s['Steve']

# alternatively, ... METHOD 2 convert to python list and find index using the 'index' list function, not pandas
ix = list(df2['Name']).index('Steve')
ans = df2.iloc[ix]['Age']

# alternatively, ...  METHOD 3
s = df2['Name'] == 'Steve' # this returns boolean pandas series whose index MATCHES that of df2 [10,...,40]
# 10    False
# 20    False
# 30     True
# 40    False
# Name: Name, dtype: bool

df2[s]  # this returns a simple dataframe
#      Name  Age
# 30  Steve   29

ans = df2[s]['Age'].iloc[0]

# so ...  PREFERRED METHOD
ans = df2[df2['Name'] == 'Steve']['Age'].iloc[0]

# or ...
ans = df2.loc[df2[(df2['Name'] == 'Steve')].index.values[0]][1]  #  bit convoluted but works

# Note that df.index.values returns np array of the index
df2.index.values
# array([10, 20, 30, 40], dtype=int64)

# alternatively ... METHOD 4  (cf. with METHOD 1
df = df2.set_index('Name')  # returns dataframe below, with 'Name' columns as index
#        Age
# Name
# Fred    28
# Jack    34
# Steve   29
# Ricky   42

s = df.loc['Steve'] # returns series
# Age    29
# Name: Steve, dtype: int64
ans = s['Age'] # returns the 'Age' value

# so ...
ans = df2.set_index('Name').loc['Steve']['Age']

# or ...
ans = df2.set_index('Name').loc['Steve'].loc['Age']




# ======================================================================================================================
# Lookup Steve's Age Part II  ... let's say that there are two 'Steve' entries ...
# ======================================================================================================================
x = pd.DataFrame(data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky', 'Steve'],'Age':[28,34,29,42,44]})
#     Name  Age
# 0    Tom   28
# 1   Jack   34
# 2  Steve   29
# 3  Ricky   42
# 4  Steve   44

ans = list(x[x['Name'] == 'Steve']['Age'])  #PREFERRED
# ans = [29, 44]

# or using Method 4
ans = list(x.set_index('Name').loc['Steve']['Age'])
# ans = [29, 44]



# Replace Function
#df.replace(self, to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad')


# Replace Names Steve & Ricky for James
df2['Name'] = df2['Name'].replace(['Steve', 'Ricky'], 'James')

# Replace two names for two
df2['Name'] = df2['Name'].replace(to_replace=['Tom', 'Jack'], value=['Tim','Jacky'])
df2['Name'] = df2['Name'].replace({'Tom':'Tim', 'Jack': 'Jacky'})
# df2.replace(to_replace=r'^Ba.$', value='Bob', regex=True)  # Replaces regex  currently giving strange error TypeError: 'NoneType' object is not callable


# ======================================================================================================================
# COLUMN OPERATIONS / ROW OPERATIONS
# ======================================================================================================================
df3['COL3'] = 7             # sets all COL3 values to 7
df3['COL4'] = [4, 8, 12]      # creates additional column
df3['COL5'] = [df3['COL4'].iloc[i]**2 for i in range(len(df3))]    # generates data for COL5 based on COL4
df3['COL0'] = pd.NA

# ================
# DELETE COLUMNS
# ================
df3.pop('COL3')    # deletes SINGLE column from df3 and returns the removed column
#del df3['COL3']   # same as above but returns None

# df4 = df3.drop(columns=['COL3', 'COL4'])  # returns df3 with multiple columns removed (df3 unchanged)
# df4 = df3.drop(['COL3', 'COL4'], axis=1)  # same as above
# Use inplace=True to change original data frame

# ================
# DELETE ROWS
# ================
# df4 = df3.drop(index=['row2','row4'])     # returns df3 with multiple rows removed (df3 unchanged)
# df4 = df3.drop(5)                         # drops row 5
# df4 = df3.drop([0, 1, 5], axis=0)         # drops rows 0,1,5  (axis=0 is default)
# df3.drop([0, 1, 5], inplace=True)         # drops rows 0,1,5
# Use inplace=True to change original data frame

df3['COL6'] = df3['COL1'] + df3['COL2']  # column addition derives COL6 which is added to df3
df3['COL7'] = df3['COL4'].map(lambda x: 2 * x)
def times_two(x):
    return 2 * x

# df3['COL7'] = df3['COL4'].map(times_two)   # same as above

df4 = df3[['COL1','COL6']]                           # Returns Subset of Columns
df4 = pd.DataFrame(df3, columns=['COL1','COL6'])     # equivalent to above (appears to be a copy)

list_of_col = df3.columns.tolist()      # Note that tolist() is operating on a numpy array
array_of_col = df3.columns.values       # returns numpy array of column names
series_of_col = df3.columns.to_series()
index_list = df3.index.to_list()        # tolist() also works
index_array = df3.index.values          # numpy array of the row names

len(df3.columns)         # returns number of columns = 5
len(df3)                 # returns number of rows

df3.index = ['rowX','rowY','rowZ'] # this changes the row names which are referenced by .loc

df3.iloc[0][0]           # returns value in first row, first column
df3.iloc[0]['COL1']      # same as above
df3['COL1'].iloc[0]      # same as above (.ix is deprecated)
df3['COL1'].loc['rowX']  # same as above
#df3[0].loc['rowX']      # this fails, first column has a name 'COL1' which must be used for dataframes but not for a series

# note 'iloc' for index number reference, 'loc' for index label reference
df3.loc['rowY']      # displays 2nd row as panda Series, based on index label
df3.loc[['rowX', 'rowZ']]      # displays 1st & 3rd row as panda DataFrame, based on index label
#df3[0]  # would return error as columns are reffered to by name
df3[0:2] # prints the first two rows index=0 and index=1 same as df3.iloc[0:2]
df3[2:3] # prints the 3rd row only, index=2, same as df3.iloc[2:3]
df3[['COL1','COL2']]    # returns first two columns
df3[df3['COL2'] >= 6]   # returns rows that fulfill the condition
df3.query("COL2 >= 6", inplace=False)  # query  achieves same as above and has 'inplace' parameter

# Renames the columns in the data frame
df3.rename(columns = {'COL1':'col_1', 'COL2':'col_2', 'COL3':'col_3', 'COL4':'col_4', 'COL5':'col_5'}, inplace=True)

df = pd.DataFrame(data=((1,2,3),), columns=['A', 'B', 'C'])
df.rename(index={0: "x", 1: "y", 2: "z"})   # renames indices
df.rename({0: "x", 1: "y", 2: "z"}, axis='index') # same as above
df.rename(columns={"A": "a", "B": "b", "C": "c"}, errors="raise")   # renames columns. raise KeyError if the column name is missing
df.rename(str.lower, axis='columns')  # lowers the case for each column


# alternatively use set_axis() without the need of the original column names
df3.set_axis(['col_1','col_2','col_3','col_4','col_5','col_6', 'col_7'], axis='columns', inplace=True)

# APPEND ROW 3 to data frame, column names must be the same
df0 = pd.DataFrame(data=[[1, 2, 4, 16, 3],
                         [5, 6, 8, 64, 11],
                         [9,10, 12, 144, 19]],
                   columns=['COL1', 'COL2','COL4','COL5','COL6'],
                   index=['rowX', 'rowY', 'rowZ'])

df1 = pd.DataFrame(data=[{'COL1': 100, 'COL2': 200,'COL4': 400, 'COL5': 500, 'COL6': 700}],
                   index=['rowN'])


df2 = df0.append(df1, sort=False)  # sort=False will be made default in newer version

#>>> df2
#      COL1  COL2  COL4  COL5  COL6
#rowX     1     2     4    16     3
#rowY     5     6     8    64    11
#rowZ     9    10    12   144    19
#rowN   100   200   400   500   700
# Note: you can append to an empty dataframe, but column orders are not preserved they are alphabetized



df = pd.DataFrame() # empty dataframe
df.empty # Returns True
df = df.append(df3, ignore_index=True, sort=False)

# You can append without an index
df = pd.DataFrame(columns = ['Name','Age'], index=[0, 1, 2]) # empty Null dataframe with 3 rows of NaN values
df = pd.DataFrame(columns = ['Name','Age'])
df = df.append({'Name' : 'Dave' , 'Age' : 22} , ignore_index=True, sort=False)   # no option for inplace=True
df = df.append({'Name' : 'Fred' , 'Age' : 25} , ignore_index=True, sort=False)   # no option for inplace=True
df.at[2] = ['Pete', 22]                   # This adds a third row
df.at[3] = {'Name' : 'Jane', 'Age' : 55}  # This adds a fourth row

# >>> df
#    Name Age
# 0  Dave  22
# 1  Fred  25
# 2  Pete  22
# 3  Jane  55

# insert column to dataFrame (modifies dataframe inplace)
df.insert(2, column='Gender', value=['M', 'M', 'M', 'F'])
#    Name Age Gender
# 0  Dave  22      M
# 1  Fred  25      M
# 2  Pete  22      M
# 3  Jane  55      F

df.to_dict()                  # {'Name': {0: 'Dave', 1: 'Fred', 2: 'Pete', 3: 'Jane'}, 'Age': {0: 22, 1: 25, 2: 22, 3: 55}}
df.to_dict(orient='records')  # [{'Name': 'Dave', 'Age': 22}, {'Name': 'Fred', 'Age': 25}, {'Name': 'Pete', 'Age': 22}, {'Name': 'Jane', 'Age': 55}]
df.to_dict(orient='list')     # {'Name': ['Dave', 'Fred', 'Pete', 'Jane'], 'Age': [22, 25, 22, 55]}
# orient : can take values {'dict', 'list', 'series', 'split', 'records', 'index'}


# Columns can be tuples
df = pd.DataFrame({('x', 1): [1, 2, 3], ('x', 2): [4, 5, 6]})
# >>> df
#    x
#    1  2
# 0  1  4
# 1  2  5
# 2  3  6
df[('x', 2)].values   #  array([4, 5, 6], dtype=int64)

# ======================================================================================================================
# Pandas concat Vs append Vs join Vs merge
# ======================================================================================================================
# Concat gives the flexibility to join based on the axis, all rows (axis=0) or all columns(axis=1)
# Append is the specific case(axis=0, join='outer') of concat
# Join is based on the indices (set by set_index) on how variable =['left','right','inner','outer']
# Merge is based on any particular column each of the two dataframes, this columns are variables on like 'left_on', 'right_on', 'on'
df1 = pd.DataFrame(data=[[1002,'David'],[1003,'Fred'], [1004,'Harold'], [1005,'Elon']], columns=['id','First'])
df2 = pd.DataFrame(data=[[1001,'Bond'], [1002,'Jones'],[1003,'Blogs'], [1006, 'Stalone']], columns=['id','Last'])

# JOIN LAST COLUMN METHOD 1
df1['Last_Column'] = df1['id'].map(df2.set_index('id')['Last'].to_dict())

# JOIN LAST COLUMN METHOD 2
x = df1.set_index('id').join(df2.set_index('id'))    # Left Join

# JOIN LAST COLUMN METHOD 3  'BEST OPTION'    how : {'left', 'right', 'outer', 'inner'}, default 'inner'
x = df1.merge(df2, how='outer', on='id', indicator=True)   #indicator=True this option has adds a _merge column

# DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)

# right : A dataframe or series to be merged with calling dataframe
# how : Merge type, values are : left, right, outer, inner. Default is ‘inner’. If both dataframes has some different columns, then based on this value, it will be decided which columns will be in the merged dataframe.
# on : Column name on which merge will be done. If not provided then merged on indexes.
# left_on : Specific column names in left dataframe, on which merge will be done.
# right_on : Specific column names in right dataframe, on which merge will be done.
# left_index : bool (default False)
# If True will choose index from left dataframe as join key.
# right_index : bool (default False)
# If True will choose index from right dataframe as join key.
# suffixes : tuple of (str, str), default (‘_x’, ‘_y’)
# Suffix to be applied on overlapping columns in left & right dataframes respectively.


x['_merge'].value_counts()
# both          2
# right_only    1
# left_only     1
# Name: _merge, dtype: int64

# METHOD 4
df1 = pd.concat([df1.set_index('id'), df2.set_index('id')['Last']], axis=1, sort='id', join='inner')

# Speed Comparison
#.merge()  38 ns ± 0.369 ns per loop
#.concat() 38.5 ns ± 0.379 ns per loop
#.join()   39.2 ns ± 0.709 ns per loop
#.map()    2.3 ms ± 131 µs per loop


# Use .merge() function to do a 'diff' on two dataframes
def dataframe_difference(df1, df2):
    """Find rows which are different between two DataFrames."""
    comparison_df = df1.merge(df2, indicator=True, how='outer')
    diff_df = comparison_df[comparison_df['_merge'] != 'both']
    diff_df.to_csv('diff.csv')
    return diff_df


df1 = pd.DataFrame(data={'A':[10,11,12],'B':[12,13,14],'C':[15,16,17]})
df2 = pd.DataFrame(data={'A':[10,11,12],'B':[12,99,14],'C':[15,16,17]})


pd.concat([df1, df2]) # default is axis=0
#
#     A   B   C
# 0  10  12  15
# 1  11  13  16
# 2  12  14  17
# 0  10  12  15
# 1  11  99  16
# 2  12  14  17

pd.concat([df1,df2], axis=1)
#     A   B   C   A   B   C
# 0  10  12  15  10  12  15
# 1  11  13  16  11  99  16
# 2  12  14  17  12  14  17



# also this is useful to indicate which columns have differences...
(df1 != df2).any()
# A    True
# B    True
# C    True
# dtype: bool

(df1 == df2).all()
# A     True
# B    False
# C     True

# ======================================================================================================================
# Pandas Melt Function
# ======================================================================================================================
df = pd.DataFrame({'A': [1,2,3,4],
                    'B': [5,6,7,8]})

#    A  B
# 0  1  5
# 1  2  6
# 2  3  7
# 3  4  8

pd.melt(df)
#   variable  value
# 0        A      1
# 1        A      2
# 2        A      3
# 3        A      4
# 4        B      5
# 5        B      6
# 6        B      7
# 7        B      8

# ======================================================================================================================
# DateFrame Function rows (axis = 1),  columns (axis = 0).
# ======================================================================================================================
# df.axes	      Returns a list with the row axis labels and column axis labels as the only members.
# df.T	          Transposes rows and columns.
# df.transpose()  Transposes rows and columns. (same as above)
# df.dtypes	      Returns the dtypes in this object for each column
# df.empty	      True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.
# df.ndim	      Number of axes / array dimensions.
# df.shape	      Returns a tuple representing the dimensionality of the DataFrame (rows,columns).
# df.size	      Number of elements in the NDFrame.
# df.values	      Numpy representation of NDFrame.
# df.index        Returns the index/row names as a pandas index type
# df.columns      Returns list of columns as a pandas index
# df.head(n)	  Returns the first n rows.
# df.tail(n)	  Returns last n rows.
# df.iloc[n1:n2]  Returns range of rows
# df.to_string()  Returns a string representation of the dataframe
# df.drop_duplicates()  Drops Duplicate Rows and returns unique set
# df.drop_duplicates(['COL_E', COL_F'])  can specify column set to search for uniqueness
# df.nunique(axis=1)    Count number of distinct elements in specified axis
# df.value_counts()     Gives tally for repeated full row content
# df.dropna()           Drops all the rows that include a missing value
# df.fillna(value)      Fills all null values with give value
# df.reindex(columns=['COLB','COLA','COLC'])  Will rearrange the column order
# df.info()             Returns each column info
# df.describe()         Gives statistics for numeric columns
# df.isnull().sum()     Returns series representing null tally for each column
# df.isna().sum()       Same as above
# df.copy()             Returns copy of dataframe
# df.reset_index()      Resets index, needed when the index gets shuffled due to merging or sorting
# df.apply()            Use to apply a function along the row or column. axis = 0 for column and axis=1 for row, 
# df.applymap()         Use for element-wise operation across the whole DataFrame
# df.astype()           Coerces columns to given data type,  Parameters copy=True returns copy, copy=False, modifies in-place, Specifies whether to return a copy (True), errors='raise' or 'ignore'
# df.shift()            Will shift the rows of a df relative to index, e.g df.shift(-3, fill_value=0) shifts up and fills with zeros
# df.query()            Query columns of df   query(expr: 'str', inplace: 'bool' = False, **kwargs)
# df.nsmallest()        Return the first `n` rows ordered by `columns` in ascending order
# df.nlargest()         Return the last `n` rows ordered by `columns` in descending
# df.memory_usage()     Returns memory (byts) used in RAM. Set parameter as deep=True. The memory footprint of object dtype columns is calculated too
# df.select_dtypes()    Returns dataframe of only the included datatypes columns, must use parameter e.g. include=['string', 'object'] or exclude=['int64']
# df.to_parquet()       Writes to parquet file which is in byte strings, stores data in columns much faster then csv and compressed
# df.sort_values()      by=['col2', 'col3], ascending=False, ignore_index=True (ignore_index will recreate a 'new' index 0,1,2), axis=0 (0 or ‘index’, 1 or ‘columns’), kind='quicksort' (‘quicksort’, ‘mergesort’, ‘heapsort’), inplace=True, na_position='last'

# ======================================================================================================================
df3.shape        # Returns(4, 5)
df3.size         # Returns 20
df3['col_2']      # Returns 2nd column as pandas data series
df3.col_2         # Returns the same as above (does not allow for spaces in column name)
df3.col_2.values  # Returns numpy array([2,6,10,200], dtype=int64)
df3.memory_usage(deep=True).sum()  # Returns full memory usage = 596 bytes, , with deep=True the memory footprint of object dtype columns is calculated too
df3.info(memory_usage='deep')      # displays memory ussage with considering  object/string type memory footprint

# ======================================================================================================================
# Statistics will be performed on all applicable rows/columns
# ======================================================================================================================
# df.count()	 Number of non-null observations - Column count of elements
# df.sum()	     Sum of values  - Column Sums or concatenates (use df.values.sum() to sum all elements of dataframe)
# df.mean()	     Mean of Values - Column Mean
# df.median()	 Median of Values - Column Median
# df.mode()	     Mode of values - Column Mode
# df.std()	     Standard Deviation of the Values
# df.min()	     Minimum Value
# df.max()	     Maximum Value
# df.abs()	     Absolute Value
# df.prod()	     Product of Values
# df.cumsum()	 Cumulative Sum
# df.cumprod()	 Cumulative Product


# SQL QUERY on Existing Data Frame
df = pd.DataFrame([[1234, 'Customer A', '123 Street', np.nan],
                   [1234, 'Customer A', np.nan, '333 Street'],
                   [1233, 'Customer B', '444 Street', '333 Street'],
                   [1233, 'Customer B', '444 Street', '666 Street']], columns=
                   ['ID', 'Customer', 'Billing Address', 'Shipping Address'])
q1 = """SELECT ID FROM df """
print(ps.sqldf(q1, locals()))


df = pd.DataFrame({'col1' : [5, 6, 3, 2, 4, 9], 'col2' : [2, 1, 9, 8, 7, 4], 'col3': [0, 1, 9, 4, 2, 3]})

# >>> df
#    col1  col2  col3
# 0     5     2     0
# 1     6     1     1
# 2     3     9     9
# 3     2     8     4
# 4     4     7     2
# 5     9     4     3

df.sort_values(by=[4], axis=1)  # SORT BY INDEX (ROWS), axis=1
#    col3  col1  col2
# 0     0     5     2
# 1     1     6     1
# 2     9     3     9
# 3     4     2     8
# 4     2     4     7
# 5     3     9     4

df.sort_values(by=[4], ascending=[False], axis=1) # Sort by row [4] DESC 7->4->2
#    col2  col1  col3
# 0     2     5     0
# 1     1     6     1
# 2     9     3     9
# 3     8     2     4
# 4     7     4     2
# 5     4     9     3


df.sort_values(by=['col2', 'col3'], ascending=[False, True], axis=0)  # SORT BY COLUMNS, axis=0 (default)
#    col1  col2  col3
# 2     3     9     9
# 3     2     8     4
# 4     4     7     2
# 5     9     4     3
# 0     5     2     0
# 1     6     1     1


# Sql query on a connection string to be collected as a dataframe
# create an sqlite database and connection
# conn = sql.connect(r'database_file')
# c = conn.cursor()
# df = pd.read_sql("select * from posts;", conn)
# pandas.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)

df = df6
# FILTER THE DATA USING '&', '|'
df[df['title'] == 'Macbeth']
df[df['title'] == 'Macbeth'].sort_index(ascending=False)  # lists rows high to low
# returns rows that satisfy conditions using '&', '|' for 'and', 'or'
df[(df['year'] >= '1990') & (df['year'] < '2000')]  # WARNING: BRACKETS () & () are required

#          title  year
# 4226   Macbeth  1913
# 9322   Macbeth  2006
# 11722  Macbeth  2013
# 17166  Macbeth  1997
# 25847  Macbeth  1998

df[df['title'] == 'Macbeth'].sort_values('year') # order by year ASC
df[df['title'] == 'Macbeth'].sort_values('year', ascending=False) # order by year DESC


# shows how many null values in all columns
# isnull() seems to be same as isna()
# notnull() seems to be same as notna()
df.isnull().sum()
# title    0
# year     1
#dtype: int64

df[df['year'].isnull()] # returns missing values, opposite to .notnull()
#             title year
# 0  The Rising Son  NaN
df = df.fillna('N/A') # fills all null vallues with string 'N/A'
# df['NUM_1'].fillna(df['NUM_2'])  this replaces the null values with data from another column

# ======================================================================
# Null types could be: np.nan, None, pd.NaT, pd.NA (from pandas 1.0)
# ======================================================================
pd.isna(df) # this is the same as df.isna()
pd.isna(np.nan)          # True
pd.isna(None)            # True
pd.isna(pd.NaT)          # True
pd.isna(pd.NA)           # True
pd.isna(float('nan'))    # True
pd.isna(Decimal('NaN'))  # True
pd.isna(0)               # False
pd.isna(float('inf'))    # False



#string operations
df[df['title'].str.startswith("Maa ")]
#                           title  year
#19              Maa Durga Shakti  1999
#3046               Maa Aur Mamta  1970
#7470           Maa Vaibhav Laxmi  1989
#7933   Maa Kande Aaji Puate Pain  2002
#17197              Maa al-Khatar  2016
#...                          ...   ...


df[df['title'].str.contains("fred")]
#                    title  year
# 1702            Sigfredo  1951
# 18347   Alfred the Great  1969

# count how many rows have that specific entry.   so 2363 movies have 'year' = 2016
df['year'].value_counts()
# 2016    2363
# 2017    2138
# 2015    1848
# 2014    1701
# 2013    1609
#        ... 


# ===========================================
# Pandas Logic
# ===========================================
# &  = AND
# |  = OR
# ~  = NOT
# ^  = XOR
# df.any()  = ANY
# df.all()  = ALL
# df.isnull() = is NaN
# df.notnull()  = is not NaN


# return only rows with null values
df = pd.DataFrame([range(3), [0, np.NaN, 0], [0, 0, np.NaN], range(3),  [pd.NA, 0, 0], [pd.NA, pd.NA, pd.NA]])
# 0     0     1     2
# 1     0   NaN     0
# 2     0     0   NaN
# 3     0     1     2
# 4  <NA>     0     0
# 5  <NA>  <NA>  <NA>



df[df.isnull().any(axis=1)]  # axis=1 OR axis='columns' for columns   (axis=0 fails)
#       0     1     2
# 1     0   NaN     0
# 2     0     0   NaN
# 4  <NA>     0     0
# 5  <NA>  <NA>  <NA>

df[df.isnull().all(axis=1)]
#       0     1     2
# 5  <NA>  <NA>  <NA>

#======================================
# Map df -> to dictionary
#======================================
# dict(zip(df['COL1'], df['COL2']))


# ======================================================================================================================
#  ITERATIONS / LOOPS  .items(), .itertuples(), .iterrows(), .iteritems()  or simply use df.iloc[i]
# ======================================================================================================================
# Iterate through Series as you would a dictionary
s =  pd.Series([0,3,6,9,12,15])
s.keys()  # returns the index range
s.items() # returns the zip of index and data
for k,v in s.items():
	print(k, ' -----> ', v)


# Iterate through dataframe by columns  METHOD1  df.items()
df = pd.DataFrame(data=[[1,2,3],[4,5,5],[1,5,2]], columns=['COLA','COLB','COLC'])
df.keys()   # returns index of columns
df.items()  # returns pair of column name and Series for each column data
for k, v in df.items():
        print(k)  # Column Name
        print(v)  # Data of row as a Series
# COLA
# 0    1
# 1    4
# 2    1
# COLB
# 0    2
# 1    5
# 2    5
# COLC
# 0    3
# 1    5
# 2    2

# Iterate through dataframe  METHOD2  df.itertuples()  - this generates named tuples  (see bezpy_81_collections.py)
for row in df.itertuples(index=True, name='Pandas'):  # index=True is default, provides Index value for each row.  name='Pandas' is default name for you tuple object for each row
        print(row)
#Pandas(Index=0, COLA=1, COLB=2, COLC=3)  Values accessed with  row.Index, row.COLA, row.COLB, row.COLC
#Pandas(Index=1, COLA=4, COLB=5, COLC=5)  row.count(5) -> returns 2 as 2 fives appear in the row
#Pandas(Index=2, COLA=1, COLB=5, COLC=2)  row.index(5) -> returns 2 as the 2nd element is first to contain a 5 (warning counts the index value as 0th element


# Iterate through dataframe METHOD3 df.iterrows()
# ROW ITERATION
df.iterrows()  # creates a generator 
for idx, row in df.iterrows():  # idx = row idx value of df, row = row as a pandas series
    print(idx, '--->',  row)


# Iterate through dataframe METHOD3 df.iteritems()
# COLUMN ITERATION
df.iteritems()  # creates a generator
for col_name, col in df.iteritems():  # col_name, col = column as a pandas series
    print(col_name, '--->',  col)


# Generate a Random 500 x 700 df
df = pd.DataFrame(np.random.randn(500, 700))

# Generates 4000 random numbers in column 'a'
df = pd.DataFrame ({'a' :  np.random.randn(4000), 'b' :  np.random.randn(4000)})

# Speed Comparison
# Fastest itertuples()  ALWAYS USE THIS
sum = 0
start_time = time()
for row in df.itertuples(index=False):  # RETURNS PANDAS 'NAMED TUPLE' - MUST USE NOTATION  row.Value NOT  row['Value']
    sum =+ row.a
end_time = time()
print("itertuples() - Time Taken=", end_time - start_time, 'seconds', 'sum=', sum)

# Regular iteration with iat[] (faster than iloc)
sum = 0
start_time = time()
for i in range(len(df)):
    sum =+ df['a'].iat[i]
end_time = time()
print("regular loop iat[] - Time Taken=", end_time - start_time, 'seconds', 'sum=', sum)

# Regular iteration with iloc[] (slower than iat)
sum = 0
start_time = time()
for i in range(len(df)):
    sum =+ df['a'].iloc[i]
end_time = time()
print("regular loop iloc[] - Time Taken=", end_time - start_time, 'seconds', 'sum=', sum)


# Slowest iterrows()
sum = 0
start_time = time()
for idx, row in df.iterrows():
    sum =+ row['a']
end_time = time()
print("iterrows() - Time Taken=", end_time - start_time, 'seconds', 'sum=', sum)


# itertuples() - Time Taken= 0.015656232833862305 seconds sum= 0.40776144911584106
# regular loop iat[] - Time Taken= 0.07813668251037598 seconds sum= 0.40776144911584106
# regular loop iloc[] - Time Taken= 0.1405632495880127 seconds sum= 0.40776144911584106
# iterrows() - Time Taken= 0.5117020606994629 seconds sum= 0.40776144911584106


# apply() operation  differs from map() in that map works on a series or column and apply on a df (multiple columns)
#
# ##########RESEARCH  apply() vs tranform() ##################   #Todo
def row_function(x):
    return x['a'] * x['b']
df['Value'] = df.apply(row_function, axis=1)                 # generates another column without iterating
df['Value2'] = df['a'] * df['b']                             # same as above
df['Value3'] = df.apply(lambda x: x['a'] * x['b'], axis=1)   # same as above

df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], columns=['Col1', 'Col2', 'Col3'])
df.apply(lambda x: x+1)   # adds 1 to both rows and columns
#    Col1  Col2  Col3
# 0     2     3     4
# 1     5     6     7
# 2     8     9    10

df.applymap(lambda x: x+1)  # same result as above, should outperform .apply()




# map is defined on Series ONLY
# map accepts dicts, Series, or callable
# map is elementwise for Series
# map is meant for mapping values from one domain to another, so is optimised for performance (e.g., df['A'].map({1:'a', 2:'b', 3:'c'}))

# applymap is defined on DataFrames ONLY
# applymap and 'apply' accept callables only
# applymap is elementwise for DataFrames
# applymap is good for elementwise transformations across multiple rows/columns (e.g., df[['A', 'B', 'C']].applymap(str.strip))

# apply is defined on BOTH Series & DataFrame
# apply also works elementwise but is suited to more complex operations and aggregation. The behaviour and return value depends on the function.
# apply is for applying any function that cannot be vectorised (e.g., df['sentences'].apply(nltk.sent_tokenize)).


# Also see Vectorization for pandas series, and Vectorization for numpy arrays to improve iterization fees


# ======================================================================================================================
#  Adjust DataFrame display
# ======================================================================================================================
pd.set_option('display.max_rows', 10)               # 5 from head, 5 from tail
pd.get_option('display.max_rows')                   # Returns value that was set above
pd.options.display.max_rows                         # Same as above
pd.options.display.precision                        # allows you to change the precision for printing the numerical data

pd.set_option('display.max_columns', 20)            # Max number of columns displayed, note number of columns = df.shape[1]
pd.set_option('display.width', 1000)                # Max chars display on one line
pd.set_option('display.max_info_columns', 105)      # Sets max columns shown in df.info
pd.set_option('max_colwidth', 500)                  # Max chars within one column
pd.set_option('display.precision', 9)               # sig. figs. displayed for floats
pd.set_option('display.float_format', '{:0.3f}'.format)

pd.options.display.float_format = '{:,.2f}'.format  # Adjust format that floats are displayed
pd.reset_option('display.float_format')             # Resets format adjustment to default

# print full df ...
#with pd.option_context('display.max_rows', None, 'display.max_columns', None,'display.max_colwidth', -1): print(df)

# ======================================================================================================================
#  disp(df): changes display settings just for this print context
# ======================================================================================================================
def disp(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', df.shape[1]):
        print(df)

# ======================================================================================================================
#  tab(df): displays tabulated
# ======================================================================================================================
from tabulate import tabulate
# Can remanme the columns using headers=['COL1', 'COL2', ... ]
# tablefmt='psql' looks nice
def tab(df):
    print(tabulate(df, headers='keys', tablefmt='rst', maxcolwidths=[None, None, 20, None, None]))

print(df.to_markdown())   # introduced in pandas 1.0 with simmilar effect to tabulate, requires tabulate installed



# Import a 100 rows starting from row 100001  TAB SEPERATED FILE DATA
# imdb1 = pd.read_csv('myfiles\\title.imdb.tsv', sep='\t', index_col=None, skiprows=100000, nrows=100, low_memory=False)
# imdb2 = pd.read_csv('myfiles\\name.imdb.tsv', sep='\t', index_col=None, skiprows=100000, nrows=100, low_memory=False)

# n.fillna('N/A',inplace=True)
# m.fillna('N/A',inplace=True)

#titles = n[n['primaryName'] == 'Tom Hanks']['knownForTitles'].iloc[0].split(',')
#m[m['tconst'].isin(titles)]   # This functions returns all records where tconst is a list or series



# ======================================================================================================================
#  Full excel sheet read into dataframe, can define where to start reading and which tab. Read all columns as object
# ======================================================================================================================
df = pd.read_excel(r'myfiles\data.xlsx',sheet_name='Sheet1', skiprows=0, usecols='A:C', dtype=object)
#     COL1  COL2  COL3
# 0     1     2     3
# 1     4     5     6
# 2     7     8     9
df['COL2'].max()     # returns 8.0, max for column
df['COL1'].median()  # returns 4.0, median value
df['COL2'][2]        # returns 8.0


# ======================================================================================================================
#  WRITES DF to Excel
# ======================================================================================================================
# this suppresses the df index column and freezes the top-row

# to_excel: For a single sheet
df.to_excel(excel_writer='.\\myfiles\\myfile.xlsx', sheet_name='Sheet1', index=False, freeze_panes=(1,0)) # for ONE sheet only

# to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True,
#          index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True,
#          encoding=None, inf_rep='inf', verbose=True, freeze_panes=None)

# startrow       : int, default 0, Upper left cell row to dump data frame.
# startcol       : int, default 0, Upper left cell column to dump data frame.
# freeze_panes   : tuple of int (length 2), optional, Specifies the one-based bottommost row and rightmost column that is to be frozen
# na_rep=''      : how to represent null values in the dataframe
# inf_rep='inf'  : how to represent infinity in the dataframe


# ExcelWriter: For multiple sheets or to modify sheet using library openpyxl or xlsxwriter  see bezpy_44_openpyxl.py
writer = pd.ExcelWriter('.\\myfiles\\PythonExport2.xlsx', engine='openpyxl')
df.to_excel(excel_writer=writer, sheet_name='Sheet5', index=False) # name sheet and suppress the index column being printed
wb = writer.book  # access the workbook
# writer.save()   # Decommissioned.  use writer.close()
writer.close()  # synonym for save, to make it more file-like (Update 10/7/2022, was having issues moving file without performing .close() operation)

# For multiple sheets ...
# with pd.ExcelWriter('output.xlsx') as writer:
#    df1.to_excel(writer, sheet_name='Sheet_name_1')
#    df2.to_excel(writer, sheet_name='Sheet_name_2')

# Append to an existing Excel file ...
# with pd.ExcelWriter('output.xlsx', mode='a') as writer:
#     df.to_excel(writer, sheet_name='Sheet_name_3')

# ======================================================================================================================
#  WRITES DF to HTML  
# ======================================================================================================================
df.to_html('output.html', border=4, justify='left', bold_rows=True, index=False)
# optional parameters:
        #header determines whether to save the column names.
        #index determines whether to save the row labels.
        #classes assigns cascading style sheet (CSS) classes.
        #render_links specifies whether to convert URLs to HTML links.
        #table_id assigns the CSS id to the table tag.
        #escape decides whether to convert the characters <, >, and & to HTML-safe strings.

# reads data and tries to parse column ['DATE_COL'] as a 'date' field
# df = pd.read_html('data.html', index_col=0, parse_dates=['DATE_COL'])
# READ THIS ...  https://pbpython.com/pandas-html-table.html  READING HTML DATA IN PYTHON



# ======================================================================================================================
#  WRITES DF TO CSV  with no index column or header row - warning: datetime field doesn't appear pretty in xl
# ======================================================================================================================

df.to_csv('.\\myfiles\\PythonExport.csv', sep=',' , index=False, header=True, float_format='%.3f', line_terminator='\n')

# In Pandas 1.4, released in January 2022, you can use the pyarrow engine (requires pip install)
# To speeden up loading csv file to the dataframe
# df.to_csv('.\\myfiles\\PythonExport.csv', sep=',' , index=False, header=True, engine="pyarrow")

# Note you can write file compressed to save space
df.to_csv('.\\myfiles\\PythonExport_compressed.gz', sep=',', index=False, header=True, float_format='%.3f', compression='gzip', line_terminator='\n')
# and read that file as normal with  df = pd.read_csv('.\\myfiles\\PythonExport_compressed.gz')
# values for compression = 'infer', 'gzip', 'bz2', 'zip', 'xz', None
# types of Compression are '.gz' '.bz2'  '.zip'  '.xz'




#Trying to style the Spreadsheet...  TRIED NEW VERSION 2.0.5  on 2/5/2020
#styleframe not working with pandas 1.0.0
# from StyleFrame import StyleFrame
# df = pd.DataFrame({'aaaaaaaaaaa': [1, 2, 3], 'bbbbbbbbb': [1, 1, 1], 'ccccccccccc': [2, 3, 4]})
# ew = StyleFrame.ExcelWriter(r'example.xlsx')
# sf = StyleFrame(df)
# sf.to_excel(excel_writer=ew, freeze_panes=(1,1), best_fit=['aaaaaaaaaaa', 'bbbbbbbbb'])
# sf.set_column_width(columns=['aaaaaaaaaaa', 'bbbbbbbbb'], width=305.3)
# sf.apply_style_by_indexes(indexes_to_style=sf[sf['aaaaaaaaaaa'] > 2],
#                           cols_to_style=['aaaaaaaaaaa'],
#                           styler_obj=Styler(bg_color=utils.colors.blue, bold=True, font_size=10))
# sf.apply_column_style(cols_to_style=['aaaaaaaaaaa'], styler_obj=Styler(bg_color=utils.colors.green),
#                       style_header=True)
# ew.save()

# ======================================================================================================================
#  WRITES DF TO PICKLE FORMAT (can serialize/flatten ANY object in python by pickling into byte form with pickle.dumps(any_object)
# ======================================================================================================================
df.to_pickle('data-index.pkl')
pd.read_pickle('data-index.pkl')    # converts back


# ======================================================================================================================
#  READ PICKLE (bytes) FORMAT TO DATAFRAME (un-pickle the data) see bezpy_pickle.py
# ======================================================================================================================
import pickle
with open('data-index.pkl', 'rb') as f:
	df = pickle.load(f)
# Pickle is faster than CSV, which is faster than Excel

# ======================================================================================================================
#  WRITES TO JSON - to_json(file_path=None, orient='records')  default orientation is 'columns',
#  allowed values = {'split', 'records', 'index', 'columns', 'values', 'table'}.
# ======================================================================================================================
df.to_json(orient='table')    # '{"schema":{"fields":[{"name":"index","type":"integer"},{"name":"COL1","type":"string"},{"name":"COL2","type":"string"},{"name":"COL3","type":"string"}],"primaryKey":["index"],"pandas_version":"0.20.0"},"data":[{"index":0,"COL1":1,"COL2":2,"COL3":3},{"index":1,"COL1":4,"COL2":5,"COL3":6},{"index":2,"COL1":7,"COL2":8,"COL3":9}]}'
df.to_json(orient='values')   # '[[1,2,3],[4,5,6],[7,8,9]]'
df.to_json(orient='index')    # '{"0":{"COL1":1,"COL2":2,"COL3":3},"1":{"COL1":4,"COL2":5,"COL3":6},"2":{"COL1":7,"COL2":8,"COL3":9}}'
df.to_json(orient='split')    # '{"columns":["COL1","COL2","COL3"],"index":[0,1,2],"data":[[1,2,3],[4,5,6],[7,8,9]]}'
df.to_json(orient='records')  # '[{"COL1":1,"COL2":2,"COL3":3},{"COL1":4,"COL2":5,"COL3":6},{"COL1":7,"COL2":8,"COL3":9}]'
df.to_json(orient='columns')  # '{"COL1":{"0":1,"1":4,"2":7},"COL2":{"0":2,"1":5,"2":8},"COL3":{"0":3,"1":6,"2":9}}'

#df.to_json('data-index.json', orient='index')  # this time provided save-to filename
#pd.read_json('data-index.json', orient='index', convert_dates=['DATE_COLUMN'])

# ======================================================================================================================
#  WRITES TO SQL see bezpy_13_SqlAlchemy.py
# ======================================================================================================================
##from sqlalchemy import create_engine
##engine = create_engine('sqlite:///data.db', echo=False)
##pd.read_sql('data.db', con=engine, index_col='ID')
##df.to_sql('data.db', con=engine, index_label='ID', if_exists='replace')
## if_exists='fail' raises a ValueError and is the default.
## if_exists='replace' drops the table and inserts new values.
## if_exists='append' inserts new values into the table.

# Convert the continuous height values into discrete buckets
df5 = pd.DataFrame([['Fred', 53.4],['James', 53.4],['Paul', 57.9],['Peter', 61.2],['Tom', 78.7]], columns=['Name', 'Height'])
df5["Height"] = pd.cut(df5['Height'],
                        bins=[0, 50, 60, 65, 70, 75, 100], 
                        labels=["Super Short","Short", "Average", "Above Average","Tall","Super Tall"])

# ======================================================================================================================
# Parquet format  see bezpy_140_parquet.py
# ======================================================================================================================




# ======================================================================================================================
#  TYPE CONVERSIONS
# ======================================================================================================================
pd.Series([pd.Timestamp(2019, 1, 1, 12, 30, 59)])     # dtype: datetime64[ns]
pd.Series([dt(2019, 1, 1, 12, 30, 59)])               # dtype: datetime64[ns]

# set Convert python datetime or string field to pandas Timestamp field
# pandas.Timestamp  = <class 'pandas._libs.tslibs.timestamps.Timestamp'>
ts = pd.to_datetime(dt.now(), errors='ignore')               # datetime -> pandas timestamp  Timestamp('2023-03-19 13:23:46.127556')
ts = pd.to_datetime('13th of November, 2020')                # String -> pandas timestamp    Timestamp('2020-11-13 00:00:00')
ts = pd.to_datetime('2019-01-24 17:58:27')                   # String -> pandas timestamp    Timestamp('2019-01-24 17:58:27')


ts.date()                  # pandas timestamp -> datetime.date
ts.to_pydatetime()         # pandas timestamp -> datetime.datetime
ts.to_datetime64()         # pandas timestamp -> numpy datetime64
ts.to_julian_date()        # pandas timestamp -> Julian date
ts.strftime('%m/%d/%Y')    # pandas timestamp -> formatted string (use strftime codes)

x = pd.Timestamp(2019, 1, 1)     # type is pandas timestamp
isinstance(x, pd.Timestamp)      # Returns True


# df['timestampcolumn'].map(lambda x: x.ctime()[:10])  # timestamp -> string  e.g 'Thu Feb 27'
# df['timestampcolumn'].map(lambda x: x.date())        # timestamp -> datetime.date field
# x['POSTING_AMT'] = x['POSTING_AMT'].map(lambda x: x if x > 0  else '')  use Ternary Operators

# ===========================================================================
# Note   datetime.datetime vs datetime.date
# ===========================================================================
x = pd.Series([date(2000,1,1)])                          # dtype: object
y = pd.Series([date(2000,1,1)], dtype='datetime64[ns]')  # dtype: datetime64[ns]  (pd.Timestamp)
z = pd.Series([dt(2000,1,1)])                            # dtype: datetime64[ns]  (pd.Timestamp)

# x.dt.to_pydatetime()  # Fails since datatype is object
y.dt.to_pydatetime()  # converts series to numpy array elements of type datetime.datetime
z.dt.to_pydatetime()  # converts series to numpy array elements of type datetime.datetime
# ===========================================================================
# Series.dt Methods, Compare with Series.str Methods but for datetime objects
# ===========================================================================
# Series.dt.to_period
# Series.dt.to_pydatetime
# Series.dt.tz_localize
# Series.dt.tz_convert
# Series.dt.normalize
# Series.dt.strftime
# Series.dt.round
# Series.dt.floor
# Series.dt.ceil
# Series.dt.month_name
# Series.dt.day_name
# ===========================================================================

pd.Timestamp.today()  # Timestamp('2022-02-22 00:24:10.725927')
pd.Timestamp.now()    # Timestamp('2022-02-22 00:24:18.849024')

# 3-ways to create a DatetimeIndex
date_from = "2019-01-01"
date_to = "2019-01-12"
index = pd.date_range(date_from, date_to, freq='D')
index = pd.to_datetime('2019-01-01') + pd.to_timedelta(np.arange(12), 'D')
index = pd.DatetimeIndex(['2020-11-01', '2020-12-01', '2021-01-01', '2021-02-01'])
data = pd.Series([0, 1, 2, 3], index=index)

# Period Index
index.to_period('D')  #  PeriodIndex(['2020-11-01', '2020-12-01', '2021-01-01', '2021-02-01'], dtype='period[D]')
pd.period_range('2020-11-10', periods=7, freq='M')  # PeriodIndex

# TimeDelta Index
pd.timedelta_range(0, periods=10, freq='H') # TimeDeltaIndex

# to_datetime : Convert argument to datetime
#        - If errors='raise', then invalid parsing will raise an exception.
#        - If errors='coerce', then invalid parsing will be set as NaT.
#        - If errors='ignore', then invalid parsing will return the input.

dft = pd.DataFrame([1,2,3], columns=['Entry'])
dft['Now1'] = pd.Timestamp.now()  # pandas TimeStamp
dft['Now2'] = dt.now()            # pandas TimeStamp also
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Entry   3 non-null      int64
#  1   Now1    3 non-null      datetime64[ns]
#  2   Now2    3 non-null      datetime64[ns]



# to_timedelta : Convert argument to timedelta

df = pd.DataFrame([['Dave', '2000-1-1', '35'], ['Alex', '2000-1-2', '45'], ['Fred', '2000-1-3', '66']], columns=['Name', 'Date', 'Age'])

# to_numeric : Convert argument to a numeric type
# Convert string -> numeric (int64 or float64)  whichever is more fitting
df['Age1'] = pd.to_numeric(df['Age'], errors='ignore')  # FOR SERIES USE pd.to_numeric(series)  converts to int64

df['Date4'] = df['Date'].astype("datetime64[ns]")             # object -> pandas Timestamp
df['Age2'] = df['Age'].astype('float64', errors='ignore')    # string -> float64 errors : {'raise', 'ignore'}, default 'raise'
df['Age3'] = df['Age'].astype(np.float64, errors='ignore')   # same as the above
df['Age4'] = df['Age'].astype('int64', errors='ignore')      # Convert string -> int64
df['Age5'] = df['Age4'].map(lambda x:str(x))                 # int64 -> string (object)
df['Age6'] = df['Age4'].apply(lambda x: True if x == 5 else False)  # True for Age = 5 Years old else False
df['Name1'] = df['Name'].astype('string', errors='raise')  # New for Pandas 1.0 converts object to string !!!!doesn't do int->string!!!

x = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
x.astype('int32')  # formats all columns at once
x = x.astype({'col1': 'float64', 'col2': 'int32'})  # Formats two columns differntly
x.astype('int8', copy=False).info()  # copy=False should modify dataframe in-place **************** but doesn's seem to be working see https://github.com/pandas-dev/pandas/issues/18837
x.dtypes  # shows datatypes for each column
# col1    float64
# col2      int32
# dtype: object

# convert the string column of dates to pandas timestamp
df['Date1'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='ignore') # Using Pandas Library
df['Date1'].dt.year  # Filters only the year for each date
df[df['Date1'].dt.month==11] # filter November months only
df['Date2'] = df['Date'].map(lambda x: dt.strptime(x, '%Y-%m-%d'))  # Using the datetime library

# Warning if a data row is converted to a Series. the TimeStamp field becomes a np.datetime64 and can be converted back
pd.Timestamp(np.datetime64('2020-10-07T00:00:00.000000000'))

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/mtcars.csv')
df = df.convert_dtypes()    # converts dtypes 'object' to 'string'  # deprecated since pandas 0.17
df.select_dtypes('string')  # Returns only columuns of type 'string'

# Manipulate only the columns which are of type 'string'
_cols = list(df.select_dtypes(include=['string']).columns)
df[_cols] = df[_cols].replace({np.nan: None})

# for a general conversion function also see infer_objects()

# ======================================================================================================================
#  AGGREGATING DATA WITH GROUPBY
# ======================================================================================================================
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky', 'Bill', 'Fred'],'Country':['Eng','Fra','Fra','Ger','Eng','Ger'], 'Score':[3,2,2,5,7,9]}
df7 = pd.DataFrame(data)

#    Name Country  Score
#0    Tom     Eng      3
#1   Jack     Fra      2
#2  Steve     Fra      2
#3  Ricky     Ger      5
#4   Bill     Eng      7
#5   Fred     Ger      9



group = df7.groupby('Country')['Score'].sum()   # returns a series
#Country
#Eng    10
#Fra     4
#Ger    14
#Name: Score, dtype: int64


# Number of Unique Entries
df7.groupby('Country').nunique()
#          Name  Score
# Country
# Eng         2      2
# Fra         2      1
# Ger         2      2


#List Distinct Countries
list(df7.groupby('Country').nunique().index)
list(df7['Country'].drop_duplicates())           # BETTER ALTERNATIVE

# Calculate Unique / distinct Names for every Country
group = df7.groupby('Country')['Name'].nunique()
# Country
# Eng    2
# Fra    2
# Ger    2
# Name: Name, dtype: int64

# Calculate Unique / distinct Scores for every Country
group = df7.groupby('Country')['Score'].nunique()
# Country
# Eng    2
# Fra    1
# Ger    2
# Name: Name, dtype: int64



# multiple aggregates collected  for 'Score'  returns dataframe
group = df7.groupby('Country')['Score'].agg(['sum', 'count', 'nunique', 'mean', 'median', 'min', 'idxmin', 'max', 'idxmax', 'std', 'prod'])
#          sum  count  nunique  mean  median  min  idxmin  max  idxmax       std  prod
# Country                                                                             
# Eng       10      2        2     5       5    3       0    7       4  2.828427    21
# Fra        4      2        1     2       2    2       1    2       1  0.000000     4
# Ger       14      2        2     7       7    5       3    9       5  2.828427    45


max_idx = df7.groupby('Country')['Score'].idxmax() # series of original indices for which the country scored max
df7[df7.index.isin(max_idx)] # Subset of original dataframe for only max scoring entries
#    Name Country  Score
# 1  Jack     Fra      2
# 4  Bill     Eng      7
# 5  Fred     Ger      9



# for web.DataReader examples see bezPy03_DateTime.py
df = pd.read_excel(r'myfiles\sales.xlsx',sheet_name='Data', skiprows=1, skipfooter=0, usecols = 'A:H')

df.groupby('Region')['Revenue'].sum()
# Region
# Midwest      10402.00
# Northeast     5349.00
# South        20533.25
# West         33998.75
# Name: Revenue, dtype: float64


df.groupby(['Region', 'Year'])['Revenue'].sum()
# Region     Year
# Midwest    2013.0     1642.00
#            2014.0     8760.00
# Northeast  2013.0     4470.00
#            2014.0      879.00
# South      2013.0     2469.50
#            2014.0    18063.75
# West       2013.0     7762.25
#            2014.0    26506.50
# Name: Revenue, dtype: float64


df.groupby(['Region', 'Year'])[['Quantity', 'Revenue']].sum()  # Returns sum of both columns Quantity and Revenue
#                   Quantity   Revenue
# Region    Year
# Midwest   2013.0     125.0   1642.00
#           2014.0     697.0   8760.00
# Northeast 2013.0      76.0   4470.00
#           2014.0      80.0    879.00
# South     2013.0     160.0   2469.50
#           2014.0     520.0  18063.75
# West      2013.0     593.0   7762.25
#           2014.0     980.0  26506.50


df.groupby(['Region', 'Year', 'Qtr'])['Revenue'].sum()
# Region     Year    Qtr
# Midwest    2013.0  Q1       200.00
#                    Q2       602.00
#                    Q3       787.50
#                    Q4        52.50
#            2014.0  Q2      1590.00
#                    Q3      2000.00
#                    Q4      5170.00
# Northeast  2013.0  Q2       400.00
#                    Q3       530.00
#                    Q4      3540.00
#            2014.0  Q1        35.00
#                    Q2       184.00
#                    Q3       660.00
# South      2013.0  Q2        70.00
#                    Q3      2399.50
#            2014.0  Q1       482.50
#                    Q2      1702.00
#                    Q3     15879.25
# West       2013.0  Q1      1520.00
#                    Q3      2200.75
#                    Q4      4041.50
#            2014.0  Q1     19262.50
#                    Q2      3292.00
#                    Q3      2212.00
#                    Q4      1740.00
# Name: Revenue, dtype: float64


# ======================================================================================================================
#  PIVOT TABLES
# ======================================================================================================================
# Try this https://link.medium.com/0LUxiwMFl5
# https://towardsdatascience.com/a-step-by-step-guide-to-pandas-pivot-tables-e0641d0c6c70

# SAME AS ABOVE GROUPBY  BUT WILL TALLY 'ALL'

pt = pd.pivot_table(df,index=['Region','Year','Qtr'], values=['Revenue'], aggfunc=[np.sum], fill_value=0, margins=True, dropna=True)

# print(pt.to_markdown())
# |                             |   ('sum', 'Revenue') |
# |:----------------------------|---------------------:|
# | ('Midwest', 2013.0, 'Q1')   |               200    |
# | ('Midwest', 2013.0, 'Q2')   |               602    |
# | ('Midwest', 2013.0, 'Q3')   |               787.5  |
# | ('Midwest', 2013.0, 'Q4')   |                52.5  |
# | ('Midwest', 2014.0, 'Q2')   |              1590    |
# | ('Midwest', 2014.0, 'Q3')   |              2000    |
# | ('Midwest', 2014.0, 'Q4')   |              5170    |
# | ('Northeast', 2013.0, 'Q2') |               400    |
# | ('Northeast', 2013.0, 'Q3') |               530    |
# | ('Northeast', 2013.0, 'Q4') |              3540    |
# | ('Northeast', 2014.0, 'Q1') |                35    |
# | ('Northeast', 2014.0, 'Q2') |               184    |
# | ('Northeast', 2014.0, 'Q3') |               660    |
# | ('South', 2013.0, 'Q2')     |                70    |
# | ('South', 2013.0, 'Q3')     |              2399.5  |
# | ('South', 2014.0, 'Q1')     |               482.5  |
# | ('South', 2014.0, 'Q2')     |              1702    |
# | ('South', 2014.0, 'Q3')     |             15879.2  |
# | ('West', 2013.0, 'Q1')      |              1250    |
# | ('West', 2013.0, 'Q3')      |              2200.75 |
# | ('West', 2013.0, 'Q4')      |              4041.5  |
# | ('West', 2014.0, 'Q1')      |             19262.5  |
# | ('West', 2014.0, 'Q2')      |              3292    |
# | ('West', 2014.0, 'Q3')      |              2212    |
# | ('West', 2014.0, 'Q4')      |              1740    |
# | ('All', '', '')             |             70283    |



pt = pd.pivot_table(df,index=['Region','Year'], columns=['Qtr'], values=['Revenue'], aggfunc=[np.sum], fill_value=0, margins=True, dropna=True)
# print(pt.to_markdown())
# |                       |   ('sum', 'Revenue', 'Q1') |   ('sum', 'Revenue', 'Q2') |   ('sum', 'Revenue', 'Q3') |   ('sum', 'Revenue', 'Q4') |   ('sum', 'Revenue', 'All') |
# |:----------------------|---------------------------:|---------------------------:|---------------------------:|---------------------------:|----------------------------:|
# | ('Midwest', 2013.0)   |                      200   |                        602 |                     787.5  |                       52.5 |                     1642    |
# | ('Midwest', 2014.0)   |                        0   |                       1590 |                    2000    |                     5170   |                     8760    |
# | ('Northeast', 2013.0) |                        0   |                        400 |                     530    |                     3540   |                     4470    |
# | ('Northeast', 2014.0) |                       35   |                        184 |                     660    |                        0   |                      879    |
# | ('South', 2013.0)     |                        0   |                         70 |                    2399.5  |                        0   |                     2469.5  |
# | ('South', 2014.0)     |                      482.5 |                       1702 |                   15879.2  |                        0   |                    18063.8  |
# | ('West', 2013.0)      |                     1250   |                          0 |                    2200.75 |                     4041.5 |                     7492.25 |
# | ('West', 2014.0)      |                    19262.5 |                       3292 |                    2212    |                     1740   |                    26506.5  |
# | ('All', '')           |                    21230   |                       7840 |                   26669    |                    14544   |                    70283    |


data = list(pt.to_records())  # Converts to nparray and then to list
# for more Pivot tables see 	http://pbpython.com/pandas-pivot-table-explained.html
# pt = pd.pivot_table(df,index=['Description'], columns=['Month','Year'], values=['AmountPaid'], aggfunc=[np.sum], fill_value=0, margins=True, dropna=True)

# Correlation Function
# df.corr(method='spearman', min_periods=1)

# Testing: note pandas._testing seems more complete
from pandas._testing import assert_frame_equal
df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df2 = pd.DataFrame({'a': [1, 2], 'b': [3.0, 4.0]})
assert_frame_equal(df1, df2, check_dtype=False)  # check_dtype=True is default, set True to ignore requirement of df1.dtypes == df2.dtypes
assert_frame_equal(df1, df2, check_frame_type=False)  # this will allow for different dataframes  e.g.  pandas.DataFrame vs MySchemaDataFrame
# assert_series_equal(s1, s2)
# assert_almost_equal(df1, df2)
