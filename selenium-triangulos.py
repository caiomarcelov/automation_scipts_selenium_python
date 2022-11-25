from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get('http://www.vanilton.net/triangulo/')

navegador.find_element('xpath', '/html/body/form/input[1]').send_keys(22)
navegador.find_element('xpath', '/html/body/form/input[2]').send_keys(22)
navegador.find_element('xpath', '/html/body/form/input[3]').send_keys(22)
navegador.find_element('xpath', '/html/body/form/input[4]').click()

from time import sleep
sleep(5)

navegador.find_element('xpath', '/html/body/form/input[1]').send_keys(20.5)
navegador.find_element('xpath', '/html/body/form/input[2]').send_keys(5.60)
navegador.find_element('xpath', '/html/body/form/input[3]').send_keys(2)
navegador.find_element('xpath', '/html/body/form/input[4]').click()

from time import sleep
sleep(5)

navegador.find_element('xpath', '/html/body/form/input[1]').send_keys(3.14)
navegador.find_element('xpath', '/html/body/form/input[2]').send_keys(3.14)
navegador.find_element('xpath', '/html/body/form/input[3]').send_keys(17.9)
navegador.find_element('xpath', '/html/body/form/input[4]').click()

from time import sleep
sleep(10)