class DEQue:
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self._data) == 0
    
    def addFirst(self, e):
        self._data.insert(0, e)
        
    def addLast(self, e):
        self._data.append(e)
        
    def removeFirst(self):
        if self.isEmpty():
            return "Queue is empty"
        return self._data.pop(0)
    
    def removeLast(self):
        if self.isEmpty():
            return "Queue is empty"
        return self._data.pop()
    
    def first(self):
        if self.isEmpty():
            return "Queue is empty"
        return self._data[0]
    
    def last(self):
        if self.isEmpty():
            return "Queue is empty"
        return self._data[-1]
    
    
D = DEQue()
D.addFirst(5)
D.addFirst(3)
D.addLast(7)
D.addLast(12)
print(D._data)
print("Length:", len(D._data))
print(D.removeFirst())
print(D.removeLast())
print(D._data)
print("First element:", D.first())
print("Last element:", D.last())