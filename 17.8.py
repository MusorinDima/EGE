# Рассматривается множество целых чисел, принадлежащих числовому отрезку [1813; 6861],
# которые делятся на 5 и не делятся на 6, 10, 15, 23. Найдите количество таких чисел и минимальное из них.
# В ответе запишите два целых числа без пробелов и других дополнительных символов: сначала количество,
# затем минимальное число.
# Для выполнения этого задания можно написать программу или воспользоваться редактором электронных таблиц.


s = []
n = 0
for i in range(1813, 6862):
    if i % 5 == 0 and i % 6 != 0 and i % 10 != 0 and i % 15 != 0 and i % 23 != 0:
        n += 1
        s.append(i)
print(n, min(s))