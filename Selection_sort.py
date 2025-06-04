def selection_sort(Arr):
    n = len(Arr)
    for i in range(n-1):
        position = i
        for j in range(i+1, n):
            if Arr[j] < Arr[position]:
                position = j
        
        Arr[i], Arr[position] = Arr[position], Arr[i]
    return Arr


Arr = [50, 41, 2, 89, 56]
print(selection_sort(Arr))