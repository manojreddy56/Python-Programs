class stackArray:
    def __init__(self):
        self.data = []
        
    def __len__(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def push(self, e):
        self.data.append(e)
        
    def pop(self):
        if len(self.data) == 0:
            return "Stack is empty"
        else:
            return self.data.pop()
        
    def top(self):
        if len(self.data) == 0:
            return "Stack is empty"
        else:
            return self.data[-1]
        
        
S = stackArray()
S.push(5)
S.push(3)
print(S.data)
print("Length: ", len(S.data))
print(S.pop())
print(S.isEmpty())
print(S.pop())
print(S.isEmpty())
S.push(7)
S.push(9)
S.push(4)
print(S.top())
print(S.data)