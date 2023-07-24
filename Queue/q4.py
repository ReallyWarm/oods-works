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
    
inp = input('Enter Input : ').split(',')

my_q = Queue()
ur_q = Queue()
count = 0
for data in inp:
    data = data.split(' ')
    my_q.enqueue(data[0])
    ur_q.enqueue(data[1])
    count += 1

print(f'My   Queue = {", ".join(my_q.queue)}')
print(f'Your Queue = {", ".join(ur_q.queue)}')

activity = {'0':'Eat', '1':'Game', '2':'Learn', '3':'Movie'}
location = {'0':'Res.', '1':'ClassR.', '2':'SuperM.', '3':'Home'}
point = 0

for i in range(count):
    same_activity = False
    same_location = False
    my_act = my_q.dequeue()
    ur_act = ur_q.dequeue()

    if my_act[0] == ur_act[0]:
        same_activity = True
    if my_act[-1] == ur_act[-1]:
        same_location = True

    if same_activity and same_location:
        point += 4
    elif same_activity:
        point += 1
    elif same_location:
        point += 2
    else:
        point -= 5

    my_replace = activity.get(my_act[0]) + ':' + location.get(my_act[-1])
    ur_replace = activity.get(ur_act[0]) + ':' + location.get(ur_act[-1])
    my_q.enqueue(my_replace)
    ur_q.enqueue(ur_replace)

print(f'My   Activity:Location = {", ".join(my_q.queue)}')
print(f'Your Activity:Location = {", ".join(ur_q.queue)}')

if point >= 7:
    print(f'Yes! You\'re my love! : Score is {point}.')
elif point > 0:
    print(f'Umm.. It\'s complicated relationship! : Score is {point}.')
else:
    print(f'No! We\'re just friends. : Score is {point}.')