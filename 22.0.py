# x = int(input())
s = 0
for y in range(1, 999999):
    a = 0
    b = 1
    x=y
    while x > 0:
        a = a + 1
        if x % 8 != 0:
            b = b * (x % 8)
        x = x // 8
    if a == 3 and b == 24:
        s += 1
            # print(a)
            # print(b)
        print(a,b,y)
print(s)