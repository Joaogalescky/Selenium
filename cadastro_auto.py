'''
Preenchendo formulário de cadastro de forma automática - Selenium

Name: cadastro_auto.py
Descripition: script para preencher um formulário de cadastro de forma automática utilizando o Selenium

Author: Ana Caroline P. e Silva
Version: 4.0 
Creation Date: 27/09/2024
Last Modified: 01/10/2024

'''
import time
import webbrowser
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

# Maximizar a janela
driver.maximize_window()

# Abre a página
driver.get("https://acpedrosa.github.io/Cadastro_teste/")

# Criando objeto wait
wait = WebDriverWait(driver, 10)

# Espera até que o campo de texto esteja visível e habilitado
text_box = wait.until(
    EC.element_to_be_clickable((By.ID, "firstname"))
)
# Preenche com o nome
text_box.send_keys("João")

# time.sleep(4)

# Preenchendo o sobrenome
lastname_box = wait.until(
    EC.element_to_be_clickable((By.ID, "lastname")) #ou By.NAME
)
lastname_box.send_keys("Vitor Campõe Galescky")

# time.sleep(4)

# Preenchendo o email
email_box = wait.until(
    EC.element_to_be_clickable((By.ID, "email"))
)
email_box.send_keys("joao@email.com")