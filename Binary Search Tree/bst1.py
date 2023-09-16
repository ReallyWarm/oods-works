class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)