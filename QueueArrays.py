class QueueArrays:
    def __init__(self) -> None:
        self.data = []
        
    def __len__(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def enqueue(self, e):
        self.data.append(e)
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.data.pop(0)
    
    def first(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.data[0]
    
    
Q = QueueArrays()
Q.enqueue(5)
Q.enqueue(3)
print(Q.data)
print("Length: ", len(Q))
Q.enqueue(7)
Q.enqueue(12)
print(Q.data)
print(Q.dequeue())
print(Q.data)
print(Q.first())