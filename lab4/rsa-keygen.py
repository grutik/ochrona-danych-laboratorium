#!/usr/bin/python
import sys
import random
import eratostenes
import math

def nwd(a,b):
	while a != b:
		if a > b:
			a = a - b
		else:
			b = b - a
	return a

def inverseModulo(b,n):
	u1 = 1
	u2 = 0
	u3 = b
	v1 = 0
	v2 = 1
	v3 = n
	while v3 != 0:
		q = u3 / v3
		t1 = u1 - q * v1
		t2 = u2 - q * v2
		t3 = u3 - q * v3
		u1 = v1
		u2 = v2
		u3 = v3
		v1 = t1
		v2 = t2
		v3 = t3
	return u1

def inverse2(b,n):
	b0 = b
	n0 = n
	t0 = 0
	t = 1
	q = int(math.floor(float(n0/b0)))
	r = n0-q*b0
	while r>0:
		temp = t0-q*t
		if temp >= 0:
			temp = temp%n
		if temp <= 0:
			temp = n - ((-temp)%n)
		t0 = t
		t = temp
	#	print "(12) "+str(t) +" * "+ str(b) +" mod "+ str(n) +" = "+ str(r)
		n0 = b0
		b0 = r
		q = int(math.floor(float(n0/b0)))
		r = n0 - q*b0

	if b0 != 1:
		return False
	else:
		return t%n

def generateKeyPair():
	minimum = 10000
	maximum = 100000
	p = random.randint(minimum,maximum)
	while eratostenes.isPrime(p) == False:
		p = random.randint(minimum,maximum) 
	
	q = random.randint(minimum,maximum)
	while eratostenes.isPrime(q) == False:
		q = random.randint(minimum,maximum) 
	
	n = p*q
	euler = (p-1)*(q-1)

	e = random.randint(1,n)
	while nwd(e,euler) != 1:
		e = random.randint(1,n)
	#print "e: "+str(e)
	d = inverse2(e,euler)
	#print "d:"+str(d)

	print "Public key: ("+str(e)+","+str(n)+")"
	print "Private key: ("+str(d)+","+str(n)+")"

generateKeyPair()

