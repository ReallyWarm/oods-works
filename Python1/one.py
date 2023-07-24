def to_sec(lst):
    lst = [int(n) for n in lst]
    if lst[1] > 59 or lst[1] < 0:
        print(f"mm({lst[1]}) is invalid!")
        return
    elif lst[2] > 59 or lst[2] < 0:
        print(f"ss({lst[2]}) is invalid!")
        return
    sec = lst[0] * 3600
    sec += lst[1] * 60
    sec += lst[2]
    print(f"{lst[0]:02d}:{lst[1]:02d}:{lst[2]:02d} = {sec:,} seconds")

print("*** Converting hh.mm.ss to seconds ***")
inp = input('Enter hh mm ss : ').split(' ')
to_sec(inp)