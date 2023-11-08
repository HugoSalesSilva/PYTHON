import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL,BTC-BRL')


cota = requisicao.json()


dolar = cota['USD']
valorDolar = dolar['high']
identificacao = dolar['name']
euro = cota['EUR']
valorEuro = euro['high']
identificacaoEuro = euro['name']
bit = cota['BTC']
valorBit = bit['high']
identificacaoBit = bit['name']

print(f"{identificacao} = {valorDolar}")

print(f"{identificacaoEuro} = {valorEuro}")

print(f"{identificacaoBit} = {valorBit}")