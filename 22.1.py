# x = int(input())
y = 0
while True:
    a = 0
    b = 1

    y += 1
    x = y
    while x > 0:
        a += 1
        b *= x % 10
        x = x // 10

    if a == 3 and b == 7:
        print(a, b, y)

# print(a)
# print(b)

