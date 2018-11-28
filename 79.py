import math
t,l=map(int,raw_input().split())
a=t * l
if math.sqrt(a).is_integer():
    print "yes"
else:
    print "no"
