def draw(n):
    half_rows = n+2
    for i in range(half_rows):
        if i < n+1:
            print('.'*(n+1-i), end='')

        print('#'*(min(i+1, half_rows)), end='')

        if i == 0 or i+1 == half_rows:
            print('+'*half_rows, end='')
        else:
            print('+', end='')
            print('#'*n, end='')
            print('+', end='')
        print()

    for i in range(half_rows):
        if i == 0 or i+1 == half_rows:
            print('#'*half_rows, end='')
        else:
            print('#', end='')
            print('+'*n, end='')
            print('#', end='')

        print('+'*(half_rows-i), end='')

        print('.'*i, end='')
      
        print()

inp = input('Enter Input : ')
draw(int(inp))