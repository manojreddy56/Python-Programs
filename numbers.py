with open("numbers.txt", "r") as f:
    data = f.read()
    l = list(map(int, data.split(", ")))
    count = 0
    for num in l:
        if num % 2 == 0:
            count += 1
        else:
            continue
    print(count)