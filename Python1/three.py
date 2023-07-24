def sum_digit(str):
    if len(str) > 30:
        return -1
    return sum([int(n) for n in str])

print(' *** Summation of each digit ***')
inp = input('Enter a positive number : ')
sd = sum_digit(inp)
if (sd != -1):
    print(f'Summation of each digit =  {sd}')
else:
    print('?')