# https://w3schools.com/python/module_math.asp
# https://w3schools.com/python/module_cmath.asp

import numpy as np
from math import *
from cmath import exp as e_complex # Note: cmath standard library for complex number operations
from fractions import Fraction

#   acos(x)          Return the arc cosine (measured in radians) of x.
#   acosh(x)         Return the inverse hyperbolic cosine of x.
#   asin(x)          Return the arc sine (measured in radians) of x.
#   asinh(x)         Return the inverse hyperbolic sine of x.
#   atan(x)          Return the arc tangent (measured in radians) of x.
#   atan2(y, x)      Return the arc tangent (measured in radians) of y/x.
#   atanh(x)         Return the inverse hyperbolic tangent of x.
#   ceil(x)          Return the ceiling of x as an Integral (smallest integer >= x).
#   comb(n,k)        Return compinations of k items from n without replacement
#   copysign(x, y)   Return a float with the magnitude (absolute value) of x but the sign of y.
#                    On platforms that support signed zeros, copysign(1.0, -0.0)  returns -1.0.
#   cos(x)           Return the cosine of x (measured in radians).
#   cosh(x)          Return the hyperbolic cosine of x.
#   degrees(x)       Convert angle x from radians to degrees.
#   dist()           Return the Euclidean distance between two points e.g. p = [3, 3]  q = [6, 12]. As of python 3.8
#   erf(x)           Error function at x (Gauss Error Function)
#   erfc(x)          Complementary error function at x.
#   exp(x)           Return e raised to the power of x.
#   expm1(x)         Return exp(x)-1. - This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
#   fabs(x)          Return the absolute value of the float x.
#   factorial(x)     Rerurns x!  Raise a ValueError if x is negative or non-integral.
#   floor(x)         Return the floor of x as an Integral. This is the largest integer <= x. Note floor rounds down and int truncates  floor(-3.5) -> -4 int(-3.5) -> -3
#   fmod(x, y)       Return fmod(x, y), according to platform C. x % y may differ.
#   frexp(x)         Return the mantissa and exponent of x, as pair (m, e). m is a float and e is an int, such that x = m * 2**e
#                    If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
#   fsum(seq)        Return an accurate floating point sum of values in the iterable seq. Assumes IEEE-754 floating point arithmetic.
#   gamma(x)         Gamma function at x.
#   gcd(x, y)        greatest common divisor of x and y, since 3.9 you can have more than two parameters
#   hypot(x, y)      Return the Euclidean distance, sqrt(x*x + y*y).
#   isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)    Determine whether two floating point numbers are close in value.
#                    rel_tol = value	Optional. The relative tolerance. It is the maximum allowed difference between value a and b. Default value is 1e-09
#                    abs_tol = value	Optional. The minimum absolute tolerance. It is used to compare values near 0. The value must be at least 0
#   isfinite(x)      Return True if x is neither an infinity nor a NaN, and False otherwise.
#   isinf(x)         Return True if x is a positive or negative infinity, and False otherwise.
#   isnan(x)         Return True if x is a NaN (not a number), and False otherwise.
#   lcm(a,b,c)       New to 3.9  Returns the lowest common multiple
#   ldexp(x, i)      Return x * (2**i). This is essentially the inverse of frexp().
#   lgamma(x)        Natural logarithm of absolute value of Gamma function at x.
#   log(x, base)     Return the logarithm of x to the given base. If the base not specified, returns the natural logarithm (base=math.e) of x.
#   log10(x)         Return the base 10 logarithm of x.
#   log1p(x)         Return the natural logarithm of 1+x (base e). The result is computed in a way which is accurate for x near zero.
#   log2(x)          Return the base 2 logarithm of x.
#   modf(x)          Return the fractional and integer parts of x. Both results carry the sign of x and are floats.
#   nextafter(x,y)   Returns the next floating-point value after x towards y. As of python 3.9
#   perm(n, k)       Number of ways to permute k items from n without repetition. As of python 3.8
#   pow(x, y)        Return x**y (x to the power of y).
#   prod(iterable)   Returns product of numeric values in the container
#   radians(x)       Convert angle x from degrees to radians.
#   remainder(x, y)  Difference between x and the closest integer multiple of y. Return x - n*y where n*y is the closest integer multiple of y.
#                    In the case where x is exactly halfway between two multiples of y, the nearest even value of n is used. The result is always exact.
#   sin(x)           Return the sine of x (measured in radians).
#   sinh(x)          Return the hyperbolic sine of x.
#   sqrt(x)          Return the square root of x.
#   tan(x)           Return the tangent of x (measured in radians).
#   tanh(x)          Return the hyperbolic tangent of x.
#   trunc(x)         Truncates the Real x to the nearest Integral toward 0.
#   ulp(x)           Returns the value of the least significant bit of the float x. As of python 3.9

# Constants in the math library:  math.e, math.inf, math.nan, math.pi, math.tau
##    e = 2.718281828459045
##    inf = infinity
##    nan = not-a-number
##    pi = 3.141592653589793
##    tau = 6.283185307179586  = 2 * pi
    

# this is more limited than the built-in factorial(), 
# will not accept as high a value for 'n'
def recursive_factorial(n):
    if n==1:
        return 1
    else:
        return n * recursive_factorial(n-1)


acos(0)  # returns pi/2
acosh(1) # returns 0



# ======================================================================================================================
# Complex Number
# ======================================================================================================================
z1 = 1j   # interprets as a complex number, can not use j on its own
z2 = 2-1j
z2.conjugate() # returns 2+1j
(2 - 3j).real   # returns 2.0
(2 - 3j).imag   # returns -3.0

z = 1j * pi
e_complex(z) # returns -1


# ======================================================================================================================
# Int Operations
# ======================================================================================================================
# integer method 'bit_length'
x = 1023             # 10 bits represent 0-1023
bin(1023)            # '0b1111111111'
x.bit_length()       # returns 10
(1023).bit_length()  # returns 10,  requires brackets as  1023.bit_length() would not be understood
x.to_bytes(4, byteorder='little', signed=True)   # b'\xff\x03\x00\x00'   converted to bytes

# ======================================================================================================================
# Float Operations
# ======================================================================================================================
x = 2.5
x.as_integer_ratio()   # (5, 2)
x.is_integer()         # False
(1.0).is_integer()     # True
h = x.hex()            # '0x1.4000000000000p+1', Returns a hexadecimal representation of a floating-point number.
float.fromhex(h)       # 2.5,  Create a floating-point number from a hexadecimal string


# ======================================================================================================================
# Fractions
# ======================================================================================================================
Fraction(16, -10) # returns Fraction(-8, 5)
Fraction(2.25)  # returns (9,4)
Fraction(2.25).denominator  # returns 4
Fraction(1, 2) + Fraction(2, 8)  # returns Fraction(3, 4)

# ======================================================================================================================
# Decimal
# ======================================================================================================================
# https://docs.python.org/3/library/decimal.html
# Be aware of the 'floating point arithmetic' error which is caused by
# how a float is stored in binary  (IEEE Standard for Floating-Point Arithmetic)
# Use the fractions or decimal module (as strings '1.2' not 1.2)
# Decimal() is designed to solve the inaccuracy problem of float, stores number in base 10 not binary
# ======================================================================================================================
# Python provides the following rounding mechanisms when executing round function e.g  round(Decimal('3.1415'), 3):
# ROUND_UP	        round away from zero
# ROUND_DOWN	    round towards zero
# ROUND_CEILING	    round to ceiling (towards positive infinity)
# ROUND_FLOOR	    round to floor (towards negative infinity)
# ROUND_HALF_UP	    round to nearest, ties away from zero
# ROUND_HALF_DOWN	round to nearest, ties towards zero
# ROUND_HALF_EVEN	round to nearest, ties to even (least significant digit)
# ======================================================================================================================
from decimal import (Decimal, DecimalTuple, Context, FloatOperation, getcontext, DivisionByZero, setcontext, localcontext,
                     BasicContext, ExtendedContext, ROUND_HALF_DOWN, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_DOWN, ROUND_UP)

x = 1 / 3                             # type float  0.3333333333333333
y = Decimal('1.0') / Decimal('3.0')   # more precision with type Decimal('0.3333333333333333333333333333')

Decimal()                        # Empty constructor treated as zero, Decimal('0')
Decimal(10.1)                    # Decimal('10.0999999999999996447286321199499070644378662109375')
Decimal(float(10.1))             # Same as above, inaccurate to convert from float
Decimal(1.2) - Decimal(1.1)      # Returns Decimal('0.09999...') DO NOT USE, YOU MAY GET LUCKY WITH RESULT BUT NOT GUARANTEED
Decimal('10.1')                  # Decimal('10.1')  CORRECT USAGE

1.2 - 1.1                                 # Returns 0.09999999999999987
float(Fraction(12,10) - Fraction(11,10))  # Returns  0.1, solving rounding issue with Fractions
Decimal('1.2') - Decimal('1.1')           # Returns Decimal('0.1')  PROBLEM SOVLED with Decimal

# Another rounding error, related to inaccuracy of a floating-point number, is solved with Decimal()
# With decimals you can select the rounding mechanism

round(3.675, 2)               # Returns 3.67
round(Decimal('3.675'), 2)    # Returns Decimal('3.68')

ctx = getcontext()            # returns the current global context object
ctx                           # see defaults values    
                              # Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, 
                              #         capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])


# since 3.3 Context precision and rounding only come into play during arithmetic operations.
ctx.prec      # 28 precision 
ctx.rounding  # ROUND_HALF_EVEN
ctx.prec = 3  # reset precision, this will only affect arithmetic operations
x = Decimal('1.22222')  # stores to 5.d.p
y = Decimal('1.33333')  # stores to 5.d.p
x + y   # returns Decimal('2.56') only now is precision affected

ctx.rounding = ROUND_HALF_DOWN  # Reassign rounding mechanism
round(Decimal('1.55'), 1)  # Decimal('1.5')


# Set traps
ctx.traps[FloatOperation] = True  # add trap warning for constructing Decimal from float
# Decimal(3.14)  # Raises Error
ctx.traps[DivisionByZero] = True
# Decimal('3') / Decimal('0')  # Raises Error

# clears the traps
ctx.clear_traps()

ctx.clear_flags()   # Clear flags
Decimal('355') / Decimal('113')   # Decimal('3.14')  flags will be set by this operation since rounding was employed

# Not sure of better good way to retrieve the flags [Inexact, Rounded] to indicate rounding
repr(ctx) # 'Context(prec=3, rounding=ROUND_HALF_DOWN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[Inexact, Rounded], traps=[])'


# Set rounding mechanism within localcontext only, but first copies values of ctx to ctx2
with localcontext() as ctx2:
    ctx2.rounding = ROUND_HALF_UP
    round(Decimal('3.35'), 1)   # Decimal('3.4')  


ctx3 = Context(prec=4, rounding=ROUND_HALF_DOWN) # create a new context object
ctx3.create_decimal('1.2345')             # Returns Decimal('1.234')
ctx3.create_decimal_from_float(1.2345)    # Returns Decimal('1.234')
setcontext(ctx3)  # ONLY NOW, this command will set the global context to the new parameters


# the DecimalTuple
Decimal((0, (3, 1, 4), -2))            # format is (sign, (digit1,digit2, digit3,...), exponent) = Decimal('3.14')
dt = DecimalTuple(0, (3, 1, 4), -2)    # returns DecimalTuple(sign=0, digits=(3, 1, 4), exponent=-2)
dt = Decimal('3.14').as_tuple()        # returns DecimalTuple(sign=0, digits=(3, 1, 4), exponent=-2)
dt.sign      # returns 0
dt.digits    # returns (3, 1, 4)
dt.exponent  # returns -4

Decimal('NaN')               # Not-A-Number
Decimal('NaN').is_nan()      # True
isnan(Decimal('NaN'))        # True
Decimal('-Infinity')         # -ve infinity  
isinf(Decimal('-Infinity'))  # True

# some mathematical functions are also available to Decimal:
Decimal('2.0').sqrt()    # = √(2.0)  
Decimal('2.0').log10()   # = log10(2.0)
Decimal('2.0').ln()      # = ln(2.0)
Decimal('2.0').exp()     # = exp(2.0)

# quantize() method rounds a number to a fixed exponent
Decimal('7.325').quantize(Decimal('.01'), rounding=ROUND_DOWN)  # Decimal('7.32')
Decimal('7.325').quantize(Decimal('1.'), rounding=ROUND_UP)     # Decimal('8')


# set decimal places
d = Decimal('1.55')
str(d)            # returns '1.55'
format(d, '.3f')  # '1.550', this is the built-in function 'format', not to be confused with str.format
f'{d:.3f}'        # '1.550' 


def set_prec_scale(value, precision, scale):
    """Sets precision=signifiant figures, and scale=decimal places"""
    return Decimal(format(Context(prec=precision, rounding=ROUND_HALF_EVEN).create_decimal(value), f".{scale}f"))


# decimal module provides two ready to use standard contexts
BasicContext    #  Context(prec=9, rounding=ROUND_HALF_UP, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[Clamped, InvalidOperation, DivisionByZero, Overflow, Underflow])
ExtendedContext #  Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[])
setcontext(BasicContext)     # Set the built-in context as the global context
setcontext(ExtendedContext)  # Set the built-in context as the global context

# ======================================================================================================================
