class Queue:
    def __init__(self, max_size = None):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, item):
        if not self.isFull():
            self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.queue)
    
    def isFull(self):
        return self.size() == self.max_size
    
inp = input('Enter Input : ').split('/')
inshelf = inp[0].split(' ')
action = inp[1].split(',')

shelf = Queue()
for book in inshelf:
    shelf.enqueue(book)

for i in action:
    if i[0] == 'E':
        shelf.enqueue(i[2:])
        
    elif i[0] == 'D':
        shelf.dequeue()

result = []
duplicate = False
while not shelf.isEmpty():
    book_num = shelf.dequeue()
    if book_num in result:
        duplicate = True
        break
    result.append(book_num)

if not duplicate:
    print('NO ', end='')
print('Duplicate')