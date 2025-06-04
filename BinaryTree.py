from queueLinkedlist import queueLinkedlist

class _Node:
    __slots__ = '_element', '_left', '_right'
    
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right
        
class binaryTree:
    def __init__(self):
        self._root = None
        
    def makeTree(self, e, left, right):
        self._root = _Node(e, left._root, right._root)
        
    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end=" ")
            self.inorder(troot._right)
        
    def preorder(self, troot):
        if troot:
            print(troot._element, end=" ")
            self.preorder(troot._left)
            self.preorder(troot._right)
            
    def postorder(self, troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element, end=" ")
    
    def levelorder(self, troot):
        Q = queueLinkedlist()
        t = self._root
        print(t._element, end=" ")
        Q.enqueue(t)
        while not Q.isEmpty():
            t = Q.dequeue()
            if t._left:
                print(t._left._element, end=" ")
                Q.enqueue(t._left)
            if t._right:
                print(t._right._element, end=" ")
                Q.enqueue(t._right)
                
    def count(self, troot):
        if troot:
            x = self.count(troot._left)
            y = self.count(troot._right)
            return x + y + 1
        return 0
    
    def height(self, troot):
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0
            
x = binaryTree()
y = binaryTree()
z = binaryTree()
r = binaryTree()
s = binaryTree()
t = binaryTree()
n = binaryTree()

x.makeTree(40, n, n)
y.makeTree(60, n, n)
r.makeTree(50, n, y)
z.makeTree(20, x, n)
s.makeTree(30, r, n)
t.makeTree(10, z, s)
t.inorder(t._root)
print()
t.postorder(t._root)
print()
t.preorder(t._root)
print()
t.levelorder(t._root)
print()
print("count:", t.count(t._root))
print(t.height(t._root)-1)