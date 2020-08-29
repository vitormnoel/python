#conexao
import pymysql.cursors

conexao = pymysql.connect(
    host='localhost', #endereço de ip
    user='root',
    password='',
    db='interacao', #banco de dados
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

#interação do banco de dados 

x = 'create table teste(nome varchar(30));'
i = 'insert into teste values("vitor");'
#n = input('digite seu nome: ')
no = input('nome: ')
en = input('endereço: ')


with conexao.cursor() as cursor:
    #cursor.execute('insert into teste values("{}");'.format(n)) #executa o que foi passado no bd
    #cursor.execute('create table cadastro(id int primary key auto_increment, nome varchar(50) not null, endereco varchar(200));')
    cursor.execute('insert into cadastro(nome, endereco) values("{}", "{}");'.format(no, en))
    conexao.commit()