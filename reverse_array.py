l = [2, 11, 5, 10, 7, 8]
start, end = 0, len(l)-1

while start < end:
    temp = l[start]
    l[start] = l[end]
    l[end] = temp
    start += 1
    end -= 1
    
print(l)