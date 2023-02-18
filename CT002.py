# Teste Para Localizar os Elementos Ativos na Página
from selenium import webdriver
from selenium.webdriver.common.by import By

# Abre o navegador Chrome
driver = webdriver.Chrome()

# Acessa a página inicial da Netflix
driver.get('https://www.netflix.com/br/')

# Busca o elemento ativo na página
elemento_ativo = driver.switch_to.active_element

# Exibe o texto do elemento ativo
print(elemento_ativo.text)

# Fecha o navegador
driver.quit()
