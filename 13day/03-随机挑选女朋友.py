list = []
while True:
	print('1:添加名片')
	print('2:查找名片')
	print('3:修改名片')
	print('4:删除名片')
	print('5:退出系统')
	number = int(input('添加名片'))
	dic = {}
	if me == 1:
		print('添加名片'.center(50,'='))
		a = input('请输入姓名: ')
		a = input('请输入年龄: ')
		a = input('请输入性别: ')
		a = input('请输入电话: ')
		a = input('请输入公司: ')
		dic1 = {'姓名':a,
				'年龄':b,
				'性别':c,
				'电话':d,
				'公司':c,}
		dic.update(dic1)
		lista.append(dic1)
		print('添加成功'.center(50.'^'))
		for a.b in dic.items():
			print(a,b)
	elif me == 2:
		print('查询名片'.center(50,'='))
		cha = input('请输入姓名 : ' )
		for i in lista:
			if cha == i['请输入姓名']
				print('姓名 %s'%i['姓名'])
				print('年龄 %s'%i['年龄'])
				print('性别 %s'%i['性别'])
				print('电话 %s'%i['电话'])
				print('公司 %s'%i['公司'])
			else:
				print('没有这个名片～～～～')
		elif me== 3 :
			print('修改名片'.center(50,'='))
			gai = input('你要修改的名片： ')
			for i in lista:
				if gai == i['姓名']:
					print('1.修改姓名\n2.修改年龄\n3.修改性别\n4.修改电话\n5.修改公司    ')
					a = int(input('请输入选项:  '))
					if a == 1:
						b = input('请输入新的姓名: ')
						i['姓名'] = b
						print('修改新的名字为 %s'%i['姓名'])
				







				





