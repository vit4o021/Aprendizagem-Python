nome_produto = input('Qual o nome do produto? ')
categoria = input('Qual a categoria do produto? ')
qtde_atual = input('Qual a a quantidade atual em estoque? ')

if nome_produto == '' or categoria == '' or qtde_atual == ''  :

    print('Preencha as informações corretamente!')

qtde_atual = int(qtde_atual)
est_alimento = 50
est_bebida = 75
est_limpeza = 30

if categoria == 'alimentos' and qtde_atual < est_alimento :
    print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque.'.format(nome_produto,qtde_atual))
else :
    pass

if categoria == 'bebidas' and qtde_atual < est_bebida :
    print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque.'.format(nome_produto,qtde_atual))
else:
    pass

if categoria == 'limpeza' and qtde_atual < est_limpeza :
    print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque.'.format(nome_produto,qtde_atual))
else:
    pass


