class Stack:
    def __init__(self):
        self.items = []

    def top(self):
        return self.items[-1]

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.items.pop()

    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)
    
def hallucinations(value):
    if value % 2 == 0:
        if value > 1:
            value -= 1
    else:
        value += 2
    return value
    
inp = input("Enter Input : ")

s = Stack()
for i in inp.split(','):
    if i[0] == 'A':
        value = int(i.split()[1])
        s.push(value)

    elif i[0] == 'B':
        look_s = Stack()
        count = 0
        top_heights = 0
        while not s.isEmpty():
            look_s.push(s.pop())
            if top_heights < look_s.top():
                top_heights = look_s.top()
            if s.isEmpty():
                count += 1
            elif s.top() > top_heights:
                count += 1

        while not look_s.isEmpty():
            s.push(look_s.pop())

        print(count)

    elif i[0] == 'S':  
        tmp_s = Stack()
        while not s.isEmpty():
            value = hallucinations(s.pop())
            tmp_s.push(value)

        while not tmp_s.isEmpty():
            s.push(tmp_s.pop())
        