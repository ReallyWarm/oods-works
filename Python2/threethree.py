def new_range(a, b=None, c=None):
    step = 1 if c is None else c
    start = 0 if b is None else a
    end = a if b is None else b
    
    rge = []
    start_decimal = str(start)[::-1].find('.')
    end_decimal = str(end)[::-1].find('.')
    step_decimal = str(step)[::-1].find('.')
    max_decimal = max(step_decimal, max(start_decimal, end_decimal))

    while start < end:
        rge.append(start)
        start += step
        
        if str(start)[::-1].find('.') > max_decimal:
            start = float(f'{start:.{max_decimal}f}')

    return rge 

print('*** New Range ***')
inp = input('Enter Input : ').split()

inp = [float(x) for x in inp]
while len(inp) < 3:
    inp.append(None)

rge = new_range(inp[0], inp[1], inp[2])
rge = [f'{n}.0' if len(str(n).split('.')) < 2 else f'{n}' for n in rge]

print(f'({", ".join(rge)})')