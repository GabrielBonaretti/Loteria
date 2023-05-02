from conectar import conexao

cursor = conexao.cursor()
cursor.execute('select database();')
linha = cursor.fetchone()


def buscar_numeros(id_user):
    sql = f"SELECT * FROM na WHERE idNa = {id_user}"
    cursor.execute(sql)
    linhas = cursor.fetchall()
    numero_novo = linhas[0][1] + 1
    sql = f"""UPDATE na SET estatisticas ='{numero_novo}' WHERE idNa = '{id_user}';"""
    cursor.execute(sql)
    conexao.commit()


def numeros_ler():
    sql = 'SELECT * from na'
    cursor.execute(sql)
    lista_numeros = cursor.fetchall()
    return lista_numeros


def ler_lista_jogos():
    sql = 'SELECT * from jogos'
    cursor.execute(sql)
    lista_usuarios = cursor.fetchall()
    return lista_usuarios
