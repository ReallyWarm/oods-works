def getChocolate(money, price, wrap):
    return (money//price) + getBonusChocolate(0, money//price, wrap)

def getBonusChocolate(bonus, quantity, wrap):
    if quantity < wrap:
        return bonus
    return getBonusChocolate(bonus+(quantity//wrap), (quantity%wrap)+(quantity//wrap), wrap)

m, p, w = map(lambda x: int(x), input('Enter m, p, w: ').split(' '))
print(getChocolate(m, p, w))