class _Node:
    __slots__ = '_next', '_element'
    
    def __init__(self, element, next) -> None:
        self._element = element
        self._next = next


class stackLinkedlist:
    def __init__(self):
        self._top = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def push(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        e = self._top._element
        self._top = self._top._next
        self._size -= 1
        return e
    
    def top(self):
        if self.isEmpty():
            return "Stack is empty"
        return self._top._element
    
    def display(self):
        p = self._top
        while p:
            print(p._element, end=" ")
            p = p._next
        print()
        
        
S = stackLinkedlist()
S.push(5)
S.push(3)
print("Lenght: ", len(S))
S.display()
print(S.pop())
print(S.isEmpty())
S.display()
S.push(7)
S.push(9)
S.push(12)
S.display()
print(S.top())