def fun():
    with open("practice.txt", "r") as f:
        line = 1
        data = True
        while data:
            data = f.readline()
            if "learning" in data:
                return line
            line += 1
            
    return -1
            
print(fun())