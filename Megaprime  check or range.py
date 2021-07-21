def is_prime(n):
	if n==1:
		return False
	for i in range(2,n//2+1):
		if n%i==0:
			return False
	return True
def is_megaprime(n):
	if is_prime(n):
		while n:
			a=n%10
			if not is_prime(a):
				return False
			n//=10
		return True
	return False
a,b=map(int,input().split())
if a>b:
	a,b=b,a
for i in range(a,b+1):
	if is_megaprime(i):
		print(i)