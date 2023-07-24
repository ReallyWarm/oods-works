class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            self.items.pop()

    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)
    
inp = input("Enter expresion : ")

s = Stack()
close_excess = False
unmatched = False
for i in inp:
    if i in ['(',')','[',']','{','}']:

        if i in [')', ']', '}']:
            if s.isEmpty():
                close_excess = True
                break
            elif (s.items[-1] == '(' and i == ')' or s.items[-1] == '[' and i == ']' or s.items[-1] == '{' and i == '}'):
                s.pop()
            else:
                unmatched = True
                break
        else:
            s.push(i)

if close_excess:
    print(f'{inp} close paren excess')
elif unmatched:
    print(f'{inp} Unmatch open-close')
elif s.isEmpty():
    print(f'{inp} MATCH')
else:
    print(f'{inp} open paren excess   {s.size()} : {"".join(s.items)}')
