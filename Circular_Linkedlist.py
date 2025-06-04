class _Node:
    __slots__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next
        

class CLL:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def isempty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
        
    def Add_last(self, e):
        newest = _Node(e, None)
        if self.isempty():
            newest._next = newest
            self._head = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
    def Add_first(self, e):
        newest = _Node(e, None)
        if self.isempty():
            newest._next = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._tail._next = newest
        self._head = newest
        self._size += 1
        
    def Add_any(self, e, position):
        newest = _Node(e, None)
        p = self._head
        i = 1
        while i < position-1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1
        
    def Remove_first(self):
        if self.isempty():
            return "List is empty"
        e = self._head._element
        self._head = self._head._next
        self._tail._next = self._head
        self._size -= 1
        if self.isempty():
            self._head = None
            self._tail = None
        return e
    
    def remove_last(self):
        if self.isempty():
            return "List is empty"
        p = self._head
        i = 1
        while i < self.__len__()-1:
            p = p._next
            i += 1
        self._tail = p
        e = p._next._element
        self._tail._next = self._head
        self._size -= 1
        return e
    
    def removeAny(self, position):
        if self.isempty():
            return "List is empty"
        p = self._head
        i = 1
        while i < position-1:
            p = p._next
            i += 1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1
        return e
       
    def display(self):
        p = self._head
        i = 0
        while i < self.__len__():
            print(p._element, end=" ")
            p = p._next
            i += 1
        print()
            

L = CLL()
L.Add_last(3)
L.Add_last(5)
L.Add_last(9)
L.Add_last(7)
L.Add_last(12)
print(L._size)
L.display()
L.Add_first(23)
L.display()
L.Add_any(15, 4)
L.display()
L.Remove_first()
L.display()
print(L._size)
print(L.remove_last())
L.display()
print(L.removeAny(3))
L.display()