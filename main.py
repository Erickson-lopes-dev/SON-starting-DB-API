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


def delete_item(id):
    # deleta um item
    cursor.execute("DELETE from pessoas WHERE id=%s ", (id,))
    db.commit()


def update_item():
    # atualiza um determinado item na db
    cursor.execute("UPDATE pessoas SET nome='fernandod', idade='10' WHERE id=6 ")

    db.commit()


def insert_item(data):
    # inserir item
    cursor.execute("INSERT INTO "
                   "pessoas " "(nome, idade) "
                   "VALUES (%s, %s)",
                   (*data, ))
    # comita as alterações no banco
    db.commit()


# exibindo quatidade de linhas especificadas
def get_fetchaamy():
    # quantidades de linhas para buscar
    rows_fet = cursor.fetchmany(1)

    print(rows_fet)


# buscando todas as linhas
def get_fetchall():
    # print(list(cursor))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # for row in cursor:
    #     print(row)


print('Conecxão feita com sucesso')
db.commit()

# limpa dados da memoria
# db.rollback()

cursor = db.cursor()

# linhas alteradas
print(cursor.rowcount)

insert_item(('José', 19))


# executa o método dentro do banco
row_effected = cursor.execute('SELECT * FROM pessoas')

# exibe linhas afetadas
print(row_effected)


get_fetchall()

# fecha banco
db.close()
