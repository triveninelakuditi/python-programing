str = raw_input().rstrip()
even num = odd  num= ''
for i, s in enumerate(str):
	if i & 1 == 0:
		even numstr += s
	else:
		odd numstr += s

	print(even numstr + " " + odd numstr)
