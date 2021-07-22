def is_prime(n):
	if n==1:
		return False
	for i in range(2,n//2+1):
		if n%i==0:
			return False
	return True
def np(l,h,n):
	if (n-l) < (h-n):
		return l
	elif (n-l) > (h-n):
		return h
	else:
		return l,h
n=int(input())
if is_prime(n):
	print(n)
else:
	h=n+1
	l=n-1	
	while (not is_prime(h)):
		h+=1
	while (not is_prime(l)):
		l-=1
	print(np(l,h,n))