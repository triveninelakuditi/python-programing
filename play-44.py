def rat(k,m):
    print(k[n:]+k[:m])
k,m=map(str,raw_input().split())
m=int(m)
n=len(k)-m
rat(k,n)
