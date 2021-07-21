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
while True:
	p=input("check or range:\n")
	if p=="Check" or p=="check":
		n=int(input("Enter a num:"))
		if is_megaprime(n):
			print("Megaprime")
		elif is_prime(n) and (not is_megaprime(n)):
			print("Not a megaprime but prime")
		else:
			print("Not a prime")
	elif p=="Range" or p=="range":
		a,b=map(int,input("Enter range: ").split())
		if a>b:
			a,b=b,a
		print("Megaprime series")
		for i in range(a,b+1):
			if is_megaprime(i):
				print(i,end=" ")
		print()
		print("Prime series")
		for i in range(a,b+1):
			if is_prime(i):
				print(i,end=" ")
		print()
	else:
		break
