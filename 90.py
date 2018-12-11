
num=raw_input().rstrip()
digits=[]
for c in num:
	if c.isdigit():
		digits.append(c)
print("".join(digits))
