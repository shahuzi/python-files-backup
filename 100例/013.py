for x in range(10,1000):
	i = x//100
	j = x%100//10
	k = x%10
	if i**3+j**3+k**3 == x:
		print(x,end=',')