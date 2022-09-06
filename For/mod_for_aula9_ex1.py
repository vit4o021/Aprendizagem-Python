meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
    ['Victor', 50000],
    ['Karol', 70000],
]
vendedor_bateu_meta = []
for i,item in enumerate(vendas):
    if item[1] >= meta:
        #print('Vendedor {} bateu a meta. Fez {} vendas'.format(item[0], item[1]))
        vendedor_bateu_meta.append(item)
        calculo_porcentagem = len(vendedor_bateu_meta)/len(vendas)

melhor_vendedor = ''
maior_vendas = 0

for venda in vendas:
    if venda[1] > maior_vendas:
        maior_vendas = venda[1]
        melhor_vendedor = venda[0]

print('A porcentagem de vendedores que bateram a meta foi de {:.1%} e o melhor vendedor foi {} com {} vendas.'.format(calculo_porcentagem,melhor_vendedor, maior_vendas))







