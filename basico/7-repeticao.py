x = 0

while x != 3:
    x = int(input('CADASTRAR\n1)SIM | 2)NÃO | 3)SAIR\n\n'))

    if x == 1:
        print('logando \n')
    elif x == 2:
        print('')
    elif x == 3:
        break
    else:
        print('ERRO')