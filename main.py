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


# deletar por id
def delete_item(id):
    cursor = db.cursor()
    # deleta um item
    cursor.execute("DELETE from pessoas WHERE id=%s ", (id,))
    db.commit()


# atualizar dados
def update_item():
    cursor = db.cursor()
    # atualiza um determinado item na db
    cursor.execute("UPDATE pessoas SET nome='fernandod', idade='10' WHERE id=6 ")

    db.commit()


# inserir dados
def insert_item(data):
    cursor = db.cursor()
    # inserir item
    cursor.execute("INSERT INTO "
                   "pessoas " "(nome, idade) "
                   "VALUES (%s, %s)",
                   (*data,))
    # comita as alterações no banco
    db.commit()


# exibindo quatidade de linhas especificadas
def get_fetchaamy():
    cursor = db.cursor()
    # quantidades de linhas para buscar
    rows_fet = cursor.fetchmany(1)

    print(rows_fet)


# buscando todas as linhas
def get_fetchall():
    cursor = db.cursor()
    # print(list(cursor))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # for row in cursor:
    #     print(row)


# exibe todos os dados do banco
def select_all():
    cursor = db.cursor()
    # executa o método dentro do banco
    row_effected = cursor.execute('SELECT * FROM pessoas')

    # exibe linhas afetadas
    print(row_effected)


# remove os dados em memoria
def remove_dados_memoria():
    cursor = db.cursor()
    # limpa dados da memoria
    db.rollback()


# inseri multiplas linhas
def insert_multiplos():
    cursor = db.cursor()
    data = ('erickson', 14), ('daniel', 14), ('Renan', 18)
    cursor.executemany("INSERT INTO pessoas (nome, idade) VALUES (%s, %s)", (*data,))
    db.commit()


insert_multiplos()



# fecha banco
db.close()
