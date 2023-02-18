# Teste Para Verificar se o Título da Página é Exibido Corretamente
from selenium import webdriver

# Abre o navegador Chrome
driver = webdriver.Chrome()

# Acessa a página inicial da Netflix
driver.get("https://www.netflix.com/")

# Verifica se o nome da página é exibido corretamente
expected_title = "Netflix"
actual_title = driver.title
assert actual_title == expected_title, f"Erro: o título esperado era '{expected_title}', mas o título atual é '{actual_title}'"
