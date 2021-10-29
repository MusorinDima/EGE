a = []
for i in range(1216, 8825):
    if i % 3 == 0 and i % 7 != 0 and i % 15 != 0 and i % 17 != 0 and i % 21 != 0:
       a.append(i)
print(str(len(a))+str(a[0]))
