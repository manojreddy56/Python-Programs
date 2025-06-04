def insertion_sort(Arr):
    n = len(Arr)
    for i in range(1, n):
        current_value = Arr[i]
        position = i
        while position > 0 and Arr[position-1] > current_value:
            Arr[position] = Arr[position-1]
            position = position - 1
        
        Arr[position] = current_value
    return Arr
        
        
Arr = [10, 89, 65, 52]
print(insertion_sort(Arr))