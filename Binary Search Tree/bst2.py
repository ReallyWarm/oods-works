class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.ninsert(self.root, data)
        return self.root
    
    def ninsert(self, node, data):
        if not node:
            return Node(data)
        if node.data > data:
            node.left = self.ninsert(node.left, data)
        if node.data < data:
            node.right = self.ninsert(node.right, data)
            
        return node
    
    def getHight(self):
        return self.ngetHeight(self.root)
    
    def ngetHeight(self, node):
        if not node:
            return -1
        
        left = self.ngetHeight(node.left)
        right = self.ngetHeight(node.right)

        if left > right:
            return left + 1
        else:
            return right + 1
    
inp = [int(i) for i in input('Enter Input : ').split(' ')]
T = BST()
for i in inp:
    T.insert(i)
print('Height of this tree is :', T.getHight())