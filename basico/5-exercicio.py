nome = input('Nome: ')
idade = int(input('Idade: '))
print('--------------')
p1 = int(input('prova 1: '))
p2 = int(input('prova 2: '))
media = (p1+p2)/2

print('\n*\n*\n*\n*\n')

print('Nome do aluno: {}'.format(nome.title()))

#media 6 aprovado
print('\nsituação:')
if media >= 6 and idade >= 18:
    print('aprovado para receber a bolsa')
    print('media do aluno: {}'.format(media))
else:
    if idade < 18:
        print('idade abaixo do esperado')
    else:
        print('nota menor que 6')