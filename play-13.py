number=int(input())
sum=0
while(number>0):
    n=int(number%10)
    sum=(n*n)+sum
    number=int(number/10)
print(sum)
