# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
#Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
# Для выполнения этого задания следует написать программу.
#Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
with open('24_demo.txt', 'r') as f:
    s = f.readline()
    k = 1
    kmax = 1
    for i in range(2, len(s)):
        if s[i] != s[i - 1]:
            k += 1
            if k > kmax:
                kmax = k
        else:
            k = 1
print(kmax)




