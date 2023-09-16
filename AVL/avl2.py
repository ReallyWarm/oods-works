class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self,node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        if data > node.data:
            node.right = self._insert(node.right, data)

        return node
    
    def closestValue(self, value):
        return self._closestValue(self.root, value, self.root.data)

    def _closestValue(self, node, value, closest):
        if node is None:
            return closest
        if node.data == value:
            return node.data
        
        if abs(node.data - value) == abs(closest - value):
            closest = max(node.data, closest)
        elif abs(node.data - value) < abs(closest - value):
            closest = node.data

        if value < node.data:
            return self._closestValue(node.left, value, closest)
        else:
            return self._closestValue(node.right, value, closest)
    
    def printInsert(self, data):
        self.insert(data)
        self.printTree(self.root, 0)
        print('--------------------------------------------------')

    def printTree(self, node, level):
        if node is not None:
            self.printTree(node.right, level+1)
            print('     ' * level, str(node.data))
            self.printTree(node.left, level+1)
    
inp, find = input('Enter Input : ').split('/')
inp = [int(n) for n in inp.split()]
T = BST()
for i in inp:
    T.printInsert(i)
print(f'Closest value of {find} : {T.closestValue(int(find))}')