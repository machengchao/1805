import time
print('正在打开系统')
time.sleep(1)
print('学生管理系统\n')
print('='*50)
p = []
while True:
	print('请选择：1,添加\n2,删除\n3,修改\n4,查找\n')
	print('='*50)
	a = int(input('请选择功能:')
	if a == 1 :
		while True:
			b = input('请输入名字')
			if b in p:
				print('您输入的名字已存在\n请重输入')
			else:
				p.append(b)
				break
		print('您已成功添加这位同学')
	elif a ==2 :
		f = input('请输入名字')
		if f in p :
			print('已删除这位同学')
			p.remove(f)
		else:
			print('没有这个名字')
	elif a == 3:
		y = input('请输入改之后的名字:')
		if y in p :
			o = input('请输入改之后的名字:')
			x = p.index(y)
			p[x]=o
		else:
			print('没有这个名字')
	if a == 4:
		print('='*50)
		print(p)
		print('='*50)










