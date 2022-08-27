

def main(user,a):
	f=open('works.txt','r')
	data=f.read()
	f.close()
	data=data.split('.')[:-1]
	assignedto=[]
	b=[]
	for i in a:
		b.append(i[0])
	l=[]
	for each in data:
		parts=each.split(',')
		if(parts[0] in b):
			l.append(','.join([parts[0],parts[1],'1']))
		else:
			l.append(','.join(parts))
	f=open('works.txt','w')
	f.write('.'.join(l)+'.')
	f.close()
	


if __name__ == '__main__':
	main('anbu',[])