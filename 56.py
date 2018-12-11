Rain,Song = map(int,raw_input().split())
lists = [int(x) for x in raw_input().split()]
if Rain and song in lists:
    print"yes"
else:
    print"no"
