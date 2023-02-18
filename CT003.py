# Teste de login no site da Netflix
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configurações
url = 'https://www.netflix.com/br/login'
email = 'seu_email'
senha = 'sua_senha'

# Iniciando o navegador
driver = webdriver.Chrome()
driver.maximize_window()

# Navegando para a página de login
driver.get(url)

# Inserindo email e senha
email_input = driver.find_element(by='name', value='userLoginId')
email_input.send_keys(email)
senha_input = driver.find_element(by='name', value='password')
senha_input.send_keys(senha)

# Submetendo o formulário de login
senha_input.send_keys(Keys.RETURN)

# Aguardando a página carregar
time.sleep(5)

# Verificando se login foi bem-sucedido
if 'https://www.netflix.com/browse' in driver.current_url:
    print('Login bem-sucedido!')
else:
    print('Não foi possível fazer login.')

# Encerrando o navegador
driver.quit()
