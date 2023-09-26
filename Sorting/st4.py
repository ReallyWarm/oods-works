class Monkey:
    def __init__(self, name, strength, intelligence, agility, id):
        self.name = name
        self.str = strength
        self.int = intelligence
        self.agi = agility
        self.id = id
        
    def __repr__(self) -> str:
        return f'{self.id}-{self.name}'

def sortMonkeys(list, type, order):
    if len(order) > 0:
        order.append('id')

    mergeSort(list, 0, len(list)-1, order, type)

    return list

def mergeSort(list, left, right, order, type):
    if left < right:
        mid = (left+right)//2

        mergeSort(list, left, mid, order, type)
        mergeSort(list, mid+1, right, order, type)
        
        merge(list, left, mid, right, order, type)

def merge(list, left, mid, right, order, type):
    i = j = 0
    k = left

    L = list[left:mid+1]
    R = list[mid+1:right+1]

    while i < len(L) and j < len(R) and len(order) > 0:
        i, j = mergeCondition(list, L, R, i, j, k, order, type)
        k += 1

    while i < len(L):
        list[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        list[k] = R[j]
        j += 1
        k += 1

def mergeCondition(list, ll, rl, il, ir, ik, order, type):
    if type == 'A' or order[0] == 'id':
        condition = ( getattr(ll[il], order[0]) < getattr(rl[ir], order[0]) )
    else:
        condition = ( getattr(ll[il], order[0]) > getattr(rl[ir], order[0]) )

    if ( condition ):
        list[ik] = ll[il]
        il += 1
        return il, ir
    
    elif ( getattr(ll[il], order[0]) == getattr(rl[ir], order[0]) ):
        if len(order) > 1:
            return mergeCondition(list, ll, rl, il, ir, ik, order[1:], type)

    list[ik] = rl[ir]
    ir += 1
    return il, ir

sort_type, order, data  = input("Enter Input: ").split('/')
order = order.split(',')
data = data.split(',')

if order[0] == '':
    order = []

monkeys = list()
for i, m in enumerate(data):
    name, str, intg, agi = m.split(' ')
    monkeys.append(Monkey(name, int(str), int(intg), int(agi), i))

print(sortMonkeys(monkeys, sort_type, order))