#for
'''
media = 0
idade = []

for i in range(0, 100) :
    idade.append(int(input('idade: ')))

    if idade[i] == -1:
        break

    media += idade[i]

idade.remove(-1)
print(f'media de idade: {media/len(idade)}')
'''
#while
idade = 0
media = 0
i = 0

while idade != -1:
    idade = int(input('idade: '))

    if idade != -1:
        media += idade
        i += 1

print('media de idade: {}'.format(media/i))