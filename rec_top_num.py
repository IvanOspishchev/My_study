huge = 0
def rec_top_num(arr):
    i = 0
    j = 1
    global huge
    if arr == 0:
        return huge
    elif arr[i] < arr[j]:
        huge = arr[j]
        i += 1
        j += 1
        return rec_top_num(arr[1:])

print (rec_top_num([1, 2, 3, 4, 5]))
