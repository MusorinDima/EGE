# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите длину самой длинной последовательности, состоящей из символов Y.
# Хотя бы один символ Y находится в последовательности.
# with open('24_demo.txt', 'r') as f:
#     count = 0
#     max_count = 0
#     string = f.read()
#     for i in string:
#         if i == 'Y':
#             count += 1
#         else:
#             count = 0
#         if count > max_count:
#             max_count = count
# print(max_count)
with open('24_demo.txt', 'r') as f:
    count = 1
    max_count = 1
    string = f.read()
    index = 0
    while string.find("Y", index) > 0:
        # if i == 'Y':
        if string[string.find("Y", index)] == string[string.find("Y", index + 1)]:
            count += 1

        if count > max_count:
            max_count = count
        index = string.find("Y", index) + 1

print(max_count)


