# ======================================================================================================================
# hashlib: used for cryptographic hashes
# ======================================================================================================================
# Documentation here: https://docs.python.org/3.9/library/hashlib.html
# This module implements a common interface to numerous secure hash and message digest algorithms,  e.g.
# FIPS (Federal Information Processing Standard) secure hash algorithms SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512.
# RSA’s MD5 algorithm (invented by Ron Rivest, Adi Shamir, and Leonard Adleman)
# see bezpy_79 for an application

# https://en.wikipedia.org/wiki/Cryptographic_hash_function
# 1. it is easy to compute the hash value for any given message
# 2. it is infeasible to generate a message that has a given hash
# 3. it is infeasible to modify a message without changing the hash
# 4. it is infeasible to find two different messages with the same hash.

import datetime
import hashlib   # built-in library
hashlib.algorithms_available
# {'whirlpool', 'sha3_224', 'sha256', 'sha512', 'sha3_384', 'sha1', 'blake2b', 'sha3_512', 'blake2s', 'sha224', 'sha512_256', 'md4', 'sha384', 'ripemd160', 'md5-sha1', 'sha512_224', 'sha3_256', 'md5', 'shake_256', 'mdc2', 'shake_128', 'sm3'}

hashlib.algorithms_guaranteed  # set of the hash algorithms names guaranteed supported by module on all platforms
# = {'blake2b', 'blake2s', 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'sha512', 'shake_128', shake_256'}


# ======================================================================================================================
# MEHTOD 1 using update()
# ======================================================================================================================
h1 = hashlib.sha256()      # also  .md5(), .sha1(), .sha224(), .sha384(), .sha512()
h1.name                    # 'sha256'  This is the canonical name which can be passed as parameter to .new() see below
h1.update(b"Welcome")
h1.update(b" to hashlib")  # appends to the object and modifies the hash
# For a larger file, better to read in blocksize=65536 = 2 ** 16 bits
# f = open ('xxx.pdf', 'rb')
# h.update(f.read(blocksize))

h1.digest()      # Hash value as byte stream = b'#\x0e\xf8W\xb7v\xe1o\xdb\xd5=y\xa7~\xc7+\xfc\xd9Fl\x89\x15\xd7k\xf6\xd5\t\x8a\x02e\x16\x86'
h1.digest_size   # = 32 bytes = 32 x 8 = 256 bits
assert h1.digest_size == len(h1.digest()) == 32  # bytes

h1.hexdigest()  # Hash value in hex form as string = '230ef857b776e16fdbd53d79a77ec72bfcd9466c8915d76bf6d5098a02651686'
h1.block_size   # 64 hex digits = 64 x 16 = 256 bits


assert h1.block_size == len(h1.hexdigest()) == 64  # hex-digits 
assert hex(h1.digest()[0]) == '0x23'   # first hex digit pair
assert hex(h1.digest()[31]) == '0x86'  # last hex digit pair


h1.copy()       # Return a copy (“clone”) of the hash object.

# ======================================================================================================================
# MEHTOD 2 "CONDENSED"
# ======================================================================================================================
h2 = hashlib.sha256(b"Welcome to hashlib")

# ======================================================================================================================
# MEHTOD 3 "Using new()"
# ======================================================================================================================
h3 = hashlib.new('sha256', b"Welcome to hashlib")

assert(h1.hexdigest() == h2.hexdigest() == h3.hexdigest())  # All three hashes are the same



# for blake2b you can provide the digest_size, default is 64
hashlib.blake2b(b"Welcome to hashlib", digest_size=4).hexdigest()   # '7b1d62cd'  digest_size = 4 bytes = 32 bits = 8 hex digits



# ======================================================================================================================
# hmac: This module provides support for HMAC (Hash-based Message Authentication Code) operations.
# ======================================================================================================================
# hmac can be treated similar to the hashlib object
import hmac
key = 'secret key'.encode()
msg = 'secret message'.encode()
h = hmac.new(key, msg, hashlib.sha512)
h.hexdigest()   # 2e012fe02de8426be7b30e7e235344930222a1323a9766d8058bb0f0e9c36ab70743bf6cc367e1164ca498edb436d9735a227a25a48f3eab295a18461b082466


# ======================================================================================================================
# A universally unique identifier (UUID) is a 128-bit label used for information in computer systems.
# Microsoft uses similar term (GUID = globally unique identifier)
# ======================================================================================================================
# 1 hex digits = 4 bits  (0000 -> 1111 bin == 0 -> 15 dec == 0 -> a hex)
# =>  128 bits = 16 bytes = 128/4 i.e 32 hex digits
# The term globally unique identifier (GUID) is also used
# https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)
from uuid import uuid4       # from standard library, Version 4 random UUID
string_uuid = str(uuid4())   # e.g. '77e5f2ab-d3a8-4582-8233-ea16d1cfe2ce'    <-----   32 hex digits
hex_uuid = uuid4().hex       # e.g. '77e5f2abd3a845828233ea16d1cfe2ce'        <-----   32 hex digits

# ======================================================================================================================
# hash() is the built-in function which returns an integer hash representation of any hashable(=immutable) object
# ======================================================================================================================
# any hashable object contains a __hash__ method
# I'm not sure how to get consistent results on this hash, every instance of the console is returning a different hash.
# may be related to environment variable PYTHONHASHSEED
# hashlib is giving consistent results for the same hash algorithm.
# All hash-sets or hash-maps in programming have a capacity (max number of integers to represent your objects)
# Then you generate an integer to represent each object, then you pigeon hole them to your set of allowed integers
# forming a hash-map to  <integer> mod <capacity if necessary.  Then you need a way to handle hash-collisions
# ======================================================================================================================
hash('Oren Bez')            # 4982229956736758018
hash(b'Oren Bez')           # 4982229956736758018, gives same value as the regular string within the same console execution
hash(48465455)              # 48465455, hash of an interger is always an integer
hash(4982229956736758018)   # 370543938309370116, but not always the same integer, same as the original up to 14-digits it seems
hash(None)                  # -9223363241732970369, hash values can be negative
hash((1, 2, 3))             # 529344067295497451
# hash([1,2,3])  # TypeError: unhashable type: 'list'
hash(datetime.date(1974, 2, 20))  # 1066577963619558221
hash(3.14)  # 322818021289917443

# ======================================================================================================================
# xxhash encryption  https://pypi.org/project/xxhash/1.3.0/
# ======================================================================================================================
import xxhash
h = xxhash.xxh64()