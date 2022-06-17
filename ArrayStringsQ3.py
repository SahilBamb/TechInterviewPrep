#1.3  URLiy: Write a method to replace all spaces in a string with '%20. You may assume that the string
#has  suficient space at the end to hold the additional characters, and that you are given the "true" length
#of  the  string.  (Note:  If implementing  in Java, please  use  a character array  so  that  you can perform this operation in place.) 

# -- EXAMPLE -- 
#Input:  "Mr John Smith  ",  13 
#Output:  "Mr%20John%20Smith" Hints: #53, # 118

def urlify(s):
	#return s.replace(' ','%20')
	
	sList = [_ for _ in s]
	start = 0
	while (sList[start]!=' '):
		start+=1
	end = len(s)-1
	while (sList[end]!=' '):
		end-=1
	for i in range(start,end+1):
		c = s[i]
		if c==' ':
			sList[i] = '%'
			sList.insert(i+1,'20')
	return ''.join(sList)


print(urlify('hello donkey '))