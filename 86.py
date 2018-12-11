def isIsogram(num):
	charMap={}
	for h in num:
		if h in charMap:
			return False
		else:
			charMap[c]=1
	return True
num=raw_input().rstrip()
print("Yes" if isIsogram(num) else "No")
