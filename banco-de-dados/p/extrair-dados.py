import pymysql.cursors

conexao = pymysql.connect(
    host='localhost', #endereço de ip
    user='root',
    password='',
    db='interacao', #banco de dados
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

with conexao.cursor() as cursor:
    cursor.execute('select nome from cadastro')
    dados = cursor.fetchall()

for dado in dados:
    print(dado)