# 1 Escreva um programa que receba uma tupla de números inteiros e retorne a soma de todos os elementos da tupla.
tupla1 = ( 200, 1100,41,28,99,100)
print(sum(tupla1))
print()

# 2 Escreva um programa que receba uma tupla de números e retorne o maior e o menor valor da tupla.
tupla2=(2023, 2200,5000,99,300,14,9,11,21,54,1)

print()

# 3 Escreva uma função que receba uma tupla de strings e retorne uma lista com as strings ordenadas por ordem alfabética.
tupla3=('Elisangela','Ricardo','Rafael','Thamires','Fernanda','Camila','Beatriz','Wanderson','Anderson')

tuplaOrdemAlfa = sorted(tupla3)
print(tuplaOrdemAlfa)

print()

# 4 Escreva um programa que receba duas tuplas de números e retorne uma nova tupla com a soma dos elementos correspondentes das duas tuplas.
Tupla4=(200,400,60000,90000,13,27,93,100,205)
Tupla5=(1900,2026,1041,290,97,88,23,22,1)

print()

# 5 Escreva um programa que apresente a quantidade de vezes que um determinado registro (Nº 2) se repete dentro da tupla.
Tupla6=(2,300,90,120,200,2,45,89,2,8000,900,999,56,2,77)
print(Tupla6.count(2))

print()

# 6 Construa um programa que faça a combinação Lista e tupla, crie uma lista com tuplas contendo o nome e o telefone de cada registro.


# 7 Faça um programa eu apresente os elementos de uma tupla a partir de uma posição específica.
# Posição 5 – 8, posição 2 – até o final, penúltima e última posição, posição 3 – 15, posição 10 – 12)

Tupla8=(2000,300,True,'312N','555',89,1990,300,'São Paulo apital',2023,257,999,654,712,'Estação Itaquera',False,400,221,'Estação Guaianazes')
print(Tupla8[5:9])
print(Tupla8[2:len(Tupla8)])
print(Tupla8[-2:len(Tupla8)])
print(Tupla8[3:16])
print(Tupla8[10:13])