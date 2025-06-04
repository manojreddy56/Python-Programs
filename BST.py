class _Node:
    __slots__ = '_element', '_left', '_right'
    
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


class binarySearchTree:
    def __init__(self):
        self._root = None
        
    def insert(self, troot, e):
        temp = None
        while troot:
            temp = troot
            if troot._element == e:
                return
            elif troot._element > e:
                troot = troot._left
            elif troot._element < e:
                troot = troot._right
                
        n = _Node(e, None, None)
        if self._root:
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n
        else:
            self._root = n
            
        
    def rinsert(self, troot, e):
        if troot:
            if e < troot._element:
                troot._left = self.rinsert(troot._left, e)
            elif e > troot._element:
                troot._right = self.rinsert(troot._right, e)    
        else:
            n = _Node(e)
            troot = n
        return troot
    
    def delete(self, e):
        p = self._root
        pp = None
        while p and p._element != e:
            pp = p
            if e < p._element:
                p = p._left
            else:
                p = p._right
        if not p:
            return False
        if p._left and p._right:
            s = p._left
            ps = p
            while s._right:
                ps = s
                s = s._right
            p._element = s._element
            p = s
            pp = ps
        c = None
        if p._left:
            c = p._left
        else:
            c = p._right
        if p == self._root:
            self._root = None
        else:
            if p == pp._left:
                pp._left = c
            else:
                pp._right = c
    
    
    def search(self, key):
        troot = self._root
        while troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                troot = troot._left
            elif key > troot._element:
                troot = troot._right
        return False
    
    def rsearch(self, troot, key):
        if troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                return self.rsearch(troot._left, key)
            elif key > troot._element:
                return self.rsearch(troot._right, key)
        else:
            return False
    
    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end=" ")
            self.inorder(troot._right)
            
        
b = binarySearchTree()
b._root = b.rinsert(b._root, 50)
b.rinsert(b._root, 30)
b.rinsert(b._root, 80)
b.rinsert(b._root, 10)
b.rinsert(b._root, 40)
b.rinsert(b._root, 60)
b.inorder(b._root)
print()
print(b.search(60))
print(b.search(30))
print(b.search(70))
print(b.rsearch(b._root, 70))
print(b.rsearch(b._root, 30))
b.delete(10)
b.inorder(b._root)