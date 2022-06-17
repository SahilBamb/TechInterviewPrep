#1.2  Check  Permutation:  Given  two  strings, write  a  method  to  decide  if one is a  permutation  of  the
#other. Hints: #7, #84, #722, #737

def checkPerm(s,s2):
	allChars = {}
	for c in s:
		allChars[c] = 0 if c not in allChars else allChars[c]+1
	for c in s2:
		if c in allChars and allChars[c]>0:
			allChars[c]-=1
		else:
			return False
		


