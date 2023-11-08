print("Exemplo de uma Tupla:")
tupla = (1, 2, 'Clodoaldo', True, False, 7.75)
print(tupla)

print()

tupla01 = ()
tupla02 = ('Python', 'Java', 'C', 'PHP')
print("Criação de tuplas:\nTupla Vazia, tupla preenchida")
print(tupla01)
print(40 * '#')
print(tupla02)

print()

print("Acessar tupla com índice:")
tupla03 = ('Prof. Elaine', 'Prof. Regiane', 'Prof. Ana Santiago')
print(tupla03[1])

print()

print("Tamanho da tupla:")
tupla04 = (2019, 2020, 2021, 2022, 2023)
print(len(tupla04))
print('Total de itens da lista: ', (len(tupla04)))

print()

print("Retornar o índice de um valor da tupla:")
tupla05 = (100, 'Dinossauro', True, "Eu sou a lenda")
print(tupla05.index('Dinossauro'))
print(tupla05.index('Eu sou a lenda'))
print(tupla05.index(True))
print(tupla05.index(100))

print()

print("Retornar a quantidade de vezes que um elemento aparece:")
tupla06 = ('2º DS', '3º DS', '2º DS', '1º DS', '2º DS')
print(tupla06.count('2º DS'))

print()

print("Fatiamento - retornar os elementos em um dado intervalo:")
tupla07 = ('2º DS', '3º DS', '2º DS', '1º DS', '2º DS', '3º Nutri', '1º Nutri')
print(tupla07[2:4])

print()

print("Ordenação de uma tupla:")
tupla08 = (99, 101, 22, 35, 12, 9, 34, 1)
tuplaOrdenada = sorted(tupla08)
print(tuplaOrdenada)

print(tupla08)

print()

nomeEndereco = []
aline = ("Aline Mendonça de Oliveira", 'Feliciano de Mendonça, 290')
clodoaldo = ('Clodoaldo Bastos Cavalcante', 'Av. Brasil, 280 - Mogi das Cruzes')

print("Lista de tuplas:")

nomeEndereco.append(aline)
print(nomeEndereco)
nomeEndereco.append(clodoaldo)
print(nomeEndereco)

print()

print("Unpacking - atribuição dos valores de uma tupla em variáveis múltiplas:")
tupla09 = ('Corinthians', "São Paulo", "Palmeiras", "Santos")
a, b, c, d = tupla09

print(a)
print(b)
print(c)
print(d)

print()

print("Valores máximo e mínimo de uma tupla:")

print(max(tupla08))
print(min(tupla08))

print()

print('Remover itens:')

tupla09 = (1, 2, 3, 4, 5)
novaTupla = tupla09[0:4]

print(novaTupla)

print()
print('Imprimindo infirmações da tupla')
print(dir(tupla07))