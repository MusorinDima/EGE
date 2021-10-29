def F(n):
    if n < 8:
        F(n + 3)
        print(n)
        F(2 * n)
print(F(1))

