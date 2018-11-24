m=raw_input()
"""if all(c in '01' for a in m):
    print "yes"
else:
    print "No"
    """
if not(m.translate(None,'01')):
    print "yes"
else:
    print "No"
