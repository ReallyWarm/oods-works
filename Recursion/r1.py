def getMax(list):
    if len(list) == 1:
        return int(list[0])
    val = int(getMax(list[1:]))
    if int(list[0]) > val:
        return list[0]
    else:
        return val

inp = input('Enter Input : ').split(' ')
print(f'Max : {getMax(inp)}')