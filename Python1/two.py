def sum_or_multi(lst):
    lst = [int(n) for n in lst]
    result = lst[0] * lst[1]
    if result > 1000:
        return lst[0] + lst[1]
    else:
        return result

print('*** multiplication or sum ***')
inp = input('Enter num1 num2 : ').split(' ')
print(f'The result is {sum_or_multi(inp)}')