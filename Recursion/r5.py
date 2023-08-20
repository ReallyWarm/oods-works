def staircase(n, m):
    if n == 0:
        return 'Not Draw!'

    if n == 1 or n == -1:
        return '#'*abs(m) + '\n'
    
    x = 1 if m > 0 else -1
    p = '_'*(x*(n-x))+'#'*(x*(m-n+x)) + '\n'

    if m > 0:
        return p + staircase(n-x, m)
    else: 
        return staircase(n-x, m) + p

m = int(input("Enter Input : "))
print(staircase(m, m))