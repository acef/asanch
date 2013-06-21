import sys

def divText(text):
	text += ' '
	strBuffer = ''
	newList = []
	
	for char in text:
		if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
			strBuffer = strBuffer + char
		elif char == ' ' or '\n':
			newList.append(strBuffer)
			strBuffer = ''
	
	return newList

def wordFrec(text):
	lst = divText(text)
	wordList = []
	countList = []
	newList = []

	for word in lst:
		if word not in wordList:
			wordList.append(word)
			countList.append(lst.count(word))
	for n in range(len(wordList)):
		newList.append([wordList[n], countList[n]])

	return sorted(newList)

def main():
	if len(sys.argv) > 1: 
		fle = open(sys.argv[1], 'Ur')
		text = fle.read()
		lst = wordFrec(text)
		for field in lst:
			print ' %s - %d' % (field[0], field[1])

	else:
		print 'Fuck you, user! specify file'


if __name__ == '__main__':
  main()