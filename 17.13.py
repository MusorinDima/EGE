count = 0
for i in range(16015, 48990):
    if (i % 7 == 0 or i % 11 == 0) and i % 9 != 0 and i % 12 != 0 and i % 13 != 0:
        count += 1
        print(count,i)
