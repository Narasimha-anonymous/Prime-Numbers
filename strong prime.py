from math import *
def prime(n):
	if n==1:
		return False
	for i in range(2,isqrt(n)+1):
		if n%i==0:
			return False
	return True
def nearest_primes(n):
	h=n+1
	l=n-1
	while (not prime(h)):
		h+=1
	while (not prime(l)):
		l-=1
	return h,l
def strong_prime(n):
	if prime(n):
		a,b=nearest_primes(n)
		if (n>((a+b)/2)):
			return True
	return False

n=int(input("Enter a prime number: "))
if strong_prime(n):
	print("Strong prime")
else:
	print("Not a strong prime")