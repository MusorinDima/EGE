for i in range(95632, 95651):
    s = []
    for x in range(1, i + 1):
        if x % 2 != 0:
            if i % x == 0:
                s.append(x)
    if len(s) == 6:
        print(s)
