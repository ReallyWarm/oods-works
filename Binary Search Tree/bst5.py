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
        if node.data <= data:
            node.right = self.ninsert(node.right, data)

        return node
    
    def printTree(self):
        print('\n'.join(self.layerPrint(self.root)[0]))

    def layerPrint(self, node):
        if node is None:
            return [], 0, 0, 0, 0
        
        if node.left is None and node.right is None:
            layer_of_string = [str(node.data)]
            data_length = len(str(node.data))
            layer_width = len(str(node.data))
            data_position = 0
            layer_height = 1
            return layer_of_string, data_length, layer_width, data_position, layer_height
        
        left, ld, lw, lp, lh = self.layerPrint(node.left)
        right, rd, rw, rp, rh = self.layerPrint(node.right)

        data, dw = str(node.data), len(str(node.data))
        data_layer = ' '*(lw+(lw>0)) + data + ' '*(rw+(rw>0))
        branch_layer = ' '*(lp+ld) + '_'*(lw-lp-ld) + '/'*(lw>0) + ' '*dw + '\\'*(rw>0) + '_'*(rp) + ' '*(rw-rp)
        zip_layer = zip(left + [' '*lw]*(rh-lh), right + [' '*rw]*(lh-rh))
        leaf_layer = [l + ' '*(dw+(lw>0)+(rw>0)) + r for l, r in zip_layer]
        
        return [data_layer, branch_layer] + leaf_layer, dw, lw+rw+dw+(lw>0)+(rw>0), lw+(lw>0), max(lh,rh)+2         

inp = [int(i) for i in input('Enter input: ').split(' ')]
T = BST()
for i in inp:
    T.insert(i)
T.printTree()

'''
                  100                
                 /   \________       
               90             120    
  ____________/          ____/   \   
60                    110         130
  \                      \           
   70                     110        
     \___                            
         75                          
        /  \                         
      74    76                       
'''