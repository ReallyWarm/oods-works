class node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.snext = None

class Snode:
    def __init__(self, data):
        self.value = data
        self.snext = None

class link:
    def __init__(self):
        self.head = None

    def next_node(self, data):
        if self.head == None:
            self.head = data
            return
        
        if self.search(data.value):
            return
        
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = data
    
    def search(self, data):
        cur = self.head
        while cur != None:
            if cur.value == data:
                return cur
            cur = cur.next
        return None
    
    def next_secondary_node(self, n, data):
        cur = self.search(n)
        if cur == None:
            return
        while cur.snext != None:
            cur = cur.snext
        cur.snext = data
    
    def show_all(self):
        cur = self.head
        scur = None
        s = ''
        while cur != None:
            s += str(cur.value) + ' : '
            scur = cur.snext
            while scur != None:
                s += str(scur.value) + ','
                scur = scur.snext
            cur = cur.next
            s += '\n'
        print(s)

inp = input("input : ").split(",")
l = link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0],Snode(h[1]))
l.show_all()
