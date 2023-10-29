import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '@$#!?'

all = lower+upper+symbols
length = 6
password = "".join(random.sample(all,length))
print(password)
