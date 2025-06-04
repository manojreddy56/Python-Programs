def linear_search(Arr, key):
    n = len(Arr)
    index = 0
    while index < n:
        if Arr[index] == key:
            return index
        index = index + 1
    return -1


Arr = [84, 21, 47, 96, 15]
print(linear_search(Arr, 96))