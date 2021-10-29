def m17(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        return m17(x + 1, y) + m17(x + 2, y) + m17(x * 3, y)


print(m17(2, 8) * m17(8, 10) * m17(10, 12))