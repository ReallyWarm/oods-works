def increase_subsequence(arr):
    longest = 1
    sub = [arr[0]]
    print(f'{1} : {sub}')

    for i in range(1, len(arr)):
        while len(sub) > 0:
            if sub[-1] < arr[i]:
                break
            sub = sub[:-1]
        sub.append(arr[i])

        if len(sub) > longest:
            longest = len(sub)

        print(f'{i+1} : {sub}')
    print('longest increasing subsequence :', longest)

inp = [int(x) for x in input('Data : ').split(' ')]
increase_subsequence(inp)