import csv
import ssl
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from parsel import Selector

# configurando para sites com certificado auto assinado
ssl._create_default_https_context = ssl._create_unverified_context

# configurando arquivo csv
arquivo = csv.writer(open('mercado_livre.csv', 'w', encoding='utf-8'))
arquivo.writerow(['Produto', 'Preco', 'Link'])

# configurando no modo background
options = webdriver.FirefoxOptions()
options.add_argument("--headless")

# configurando o driver
driver = webdriver.Firefox(options=options, executable_path='geckodriver')

# pesquisando produto
driver.get('https://mercadolivre.com.br/')
busca = driver.find_element(By.NAME, 'as_word')
busca.send_keys('batata')
busca.send_keys(Keys.RETURN)
sleep(3)

try:
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/button').click()
except:
    pass

# entrega full
driver.find_element(By.XPATH, '/html/body/main/div/div[1]/aside/form/div[1]/ul/li/section/div/label/span[2]').click()

# capturar os produtos
produtos = driver.find_elements(By.XPATH, '//div[@class="ui-search-item__group ui-search-item__group--title"]/a')
produtos_lista = [produto.get_attribute('href') for produto in produtos]

count = 0
for produto in produtos_lista:
    driver.get(produto)
    sleep(2)

    response = Selector(text=driver.page_source)
    try:
        nome = response.xpath('/html/body/main/div[2]/div[4]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/h1/text()').extract()[0]
        inteiro = response.xpath('/html/body/main/div[2]/div[4]/div[1]/div[1]/div/div[1]/div[2]/div[3]/div[1]/span/span[3]/text()').extract()[0]
        centavo = response.xpath('/html/body/main/div[2]/div[4]/div[1]/div[1]/div/div[1]/div[2]/div[3]/div[1]/span/span[4]/text()').extract()[0]
        #print(f'Produto: {nome}, Valor: R${inteiro},{centavo}, Link: {produto}')
        arquivo.writerow([nome, inteiro + ',' + centavo, produto])
    except:
        pass

    count += 1
    if count >= 3:
        break

driver.close()


