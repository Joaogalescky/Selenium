'''
    author: Ana Caroline Pedrosa e Silva
    date: 29 - 09 - 2024
    name: cadastro_auto.py
'''
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Permite que o navegador permaneça aberto

servico = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=servico, options=chrome_options)

#maximizar a janela
driver.maximize_window()

# Abre a página
driver.get("http://127.0.0.1:5501/page/index.html#")

#criando objeto wait
wait = WebDriverWait(driver, 10)

# Espera até que o campo de texto esteja visível e habilitado
text_box = wait.until(
    EC.element_to_be_clickable((By.ID, "firstname"))
)

#preenche com o nome
text_box.send_keys("Ana Caroline")

time.sleep(4)

# Preenchendo o sobrenome
lastname_box = wait.until(
    EC.element_to_be_clickable((By.ID, "lastname"))
)

lastname_box.send_keys("Pedrosa")

time.sleep(4)

# Preenchendo o e-mail
email_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "email"))
)

email_box.send_keys("ana.pedrosa@example.com")

time.sleep(4)


#preenchendo número de telefone
telefone_box = wait.until(
    EC.element_to_be_clickable((By.ID, "number"))
)

telefone_box.send_keys("99 9999-9999")

time.sleep(4)

#preenchendo a senha
password_box = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))
)

password_box.send_keys("1234567")

time.sleep(4)

#preenchendo a senha
conf_password_box = wait.until(
    EC.element_to_be_clickable((By.ID, "confirmPassword"))
)

conf_password_box.send_keys("1234567")

time.sleep(4)


# Selecionando o botão de opção "Feminino"
female_radio = wait.until(
    EC.element_to_be_clickable((By.ID, "female"))
)
female_radio.click()

time.sleep(4)

#botão de confirmação
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[4]/button'))
)

button.click()



