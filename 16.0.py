
def G( n ):
    global a
    a += n+2
    #print(n+2)

    if n > 1:
        a += n+6
        #print(n+6)
        G(n-1)
        G(n-2)
a = 0
i = 1
while a <=120000:
    i+=1
    G(i)
print(a,i)

ХЗ как решать



