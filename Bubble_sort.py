def bubble_sort(Arr):
    n = len(Arr)
    for passes in range(n-1, 0, -1):
        for i in range(passes):
            if Arr[i] > Arr[i+1]:
                Arr[i], Arr[i+1] = Arr[i+1], Arr[i]
    return Arr
                
                
Arr = [23, 65, 45, 86, 53, 32]
print(bubble_sort(Arr))