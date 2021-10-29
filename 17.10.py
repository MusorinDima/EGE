count = 0
for i in range(3361,9206):

    if (i % 4 == 0 or i % 5 == 0) and i % 9 != 0 and i % 11 != 0 and i % 17 != 0 and i % 23 != 0:
        count += 1
        print(count, i)