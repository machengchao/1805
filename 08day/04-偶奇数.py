a = 0
b = 0
c = 0
e = 0
d = int(input('输入您要输入的数字:')) 
while a<= d :
    e += a
    if a % 2 == 0:
        print('偶数是%d'%a)
        b += a
    else:
        print('奇数是%d'%a)
        c += a
    a +=1     
print('偶数是%d'%b)
print('奇数是%d'%c)
print('总和是%d'%e)
