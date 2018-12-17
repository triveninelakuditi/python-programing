num,k=map(int,raw_input().split())
num=int(num)
k=int(k)
         
if num > k: 
    small = k
else: 
    small = num 
for i in range(1, small+1): 
    if((num % i == 0) and (k % i == 0)): 
        gcd = i 
print(gcd) 
