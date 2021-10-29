# def F(n):
#
#
#
#     print(n+2)
#     print(n+3)
#     print(n * 10 + 1)
# F(3)

def F(n):
    global c

    #print(n+2)
    c += 1
    if n != 25:
        #print(n+5)
        #c += n + 5
        F(n+2)
        F(n+3)
        F(n*10 +1)
    return c

c = 0
F(3)