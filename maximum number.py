def h(arr,n):
	max = arr[0]
	for i in range(1,n):
		if arr[i] >max:
			max = arr[i]
	return max
arr = [20,30,32,88,100]
n = len(arr)
ans = h(arr,n)
print(ans)
