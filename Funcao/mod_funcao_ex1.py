preco = int(input('Qual o preço do produto: '))
custo = int(input('Qual o custo do produto: '))
lucro = int(input('Qual o lucro do produto: '))

def carga_tributaria(preco_prod, custo_prod, lucro_prod):
    imposto = preco_prod - custo_prod - lucro_prod
    return imposto / preco_prod

print('A porcentagem da carga tributária foi de {:.1%}.'.format(carga_tributaria(preco_prod=preco, custo_prod=custo, lucro_prod=lucro)))
#OU
print('A porcentagem da carga tributária foi de {:.1%}.'.format(carga_tributaria(preco,custo, lucro)))


