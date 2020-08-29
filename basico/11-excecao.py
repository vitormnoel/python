try:
    x = int(input('idade: '))
except:
    print('nao reconhecido')
else:
    print(f'sua idade é {x}')
finally: 
    print('obrigado por acessar')