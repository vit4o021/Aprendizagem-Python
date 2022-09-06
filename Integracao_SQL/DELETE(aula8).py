import pyodbc

dados_conexao = ('Driver={SQLite3 ODBC Driver};'
                 'Server=localhost;'
                 'Database=chinook.db')

conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida!')

cursor = conexao.cursor()

cursor.execute('DELETE FROM albums WHERE AlbumId = 2')

cursor.commit() #Usado para os comendos em SQL digitados sejam definitivos e não temporários

cursor.close()
conexao.close()