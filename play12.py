_,NM = map(int,raw_input().split(" "))
data = map(int,raw_input().split(" "))
l = len(data)
for __ in range(NM):
    data = [data[l-1]] + data[0:l-1]
print " ".join(map(str,data))
