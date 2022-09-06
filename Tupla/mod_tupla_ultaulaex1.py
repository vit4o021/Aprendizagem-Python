meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

for venda in vendas:
    nome, qtd_vendas = venda
    if qtd_vendas >= meta:
        print('Vendedor {} bateu a meta, fez {} vendas.'.format(nome, qtd_vendas))

