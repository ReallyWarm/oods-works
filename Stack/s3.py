class Stack:
    def __init__(self):
        self.items = []

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
    
def precedence(i):
    return 3 if (i == '^') else 2 if (i == '*' or i == '/') else 1 if (i == '+' or i == '-') else -1
    
inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')

for i in inp:
    if i.isalpha():
        print(i, end='')

    elif i == '(':
        S.push(i)

    elif i == ')':
        while not S.isEmpty() and S.items[-1] != '(':
            print(S.pop(), end='')
        if not S.isEmpty() and S.items[-1] == '(':
            S.pop()

    else:
        while not S.isEmpty() and precedence(i) <= precedence(S.items[-1]):
            print(S.pop(), end='')
        S.push(i)

while not S.isEmpty():

    print(S.pop(), end='')

print()