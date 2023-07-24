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
    
inp = input('Enter people and time : ').split(' ')
q_main = Queue()
q_one = Queue(5)
q_two = Queue(5)
min_one = 0
min_two = 0

for data in inp[0]:
    q_main.enqueue(data)

for i in range(1, int(inp[1])+1):
    dq = q_main.dequeue()
    if not q_one.isEmpty():
        min_one += 1
        if min_one%3 == 0:
            q_one.dequeue()
    if not q_two.isEmpty():
        min_two += 1
        if min_two%2 == 0:
            q_two.dequeue()

    if dq is not None:
        if not q_one.isFull():
            q_one.enqueue(dq)
        elif not q_two.isFull():
            q_two.enqueue(dq)

    print(f'{i} {q_main.queue} {q_one.queue} {q_two.queue}')