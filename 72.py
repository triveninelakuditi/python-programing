n=raw_input("")
vowel=set('aeiou')
if not vowel.isdisjoint(n):
    print "yes"
else:
    print "no"
