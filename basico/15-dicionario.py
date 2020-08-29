'''
x = dict(nome= 'caio', idade= 18, tel= 98133) 
#{'variavel':'valor' , ...} pode ser usado também

print(x['tel'])
print(len(x))
x.pop('idade')
print(x)
'''

cadastroPessoas = [{'nome': 'vitor', 'idade': 18, 'tel': '98133', 'cpf': '928373'}, \
    {'nome': 'joao', 'idade': 28, 'tel': '2842', 'cpf': '12345'},\
    {'nome': 'ana', 'idade': 21, 'tel': '00000', 'cpf': '55441'},\
    {'nome': 'rafa', 'idade': 98, 'tel': '11111', 'cpf': '22233'},\
    {'nome': 'pedro', 'idade': 13, 'tel': '22222', 'cpf': '99999'},\
    {'nome': 'jorge', 'idade': 22, 'tel': '33333', 'cpf': '12121'}]

for i in range(0, len(cadastroPessoas)):
    print(cadastroPessoas[i]['nome'])