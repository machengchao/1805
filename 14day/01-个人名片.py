list=[]
print('个人名片'.center(50,' '))
while True:
	print('1:添加名片'.center(50,' '))
	print('2:查找名片'.center(50,' '))
	print('3:修改名片'.center(50,' '))
	print('4:删除名片'.center(50,' '))
	print('5:退出'.center(50,' '))
	a=input('请选择功能: ')
	if a=='1':
		e={}
		name=input('输入姓名: ')
		sj=input('输入电话号码: ')
		zhiwei=input('输入职位: ')
		e['name']=name
		e['sj']=sj
		e['zhiwei']=zhiwei
		list.append(e)
		print(list)
	elif a=='2':
		
	







