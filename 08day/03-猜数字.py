import random
suiji = random.randint (1,100)
a = 0
while a <=100:
    user = int(input('请输入数字:'))
    if user < suiji:
        print('猜小了')
    elif user > suiji:
        print('猜大了')
    else:
        print('恭喜你,把我奖励给你')
        i = 10
    a +=1
