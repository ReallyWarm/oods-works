class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self) -> str:
        return str(self.data)

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
    
    def _insert(self, node, data):
        if node is None:
            return Node(data)
        elif node.data > data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance_factor = self.getBalance(node)

        if balance_factor > 1:
            if node.left.data > data:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
        if balance_factor < -1:
            if node.right.data < data:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)

        return node

    def getHeight(self, node):
        if node is None:
            return 0
        
        return node.height
    
    def getBalance(self, node):
        if node is None:
            return 0
        
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def leftRotate(self, node):
        head = node.right
        tmp = head.left

        head.left = node
        node.right = tmp
        
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        head.height = 1 + max(self.getHeight(head.left), self.getHeight(head.right))

        return head
    
    def rightRotate(self, node):
        head = node.left
        tmp = head.right

        head.right = node
        node.left = tmp

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        head.height = 1 + max(self.getHeight(head.left), self.getHeight(head.right))

        return head
    
    def find(self, node_data):
        return self._find(self.root, node_data)

    def _find(self, node, data):
        if node is None:
            return None
        if node.data == data:
            return node
        if node.data > data:
            return self._find(node.left, data)
        if node.data < data:
            return self._find(node.right, data)
        
    def nodesParent(self):
        root, nodes_parent = self.findParent(self.root)
        return nodes_parent + [[root, None]]
        
    def findParent(self, node):
        if node is None:
            return node, []
        if node.left is None and node.right is None:
            return node, []
        
        left, ll = self.findParent(node.left)
        right, lr = self.findParent(node.right)

        if left is not None:
            ll.append([left, node])
        if right is not None:
            lr.append([right, node])

        return node, ll + lr
    
    def parentLookup(self, nodes_parent, node):
        parent = [nodeparent[1] for nodeparent in nodes_parent if nodeparent[0] is node]
        if parent:
            return parent[0]
        return None
    
    def burnTree(self, node_data):
        start_node = self.find(node_data)
        if start_node is None:
            print(f'There is no {node_data} in the tree.')
            return
        
        nodes_parent = self.nodesParent()
        burn_trails = self._burnTree([[start_node]], set(), nodes_parent)
        print('\n'.join([' '.join([str(node.data) for node in line]) for line in burn_trails]))

    def _burnTree(self, burn_nodes, last_nodes, nodes_parent):
        next = []
        for node in burn_nodes[-1]:
            # print(str(node.data) + ' ', end='')
            if node.left and node.left not in last_nodes:
                next.append(node.left)
            if node.right and node.right not in last_nodes:
                next.append(node.right)
            parent = self.parentLookup(nodes_parent, node)
            if parent and parent not in last_nodes:
                next.append(parent)
        # print()

        if len(next) == 0:
            return burn_nodes
        
        burn_nodes.append(next)
        return self._burnTree(burn_nodes, set(burn_nodes[-2]), nodes_parent)

    def printTree(self, node, level):
        if node is not None:
            self.printTree(node.right, level+1)
            print('       ' * level, str(node.data))
            self.printTree(node.left, level+1)

inp, burn = input('Enter node and burn node : ').split('/')
inp = [int(x) for x in inp.split()]
T = AVL()
for i in inp:
    T.insert(i)
    
# T.printTree(T.root, 0)
T.burnTree(int(burn))