print('登录')
i = 0
while i<=3:
	a = input('请输入帐号')
    b = input('请输入密码')
	if a == 'mcc' and b == '123456':
		print('登录成功')
		print('*' *35)
		e = input('0adc 1肉 3法师')
		if e == '0':
			print('鲁班大师')
			break
		elif e == '1':
			print('诚邀经')
			break
		elif e == '3':
			print('王昭君')
			break
	else:
		print('登录失败,请重新输入帐号密码')
	i+=1
