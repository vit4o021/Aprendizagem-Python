#API É um conjunto de códigos para usar um serviço/site/aplicativo específico. Cada site/ferramenta tem sua própria API.
import requests #Serve para fazer a requisição/pegar informações de um site
import json #Tratar essas informações que virão no formato JSON
#Link da API: https://docs.awesomeapi.com.br/api-de-moedas

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all') #O python pega todas as informações de todas as moedas
cotacoes_dic = cotacoes.json() #Tranforma o dicionario JSON em um dicionario Python
print(cotacoes_dic)
print('---------------------------------------------------------------------------------------')

print('Dólar: {}'.format(cotacoes_dic['USD']['bid'])) #O python irá exibir a cotação do dólar
print('Euro: {}'.format(cotacoes_dic['EUR']['bid'])) #O python irá exibir a cotação do Euro
print('Bitcoin: {}'.format(cotacoes_dic['BTC']['bid'])) #O python irá exibir a cotação do Bitcoin
print('---------------------------------------------------------------------------------------')

cotacoes_dolar30d = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30') #O python irá pegar a cotação do dólar em 30 dias
cotacoes_dolar_dic = cotacoes_dolar30d.json()
lista_cotacao_dolar30d = [float(item['bid']) for item in cotacoes_dolar_dic] #Exibe somente as informações de cotações do dólar
print(lista_cotacao_dolar30d)
print('---------------------------------------------------------------------------------------')

cotacoes_btc = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/200?start_date=20220101&end_date=20220901') #O Python vai pegar as cotações do bitcoin de 01/01/2022 até 01/09/2022
cotacoes_btc_dic = cotacoes_btc.json()
lista_cotacao_bitcoin_jans_set = [float(item['bid']) for item in cotacoes_btc_dic]
print(lista_cotacao_bitcoin_jans_set)
