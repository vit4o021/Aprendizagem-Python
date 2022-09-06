vendas_produtos = [
    ('iphone', 558147, 951642),
    ('galaxy', 712350, 244295),
    ('ipad', 573823, 26964),
    ('tv', 405252, 787604),
    ('máquina de café', 718654, 867660),
    ('kindle', 531580, 78830),
    ('geladeira', 973139, 710331),
    ('adega', 892292, 646016),
    ('notebook dell', 422760, 694913),
    ('notebook hp', 154753, 539704),
    ('notebook asus', 887061, 324831),
    ('microsoft surface', 438508, 667179),
    ('webcam', 237467, 295633),
    ('caixa de som', 489705, 725316),
    ('microfone', 328311, 644622),
    ('câmera canon', 591120, 994303),
]

for venda in vendas_produtos:
    produto, vendas2019, vendas2020 = venda
    if vendas2020 > vendas2019:
       crescimento = vendas2020/vendas2019 - 1
       format_2019 = '{:_}'.format(vendas2019)
       format_2019 = format_2019.replace('_', '.')
       format_2020 = '{:_}'.format(vendas2020)
       format_2020 = format_2020.replace('_', '.')
       print('O produto {} foi vendido {} em 2019 e {} em 2020, a porcentagem do crescimento foi de {:.1%}'.format(produto, format_2019, format_2020, crescimento))