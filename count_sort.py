def count_sort(Arr):
    max_size = max(Arr)
    c_array = [0] * (max_size + 1)
    
    for i in range(len(Arr)):
        c_array[Arr[i]] = c_array[Arr[i]] + 1
        
    i = 0
    j = 0
    while i < max_size + 1:
        if c_array[i] > 0:
            Arr[j] = i
            j += 1
            c_array[i] = c_array[i] - 1
        else:
            i += 1
    

Arr = [2, 6, 45, 38, 465]   
print("Original Array: ", Arr)
count_sort(Arr)
print("Sorted Array: ",Arr)