def quick_sort(Arr, low, high):
    if low < high:
        pi = partition(Arr, low, high)
        quick_sort(Arr, low, pi)
        quick_sort(Arr, pi+1, high)
        
        
def partition(Arr, low, high):
    pivot = Arr[low]
    i = low + 1
    j = high
    while True:
        while i<=j and Arr[i] <= pivot:
            i += 1
    
        while i<=j and Arr[j] > pivot:
            j -= 1
        if i <= j:
            Arr[i], Arr[j] = Arr[j], Arr[i]
        else:
            break
    
    Arr[j], Arr[low] = Arr[low], Arr[j]
    return j


Arr = [3, 9, 5, 4, 6, 8]
print("Original Array:", Arr)
quick_sort(Arr, 0, 5)
print("Sorted Array: ", Arr)
