def nameValue(val):
    return sum([ord(s) for s in str(val)])

class TreeNode(object):
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):

    def insert(self, root, data):
        val_data = nameValue(data)
        if root is None:
            return TreeNode(data)
        elif nameValue(root.key) > val_data:
            root.left = self.insert(root.left, data) 
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance_factor = self.getBalance(root)

        if balance_factor > 1:
            if nameValue(root.left.key) > val_data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balance_factor < -1:
            if nameValue(root.right.key) < val_data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def delete(self, root, data):
        val_data = nameValue(data)
        if root is None:
            return None
        elif nameValue(root.key) > val_data:
            root.left = self.delete(root.left, data) 
        elif nameValue(root.key) < val_data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                tmp = root.right
                root = None
                return tmp
            elif root.right is None:
                tmp = root.left
                root = None
                return tmp
            else:
                tmp = self.getMinValueNode(root.right)
                root.key = tmp.key
                root.right = self.delete(root.right, tmp.key)

        if root is None:
            return None
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance_factor = self.getBalance(root)

        if balance_factor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balance_factor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        h = z.right
        tmp = h.left

        h.left = z
        z.right = tmp

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        h.height = 1 + max(self.getHeight(h.left), self.getHeight(h.right))
        
        return h

    def rightRotate(self, z):
        h = z.left
        tmp = h.right

        h.right = z
        z.left = tmp

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        h.height = 1 + max(self.getHeight(h.left), self.getHeight(h.right))
        
        return h

    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    def getBalance(self, root):
        if root is None:
            return 0
        
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def printTree(self, root, level=0):
        if root is not None:
            print('    '*level + f'{root.key} ({nameValue(root.key)})')
            if root.left is not None and root.right is not None:
                self.printTree(root.left, level+1)
                self.printTree(root.right, level+1)
            elif root.left is not None:
                self.printTree(root.left, level+1)
                print('    '*(level+1) + '*')
            elif root.right is not None:
                print('    '*(level+1) + '*')
                self.printTree(root.right, level+1)

avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    if op == "I":
        root = avl_tree.insert(root, data)
    elif op == "D":
        root = avl_tree.delete(root, data)
    elif op == "P":
        avl_tree.printTree(root)
        print("------------------------------")