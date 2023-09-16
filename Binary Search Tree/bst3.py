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

    def levelInsert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)

            if node.left is None:
                node.left = Node(data)
                return
            else:
                queue.append(node.left)
            
            if node.right is None:
                node.right = Node(data)
                return
            else:
                queue.append(node.right)

    def maxPath(self):
        all_path = self.allPath(self.root)

        max_path = all_path[0]
        for path in all_path:
            max_path = path if sum(max_path) < sum(path) else max_path

        return max_path
    
    def allPath(self, node):
        if node.left is None and node.right is None:
            return [[node.data]]
        
        paths = []
        if node.left:
            for path in self.allPath(node.left):
                paths.append([node.data] + path)

        if node.right:
            for path in self.allPath(node.right):
                paths.append([node.data] + path)

        return paths
          
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

inp = [int(i) for i in input('Enter tree: ').split(' ')]
T = BST()
for i in inp:
    T.levelInsert(i)
print('Maximum path:', T.maxPath())
