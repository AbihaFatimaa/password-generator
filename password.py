import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '@$#!?'

all = lower+upper+symbols
length = 6
password = "".join(random.sample(all,length))
print(password)
hashcode =password.encode('utf-8')
print(hashcode)
salt = bcrypt.gensalt()
print('Salt:', salt)
hashed_password = bcrypt.hashpw(hashcode, salt)
print(hashed_password)
