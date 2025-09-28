import random
import string

print('your password: ')

chars = string.ascii_letters + string.digits 

password = ''
for x in range(16):
    password += random.choice(chars)

print(password)