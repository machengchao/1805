list = []#存放名字
def ma():
	print("1:点菜".center(50," "))
	print("2:查找菜".center(50," "))
	print("3:修改点过的菜".center(50," "))
	print("4:删除点过的菜".center(50," "))
	print("5:看一下点过的菜".center(50," "))
	print("富家楼饭馆".center(50,"*"))

def add():
	a = {}
	print("菜单".center(50," "))
	print("热菜：")
	print("1:干椒牛柳-40*****2：西红柿炒鸡蛋-15,3：蘑菇炒肉-25")
	print("凉菜：")
	print("1:拍黄瓜-10,2:凉拌猪头肉-20,3:凉拌豆腐皮-15")
	print("汤：")
	print("1:海鲜汤-40,2:地三鲜-40,3:丸子汤-25")
	print("烧烤:")
	print("1:羊肉串-2/,2:鱼豆腐-2/,3:面筋-2/,4:烤全羊-45/")
	while True:
		name=input("您要吃些什么(菜系)：　")
		if name == "热菜":
			chi = int(input("请输入您要吃什么(输入菜的序号)：　"))
				if chi == 1:
					a["name"] = ("1:干椒牛柳,2:西红柿炒鸡蛋,3:蘑菇炒肉")
		if name = "凉菜":	
			chi = int(input("请输入您要吃什么(输入菜的序号)：　"))
				if chi == 2:
					b["liang"] = ("1:拍黄瓜,2:凉拌猪头肉,3:凉拌豆腐皮")
		if name = "汤":	
			chi = int(input("请输入您要吃什么(输入菜的序号)：　"))
				if chi == 3:
					c["tang"] = ("1:海鲜汤,2:地三鲜,3:丸子汤")
		if name = "烧烤":	
			chi = int(input("请输入您要吃什么(输入菜的序号)：　"))
				if	chi == 4:
					d["shao"] = ("1:羊肉串-2/,2:鱼豆腐-2/,3:面筋-2/,4:烤全羊-45")
				

				list.append(a)


#主运行
while True:
	print("欢饮来到".center(50,"*"))
	me = int(input("请输入选项：　"))
	if me == 1:
		ma()
	elif me == 2:
		add()
		





'''
(dd():
 23     a = {}
 24     name=input('请输入名字')
 25     job=input('请输入职位')
 26     age=input('请输入年龄')
 27     phone=input('请输入手机号')
 28     a['name']=name
 29     a['job']=job
 30     a['age']=age
 31     a['phone']=phone
 32     list.append(a)
 33 def find():
 34     name = input("输入姓名")#输入要查找的人
 35     flag = False#假设没有找到那个人
 36     for i in list:
 37         if name== i['name']:
 38             print('姓名%s\n职位:%s\n年龄:%s\n手机号:%s'%(i['name'],i['job'],    i['age'],i['phone']))
 39 
 40             flag = True#找到了
 41             break
 42     if flag == False:
 43         print('查无此人')
"凉拌猪头肉")
'''
