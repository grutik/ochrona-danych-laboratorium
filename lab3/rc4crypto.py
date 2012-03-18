#!/usr/bin/python
import sys
import time

plain = open(sys.argv[1])
#print plain
key = sys.argv[2]
#print key
inputFile = ""

for line in plain.readlines():
   for char in line:
      inputFile += char


t1 = time.time()
from Crypto.Cipher import ARC4
cipher = ARC4.new(key)
cryptogram  = cipher.encrypt(inputFile)
t2 = time.time()

#newStream =  rc4crypt(inputFile, key)
#cryptogram = xor(inputFile,newStream)

file = open(sys.argv[3], 'wb')
for item in cryptogram:
   file.write(''.join(item))	


diff = t2 - t1
print diff


