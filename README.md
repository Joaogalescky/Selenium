# Automação Web com Selenium

Neste repositório, você encontrará conceitos relacionados ao framework Selenium e as ferramentas que ele utiliza para as Automações Web. Além disso, há nesse repositório um exemplo de código de como automatizar o processo de preenchimento de um formulário de cadastro.

## Índice

- [Introdução](#introdução)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Exemplo de Uso](#exemplo-de-uso)
- [Referências](#referencias)

## Introdução

O Selenium é um conjunto de ferramentas que ajuda a automatizar navegadores da web. Em essência, ele permite que você controle o navegador de forma remota, simulando como um usuário interage com ele. Isso significa que você pode fazer coisas como clicar em botões, preencher formulários e navegar em sites automaticamente, em vez de fazer isso manualmente.


## Requisitos

Antes de começar, você precisará ter instalado:

- Python 3.12
- Pip (gerenciador de pacotes do Python)
- Um navegador (Chrome, Firefox, etc.)
- WebDriver correspondente ao navegador escolhido (ex: ChromeDriver para Chrome)

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/ACPedrosa/Selenium.git
    cd Selenium
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Baixe o WebDriver correspondente ao seu navegador e adicione ao PATH.

## Exemplo de Uso

Exemplo básico de como usar o Selenium para abrir uma página web e realizar uma ação simples, como buscar algo no Google:

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inicializa o navegador
driver = webdriver.Chrome()

# Abre o Google
driver.get("http://www.google.com")

# Encontra a caixa de busca
search_box = driver.find_element("name", "q")

# Digita uma pesquisa
search_box.send_keys("Automação com Selenium")
search_box.send_keys(Keys.RETURN)

# Fecha o navegador após 5 segundos
driver.implicitly_wait(5)
driver.quit()
```
## Referências

Selenium. Selenium Documentation. Disponível em: https://www.selenium.dev/pt-br/documentation/overview/. Acesso em: 29 set. 2024.

Selenium. WebDriver Documentation. Disponível em: https://www.selenium.dev/pt-br/documentation/webdriver/. Acesso em: 29 set. 2024.

Selenium. Selenium WebDriver: Waits. Disponível em: https://www.selenium.dev/documentation/webdriver/waits/. Acesso em: 29 set. 2024.
