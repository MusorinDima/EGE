s = '1' * 70
while '11111' in s:
    s = s.replace('2222', '1', 1)
    s = s.replace('1111', '2', 1)
print(s)