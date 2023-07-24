def move2_right(string):
    last2 = string[-2:]
    return last2 + string[:-2] 

def move3_left(string):
    first3 = string[:3]
    return string[3:] + first3

print('*** String Rotation ***')
inp = input('Enter 2 strings : ').split(' ')

str1 = move2_right(inp[0])
str2 = move3_left(inp[1])
count = 1
while str1 != inp[0] or str2 != inp[1]:
    if count <= 5:
        print(f'{count} {str1} {str2}')
    str1 = move2_right(str1)
    str2 = move3_left(str2)
    count += 1
if count > 5:
    print(' . . . . . ')
print(f'{count} {str1} {str2}')
print(f'Total of  {count} rounds.')
    