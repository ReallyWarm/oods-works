def add_list(lst, data):
    if data not in lst:
        lst.append(data)

print(' *** String count ***')
inp = input('Enter message : ')

alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upcase = []
upcase_num = 0
lowcase = []
lowcase_num = 0
for c in inp:
    if c in alp:
        add_list(upcase, c)
        upcase_num += 1
    elif c in alp.lower():
        add_list(lowcase, c)
        lowcase_num += 1

print(f'No. of Upper case characters : {upcase_num}')
print(f'Unique Upper case characters : {"  ".join(sorted(upcase))}')
print(f'No. of Lower case Characters : {lowcase_num}')
print(f'Unique Lower case characters : {"  ".join(sorted(lowcase))}')