# zlib is from the standard library, which is based on GNU zip or gzip
# gzip is from the standard library, provides support for reading and writing gzip-compressed files.
# ziplib requires 'pip install'

# ======================================================================================================================
# zlib ...  to compress strings/objects  for files see bezpy_21_zip_files.py
# ======================================================================================================================
# adler32(string[, start]) -- Compute an Adler-32 checksum.
# compress(data[, level]) -- Compress data, with compression level 0-9 or -1.
# compressobj([level[, ...]]) -- Return a compressor object.
# crc32(string[, start]) -- Compute a CRC-32 checksum.
# decompress(string,[wbits],[bufsize]) -- Decompresses a compressed string.
# decompressobj([wbits[, zdict]]]) -- Return a decompressor object.


import zlib

h = b"Hello, it is me, you're friend Emmett! This is a sample string of text to be compressed"
print(len(h))
t = zlib.compress(h)
print(len(t))
z = zlib.decompress(t)
print(len(z))