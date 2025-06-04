class Heap:
    def __init__(self):
        self._maxsize = 10
        self._data = [-1] * self._maxsize
        self._csize = 0
        
    def __len__(self):
        return len(self._data)
    
    def isempty(self):
        return len(self._data) == 0
    
    def insert(self, e):
        if self._csize == self._maxsize:
            return "No Space in Heap"
        self._csize += 1
        hi = self._csize
        while hi > 1 and e > self._data[hi//2]:
            self._data[hi] = self._data[hi//2]
            hi = hi // 2
        
        self._data[hi] = e
        
    def max(self):
        if self._csize == 0:
            return "Heap is Empty"
        return self._data[1]
    
    def deleteMax(self):
        if self._csize == 0:
            return "Heap is empty"
        e = self._data[1]
        self._data[1] = self._data[self._csize]
        self._data[self._csize] = -1
        self._csize = self._csize - 1
        i = 1
        j = i * 2
        while j <= self._csize:
            if self._data[j] < self._data[j + 1]:
                j += 1
            if self._data[i] < self._data[j]:
                temp = self._data[i]
                self._data[i] = self._data[j]
                self._data[j] = temp
                i = j
                j = i * 2
            else:
                break
        return e
                
    
    
H = Heap()
H.insert(25)
H.insert(14)
H.insert(2)
H.insert(20)
H.insert(10)
print(H._data)
H.insert(40)
print(H._data)
print(H.deleteMax())
print(H._data)
print(H.deleteMax())
print(H._data)
print(H.deleteMax())
print(H._data)