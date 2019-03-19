i = 10
def count_down(i):
	print(i)
	if i < 1:
		print("finish")
	else:
		count_down(i - 1)

print(count_down(10))