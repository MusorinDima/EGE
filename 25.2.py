# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [194455; 194500],
# числа, имеющие ровно 4 различных делителя.
# В ответе для каждого найденного числа запишите два его наибольших делителя в порядке возрастания.
for i in range(194455, 194500):
    s = []
    for x in range(1, i + 1):
        if i % x == 0:
            s.append(x)
    if len(s) == 4:
        print(s[2:])
