produto = input('Digite o nome do produto: ')
quantidade = int(input('Digite a quantidade do produto {}: '.format(produto)))
vendas = []

while produto and quantidade != '' :
    vendas.append([produto,quantidade])
    produto = input('Digite o nome do produto: ')
    quantidade = input('Digite a quantidade do produto {}: '.format(produto))
#print(','.join(vendas))
print(vendas)
