from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get('http://www.vanilton.net/triangulo/')

from time import sleep
sleep(5)

ERRO_MSG = 'Triângulo Inválido: o valor de {} é maior que a soma de {} e {}'

V1 = float(input('Digite o primeiro valor: '))
navegador.find_element('xpath', '/html/body/form/input[1]').send_keys(V1)

V2 = float(input('Digite o segundo valor: '))
navegador.find_element('xpath', '/html/body/form/input[2]').send_keys(V2)

V3 = float(input('Digite o terceiro valor: '))
navegador.find_element('xpath', '/html/body/form/input[3]').send_keys(V3)

if V1 > V2 + V3:
    {print(ERRO_MSG.format(V1,V2,V3))}

elif V2 > V1 + V3:
   {print(ERRO_MSG.format(V2,V1,V3))}

elif V3 > V1 + V2:
    {print(ERRO_MSG.format(V3,V1,V2))}

elif V1 == V2 == V3:
    print('O Triângulo é Equilátero')

elif V1 == V2 or V2 == V3 or V1 == V3:
    print('O Triângulo é Isósceles')

elif V1 != V2 != V3:
    print('O Triângulo é Escaleno')

navegador.find_element('xpath', '/html/body/form/input[4]').click()

navegador.find_element('xpath', '/html/body/form/input[3]').send_keys(V3)

from time import sleep
sleep(120)

