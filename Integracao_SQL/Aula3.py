import pyodbc

dados_conexao = ('Driver={SQLite3 ODBC Driver};'
                 'Server=localhost;'
                 'Database=salarios.sqlite')
#caso precisasse de login e senha:
#dados_conexao = ("Driver={Seu_Driver};"
#            "Server=Seu_Servidor;"
#            "Database=NomeBaseDeDados;"
#            "UID=Login;"
#            "PWD=Senha;")

conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida!')

cursor = conexao.cursor() #Cursor é basicamente quem vai executar os nossos códigos SQL

cursor.execute('SELECT * FROM Salaries')

valores = cursor.fetchall() #Lista de tuplas com todos os valores da tabela
print(valores[:10])

cursor.close() #Finaliza a conexão com o banco de dados
conexao.close() # ^