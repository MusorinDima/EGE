# x = int(input())
# s = []
# for x in range(100,1000000):
#     a = 0
#     b = 0
#     while x > 0:
#         if x % 2 == 0:
#             a += 1
#         else:
#             b += 1
#         x //= 10
#     if a == 2 and b == 3:
#         s.append(x)
#
# print(a, b, s)

for x in range(1, 999999 + 1):
    a = 0
    b = 0

    s = x
    while x > 0:

        if x % 2 == 0:
            a += 1
        else:
            b += 1
        # print(a,b,x)

        x //= 10
    if a == 2 and b == 3:


        print(a,b,s)

