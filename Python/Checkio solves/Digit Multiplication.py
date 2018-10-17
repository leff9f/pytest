def checkio(number: int) -> int:
    x = 1
    for i in str(number):
        if i != '0':
            x *= int(i)
    return x


checkio(123405)
