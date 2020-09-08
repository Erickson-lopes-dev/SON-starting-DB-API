import MySQLdb

user = 'root'
passwd = ''
database = 'rf_db_v'
host = 'localhost'
port = 3306

MySQLdb.connect(
    user=user,
    passwd=passwd,
    db=database,
    host=host,
    port=port

)

print('Conecxão feita com sucesso')
