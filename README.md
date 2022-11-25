# _Automação de Testes Web_

## Criação de scripts para automação

Script para automatizar a execução de testes web usando Selenium e Python - _selenium-triangulos.py_.

Tester: **Caio Marcelo**


### Resumo

O script desenvolvido tem por objetivo a automação de um cenário de testes em uma página web, permitindo um maior número de interações em menor tempo se comparado ao mesmo teste executado de forma manual.


### Requisitos

* [Python 3+](http://python.org/)
* [Anaconda](/www.anaconda.com/download)
* [Jupyter](http://jupyter.org/)
* [Selenium](https://www.selenium.dev/)
* [WebDriver](https://www.w3.org/TR/webdriver/)


### Instalação

* Recomenda-se que a instalação de Python e Anaconda seja feita através do instalador de programas Windows, após baixar os arquivos *.exe* em seus respectivos sites;

* Apesar da recomendação para utilização do Jupyter, fica a seu critério escolher a IDE com a qual tem mais familiaridade;

* A instalação do Selenium e WebDriver pode ser feita no prompt de comando Anaconda através dos seguintes comandos:


  _pip install selenium_ (Selenium)

  _pip install webdriver-manager_ (WebDriver)


### Cenários de Teste

#### Cenário 1 - Reconhecimento de Triângulo Equilátero

Neste cenário de testes, são inseridos 3 valores iguais para as dimensões de um triângulo, que deve ser reconhecido por triângulo equilátero.

#### Cenário 2 - Reconhecimento de Triângulo Escaleno

Neste cenário de testes, são inseridos 3 valores distintos para as dimensões de um triângulo, que deve ser reconhecido por triângulo escaleno. Nesse cenário, foi também analisada a capacidade do programa de processar números com casas decimais em dois campos de dados fornecidos.

#### Cenário 3 - Reconhecimento de Triângulo Isósceles

Neste cenário de testes, são inseridos 2 valores iguais e 1 valor distinto para as dimensões de um triângulo, que deve ser reconhecido por triângulo isósceles. Nesse cenário, foi também analisada a capacidade do programa de processar números com casas decimais em todos os campos de dados fornecidos.
