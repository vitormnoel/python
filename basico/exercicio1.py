peso = []
con = 0

for i in range(0, 7):
    peso.append(float(input(f'peso da {i} pessoa: ')))
    if peso[i] > 90:
        con += 1

print(f'Pessoas acima de 90kg: {con}')
print(f'Media de pesos: {sum(peso)/7}')
