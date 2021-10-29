s = 0
n = 0
for i in range(1, 1320 + 1):
    s = i
    n = 24
    while s <= 1320:
        s = s + 5
        n = n + 14
    if (n == 542):
        print(n, ' ', i)
