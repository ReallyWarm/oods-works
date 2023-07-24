def get_divider(num):
    divider = [1]
    add_list(divider,int(num))
    tmp = num
    for i in range(2,num//2):
        if tmp % i == 0:
            add_list(divider,int(i))
            while tmp % i == 0:
                tmp /= i
                add_list(divider,int(tmp))
        tmp = num

    return divider

def add_list(lst, num):
    if num not in lst:
        lst.append(num)

print(' *** Divisible number ***')
inp = int(input('Enter a positive number : '))
if inp <= 0:
    print(f'{inp} is OUT of range !!!')
else:
    lst = sorted(get_divider(inp))
    print(f'Output ==> {" ".join([str(n) for n in lst])}')
    print(f'Total ==> {len(lst)}')
