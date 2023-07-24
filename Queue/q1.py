class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0
    
def display(queue):
    if queue.isEmpty():
        print('Empty')
    else:
        print(', '.join(queue.queue))
    
inp = input('Enter Input : ').split(',')
q = Queue()
data_dequeued = []
for i in inp:
    if i[0] == 'E':
        q.enqueue(i[-1])
        display(q)

    elif i[0] == 'D':
        if q.isEmpty():
            print('Empty')
        else:
            dq = q.dequeue()
            data_dequeued.append(dq)
            print(dq, end='')
            print(' <- ', end='')
            display(q)

if len(data_dequeued) > 0:
    print(', '.join(data_dequeued), end='')
else:
    print('Empty', end='')
print(' : ', end='')
display(q)