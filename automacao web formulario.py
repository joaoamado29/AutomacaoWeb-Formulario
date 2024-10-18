from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os
#### pegar dados ##########

caminho = os.getcwd()
arquivo = caminho + r"\Modulo 19 - Automação web\Projeto automacao de formulario web\produtos.csv"
df_produtos = pd.read_csv(arquivo)


#### automação ###########
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Usar o arquivo Formulario.html caso o site esteja off
navegador.get("https://dlp.hashtagtreinamentos.com/python/intensivao/tabela")
time.sleep(1)

formularios = navegador.find_elements(By.CLASS_NAME, 'form-campo')


# Percorrer a lista
# Pegar dados
for item, linha in df_produtos.iterrows():
    for i, campo in enumerate(formularios):
        dados = linha[i]
        dados = str(dados)
        campo.find_element(By.TAG_NAME, 'input').clear()  # Limpa o campo antes de preenchê-lo
        campo.find_element(By.TAG_NAME, 'input').send_keys(str(dados))
        campo.find_element(By.XPATH, '//*[@id="pgtpy-botao"]').click()
        campo.find_element(By.XPATH, '//*[@id="pgtpy-botao"]').click()
        if dados.lower() == 'nan':
            campo.find_element(By.XPATH, '//*[@id="obs"]').clear()