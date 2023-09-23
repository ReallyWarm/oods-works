def somethingDrome(list):
    ascend = False
    descend = False
    repeat = False

    for i in range(len(list)-1):
        if list[i] < list[i+1]:
            ascend = True
        elif list[i] > list[i+1]:
            descend = True
        else:
            repeat = True
        
        if ascend and descend:
            return "Nondrome"
        
    if ascend:
        if repeat: return "Plaindrome"
        return "Metadrome"
    
    if descend:
        if repeat: return "Nialpdrome"
        return "Katadrome"
    
    return "Repdrome"

inp = [int(n) for n in input("Enter Input : ")]
print(somethingDrome(inp))
