def merge_sort(Arr, left, right):
    if left < right:
        mid = (left+right) // 2
        merge_sort(Arr, left, mid)
        merge_sort(Arr, mid+1, right)
        merge(Arr, left, mid, right)
        
        
def merge(Arr, left, mid, right):
    B = [0] * (right+1)
    i = left
    j = mid+1
    k = left
    while i <= mid and j <= right:
        if Arr[i] < Arr[j]:
            B[k] = Arr[i]
            i += 1
        else:
            B[k] = Arr[j]
            j += 1
        k += 1
            
    while i <= mid:
        B[k] = Arr[i]
        i += 1
        k += 1
        
    while j <= right:
        B[k] = Arr[j]
        j += 1
        k += 1
        
    for m in range(left, right+1):
        Arr[m] = B[m]
    
    
Arr = [10, 56, 89, 56, 23]
merge_sort(Arr, 0, len(Arr)-1)
print(Arr)