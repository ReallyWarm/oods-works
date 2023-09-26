def insertMinHeap(h, i):
    root = (i-1) // 2
    insert = h[i]

    while root >= 0 and insert < h[root]:
        h[root], h[i] = h[i], h[root]
        i = root
        insert = h[root]
        root = (root-1) // 2

def delMin(h, last):
    print(f'deleteMin = {h[0]} FindPlaceFor {h[last]}')
    h[0], h[last] = h[last], h[0]
    root = 0
    left = root * 2 + 1
    right = root * 2 + 2
    replace = h[root]

    while left < last:
        right = left if right == last else right
        min = left if h[left] < h[right] else right

        if replace > h[min]:
            h[root], h[min] = h[min], h[root]
            root = min
        else:
            break

        left = root * 2 + 1
        right = root * 2 + 2
        replace = h[root]

    print(' '.join([str(num) for num in h]))

h = []
a = input("Enter list of number: ").split(",")
for i in range(len(a)):
    h.append(int(a[i]))
    insertMinHeap(h, i)

print("Heap: ", end="")
print(*h)
print("==== heap sort ====")
for last in range(len(h)-1, 0, -1):
    delMin(h, last)
print("==== Sorting a ====")
h.reverse()
print(*h)