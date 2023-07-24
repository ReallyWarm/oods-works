def weirdSubtract(n,k):
    for i in range(k):
        if n > 0:
            if n % 10 == 0:
                n = int(str(n)[:-1])
            else:
                n -= 1

    return n
        

n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))