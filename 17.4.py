# s = [7, 17, 37, 47, 57]
# sum = 0
# n = 0
# for i in range(12345, 23456):
#     count = 0
#     d = []
#
#     for x in s:
#         if i % x == 0:
#             sum += i
#             d.append(x)
#             count += 1
#         if count == 2:
#             n += 1
#             print(i, d, sum, n)

# for i in range(12345, 23456):
#     count = 0
#     for x in (7, 17, 37, 47, 57):
#         if i % x == 0:
#             count += 1
#         if count == 2:
#             print(i, x, count)
s = 0
c = 0
for i in range(12345, 23456):

    count = 0
    if i % 7 == 0:
        count += 1
    if i % 17 == 0:
        count += 1
    if i % 37 == 0:
        count += 1
    if i % 47 == 0:
        count += 1
    if i % 57 == 0:
        count += 1
    if count == 2:
        s += i
        c += 1
print(s, c)











