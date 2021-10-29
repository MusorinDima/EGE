import random
def sum2(d):
    global value
    value +=2

    return value

def mult3(d):
    global value
    value *= 3
    return value

value = 2

funcs = [sum2(value),mult3(value)]
print(random.choice(funcs))
