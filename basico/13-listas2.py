#x = []                     #lista
#for i in range(1, 1001):
#    x.append(i)
#print(x)

#x = list(range(1, 101))    #lista

y = [1, 2, 3, 4, 5]

print(y)

z = int(input('apagar: '))

if z in y:
    y.remove(z)
    print('\n\nvalor removido')

print(y)
