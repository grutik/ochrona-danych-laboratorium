import string
import sys
import hashlib
import time
import random

from Crypto.Cipher import AES

plik = sys.argv[1]
haslo = sys.argv[2]

sol = hashlib.sha224(str(time.time()) + str(random.random()) + 
'cfjnisdjnsevhdfhfgbcvjkdhvchvsdjfvdv').hexdigest()

for i in range(1000):
	haslo = hashlib.sha224(haslo + sol).hexdigest()

f = open(plik, 'r')
dane = f.read()

PADDING = ' '

# one-liner to sufficiently pad the text to be encrypted
BLOCK_SIZE = 32
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

cipher = AES.new(hashlib.sha256(haslo + sol).digest())
dane = cipher.encrypt(pad(dane))

#print sol + dane

#print cipher.decrypt(dane)
import sys
import string
import time
import math
from Crypto.Cipher import ARC4

def rc4wl(data, key):
    x = 0
    box = range(256)
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = 0
    y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))
    
    return ''.join(out)

def histogram(tekst):
        stat = {}
        for znak in tekst:
                if znak in stat:
                	stat[znak] += 1
                else:
                	stat[znak] = 1
        return stat



haslo = sys.argv[2]
dlugosc = len(haslo)
hist = histogram(haslo)
#print dlugosc
#print hist
#print plik

entropia = 0
#print hist
for klucz in hist:
	entropia += (float(hist[klucz]) / dlugosc) *  (math.log(float(hist[klucz]) / dlugosc, 2))
	#print hist[klucz] / dlugosc
	#print hist[klucz]

entropia = -entropia
entropia = entropia * dlugosc

if entropia < 80:
	print "Za mala entropia: " + str(entropia)
else:
	print sol + dane
