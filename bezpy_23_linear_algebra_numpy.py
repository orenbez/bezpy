# Try this: https://medium.com/@yp7121/a-visual-intro-to-numpy-2903458d25ea?source=bookmarks---------4----------------------------
# Try this: https://medium.com/python-features/array-data-structures-in-python-6ae400a01122
# Try this: https://towardsdatascience.com/matrices-are-graphs-c9034f79cfd8
# Try this: https://towardsdatascience.com/the-ultimate-beginners-guide-to-numpy-f5a2f99aef54?source=bookmarks---------63----------------------------
# Try this: https://towardsdatascience.com/27-things-that-a-beginner-needs-to-know-about-numpy-edda217fb662?source=bookmarks---------52----------------------------
# Try this: https://towardsdatascience.com/5-smart-python-numpy-functions-dfd1072d2cb4?source=bookmarks---------0----------------------------
# Try this: https://towardsdatascience.com/all-the-eigen-stuff-they-never-thought-you-should-know-3d87ddfa5346


# REACHED HERE: https://www.w3schools.com/python/numpy_array_indexing.asp
# https://www.w3schools.com/python/numpy/default.asp

# Linear Transformations (Rotations, Scaling, Shearing)
# 1. Keeps parallel lines parallel
# 2. Maintains an equal distance between parallel lines that were equally spaced to begin with
# 3. Leaves the origin at the origin

# n-dimensional array 'ndarray'  replaces the 'matrix' class which is deprecated

# For Tensors use 'torch' library
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, datetime


# numpy datatypes
issubclass(np.int64, np.integer)  # True - np.integer is the abstract parent class for all numpy integer types
issubclass(np.int32, np.integer)  # True - np.integer is the abstract parent class for all numpy integer types
issubclass(np.float16, np.floating) # True - np.floating is the abstract parent class for all numpy floating types
issubclass(np.float_, np.floating) # True - np.floating is the abstract parent class for all numpy floating types


# based on python data types
np.int_    # == np.dtype(int) == np.int32
np.bool_
np.float_  # == np.dtype(float) == np.float64
np.str_    # == np.dtype(str)
np.dtype(date)
np.dtype(datetime)

np.NaN  # Not a Number  also np.nan & np.NAN are the same


isinstance(np.bool_(True), np.bool_)  # True

np.isnan(float('nan')) # True
np.isnan(np.nan) # True
#>>> numpy.isnan(None) # TypeError


# Numpy datatypes in addition to basic python types int, float, bool, str, complex
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )
# For i, u, f, S and U we can define size as well.  e.g 'i4' is a 4-byte integer
np.array([1, 2, 3, 4], dtype='i4')    # dtype('int4')

np.array([1, 2]).dtype                # dtype('int32')
np.array([1.1, 2.1]).dtype            # dtype('float64')
np.array(['one', 'two']).dtype        # dtype('<U3')


# conversion where possible
np.array([1.1, 2.1, 3.1]).astype('i')  # array([1, 2, 3], dtype=int32)
np.array([1, 0, 3]).astype(bool)       # array([ True, False,  True])


# Numpy datetime
date_array = np.array(['2020-11-13'], dtype='datetime64[D]')  # Don't require brackets [] for single entry
np.datetime64('2020-11-13')                    # numpy.datetime64('2020-11-13')
np.datetime64('2020-11-13 12:00')              # numpy.datetime64('2020-11-13T12:00')
np.datetime64('2020-11-13 12:00:30.50', 'ns')  # numpy.datetime64('2020-11-13T12:00:30.500000000')


# Code  Meaning
# Y	    Year
# M	    Month
# W	    Week
# D	    Day
# h	    Hour
# m	    Minute
# s	    Second
# ms	Millisecond
# us	Microsecond
# ns	Nanosecond
# ps	Picosecond
# fs	Femtosecond
# as	Attosecond

# Vectorized Operations: on NumPy allows the use of more optimal and pre-compiled functions and mathematical operations
date_array + np.arange(3) # array(['2020-11-13', '2020-11-14', '2020-11-15'], dtype='datetime64[D]')

def angle_between(v1, v2):
    dot_pr = v1.dot(v2) # dot product |v1||v2|cos(ϑ)
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
    return np.rad2deg(np.arccos(dot_pr / norms))

def unit_vector(v):
    return v / np.linalg.norm(v)

if __name__ == '__main__':
    np.__version__  # version in use
    np.isscalar(3)       # True
    np.isscalar(3.1)     # True
    np.isscalar([3,0])   # False - this is a vector
    np.isreal(3 + 2j)    # False
    np.iscomplex(3 + 2j) # False

    # Below are all of type <class 'numpy.ndarray'>
    zero_d = np.array(42)
    one_d = np.array([1, 2, 3, 4, 5])
    one_d.shape  # (5,)
    two_d = np.array([[1, 2, 3], [4, 5, 6]])
    two_d.shape  # (2, 3)

    three_d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
    three_d.ndim    # Returns 3 indicating the dimension
    three_d.shape   # (2, 2, 3)


    five_d = np.array([1, 2, 3, 4], ndmin=5)  # array([[[[[1, 2, 3, 4]]]]])
    five_d.shape  # (1, 1, 1, 1, 4)

    # np.ndarray.nbytes : Total bytes consumed by the elements of the array.


    # reshape returns a view of original array
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    newarr = arr.reshape(2, 3, 2)  # From 1-D to 3-D
    # array([[[1, 2],
    #         [3, 4],
    #         [5, 6]],
    #        [[7, 8],
    #         [9, 10],
    #         [11, 12]]])


    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    newarr = arr.reshape(4, 3)  # From 1-D to 2-D
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9],
    #        [10, 11, 12]])

    # looping over array
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    for x in arr:
        print(x)
    # [1 2 3]
    # [4 5 6]

    for x in arr:
        for y in x:
            print(y)
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6

    # #### REACHED https://www.w3schools.com/python/numpy/numpy_array_iterating.asp  6\6\22


    # arrays can be indexed & sliced with steps
    np.array([1, 2, 3, 4])[2]  # 3  (1-d array)
    np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])[1, 4]   # 10 (2-d array)
    np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])[1, -1]  # 10 (2-d array)
    np.array([1, 2, 3, 4, 5, 6, 7])[:4] # array([1, 2, 3, 4])
    np.array([1, 2, 3, 4, 5, 6, 7])[1:5:2]   # array([2, 4]

    # array copy & view
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy()
    y = arr.view()

    x.base  # returns none, as x does not have a base array, it is a copy
    y.base  # returns array([1, 2, 3, 4, 5]) as arr is its base

    x[4] = 2   # changes copy (x) 4th element only
    y[0] = 3   # changes view (y) and original array (arr)
    arr        # array([3, 2, 3, 4, 5])


    # Vector Addition
    v = np.array([3, 7])
    u = np.array([2, 2])
    print(v + u)
    print(np.add(v,u)) # same as above

    v.mean()
    v.sum()
   
    # Vector Scalar multiplication
    v = np.array([3, 7])
    print(2 * v)

    # Vector Dot Product   |v||u|cos(ϑ)
    v = np.array([3, 7])
    u = np.array([2, 2])
    print(v.dot(u))
    print(np.dot(v,u)) #same as above

    # Vector Cross Product.  Magnitude = |v||u|sin(ϑ)
    # (u2v3-v2u3)i - (u1v3-u3v1)j + (u1v2-u2v1)k = a × b
    # = Determinant
    #| i  j  k  |
    #| u1 u2 u3 |
    #| v1 v2 v3 |
    print(np.cross(v, u))

    # Vector Norm (length with pythagoras)
    v = np.array([3, 2, 7])
    print(np.linalg.norm(v))

    v.tolist() # converts to list

    # Unit Vector u/|u|
    u = np.array([3, 6, 4])
    print(unit_vector(u))

    # Angle Between Vectors using dot product
    v = np.array([1, 4, 5])
    u = np.array([2, 1, 5])
    print(angle_between(v, u))
    
    # Matrix Addition
    A = np.array([
        [3, 5],
        [1, 0]])
    A.shape # retruns matrix shape
    B = np.array([
        [2, -3],
        [1, 2]])
    print(A + B)

    # Scalar Multiplication
    A = np.array([
        [3, 5],
        [1, 0]])
    print(2 * A)

    # Matric Multiplication
    A = np.array([
        [3, 4],
        [1, 0]])
    B = np.array([
        [2, 2],
        [1, 2]])
    print(A.dot(B))
    print(np.matmul(A,B)) 

    # Matrix Transpose
    A = np.array([
        [3, 4],
        [1, 0]])
    print(A.T)
    print(A.transpose()) # Same as above

    # 3x3 Identity Matrix
    A = np.eye(3)
    print(A)

    # Determinant
    A = np.array([
        [3, 2],
        [1, 6]])
    print(np.linalg.det(A))

    # Matrix Inverse
    A = np.array([
        [4, 3],
        [5, 4]])
    print(np.linalg.inv(A))
    print(A.dot(np.linalg.inv(A)))  # Product gives identity matrix

    # Eigenvalues & Eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)


    # Diagonal Matrix
    v = np.array([2, 4, 3, 1])
    np.diag(v)
##    array([[2, 0, 0, 0],
##           [0, 4, 0, 0],
##           [0, 0, 3, 0],
##           [0, 0, 0, 1]])    

    # Orthogonal vectors (seperated by 90 degrees)

    x = [0,0,2,2]
    y = [0,0,2,-2]
    
    
    plt.quiver([x[0], y[0]],
               [x[1], y[1]],
               [x[2], y[2]],
               [x[3], y[3]],
               angles='xy', scale_units='xy', scale=1)

    plt.xlim(-2, 4)
    plt.ylim(-3, 3)
    plt.axvline(x=0, color='grey')
    plt.axhline(y=0, color='grey')

    plt.text(1, 1.5, r'$\vec{u}$', size=18)
    plt.text(1.5, -1, r'$\vec{v}$', size=18)

    plt.show()
    plt.close()

    v1 = np.array([2,2])
    v2 = np.array([2,-2])
    print(angle_between(v1,v2))  # = 90 degrees
    
    # Orthonormal Matrices(A transpose is the inverse matrix)
    A = np.array([[np.cos(50), -np.sin(50)], [np.sin(50), np.cos(50)]])

    B = A.T
    C = np.linalg.inv(A)

    np.array_equal(C,B)  # test if same shape, same elements values
    np.array_equiv(C,B)  # test if broadcastable shape, same elements values
    np.allclose(C,B)     # test if same shape, elements have close enough values

    score = np.array([70, 60, 50, 10, 90, 40, 80])
    name = np.array(['Ada', 'Ben', 'Charlie', 'Danny', 'Eden', 'Fanny', 'George'])

    max_score_idx, min_score_idx = np.argmax(score), np.argmin(score)  # 4, 3

    sorted_score = np.argsort(score) # an array of scores in ascending  [3, 5, 2, 1, 0, 6, 4]
    sorted_name = name[sorted_score] # an array of names in ascending order of their scores ['Danny', 'Fanny', 'Charlie', 'Ben', 'Ada', 'George', 'Eden']


    def f(x):
        return x**2 - 3*x 


    pi = np.pi
    xlist_1 = np.linspace(-30, 30, 200)      # Creates 200 points between limits  array([-30, ... ,30])
    xlist_2 = np.arange(-2*pi, 2*pi, 0.1)    # creates points at every 0.1 interval array([-6.28318531, ... ,6.28318531])  = 126 points

    ylist_1 = f(xlist_1)                     # creates output array for function 'f'
    ylist_2 = np.sin(xlist_2)                # creates output array for sin
    ylist_3 = np.cos(xlist_2)                # creates output array for cos
    ylist_4 = np.tan(xlist_2)                # creates output array for tan
    ylist_5 = np.exp(xlist_2)                # creates output array for the exponential function
    np.random.rand(100)                      # generates array of 100 random points between 0 & 1  array([0.46566083,..., 0.73152314])

# ======================================================================================================================
# Full Numpy Datatype List
# ======================================================================================================================
# Data type	Description
# bool_	Boolean (True or False) stored as a byte
# int_	Default integer type (same as C long; normally either int64 or int32)
# intc	Identical to C int (normally int32 or int64)
# intp	Integer used for indexing (same as C ssize_t; normally either int32 or int64)
# int8	Byte (-128 to 127)
# int16	Integer (-32768 to 32767)
# int32	Integer (-2147483648 to 2147483647)
# int64	Integer (-9223372036854775808 to 9223372036854775807)
# uint8	Unsigned integer (0 to 255)
# uint16	Unsigned integer (0 to 65535)
# uint32	Unsigned integer (0 to 4294967295)
# uint64	Unsigned integer (0 to 18446744073709551615)
# float_	Shorthand for float64.
# float16	Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
# float32	Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
# float64	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
# complex_	Shorthand for complex128.
# complex64	Complex number, represented by two 32-bit floats
# complex128	Complex number, represented by two 64-bit floats


np.min([4,1,5]) # returns min element = 1
np.max([4,1,5]) # returns max element = 5

# ===========================================================================================
# ufunc
# ===========================================================================================

np.minimum([4,1,5], [1,3,1])  # returns array([1, 1, 1]), function is used to find the element-wise minimum of array elements.
np.maximum([4,1,5], [1,3,1])  # returns array([4, 3, 5]), function is used to find the element-wise maximum of array elements.
np.multiply([1,2,3], [4,5,6]) # returns array([ 4, 10, 18]), function is used to find the element-wise product of array elements.