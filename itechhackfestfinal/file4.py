

def main(user,leader):
	f=open('works.txt','r')
	data=f.read()

	f.close()
	data=data.split('.')[:-1]
	
	assignedto=[]
	
	if leader:
		for each in data:
			parts=each.split(',')
			assignedto.append(parts)
		return assignedto

	for each in data:
		parts=each.split(',')
		if parts[1]==user:
			assignedto.append([parts[0],parts[2]])
	return assignedto

if __name__ == '__main__':
	main('anbu')