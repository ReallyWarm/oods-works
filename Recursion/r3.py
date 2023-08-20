def keroroJump(distance):
    if distance % 14 == 0:
        return print('Mission Failed')
    total = []
    calcJump(distance, 0, total)
    return print(f'Minimum Distance is {min(total)}\nMaximum Way is {len(total)}')

def calcJump(d, times, t):
    if d == 0:
        return t.append(times)
    for jump in [1,5,7]: 
        if d >= jump and d % 14 != 0:
            calcJump(d-jump,times+1, t) 

d = input('Input number : ')
keroroJump(int(d))