i = 0
def rec_count(arr):
    global i
    if len(arr) == 0:
        return i
    else:
        i += 1
        return rec_count(arr[1:])

print(rec_count([1, 2, 3, 4, 5]))