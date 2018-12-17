number=int(raw_input())
num1=list(map(int,raw_input().split()))
num2=list(map(int,raw_input().split()))
if set(num1)==set(num2):
    print("yes")
else:
    print("no")
