def putin_boxes(items_weight, num_box, capacity):
    it = 0
    ib = 0
    size_items = len(items_weight)
    box = [[] for _ in range(num_box)]

    while it < size_items:
        if sum(box[ib]) + items_weight[it] > capacity:
            ib += 1
        if ib >= num_box:
            return False
        box[ib].append(items_weight[it])
        it += 1

    return True if it == size_items else False

def item_boxes(items_weight, num_box):
    sum_w = sum(items_weight)
    min_w = sum_w//num_box

    max_w = max(items_weight)
    min_w = max_w if min_w < max_w else min_w

    done = False
    while not done:
        done = putin_boxes(items_weight, num_box, min_w)
        if not done: min_w += 1

    return min_w

inp = input('Enter Input : ').split('/')
arr, n = [int(x) for x in inp[0].split()], int(inp[1])
weight = item_boxes(arr, n)
print(f'Minimum weigth for {n} box(es) =', weight)