'''
sum = 0
for i in range(101):
	sum+=i
print(sum)
def print_sum(num):
	sum = 0
	for i in range(num+1):
		sum+=i
	print(sum)
print_sum(101)
'''

def zhuce(account,password):
	if len(account)==11 and account.startswith('1') and len(password) >6: 
		print('注册成功')

	else:
		print('注册失败')	
	
account=input('请输入账号')
password=input('请输入密码')
zhuce(account,password)

list = []#盛装注册的密码和账号
def register(account,password):
    user = {}#初始化字典
    if len(account) == 11 and account.startswith("1")and len(password) > 6:
        print("注册成功")
        #保存账号和密码
        user["account"] = account
        user["password"] = password
        list.append(user)
    else:
        print("注册失败")



def login(account,password):#登录函数
    for i in list:
        if account == i["account"] and password == i["password"]:
            print("登录成功")
        else:
            print("登录失败")
'''
#注册
acc = input("请输入账号")
pwd = input("请输入密码")
register(acc,pwd)#调用注册函数

#登录
if list:#不是空的，就代表注册成功
    acc = input("请输入账号")
    pwd = input("请输入密码")
    login(acc,pwd)
'''
'''
import time
def play_game(xxxxxx):
	time.sleep(1)
	print(xxxxxx)
while True:
	play_game('我喜欢写代码')
	play_game('我喜欢玩游戏')
'''	
	
	










