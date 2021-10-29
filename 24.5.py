with open('24_demo.txt', 'r') as f:
    s = f.readline()
    k = 1
    kmax = 1
    for i in range(2, len(s)):
        if (s[i] == s[i - 1]) and s[i] == 'Y':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 1
print(kmax)