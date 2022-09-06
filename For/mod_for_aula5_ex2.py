#---------------ÍNDICE ESPECÍFICO-----------
meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

for item in vendas:
    if item[1] >= meta:
        print('Vendedor {} bateu a meta. Fez {} vendas'.format(item[0], item[1]))