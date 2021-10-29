def may(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        return may(x + 1, y) + may(x + 3, y)


print(may(1, 8) * may(8, 15))
