import pyautogui, time

#1. Crie um programa que mova o cursor do mouse para a bandeja do
#sistema e clique no calendário do sistema (Windows).

width, height = pyautogui.size()
pyautogui.moveTo(width-100, height, duration=0.2)
pyautogui.click()


#2. Crie um programa que escreva um texto em um campo de entrada
#no site do bing, assunto “PyAutoGui”.

time.sleep(1)
pyautogui.hotkey('win', 'r')
pyautogui.write('chrome')
pyautogui.hotkey('enter')
time.sleep(0.8)
pyautogui.write('https://www.bing.com/')
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.write('PyAutoGui')


#3. Crie um script que tire uma captura de tela da tela inteira e salve-a
#em um arquivo de imagem:

pyautogui.screenshot('screenshot.png')


#4. Crie um script que encontre uma imagem em uma captura de tela e
#clique na posição onde a imagem foi encontrada:

time.sleep(0.6)
posX, posY = pyautogui.locateCenterOnScreen('x.png')
pyautogui.moveTo(posX, posY)
pyautogui.click()


#5. Escreva um programa que envie uma mensagem para o usuário
#Indicando uma conexão bem sucedida.

pyautogui.alert(title="Conexão", text="Conexão bem sucedida")


#6. Escreva um programa que apresente três botões de escolha (Sim, Não
#e Talvez) e apresente a opção escolhida pelo usuário em uma
#mensagem de alert.

opcao = pyautogui.confirm(title="Escolha uma opção", buttons=['Sim', 'Não', 'Talvez'])
pyautogui.alert(title="Escolha", text=f"A sua escolha foi: {opcao}")


#7. Escreva um programa que tenha três opções (Janeiro, Fevereiro,
#Março), as escolha correta deve ser a alternativa Março. Mostre a
#mensagem de “Opção correta” quando o usuário escolher a opção
#Março e “Opção errada” quando o usuário escolher uma opção
#diferente.

mes = pyautogui.confirm(title="Escolha um mês", buttons=['Janeiro', 'Fevereiro', 'Março'])
if mes == 'Março':
    pyautogui.alert(title="Escolha", text="Opção correta")
else:
    pyautogui.alert(title="Escolha", text="Opção errada")


#8. Faça um programa que realize a captura de tela Screeshot depois de
#3 Segundos, salve a imagem com o nome de captura10052023.

time.sleep(3)
pyautogui.screenshot('captura10052023.png')
