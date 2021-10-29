
for i in range(30001, 70001):
    s = []
    count = 0
    n = 1
    while n <= 17:
        if i % n == 0:
            n += 1
        count += 1
    print(i, count)
