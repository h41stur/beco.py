import mysql.connector as mysql

# cria a conexão
db = mysql.connect(
    host = '192.168.0.12',
    user = 'root',
    port = 3306,
    password = '',
    db = 'mysql',
    use_pure = True,
    charset = 'utf8'
)

# cria o cursor
cursor = db.cursor()

# executa o comando

#cursor.execute('create user "h41stur"@"%" identified by "H41stur!123"')
cursor.execute('select * from user')

#carregando resultado em variável
databases = cursor.fetchall()

# organizando a lista
for i in databases:
    print(i)

