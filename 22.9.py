# x = int(input())
for x in range(1, 1000):
    a = 0
    b = 0
    d = x
    while x > 0:
        if x % 2 == 0:
            a += 1
        else:
            b += x % 6
        x = x // 6
    if a == 2 and b == 4:
        print(d, a, b)

# print(a, b)
