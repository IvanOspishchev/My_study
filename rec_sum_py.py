def rec_sum(arr):
	if len(arr) == 1:
		return arr[0]
	else:
		return (arr[0] + rec_sum(arr[1:]))

print (rec_sum([1, 2, 3, 4]))
