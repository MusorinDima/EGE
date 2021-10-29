# x = int(input())
for x in range(1, 100):
    a = 0
    b = 1
    c = x
    while x > 0:
        a += 1
        b *=x % 10
        x //=  10
    if a == 2 and b == 0:
        print(c)
# print(a)
# print(b)