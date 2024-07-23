from string import ascii_lowercase
from string import ascii_uppercase
from string import ascii_letters  # combination of above
from string import digits, hexdigits, octdigits
from string import punctuation, whitespace
from string import printable      # combination of all above


assert ascii_lowercase == 'abcdefghijklmnopqrstuvwxyz'
assert ascii_uppercase == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
assert ascii_letters == 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
assert digits == '0123456789'
assert hexdigits =='0123456789abcdefABCDEF'
assert octdigits == '01234567'
assert punctuation == '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
assert whitespace == ' \t\n\r\x0b\x0c'
assert printable == '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
