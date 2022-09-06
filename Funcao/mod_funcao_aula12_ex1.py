meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}

def func_vendedores(vendedores):
    vendedores_bateu_meta = []
    percentual = 0
    for chave in vendedores:
        if vendedores[chave] > 10000:
            vendedores_bateu_meta.append(chave)
            percentual = len(vendedores_bateu_meta) / len(vendedores)
    return print('Os vendedores que bateram a meta foram {} e a porcentagem foi de {:.1%}.'.format(vendedores_bateu_meta, percentual))

print(func_vendedores(vendas))
