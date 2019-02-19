A=int(raw_input())
if(A%3==0 or A%7==0):
    print("yes")
elif(A%(7+3)==0):
    print("yes")
else:
    print("no")
