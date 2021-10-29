def count_pairs(list: list):
    c = 0
    para = 0
    while c < len(list):
        para += list[c:].count(list[c]) - 1
        c += 1
    print(para)

a = list(map(int, input().split()))

# первый способ
i = 0
b = len(a)
cnt = 0
while i < b:
    for _ in a[i+1:]:
        if a[i] == _:
            cnt +=1
    i += 1
print(cnt)

# второй способ
#count_pairs(a)









