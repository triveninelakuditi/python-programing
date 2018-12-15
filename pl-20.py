a1=raw_input()
b=len(a1)
c=list(a1)
for i in range(b):
    c[i]=ord(a[i])+3
for j in range(b):
    c[j]=chr(c[j])
print ''.join(c)
