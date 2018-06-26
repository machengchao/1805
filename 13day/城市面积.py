list = [{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}] 
for i in list:
	for b,c in i.items():
		for d,f in c.items():
			print(b,d,f)
