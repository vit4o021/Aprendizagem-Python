meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_total = vendas_1sem + vendas_2sem

maior_valor= max(vendas_total)
#print(maior_valor)
i = vendas_total.index(49051)
#print(i)

menor_valor = min(vendas_total)
#print(menor_valor)
i2 = vendas_total.index(9650)
#print(i2)

melhor_mes = meses[10]
pior_mes = meses[11]

print('O melhor mês do ano foi {} com faturamento de R${} e o pior mês do ano foi {} com faturamento de R${}.'.format(melhor_mes, maior_valor, pior_mes, menor_valor))

fat_total = sum(vendas_total)
percentual = maior_valor/fat_total
print('O faturamento total foi de {} e o melhor mês representa {:.1%} do faturamento.'.format(fat_total, percentual))
top3 = []
top3.append(maior_valor)
vendas_total.remove(maior_valor)
segundo_maior = max(vendas_total)
top3.append(segundo_maior)
vendas_total.remove(segundo_maior)
terceiro_maior = max(vendas_total)
top3.append(terceiro_maior)
top3.sort(reverse = True)
print('O top 3 de valores de vendas foi de {}.'.format(top3))