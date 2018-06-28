'''
list = [1,3,2,45,46,100,76,24,88,]
#list.sort系统排序的方法
for i in range(0,len(list)-1):
	for j in range(i+1,len(list)):
		if list[i]>list[j]:
			list [i],list[j] = list[j],list[i]
			print(list)
'''


a = [1,100,48,10,56,3,2,37]
for position,i in enumerate(list):
	if i ==3:
		print("索引是%d"%position)
		break
#**************
 
#a = [1,100,48,10,56,3,2,37]














