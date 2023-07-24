def draw(n):
    rows = n*2+(n-1)*2-1
    for i in range(n*2 - 1):
        for j in range(i):
            if j % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')

        if i % 2 == 0:
            print('#'*(rows-i*2), end='')
        else:
            print('.'*(rows-i*2), end='')

        for k in range(i,i*2):
            if k % 2 == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()

    for i in range(n*2 - 2):
        for j in range(n*2 - 2 - i):
            if j % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')

        if i % 2 == 0:
            print('.'*(i*2+1), end='')
        else:
            print('#'*(i*2+1), end='')

        for k in range(i, n*2 - 2):
            if k % 2 == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()

print('*** Fun with Drawing ***')
inp = input('Enter input : ')
draw(int(inp))