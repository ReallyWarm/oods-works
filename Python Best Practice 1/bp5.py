class MyInt():
    roman = {"M":1000, "CM":900, "D":500, "CD":400,
                 "C":100, "XC":90, "L":50, "XL":40,
                 "X":10, "IX":9, "V":5, "IV":4, "I":1}
    
    def __init__(self, value) -> None:
        self.value = value

    def toRoman(self) -> str:
        tmp_val = self.value
        roman_str = ""
        for symbol, val in self.roman.items():
            while tmp_val >= val:
                tmp_val = tmp_val - val
                roman_str += symbol
        return roman_str
    
    def __add__(self, other) -> int:
        return int((self.value + other.value) * 3 // 2)

print(' *** class MyInt ***')
inp = input('Enter 2 number : ').split(' ')

a = MyInt(int(inp[0]))
b = MyInt(int(inp[1]))

print(f'{a.value} convert to Roman : {a.toRoman()}')
print(f'{b.value} convert to Roman : {b.toRoman()}')

print(f'{a.value} + {b.value} = {a+b}')