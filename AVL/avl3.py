class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class CompleteBT:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data) 
            return
        
        queue = [self.root]
        while len(queue):
            node = queue.pop(0)

            if node.left is None:
                node.left = Node(data)
                return
            if node.right is None:
                node.right = Node(data)
                return

            queue.append(node.left)
            queue.append(node.right)

    def maiYab(self, num_nodes, values):
        if len(values) != num_nodes//2 + 1:
            return 'Incorrect Input'

        insert = [0]*(num_nodes-len(values)) + values      
        for i in insert:
            self.insert(i)
        _, all_sum = self.crossMaiYab(self.root)
        return all_sum

    def crossMaiYab(self, node):
        if node.left is None and node.right is None:
            return node.data, 0
        
        left, lsum = self.crossMaiYab(node.left)
        right, rsum = self.crossMaiYab(node.right)
        min_data = min(left, right)

        return min_data, min_data + (node.left.data-min_data) + (node.right.data-min_data) + lsum + rsum

num_nodes, inp = input('Enter Input : ').split('/')
CBT = CompleteBT()
print(CBT.maiYab(int(num_nodes), [int(n) for n in inp.split()]))

'''
      0                 0                 1      
   __/ \__           __/ \__           __/ \__   
  0       0   -->   1       3   -->   0       2  
 / \     / \       / \     / \       / \     / \ 
1   2   3   4     0   1   0   1     0   1   0   1
'''