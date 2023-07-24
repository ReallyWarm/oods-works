def hbd(age):
    base = age // 2
    saimai_age = 20 + (age % 2)
    return f'saimai is just {saimai_age}, in base {base}!'

year = input("Enter year : ")

print(hbd(int(year)))