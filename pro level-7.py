a=int(input())
if(a>0 and (a & (a-1))==0):
    print("0")
else:
    if(a%2!=0):
        print("1")
    else:
        print("2")    
