account = input('请输入您的账户')
password = input('请输入您的密码')
nick_name = input('请输入姓名')
money = 2000#原有的存款
need_money = int(input('请输入您要提取的金额'))
sm = money - need_money
print('账户%s'%account)
print('密码%s'%password)
print('姓名%s'%nick_name)
print('原有的存款为%d'%money)
print('提取的金额为%s'%need_money)
print('剩余%d'%sm)
