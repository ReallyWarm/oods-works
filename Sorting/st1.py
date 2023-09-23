def bubble_sort(list, show_step=True):
    move_count = 0
    for i in range(len(list)):
        move = None

        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                move = list[j]
                list[j] = list[j+1]
                list[j+1] = move

        if not move or j == 0:
            if show_step: print(f'last step : {list} move[{move}]') 
            break

        move_count += 1
        if show_step: print(f'{move_count} step : {list} move[{move}]')
        
inp = [int(n) for n in input("Enter Input : ").split()]
bubble_sort(inp)