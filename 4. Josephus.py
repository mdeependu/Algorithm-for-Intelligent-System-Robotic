def josephus(n,k):

	if (n==1):
		return 1
	else:
		return (josephus(n-1,k)+(k-1)) % n+1
    
n=int(input("Enter no.of soldiers: "))
k=2
result=josephus(n,k)
print("Safe Position is",result)
