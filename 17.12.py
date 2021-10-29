coont = 0
for i in range(5913, 11754):
    if i % 5 == 0 and i % 11 == 0 and i % 7 != 0 and i % 10 != 0 and i % 13 != 0 and i % 22 != 0:
        coont += 1
        print(coont, i)
