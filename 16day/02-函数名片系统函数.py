'''
def ma():
	print('1:个人名片')
	print('2:查找名片')
	print('3:修改名片')
	print('4:删除名片')
	print('5:退出系统')
	nub =int(input('请选择功能'))
'''


list = []#存放名字

def ma():
	print("1:添加名片".center(50," "))
	print("2:查找名片".center(50," "))
	print("3:修改名片".center(50," "))
	print("4:删除名片".center(50," "))
	print("5:打印名片".center(50," "))
    
	print("名片管理系统".center(50,"*"))
def add():	
	a = {}
	name=input('请输入名字')
	job=input('请输入职位')
	age=input('请输入年龄')
	phone=input('请输入手机号')
	a['name']=name
	a['job']=job
	a['age']=age
	a['pZZhone']=phone
	list.append(a)
def find():
	name = input("输入姓名")#输入要查找的人
	flag = False#假设没有找到那个人
	for i in list:
		if name== i['name']:
			print('已下是隋静的信息')
			print('姓名%s\n职位:%s\n年龄:%s\n手机号:%s'%(i['name'],i['job'],i['age'],i['phone']))
				
			flag = True#找到了
			break
	if flag == False:	
		print('查无此人')
		
def Modify():
	#要修改之前先要找到要修改的名字
	name = input('请输入您要修改的名字')
	flag = False
	for i in list:
		if name == i['name']:
			print('1:修改名字')
			print('2:修改职位')
			print('3:修改年龄')
			print('4:修改手机号')
			num_1 = int(input('请选择功能'))
			if num_1 == 1:
				new_name = input('请输入新的名字')
				i['name'] = new_name
			elif num_1 == 2:
				new_job = input('请输入新的职位')
				i['job']=new_job
			elif num_1 ==3:
				new_age = input('请输入新的年龄')
				i['age']=new_age
			elif num_1 == 4:
				new_phone = input('请输入新的手机号')
				i['phone']=new_phone
			flag = True
			break
	if flag == False:
		print('查无此人')
def dlt():
	name = input('输入您要删除的名字')
	flag = False
	for position,i in enumerate(list):#把索引遍历出来
		if name == i["name"]:
			flag = True#找到了
			print("1:确认删除")
			print("2:取消删除")
			num_2 = int(input("请选择序号"))
			if num_2 == 1:
				list.pop(position)#直接删除
			break
		if flag == False:
			print('输入有误')






while True:
	ma()#调出用户界面
	num = int(input("请选择功能"))
	if num == 1:
		add()
	elif num ==2:
		find()
	elif num ==3:
		Modify()
	elif num ==4:
		dlt()
'''
    if num  == 1:
        d = {}#空字典
        while True:
            name = input("请输入要添加的名字")
            if len(name) > 4:
                print("太长，请重新输入")
                continue
            job = input("请输入要添加的职位")
            if len(job) > 4:
                print("太长，请重新输入")
                continue
            phone = input("请输入手机号")
            if len(phone) != 11 or  phone.startswith("1") == False:
                print("手机号输入有误，请重新输入")
                continue
            d["name"] = name
            d["job"] = job
            d["phone"] = phone

            #添加到列表
            list.append(d)
            print("添加成功")
            break
    elif num == 2:
        name = input("请输入要查找的姓名")
        flag = False#假设没有咱们要找的人
        for i in list:
            if name == i["name"]:
                print("姓名:%s\n职位:%s\n电话:%s"%(i["name"],i["job"],i["phone"]))
                flag = True#找到了
                break

        if flag == False:
            print("查无此人")                
    elif num == 3:
        #要改之前，你得先查到你要找的那个
        name = input("请输入你要改的人的姓名")
        flag = False
        for i in list:
            if name == i["name"]:
                print("1:修改名字")
                print("2:修改职位")
                print("3:修改电话")
                num_1 = int(input("请选择功能"))
                if  num_1 == 1:
                    new_name = input("请输入新的名字")
                    i["name"] = new_name
                elif num_1 == 2:
                    new_job = input("请输入新的职位")
                    i["job"] = new_job
                elif num_1 == 3:
                    new_phone = input("请输入新的电话")
                    i["phone"] = new_phone
                flag = True
                break
        if flag == False:
            print("查无此人")
    elif num  == 4:
        name = input("请输入你要删除的名字")
        flag = False
        for position,i in enumerate(list):#把索引遍历出来
            if name == i["name"]:
                flag = True#找到了
                print("1:确认删除")
                print("2:取消删除")
                num_2 = int(input("请选择序号"))
                if num_2 == 1:
                    list.pop(position)#直接删除
                break
        if flag == False:
            print("查无此人") 
    elif num == 5:#打印名片
        print("名字\t职位\t电话")
        for i in list:
            print(" "+i["name"]+"\t "+i["job"]+"\t "+i["phone"])
'''








