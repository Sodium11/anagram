def anagram(data):
	if len(data)<=1:
		return [data]

	if len(data)==2:
		return [data,[data[1],data[0]]]
	elif len(data)>2:
		result=[]
		for i in range(len(data)):
			for j in anagram(data[:i]+data[i+1:]):
				n1=[data[i]]
				for n in j:
					n1.append(n)
				result.append(n1)
		return result
str="quizknock"
ans=anagram(list(str))
file =open("anagram.txt","w")
for i in ans:
	file.write("".join(i)+"\n")
file.close()

