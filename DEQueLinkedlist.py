class _Node:
    __Slots__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next
     
        
class dequeLinkedlist:
    def __init__(self):
        self._size = 0
        self._front = None
        self._rear = None
        
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def addFirst(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            self._front = newest
            self._rear = newest
        else:
            newest._next = self._front
            self._front = newest
        self._size += 1
        
    def Add_last(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            self._front = newest
        else:
            self._rear._next = newest
        self._rear = newest
        self._size += 1
        
    def remove_first(self):
        if self.isEmpty():
            return "List is empty"
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isEmpty():
            self._rear = None
        return e
    
    def remove_last(self):
        if self.isEmpty():
            return "List is empty"
        p = self._front
        i = 1
        while i < self.__len__() - 1:
            p = p._next
            i += 1
        self._rear = p
        p = p._next
        e = p._element
        self._rear._next = None
        self._size += 1
        return e
    
    def first(self):
        if self.isEmpty():
            return "DEQue is empty"
        return self._front._element
    
    def last(self):
        if self.isEmpty():
            return "DEQue is empty"
        return self._rear._element
    
    def display(self):
        p = self._front
        while p:
            print(p._element, end="  ")
            p = p._next
        print()
        
    def search(self, key):
        p = self._front
        index = 0
        while p:
            if p._element == key:
                return index
            else:
                p = p._next
                index += 1
        else:
            return "Element not found"
        
        
D = dequeLinkedlist()
D.addFirst(3)
D.addFirst(5)
D.addFirst(9)
D.Add_last(6)
D.Add_last(4)
D.display()
print("Length:", len(D))
print(D.remove_first())
D.display()
print(D.remove_last())
D.display()
print("First element:", D.first())
print("Last element:", D.last())