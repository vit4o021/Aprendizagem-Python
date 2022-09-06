niveis_co2 = {
    'AC': [325,405,429,486,402],
    'AL': [492,495,310,407,388],
    'AP': [507,503,368,338,400],
    'AM': [429,456,352,377,363],
    'BA': [321,508,372,490,412],
    'CE': [424,328,425,516,480],
    'ES': [449,506,461,337,336],
    'GO': [425,460,385,485,460],
    'MA': [361,310,344,425,490],
    'MT': [358,402,425,386,379],
    'MS': [324,357,441,405,427],
    'MG': [345,367,391,427,516],
    'PA': [479,514,392,493,329],
    'PB': [418,499,317,302,476],
    'PR': [420,508,419,396,327],
    'PE': [404,444,495,320,343],
    'PI': [513,513,304,377,475],
    'RJ': [502,481,492,502,506],
    'RN': [446,437,519,356,317],
    'RS': [427,518,459,317,321],
    'RO': [517,466,512,326,458],
    'RR': [466,495,469,495,310],
    'SC': [495,436,382,483,479],
    'SP': [495,407,362,389,317],
    'SE': [508,351,334,389,418],
    'TO': [339,490,304,488,419],
    'DF': [376,516,320,310,518],
}
# Os níveis normais de CO2 são em média 350.
# Isso significa que se tivermos os 5 sensores do Rio de Janeiro marcando: 350, 400, 450, 350, 300, o nível de CO2
# do Rio de Janeiro será dado por: (350 + 400 + 450 + 350 + 300) / 5 = 370.
# Caso o nível seja maior do que 450, um aviso deve ser exibido pelo seu programa dizendo, por exemplo: Rio de Janeiro
# está com níveis altíssimos de CO2 (490), chamar equipe especializada para verificar a região.
#teste = niveis_co2['AC']
#teste = {'VENDAS': [350, 400, 450, 350, 300]}
#teste1 = teste['VENDAS']
#media = (sum(teste1)) / 5
#print(media)
for chave in niveis_co2:
    media = (sum(niveis_co2[chave])) / 5
    if media > 450:
        print('{} está com níveis altíssimos de CO2 ({}), chamar equipe especializada para verificar a região.'.format(chave, media))


