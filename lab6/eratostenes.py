#!/usr/bin/python

def sito(n):

	numbers = [0]*(n+1)
	i = 2
	while (i*i) <= n:
		if(numbers[i] == 1):
			i= i+1
			continue
		j=2*i
		while( j <= n ):
			numbers[j] = 1	
			j = j+i	
		i= i+1

	result = []

	k = 2
	while k <= n:
		if numbers[k] == 0:
			result.append(k)
		k = k+1

	return

def isPrime(n):
	

	return
