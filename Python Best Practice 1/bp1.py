def class_speed(speed):
    if speed < 0:
        return -1
    if 0.00 <= speed <= 51.99:
        return 'Breeze'
    elif 52.00 <= speed <= 55.99:
        return 'Depression'
    elif 56.00 <= speed <= 101.99:
        return 'Tropical Storm'
    elif 102.00 <= speed <= 208.99:
        return 'Typhoon'
    elif 209.00 <= speed:
        return 'Super Typhoon'

print(' *** Wind classification ***')
inp = input('Enter wind speed (km/h) : ')
result = class_speed(float(inp))
if result == -1:
    print('!!!Wrong value can\'t classify.')
else:
    print(f'Wind classification is {result}.')
