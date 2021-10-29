count = 0
s = []
for i in range(7525, 13487):
    if i % 7 == 0 and i % 6 != 0 and i % 9 != 0 and i % 14 != 0 and i % 21 != 0:
        count += 1
        s.append(i)
print(count, min(s))

