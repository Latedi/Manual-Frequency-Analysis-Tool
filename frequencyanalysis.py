#This script contains a set of functions for frequency analysis mostly used
#for breaking monoalphabetic ciphers. Put ciphertexts in the ciphertexts
#variable and change the key in freqalpha.
ciphertexts = ""

def printpretty(inputstr, blocksize=5, newline=65):
	index = 0
	totlen = len(inputstr)
	while(index < totlen):
		if(index + blocksize < totlen):
			print(inputstr[index:index+blocksize], end="")
			index += blocksize
		else:
			print(inputstr[index:totlen], end="")
			index = totlen
		if(index % newline == 0):
			print()
		else:
			print(" ", end="")
	
def frequency(inputstr):
	countarr = []
	for i in range(0, ord('Z') - ord('A') + 1):
		currentchar = chr(ord('A') + i)
		c = inputstr.count(currentchar)
		countarr.append([currentchar, float("%.2f" % (c / len(inputstr) * 100))])
	return countarr
	
def doublecount(inputstr):
	doublearr = []
	for i in range(0, ord('Z') - ord('A') + 1):
		currentchar = chr(ord('A') + i)
		c = 0
		for j in range(0, len(inputstr) - 1):
			if(inputstr[j] == currentchar and inputstr[j + 1] == currentchar):
				c += 1
		doublearr.append([(currentchar + currentchar), c]);
	return doublearr
	
def commondigraphcount(inputstr):
	common = ["TH", "HE", "AN", "IN", "ER", "ON", "RE", "ED", "ND", "HA", "AT", "EN", "ES", "OF", "NT", "EA", "TI", "TO", "IO", "LE", "IS", "OU", "AR", "AS", "DE", "RT", "VE"]
	diagrapharr = []
	for i in range(0, len(common)):
		diagrapharr.append([common[i], inputstr.count(common[i])])
	return diagrapharr
	
def alldigraphcount(inputstr, threshold=20):
	arr = []
	for i in range(0, ord('Z') - ord('A') + 1):
		for j in range(0, ord('Z') - ord('A') + 1):
			c = 0
			currenti = chr(ord('A') + i)
			currentj = chr(ord('A') + j)
			c = inputstr.count(currenti + currentj)
			if(c >= threshold):
				arr.append([(currenti + currentj), c])
	return arr
	
def commontrigraphcount(inputstr):
	common = ["THE", "AND", "THA", "ENT", "ION", "TIO", "FOR", "NDE", "HAS", "NCE", "TIS", "OFT", "MEN"]
	trigrapharr = []
	for i in range(0, len(common)):
		trigrapharr.append([common[i], inputstr.count(common[i])])
	return trigrapharr
	
def alltrigraphcount(inputstr, threshold=10):
	arr = []
	for i in range(0, ord('Z') - ord('A') + 1):
		for j in range(0, ord('Z') - ord('A') + 1):
			for k in range(0, ord('Z') - ord('A') + 1):
				c = 0
				currenti = chr(ord('A') + i)
				currentj = chr(ord('A') + j)
				currentk = chr(ord('A') + k)
				c = inputstr.count(currenti + currentj + currentk)
				if(c >= threshold):
					arr.append([(currenti + currentj + currentk), c])
	return arr
	
def runandprint(header, function, inputstr):
	print(header)
	arr = function(inputstr)
	arr.sort(key=getsortkey)
	arr.reverse()
	if(len(arr) > 0):
		for i in range(0, len(arr)):
			print(arr[i][0] + ": " + str(arr[i][1]))
	print()
	return arr

def getsortkey(tuple):
	return tuple[1]
	
#Change this
freqalpha = "ETAOINSRHDLUCMFYWGPBVKXQJZ"

#Common doubles SS LL OO EE NN PP
#Common digraphs TH HE IN ER AN RE ND
#http://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/hints.html

countarr = runandprint("CIPHERTEXT FREQUENCIES", frequency, ciphertexts)
runandprint("CIPHERTEXT DOUBLES", doublecount, ciphertexts)

#TRANSLATE CIPHERTEXT INTO AN ARRAY
newtext = []
for i in range(0, len(ciphertexts)):
	newtext.append(ciphertexts[i])
replacedindex = []
for i in range(0, len(countarr)):
	for j in range(0, len(newtext)):
		if(newtext[j] == countarr[i][0] and not j in replacedindex):
			replacedindex.append(j)
			newtext[j] = freqalpha[i]
strtext = "".join(newtext)

runandprint("MESSAGE FREQUENCIES", frequency, strtext)
runandprint("MESSAGE DOUBLES", doublecount, strtext)
runandprint("MESSAGE DIGRAPHS", commondigraphcount, strtext)
runandprint("MESSAGE ALL DIGRAPHS", alldigraphcount, strtext)
runandprint("MESSAGE TRIGRAPHS", commontrigraphcount, strtext)
runandprint("MESSAGE ALL TRIGRAPHS", alltrigraphcount, strtext)

#printpretty(ciphertexts)
print("MESSAGE")
printpretty(strtext)
