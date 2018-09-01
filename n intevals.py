n = int(input(" "))
temp = n
sum = 0
while(temp > 0):
    dig = temp % 10
    sum += dig ** 3
    temp // = 10
if(num == sum):
	print("yes")
else:
	print("no")
   
