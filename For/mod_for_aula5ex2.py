meta = 10000
vendas = [
    ['João', 15000],
    ['Júlia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],

]
for vendedor in vendas:
    if vendedor[1] >= meta:
        print('O vendedor {} bateu a meta, fazendo {} vendas.'.format(vendedor[0], vendedor[1]))
