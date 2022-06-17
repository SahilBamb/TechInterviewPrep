
### Array Strings: Question 1.1

# 1.1  Is  Unique: Implement an algorithm to determine if a  string  has all  unique characters. 
# What if you cannot use additional data structures? Hints:  #44, #7 7 7, #732


def UniqueChars(s):
	allChars = {}
	for c in s:
		if c in allChars: return False
		else: allChars[c] = 1
	return True

def UniqueCharsNoSpace(s):
	if len(s)<2: return False
	sList = [_ for _ in s]
	sList.sort()
	prev = sList[0]
	for c in sList[1:]:
		if c == prev: return False
		prev = c
	return True



