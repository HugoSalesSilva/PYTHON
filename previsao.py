import requests

"""
    Data;
    Dia da semana;
    Descrição do tempo (Nublado, sol ,chuva);
    Temperatura Mínima;
    Temperatura Máxima;
    Velocidade do vento;
    Humidade relativa do Ar;
    Hora do nascer do sol;
    hora do por do sol;
    Fase da lua;
"""

requisicao = requests.get('https://api.tempo.com/index.php?api_lang=br&localidad=12996&affiliate_id=tk99un15usak&v=3.0')

previsao = requisicao.json()

print("=== Previsão do tempo de amanhã ===")

#Data;
Dia = previsao['day']
diaSemana = Dia['2']
data = diaSemana['date']

ano = data[0:4]
mes = data[4:6]
dia = data[6:len(data)]

print(f" Data: {dia}/{mes}/{ano}")

#Dia da semana;

diaSemananome = diaSemana['name']

if not diaSemananome == 'Sábado' and not diaSemananome == 'Domingo':
    diaSemananome+="-feira"

print(f" Dia da Semana: {diaSemananome}")

#Descrição do tempo (Nublado, sol ,chuva);

DescDia = diaSemana['symbol_description']

print(f" Descrição do Tempo: {DescDia}")

# Temperatura Mínima;

TempMin = diaSemana['tempmin']

print(f" Temperatura Minima: {TempMin}°C")

#   Temperatura Máxima;

TempMax = diaSemana['tempmax']

print(f" Temperatura Maxima: {TempMax}°C")

# Velocidade do vento;

vento = diaSemana['wind']
velocidadeVento = vento['speed']

print(f" Velocidade do vento: {velocidadeVento}km/h")

#Umidade relativa do Ar;

umidade = diaSemana['humidity']

print(f" Umidade relativa do Ar: {umidade}%")

# Hora do nascer do sol;

sol = diaSemana['sun']
nascer = sol['in']

print(f" Hora do nascer do sol: {nascer}")

# hora do por do sol;

por = sol['out']

print(f" Hora do por do sol: {por}")

#Fase da lua;

lua = diaSemana['moon']
Descricao = lua['desc']

print(f" Fase da lua: {Descricao}")

