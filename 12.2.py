def str_to_int(x):
    try:
        return int(x)
    except ValueError:
        return 0


s = '>' + '1' * 10 + '2' * 20 + '3' * 30
b = list(s)
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)
# print(s)
s = list(s)

print(s.remove(s[-1]), s)
print(sum(list(map(int, s))))
print(sum(map(str_to_int, b)))
