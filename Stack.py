class mystack:
    def __init__(self) -> None:
        self.l=[]
        
        
    def push(self, ele):
        self.l.append(ele)
        
        
    def pop(self):
        if len(self.l) > 0:
            x = self.l.pop()
            print(x, "is removed from the stack")
        else:
            print("stack is underflow")
            
            
    def peek(self):
        if len(self.l) > 0:
            x = self.l[-1]
            print("top element is", x)
        else:
            print("Stack is underflow")
            
            
    def display(self):
        if len(self.l) > 0:
            print(self.l)
        else:
            print("stack is empty")
            
            
s = mystack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display()
s.peek()
s.pop()
s.display()