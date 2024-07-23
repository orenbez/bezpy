# ========================================================================
# https://pypi.org/project/cryptography/
# https://www.pythoninformer.com/python-libraries/cryptography/fernet/
# ========================================================================
from cryptography.fernet import Fernet

key = Fernet.generate_key()   # b'v6zj5rudntJq1cuKR2HJwILOLHIWo3iD09YV_e1-yNw=' Put this somewhere safe!
print('key:', key)
fkey = Fernet(key)  # to generate for first time.
fkey = Fernet(b'v6zj5rudntJq1cuKR2HJwILOLHIWo3iD09YV_e1-yNw=') # saved key from before

x = "A really secret message. Not for prying eyes."  # Message to encrypt

# Convert to bytes in one of the below ways
x_bytes = b"A really secret message. Not for prying eyes."
x_bytes = x.encode(encoding='utf-8', errors='strict')
x_bytes = x.encode('utf-8')


token = fkey.encrypt(x_bytes)
print('token:', token)

decoded_bytes = fkey.decrypt(token)
decoded_token = decoded_bytes.decode('utf-8')
print('decoded_token:', decoded_token)
