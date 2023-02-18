# Teste Para Verificar buscar um filme na Netflix pelo atributo 'src' da imagem
from selenium import webdriver

# Configurar o driver do navegador
driver = webdriver.Chrome()

# Acessar a página da Netflix
driver.get("https://www.netflix.com/br/browse/genre/34399")

# Encontrar o elemento com o xpath especificado
element = driver.find_element(
    by='xpath', value='//*[@id="appMountPoint"]/div/div[2]/main/section[5]/div/ul/li[2]/a/img')

# Imprimir o atributo 'src' da imagem
print(element.get_attribute('src'))

# Fechar o navegador
driver.quit()
