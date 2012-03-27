#!/usr/bin/python
import sys
import random
import math
import hashlib
from Crypto.Cipher import DES,AES
import time
des = DES.new("key12345")
des = DES.new("key12345",DES.MODE_CBC)
#encrypted = des.encrypt("secret12")
#print encrypted
aes = AES.new("1234567890123456",AES.MODE_CFB)
encrypted = aes.encrypt("test")
#print encrypted





haslo = sys.argv[1]
random.seed(time.time())
sol = ""
for s in range(8):
	sol += str(random.randint(0,9))
print "sol:"
print sol

print "pass:"
password = hashlib.sha224(haslo).hexdigest()
for i in range(1000):
	password = hashlib.sha224(password+str(sol)).hexdigest()
print password
