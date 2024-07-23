# https://docs.python.org/3/library/random.html

# The pseudo-random generators of this module should not be used for security purposes.
# For security or cryptographic uses, see the secrets module.
# Use os.urandom() or SystemRandom or secrets module


from random import *   # From Standard Library (built-in module)

### UPON Start of the program a random staring seed is chosen

# ======================================================================================================================
# Discrete Random Selection
# ======================================================================================================================
ri = randint(0, 9)           # Return a random integer N such that 0 <= N <= 9.

rr = randrange(0, 10, 2)     # Returns int in range(0,10,2); 2 is optional 'step' argument.
                             # So randint(0,9) same as randrange(0,10)

grb = getrandbits(3)         # Returns int with binary value maximum of three bits
                             # binary i.e 0b000 = 0 to 0b111 = 7  in decimal. so getrandbits(3) is the same as randint(0,7)


# Combinations
ch = choice(['a', 'b', 'c'])   # Return a random element   e.g. 'c'
chs = choices([1, 2, 3, 4, 5], k=3, weights=None, cum_weights=None)  # Returns random sample of k objects from population as list with replacement e.g. [3, 2, 2]
# you can weight choices with weights or cum_weights (cumulative)  e.g.
# weights=[10, 5, 30, 5] are equivalent to the cumulative weights cum_weights=[10, 15, 45, 50]

import string
''.join(random.choices(string.ascii_lowercase, k=8))  # returns random 8 digit lowercase strin of ascii chars



# Permutations
x = [1, 2, 3]
shuffle(x)  # shuffles elements of mutable 'x', modifying 'x' itself inplace. e.g x = [1, 3, 2]  and returns None



sample((1, 2, 3, 4, 5), k=3) # Returns random sample of k objects from population as list without replacement e.g. [5, 2, 1]
sa1 = sample(('red', 'red', 'blue'), k=2)        # This returns 2 elements from the population of 2 as a sample without replacement
                                                 # Note the poplulation ('red', 'red', 'blue') can be list or tuple

# sa2 =  sample(('red', 'blue'), counts=[2, 1], k=2) # equivalent to above (Introduced in 3.9 'counts' was introduced). i.e. 2 x red, 1 x blue in the pot

# ascii_chars_string !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~
ascii_chars_string = ''.join([chr(i) for i in range(33, 127)])
password = ''.join(sample(ascii_chars_string, 8)) # Generates random 8-digit password

# ======================================================================================================================
# CONTINUOUS DISTRIBUTIONS
# ======================================================================================================================
ra = random()         # returns float in range 0.0 <= x < 1.0    Using the uniform Distribution with no arguments (15 dp ?)
uni = uniform(0, 9)   # returns float in range 0.0 <= x <= 9.0   Using the uniform Distribution
                      # equivalent to random() but with arguments

seed(8675309)  # This will reset the starting seed for the random generator
for _ in range(3):
    print(random())   # Will always display the same 3 values since the seed was fixed

tri = triangular(low=0.0, high=1.0, mode=0.7)  # returns float in range low <= x <= high with modal value of 0.7
                                         # Using the Triangular Distribution.
                                         # Note Mode=None sets mode=median and is symmetric

nv = normalvariate(0, 1)  # normalvariate(mu, sigma)   # Normal DistN
gs = gauss(0, 1)          # gauss(mu, sigma) # slightly faster than the normalvariate()


# outside of two standard deviations
for i in range (1, 101):
    gs = normalvariate(0, 1)
    if  gs >= 2 or gs <= -2:
        print (i, gs)


pause = True


# betavariate(alpha, beta) # Beta distribution. Conditions on the parameters are alpha > 0 and beta > 0.
                           #  Returned values range between 0 and 1.
# expovariate(lambd)       # Exponential distribution. lambd is 1.0 divided by the desired mean. It should be nonzero

# gammavariate(alpha, beta)  # THIS IS NOT the gamma distN
#           x ** (alpha - 1) * math.exp(-x / beta)
# pdf(x) =  --------------------------------------
#             math.gamma(alpha) * beta ** alpha

#lognormvariate(mu, sigma)  # Log normal distN


# ======================================================================================================================
# Random Methods: https://www.w3schools.com/python/module_random.asp
# ======================================================================================================================
# seed()	        # Initialize the random number generator
# getstate()	    # Returns the current internal state of the random number generator
# setstate()	    # Restores the internal state of the random number generator
# getrandbits()	    # Returns a number representing the random bits
# randrange()	    # Returns a random number between the given range
# randint()	        # Returns a random number between the given range
# choice()	        # Returns a random element from the given sequence
# choices()	        # Returns a list with a random selection from the given sequence (WITH replacment)
# shuffle()	        # Takes a sequence and returns the sequence in a random order
# sample()	        # Returns a list with a random selection from the given sequence (WITHOUT replacement)
# random()	        # Returns a random float number between 0 and 1
# uniform()	        # Returns a random float number between two given parameters
# triangular()	    # Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
# betavariate()	    # Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
# expovariate()	    # Returns a random float number based on the Exponential distribution (used in statistics)
# gammavariate()    # Returns a random float number based on the Gamma distribution (used in statistics)
# gauss()	        # Returns a random float number based on the Gaussian distribution (used in probability theories)
# lognormvariate()	# Returns a random float number based on a log-normal distribution (used in probability theories)
# normalvariate()	# Returns a random float number based on the normal distribution (used in probability theories)
# vonmisesvariate()	# Returns a random float number based on the von Mises distribution (used in directional statistics)
# paretovariate()	# Returns a random float number based on the Pareto distribution (used in probability theories)
# weibullvariate()	# Returns a random float number based on the Weibull distribution (used in statistics)
# ======================================================================================================================

import string  # from standard library, module provides a set of string-related functions

string.ascii_letters       # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_lowercase     # 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase     # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits              # '0123456789'
string.hexdigits           # '0123456789abcdefABCDEF'
string.octdigits           # '01234567'
string.printable           # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
string.punctuation         # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
string.whitespace          # ' \t\n\r\x0b\x0c'

# ======================================================================================================================
# Secrets module is an excellent secure source to produce random data, the issue with random is that the choice can
# be determined if you know the seed which limits the randomness
import secrets

secrets.choice(string.digits)  # returns a random digit e.g. '6'

x = ''   # Generate 8 digit random number
for _ in range(8):
    x += secrets.choice(string.digits)

# generate a truly random integer below the specified value
secrets.randbelow(exclusive_upper_bound=5)  # 4

# generate a truly random integer of 8 bits i.e  0-255
secrets.randbits(8)

secrets.token_urlsafe()  # 'vN4yQy-3T7YE6xzAzw3kZcPMZL1GZUmFpNmlXirAzZA'
secrets.token_hex()      # '28dbfdf2897adaa53a91db7808cf4db2be10b0acec95af019dbbaf06ef356e73'

# create a secure link to reset a password
'https://mywebsite.com/reset=' + secrets.token_urlsafe(7)  # 'https://mywebsite.com/reset=dvDeW0e9aA'

# string comparison that avoids a 'timing attack'
secrets.compare_digest('password123','password123') # True

# ======================================================================================================================