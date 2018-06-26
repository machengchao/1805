'''
def d_sum(a,b,*args,**kwargs):
	print(a)
	print(b)
	print(args)
	print(kwargs)
'''	

'''
t= (1,2,3,4,5,6)
d= {'wei':1,'ma':19}
d_sum(1,2,*t,**d)
'''
def	ma(a,b,*args,**kwargs):
	sum = a+b
	for b in args:
		print(b)
		sum = sum+b
	for i in kwargs.values():
		print(i)
		sum=sum+i
	print(sum)
t= (1,2,3,4,5,6)
d= {'wei':12,'ma':24}
ma(1,2,*t,**d)



