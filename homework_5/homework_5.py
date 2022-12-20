


def gen(start,stop,step):
	list = []
	for i in range(start,stop,step):
		list.append(i)
	return list
a, b, c = int(input("start:")), int(input("stop:")), int(input("step:"))
print(gen(a,b,c))