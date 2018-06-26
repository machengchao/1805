list = []
for i in range (100,201):
	a = 0
	for j in range(100,i-1):
		if i %j == 0:
			a = 1
			break
	if a == 0:
		print(i)






