import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='loteria'
)

if conexao.is_connected():
    print(f'conectou a {conexao.get_server_info()}')
