class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.all_digit = True

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        conj = ' <-> ' if self.all_digit else ' > '
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s += conj + str(cur.next.value)
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if not item.isdigit():
            self.all_digit = False
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node

    def nextNode(self, node, times):
        if node == None:
            return None
        elif times == 0:
            return node
        return self.nextNode(node.next, times-1)

    def reverseGroup(self, size):

        def reverse(first_node, last_node):
            cur = first_node
            prev = None
            while cur != None and cur != last_node:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
        
        prev = None
        cur = self.head
        next_group = self.nextNode(self.head, size)
        self.head = reverse(self.head, next_group)
        while next_group:
            prev = cur
            cur = next_group
            next_group = self.nextNode(next_group, size)
            next_node = reverse(cur, next_group)
            prev.next = next_node

l, s = input('Enter the elements of Linked list/group\'s size: ').split('/')
l = l.split(' ')
llist = LinkedList()
for i in l:
    if i:
        llist.append(i)
error = False
if llist.isEmpty():
    print('No elements in Linked List ? OK!')
    error = True
if int(s) <= 0:
    print('Group\' size should be greater than 0')
    error = True
if not error:
    print(f'\nOriginal Linked list: {llist}')
    llist.reverseGroup(int(s))
    print(f'Modified Linked list: {llist}')