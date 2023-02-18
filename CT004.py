# Teste Para Verificar se o Título da Página é Exibido Corretamente
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Cria uma instância do driver do navegador
driver = webdriver.Chrome()

# Navega para a página inicial da Netflix
driver.get("https://www.netflix.com/browse")

# Espera até que a barra de pesquisa seja exibida
search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//input[@placeholder="Títulos, gente e gêneros"]'))
)

# Clica na barra de pesquisa
search_bar.click()

# Digita o nome do filme "Harry Potter" na barra de pesquisa
search_bar.send_keys("Harry Potter")

# Espera até que a sugestão do filme seja exibida
suggestion = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//div[contains(@class,"suggestionWrapper")]/a[contains(text(),"Harry Potter e a Pedra Filosofal")]'))
)

# Clica na sugestão do filme "Harry Potter e a Pedra Filosofal"
suggestion.click()

# Espera até que a página do filme seja carregada
title = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//h1[contains(@class,"title") and contains(text(),"Harry Potter e a Pedra Filosofal")]'))
)

# Verifica se o nome do filme exibido na página é "Harry Potter e a Pedra Filosofal"
assert title.text == "Harry Potter e a Pedra Filosofal"

# Fecha a janela do navegador
driver.quit()
