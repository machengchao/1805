sex = input("请输入性别")
if sex =='男':
    weight=input('请输入您的身高')
    money=input('请输入您的财富')
    color=input('请输入您的颜值')
    if weight>'180'and money>'1000' and color>'90':
        print('高富帅')
    else:
        print('稳住,别浪')
if sex == '女':
    pifucolor=input('请输入您的皮肤颜色')
    money=input('请输入您的财富')
    colo=input('请输入您的颜色')
    if pifucolor=='白色' and money>'800' and colo<'90':
        print('白富美')
    else:
        print('哈哈哈')

