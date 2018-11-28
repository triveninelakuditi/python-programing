def do_stuff(input):
	m, k= [int(m) for m in input.split(" ")]
	print(k-m)
		

while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) 
  except (EOFError):
    break 
