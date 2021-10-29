for i in range(568023, 569231):
    s = []
    sch = 0
    for x in range(1, i + 1):
        if i % x == 0:
            s.append(x)
print(s)
