

    def fazer_download_do_arquivo(self, url_arquivo:str, tipo_arquivo: str, endereco_do_arquivo: str, numero_do_arquivo: int):

        # Corrigindo a extensão
        def novo_nome_de_arquivo(numero_do_arquivo: int, endereco_do_arquivo: str, nome_arquivo_original: str, tipo_arquivo: str):

            extensao_da_lista = tipo_arquivo.lower()
            extensao_do_arquivo_para_download = nome_arquivo_original[-len(extensao_da_lista):].lower()

            print('>>> ', extensao_da_lista, extensao_do_arquivo_para_download)

            if extensao_da_lista == extensao_do_arquivo_para_download:
                novo_caminho = os.path.join(endereco_do_arquivo, str(numero_do_arquivo) + "_" + nome_arquivo_original)
            else:
                novo_caminho = os.path.join(endereco_do_arquivo, str(numero_do_arquivo) + "_" + nome_arquivo_original) + tipo_arquivo

            return novo_caminho


        #try:
        resposta = requests.get(url_arquivo)

        print('baixando...', url_arquivo)
        
        
        
        caminho_atual = os.path.join(endereco_do_arquivo, nome_arquivo)
        
        print(novo_nome_de_arquivo(numero_do_arquivo, endereco_do_arquivo, nome_arquivo, tipo_arquivo))

        with open(caminho_atual, 'wb') as arquivo:
            arquivo.write(resposta.content)

        os.rename(caminho_atual, novo_nome_de_arquivo(numero_do_arquivo, endereco_do_arquivo, nome_arquivo))
        
        print(str(numero_do_arquivo), ': arquivo baixado!')

        #except:
            #print(str(numero_do_arquivo), ': o download do arquivo não foi realizado.')
        



        

    def baixar_e_organizar_arquivos(self, endereco_de_download: str, endereco_do_arquivo: str, numero_do_arquivo: str):

        
                
        def corrigir_extensao_do_arquivo(nome_arquivo: str):

            posicao = nome_arquivo.lower().find('pdf')
            novo_nome = ''
            if posicao != -1:
                novo_nome = nome_arquivo[:posicao+3]
            else:
                novo_nome = nome_arquivo + '.pdf'

            return novo_nome
            
        def nome_atual_do_arquivo():
            nome_arquivo = endereco_de_download.split('/')[-1]
            return nome_arquivo

        def caminho_atual_do_arquivo():
            caminho_atual = os.path.join(endereco_do_arquivo, nome_atual_do_arquivo())
            return caminho_atual

        def novo_nome_de_arquivo(nome_atual_do_arquivo: str, numero_do_arquivo: int):

            novo_nome = nome_atual_do_arquivo
            remover = ['#', '/', '\\', '@', '*', '!', "$", '=', '?', ':']
            for caractere in remover:
                novo_nome = novo_nome.replace(caractere, '')

            novo_nome = catalogar_numero(numero_do_arquivo) + '__' + corrigir_extensao_do_arquivo(novo_nome)

            return novo_nome

        if endereco_de_download != None:

            self.fazer_download_do_arquivo(endereco_do_arquivo)
            

        else:
            print('Não há arquivo especificado para download.')












        -----------------------------


        from base.referencia import Referencia
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import requests
import os

import time

class Webscrapper:

    def __init__(self):
        self.__configurar_webdriver__()




    def __configurar_webdriver__(self):
        print("CONFIGURANDO WEBDRIVER")
        self.driver_options = webdriver.ChromeOptions()
        self.driver_options.add_argument("start-maximized")
        self.driver_options.add_argument('--disable-notifications')
        self.driver_options.add_argument('--disable-gpu')
        self.driver_options.add_argument('--incognito')
    
        self.driver = webdriver.Chrome(
            options=self.driver_options)





    def __manter_janela_aberta__(self):
        while (True):
            pass



    def __aguardar_operacao__(self, timer: int, silecioso: bool) -> None:
        if silecioso == False:
            texto = "| AGUARDANDO |" + ("-" * 50) + "|"
            print(texto)
            for num in range(1, timer + 1):
                time.sleep(1)
                print('  Aguardando', '.' * num)
            print("|", ('-' * (len(texto)-2)), "|")
        else:
            time.sleep(timer)


    def acessar_pagina(self, url_de_acesso):
        self.driver.get(url_de_acesso)


    def obter_objeto_especifico_por_xpath(self, objeto_xpath):
        try:
            return self.driver.find_element(By.XPATH, objeto_xpath)
        except:
            return None


    def obter_lista_de_objetos_por_xpath(self, objeto_xpath):
        try:
            return self.driver.find_elements(By.XPATH, objeto_xpath)
        except:
            return None


    def obter_lista_de_objetos_por_elemento(self, objeto: WebElement, objeto_xpath: str):
        try:
            return objeto.find_elements(By.XPATH, objeto_xpath)
        except:
            return None


    def conteudo_de_elemento_especifico_xpath(self, objeto_xpath):
        try:
            return self.obter_objeto_especifico_por_xpath(objeto_xpath).text
        except:
            return "x"


    def conteudo_de_elemento_especifico_por_objeto(self, objeto: WebElement):
        try:
            return objeto.text
        except:
            return "x"


    def link_de_elemento_especifico_xpath(self, objeto_xpath):
        try:
            return self.obter_objeto_especifico_por_xpath(objeto_xpath).get_attribute('href')
        except:
            return "x"


    def link_de_elemento_especifico_por_objeto(self, objeto: WebElement):
        try:
            return objeto.get_attribute("href")
        except:
            return "x"


    def obter_objeto_complementar(self, objeto: WebElement, objeto_xpath):
        try:
            return objeto.find_element(By.XPATH, objeto_xpath)
        except:
            return objeto



    def verificar_se_objeto_por_xpath_existe(self, objeto_xpath):
        try:
            resultado = self.obter_objeto_especifico_por_xpath(objeto_xpath).text
            print(resultado)
            if resultado != None or resultado != "":
                return True
            else:
                return False
        except:
            return False


    def obter_xpath_de_objeto(self, objeto: WebElement):
        try:
            return objeto.get_attribute("xpath")
            objeto.get_attribute
        except:
            return "x"
        






    
    def fazer_download_do_arquivo(self, endereco_de_download: str, endereco_do_arquivo: str, numero_do_arquivo: str):
        try:
            resposta = requests.get(endereco_de_download)
            nome_arquivo = endereco_de_download.split('/')[-1]
            caminho_atual = os.path.join(endereco_do_arquivo, nome_arquivo)

            with open(caminho_atual, 'wb') as arquivo:
                arquivo.write(resposta.content)
            
            novo_caminho = os.path.join(endereco_do_arquivo, str(numero_do_arquivo) + "_" + nome_arquivo)
            os.rename(caminho_atual, novo_caminho)
            
            print(str(numero_do_arquivo), ': arquivo baixado!')

        except:
            print(str(numero_do_arquivo), ': o download do arquivo não foi realizado.')