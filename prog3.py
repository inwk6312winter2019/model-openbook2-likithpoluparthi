def histogram():
	hist=dict()
	for line in file:
		line=line.split(',')
		word=(line[12])
		if word not in hist:
			hist[word]=1
		else:
			hist[word]+=1
	print(hist)

#histogram()	


"""List of unique owners"""

def uniquelist():
	ulist=[]
	for line in file:
		line=line.split(',')
		word=line[11]
		if word not in ulist:
			ulist.append(word)
	print(ulist)

#uniquelist()


"""Types of Street classes & list of streets"""

def Strclass():
	stclass=[]
	for line in file:
		line=line.split(',')
		word=line[10]
		if word not in stclass:
			stclass.append(word)
	print(stclass)
	
Strclass()

