def isp(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        return isp(x + 1, y) + isp(x * 2, y) + isp(2 * x + 1, y) + isp(x * 10, y)


print(isp(1, 15))