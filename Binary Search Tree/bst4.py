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
    
    def preorder(self):
        return self.npreorder(self.root)

    def npreorder(self, node):
        data = str(node.data) + ' '
        if node.left is not None:
            data += self.npreorder(node.left)
        if node.right is not None:
            data += self.npreorder(node.right)

        return data
    
    def inorder(self):
        return self.ninorder(self.root)
    
    def ninorder(self, node):
        data = str(node.data)
        if node.left is not None:
            data = self.ninorder(node.left) + ' ' + data
        if node.right is not None:
            data = data + ' ' + self.ninorder(node.right)

        return data
    
    def postorder(self):
        return self.npostorder(self.root)
    
    def npostorder(self, node):
        data = ''
        if node.left is not None:
            data += self.npostorder(node.left) + ' '
        if node.right is not None:
            data += self.npostorder(node.right) + ' '

        return data + str(node.data)
    
    def breadth(self):
        queue = [self.root]
        data = ''

        while len(queue):
            node = queue.pop(0)
            data += str(node.data) + ' '

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return data

inp = [int(i) for i in input('Enter Input : ').split(' ')]
T = BST()
for i in inp:
    T.insert(i)
print('Preorder :', T.preorder())
print('Inorder :', T.inorder())
print('Postorder :', T.postorder())
print('Breadth :', T.breadth())

'''
Enter Input : 10 4 20 1 5
Preorder : 10 4 1 5 20 
Inorder : 1 4 5 10 20 
Postorder : 1 5 4 20 10 
Breadth : 10 4 20 1 5 
'''