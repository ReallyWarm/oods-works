class StackCalc:
    def __init__(self):
        self.items = []
        self.invaild_instruction = ''

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
    
    def add(self):
        a = self.pop()
        b = self.pop()
        self.push(a + b)

    def subtract(self):
        a = self.pop()
        b = self.pop()
        self.push(a - b)

    def multiply(self):
        a = self.pop()
        b = self.pop()
        self.push(a * b)

    def divide(self):
        a = self.pop()
        b = self.pop()
        self.push(a // b)

    def duplicate(self):
        self.push(self.top())
    
    def run(self, data):
        for arg in data.split(' '):
            if arg.isdecimal():
                self.push(int(arg))

            elif arg == '+':
                self.add()

            elif arg == '-':
                self.subtract()

            elif arg == '*':
                self.multiply()
            
            elif arg == '/':
                self.divide()

            elif arg == 'DUP':
                self.duplicate()

            elif arg == 'POP':
                self.pop()

            elif arg == 'PSH':
                self.duplicate()

            else:
                self.invaild_instruction = arg
                break

    def getValue(self):
        if self.invaild_instruction != '':
            return f'Invalid instruction: {self.invaild_instruction}'
        elif self.isEmpty():
            return 0
        return self.top()

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())