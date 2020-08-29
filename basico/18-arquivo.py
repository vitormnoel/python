arquivo = open('aula.txt', 'r')

'''t = 
ou gatinha
me da uma chance
por favor

arquivo.write(t)
'''
#t = arquivo.read()
t = arquivo.readlines()

for i in range(0, len(t)):
    print('linha {}: {}'.format(i, t[i]))

arquivo.close