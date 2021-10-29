# Рассматривается множество целых чисел,
# принадлежащих числовому отрезку [2050; 9166], которые делятся на 7 и не делятся на 13, 14, 19, 22.
# Найдите количество таких чисел и максимальное из них.
# В ответе запишите два целых числа без пробелов и других дополнительных символов:
# сначала количество, затем максимальное число.


s = []
n = 0
for i in range(2050, 9167):
    if i % 7 == 0 and i % 13 != 0 and i % 14 != 0 and i % 19 != 0 and i % 22 != 0:
        n += 1
        s.append(i)

print(n, max(s))