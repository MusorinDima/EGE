for x in range(100, 1001):
# x = int(input())
    L = x-30
    M = x+30
    while L != M:
        if L > M:
          L = L - M
        else:
          M = M - L
    if M == 30:
        print(x, M)