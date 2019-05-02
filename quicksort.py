def quicksort(array):
	if len(array) < 2:
		return array
	else:
		base = array[0]
		less = (i for i in array[1:] if i <= base)
		grater = (i for i in array[1:] if i > base)
		return (quicksort(less) + [base] + quicksort(grater))


print (quicksort([1, 2, 3, 6, 8, 2]))