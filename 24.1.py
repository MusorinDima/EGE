# В текстовом файле находится цепочка из символов латинского алфавита A, B, C, D, E, F.
# Найдите длину самой длинной подцепочки, не содержащей символов C и F.
def checkCF(str):
    if ('C' in str) or ('F' in str):
        return True
    else:
        return False

with open('24 (1).txt', 'r') as f:
    file = f.readline()
    #count = 0
    maks = 0
    min_str = ''
    for i in file:
        min_str += i
        if checkCF(min_str):
            min_str = ''

            count = 0
        else:
            if len(min_str) > maks:
                maks = len(min_str)
            #count += 1
            #print(min_str)
print(maks)