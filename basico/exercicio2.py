#fatorial

n = int(input('numero: '))
c = 1

for i in range(n, 0, -1):
    c *= i

print(c)