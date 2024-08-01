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

hashlib.algorithms_available   # {'whirlpool', 'sha3_224', 'sha256', 'sha512', 'sha3_384', 'sha1', 'blake2b', 'sha3_512', 'blake2s', 'sha224', 'sha512_256', 'md4', 'sha384', 'ripemd160', 'md5-sha1', 'sha512_224', 'sha3_256', 'md5', 'shake_256', 'mdc2', 'shake_128', 'sm3'}
hashlib.algorithms_guaranteed  # set of the hash algorithms names guaranteed supported by module on all platforms {'blake2b', 'blake2s', 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'sha512', 'shake_128', shake_256'}

# hash.digest_size= "The size of the resulting hash in bytes."
# hash.block_size = "The internal block size of the hash algorithm in bytes. Hashing is processed in chunks of this fixed block size

# One Byte can be represented as a ...
# 1) decimal: integer                            000 -> 255
# 2) binary: 8 bits (2^8=256),             b00000000 -> b11111111
# 3) hexadecimal: 2 hex-digits (16^2=256),       x00 -> xff

# One hex digit can be represented as
# 1) decimal: integer                    00    -> 15
# 2) binary: 4 bits (2^4=16),            b0000 -> b1111
# 3) hexadecimal: 1 hex-digit (16^1=16), x0    -> xf

1 byte = 8 bits = 2 hex-digits

# ======================================================================================================================
# MEHTOD 1 using update()
# ======================================================================================================================
h1 = hashlib.sha256()      # also  .md5(), .sha1(), .sha224(), .sha384(), .sha512()
h1.name                    # 'sha256'  This is the canonical name which can be passed as parameter to .new() see below
h1.update(b"Welcome")
h1.update(b" to hashlib")  # appends to the object and modifies the hash

# For a larger file, better to read in blocksize=65536 = 2 ** 16 bits
# while open('xxx.pdf', 'rb') as f:
#   h.update(f.read(blocksize))

h1.copy()       # Return a copy (“clone”) of the hash object.

h1.digest()      # Hash value as byte stream = b'#\x0e\xf8W\xb7v\xe1o\xdb\xd5=y\xa7~\xc7+\xfc\xd9Fl\x89\x15\xd7k\xf6\xd5\t\x8a\x02e\x16\x86'
h1.digest_size   # 32 bytes = 32 x 8 = 256 bits
assert h1.digest_size == len(h1.digest()) == 32  # bytes

# each byte can be represented as an integer
assert h1.digest()[0] == 35 and h1.digest()[31] == 134    # first and last bytes as an integer
assert [i for i in h1.digest()] == [35, 14, 248, 87, 183, 118, 225, 111, 219, 213, 61, 121, 167, 126, 199, 43, 252, 217, 70, 108, 137, 21, 215, 107, 246, 213, 9, 138, 2, 101, 22, 134]

# each byte can also be represented as a pair of hex digits
assert hex(h1.digest()[0]) == '0x23' and hex(h1.digest()[31]) == '0x86'  # first and last bytes as hex digit pair
assert [hex(i) for i in h1.digest()] == ['0x23', '0xe', '0xf8', '0x57', '0xb7', '0x76', '0xe1', '0x6f', '0xdb', '0xd5', '0x3d', '0x79', '0xa7', '0x7e', '0xc7', '0x2b', '0xfc', '0xd9', '0x46', '0x6c', '0x89', '0x15', '0xd7', '0x6b', '0xf6', '0xd5', '0x9', '0x8a', '0x2', '0x65', '0x16', '0x86']

h1.hexdigest()  # Hash value as 64 hex-digit string = '230ef857b776e16fdbd53d79a77ec72bfcd9466c8915d76bf6d5098a02651686'
                # each pair of hex digits represents a byte ...
                # 000 = b00000000 = x00
                # 255 = b11111111 = xff

assert len(h1.hexdigest()) == 64  # 64 hex-digits = 32 bytes = 32 x 8 = 256 bits


# ======================================================================================================================
# MEHTOD 2 "CONDENSED"
# ======================================================================================================================
h2 = hashlib.sha256(b"Welcome to hashlib")

# 32 bytes = 32x8 bits ... b'#\x0e\xf8W\xb7v\xe1o\xdb\xd5=y\xa7~\xc7+\xfc\xd9Fl\x89\x15\xd7k\xf6\xd5\t\x8a\x02e\x16\x86'
assert h2.digest_size == len(h2.digest()) == 32

# 64 hex digit string ... '230ef857b776e16fdbd53d79a77ec72bfcd9466c8915d76bf6d5098a02651686'
assert len(h2.hexdigest())== 64


# ======================================================================================================================
# MEHTOD 3 "Using new()"
# ======================================================================================================================
h3 = hashlib.new('sha256', b"Welcome to hashlib")
assert(h1.digest() == h2.digest() == h3.digest())  # All three hashes are the same
assert(h1.hexdigest() == h2.hexdigest() == h3.hexdigest())  # All three hashes are the same

# ======================================================================================================================
# md5 -
# ======================================================================================================================
h4 = hashlib.md5(b"Welcome to hashlib")

h4.digest()  # 16 bytes = b'\x1c\xd5\x01\xa2\x8d\x95\xcd\xb9\x17\xc1u\x00\x03&]\xf9'
assert len(h4.digest()) == h4.digest_size == 16

h4.hexdigest()  # '1cd501a28d95cdb917c1750003265df9'
assert len(h4.hexdigest()) == 32 # 32 hex digits representing the 16 bytes

# ======================================================================================================================
# blake2b - you can provide the digest_size, default is 64
# ======================================================================================================================
# digest_size = 4 bytes = 32 bits = represented by 8 hex digits
hashlib.blake2b(b"Welcome to hashlib", digest_size=4).hexdigest()   # '7b1d62cd'

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
# 128 bits = 16 bytes = 32 hex digits
# The term globally unique identifier (GUID) is also used
# https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)

from uuid import uuid4       # from standard library, Version 4 random UUID
string_uuid = str(uuid4())   # e.g. '77e5f2ab-d3a8-4582-8233-ea16d1cfe2ce'    <-----   32 hex digits = 16 bytes = 128 bits
hex_uuid = uuid4().hex       # e.g. '77e5f2abd3a845828233ea16d1cfe2ce'        <-----   32 hex digits = 16 bytes = 128 bits


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