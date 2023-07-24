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
    
def find_exit(w, h, map):
    if len(map) != h:
        print('Invalid map input.')
        return
    for row in map:
        if len(row) != w:
            print('Invalid map input.')
            return
        
    q = Queue()
    found_end = False
    for y in range(h):
        for x in range(w):
            if map[y][x] == 'F':
                q.enqueue((x,y))
                print(f'Queue: {q.queue}')
                map[y][x] = '#'
            if map[y][x] == 'O':
                found_end = True

    if q.isEmpty():
        print('Invalid map input.')
        return
    if not found_end:
        print('Cannot reach the exit portal.')
        return
        
    vector = [[0,-1], [1,0], [0,1], [-1,0]]
    while not q.isEmpty():
        pos = q.dequeue()
        for v in vector:
            nx = pos[0] + v[0]
            ny = pos[1] + v[1]
            if (ny >= 0 and nx >= 0 and ny < h and nx < w):
                if map[ny][nx] == '_':
                    q.enqueue((nx,ny))
                    map[ny][nx] = '#'
                elif map[ny][nx] == 'O':
                    print('Found the exit portal.')
                    return
        if not q.isEmpty():
            print(f'Queue: {q.queue}')
    print('Cannot reach the exit portal.')

w, h, map = input('Enter width, height, and room: ').split(' ')
map = [[col for col in row] for row in map.split(',')]
find_exit(int(w),int(h),map)