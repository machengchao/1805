#身份证
id_card = {'name':'ma','sheng': '1999.12.12','mingzhu': 'han','xiebie':'nan','zhuzhi':'gebi'}
#print(id_card)
print(type(id_card))
#新增
id_card['birthday'] = 180
print(id_card)
#查找
print(id_card.get('wojishiwojishiwojishiwo'))
print(id_card['name'])


#改
id_card['name'] = 'laowang'
print(id_card)



#删
id_card.pop('name')










