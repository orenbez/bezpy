import secrets
import string
OTP = ''
digit = string.digits
for i in range(6):
    OTP +=str(''.join(secrets.choice(digit)))

print(OTP)