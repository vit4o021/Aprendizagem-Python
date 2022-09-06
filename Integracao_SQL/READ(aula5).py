import pyodbc

dados_conexao = ('Driver={SQLite3 ODBC Driver};'
                 'Server=localhost;'
                 'Database=chinook.db')

conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida!')

cursor = conexao.cursor()

cursor.execute('SELECT * FROM customers')

valores = cursor.fetchall() #Lista de tuplas  com todos os valores da tabela
print(valores[0])
cursor.close()
conexao.close()