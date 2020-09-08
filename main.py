import MySQLdb

user = 'root'
passwd = ''
database = 'db_api'
host = 'localhost'
port = 3306

db = MySQLdb.connect(
    user=user,
    passwd=passwd,
    db=database,
    host=host,
    port=port

)

print('Conecxão feita com sucesso')
db.commit()

# limpa dados da memoria
# db.rollback()

cursor = db.cursor()
# executa o método dentro do banco
row_effected = cursor.execute('SELECT * FROM pessoas')

# exibe linhas afetadas
print(row_effected)

# print(list(cursor))
rows = cursor.fetchall()

for row in rows:
    print(row)

for row in cursor:
    print(row)

db.close()
