meta = 50000
qtd_vendida = 65300
if qtd_vendida > meta:
    print('Batemos a meta de vendas de iphone,vendemos {} unidades.'.format(qtd_vendida))
else:
    print('Infelizmente não batemos a meta, vendemos {} unidades. A meta era de {} unidades.'.format(qtd_vendida,meta))
