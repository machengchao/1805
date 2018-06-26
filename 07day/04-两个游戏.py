print('请选择您的游戏')
game=input('1:王者荣耀，2:植物大战僵尸')
account='123'
pwd='123'
if game=='1':
    account=input('请输入您的帐号')
    pwd=input('请输入您的密码')
    if account == '123456' and pwd == '123456':
        print('登录成功/n欢迎来到王者荣耀')
    else:
        print('登录失败')
if game=='2':
    print('一大波僵尸正在来袭')

