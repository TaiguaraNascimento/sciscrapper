from base.referencia import Referencia
from webscrappers.webscrapper import Webscrapper
from exporter.research_exporter import ResearchExporter

class GoogleScholar:

    def __init__(self, webscrapper: Webscrapper, exporter: ResearchExporter,  keywords: list, ano_inicial: int, ano_final: int):

        self.exporter = exporter
        self.keywords = keywords
        self.webscrapper = webscrapper
        self.ano_inicial = ano_inicial
        self.ano_final = ano_final


    def processar_pesquisa_das_keywords(self):

        for keyword in self.keywords:
            print('>>>>>>>>> processar ........ ', keyword)
            self.pesquisar_resultado(keyword)

        self.exporter.fechar_arquivo()

        self.webscrapper.__manter_janela_aberta__()



    def pesquisar_resultado(self, termo_pesquisado: str):

        processamento = True
        
        # Controle de páginas
        pagina = 0


        while (processamento):
            
            # Realizar a primeira execução
            pagina += 1

            # Compõe a URL de início da pesquisa
            url_base = self.__compor_url_de_pesquisa__(termo_pesquisado, self.ano_inicial, self.ano_final, pagina)

            # Acessar a página antes de começar a captura
            self.webscrapper.acessar_pagina(url_base)

            # Pausa para resolver captcha
            passa_captcha = False
            while(passa_captcha == False):
                captcha = "/html/body/div[1]/div[10]/div[2]/div/form/h1"
                if self.webscrapper.conteudo_de_elemento_especifico_xpath(captcha) == "Mostre que você não é um robô":
                    # Antes de começar o processamento
                    self.webscrapper.__aguardar_operacao__(15, False)
                else:
                    passa_captcha = True
            
            # Processar captura de dados
            resultados = self.__retornar_resultados_da_pagina_especifica__(pagina)
            
            # Processar gravação de todas as pulicações obtidas
            for item in resultados:
                self.exporter.adicionar_referencia(item)
                
                # Salvar arquivo se aplicável
                try:
                    self.webscrapper.fazer_download_do_arquivo(item.endereco_de_arquivo¹, self.exporter.endereco_de_exportacao, self.exporter.numeracao)
                except:
                    pass





            # Verificar se o mais/avançar existe
            botao_avancar_primeira_execucao = '/html/body/div/div[10]/div[2]/div[3]/div[3]/div[2]/center/table/tbody/tr/td[12]/a/b'
            botao_avancar_proximas_execucoes = '/html/body/div/div[10]/div[2]/div[3]/div[3]/div[2]/center/table/tbody/tr/td[12]/a/b'

            if pagina == 1:
                if self.webscrapper.verificar_se_objeto_por_xpath_existe(botao_avancar_primeira_execucao):
                    pass
                else:
                    processamento = False
                    print('Não foi encontrada a paginação de primeira página')
            else:
                if self.webscrapper.verificar_se_objeto_por_xpath_existe(botao_avancar_proximas_execucoes):
                    pass
                else:
                    processamento = False
                    print('Não foi encontrada a paginação contínua')



    def __obter_dados_de_publicacao__(self, publicacao, posicao_da_pagina: int, posicao_da_publicacao_na_pagina: int):

        referencia = Referencia()

        referencia.titulo_do_conteudo = self.webscrapper.conteudo_de_elemento_especifico_por_objeto(
            self.webscrapper.obter_objeto_complementar(publicacao, 'div[2]/h3/a')).replace('[PDF] ', '').replace('[HTML] ', '')

        referencia.pagina_consultada = posicao_da_pagina

        referencia.posicao_na_pagina = posicao_da_publicacao_na_pagina

        def obter_link_de_acesso():
            link = self.webscrapper.link_de_elemento_especifico_por_objeto(self.webscrapper.obter_objeto_complementar(publicacao, 'div[2]/h3/a'))
            return link

        referencia.link_de_acesso = obter_link_de_acesso()

        def tipo_de_conteudo():
            texto = self.webscrapper.conteudo_de_elemento_especifico_por_objeto(
                self.webscrapper.obter_objeto_complementar(publicacao, 'div[1]/div/div/a'))

            if texto.lower().find('pdf') != -1:
                return "PDF"
            elif texto.lower().find('html') != -1:
                return "HTML"
            else:
                return "outro"

        referencia.tipo_de_conteudo = tipo_de_conteudo()

        referencia.endereco_de_arquivo = self.webscrapper.link_de_elemento_especifico_por_objeto(
            self.webscrapper.obter_objeto_complementar(publicacao, 'div[1]/div/div/a'))

        referencia.referencia = self.webscrapper.conteudo_de_elemento_especifico_por_objeto(
            self.webscrapper.obter_objeto_complementar(publicacao, 'div[2]/div[1]'))


        def ano_de_publicacao(referencia: Referencia):
            for ano in range(self.ano_inicial, self.ano_final+1):
                try:
                    if referencia.referencia.find(str(ano)) != -1:
                        return str(ano)
                except:
                    return "Não identificado"

        referencia.ano_de_publicacao = ano_de_publicacao(referencia)

        referencia.resumo = self.webscrapper.conteudo_de_elemento_especifico_por_objeto(
            self.webscrapper.obter_objeto_complementar(publicacao, 'div[2]/div[2]'))

        return referencia



    def __retornar_resultados_da_pagina_especifica__(self, posicao_da_pagina: int):

        lista_de_publicacoes = []

        self.webscrapper.__aguardar_operacao__(3, True)

        endereco_quadro_com_todas_as_publicacoes = "/html/body/div[1]/div[10]/div[2]/div[3]/div[2]/div"
        quadro_com_todas_as_publicacoes = self.webscrapper.obter_lista_de_objetos_por_xpath(endereco_quadro_com_todas_as_publicacoes)

        print('Publicações encontradas: ', len(quadro_com_todas_as_publicacoes), ' | Posição da página: ', posicao_da_pagina)

        publicacoes = 0

        for publicacao in quadro_com_todas_as_publicacoes:
            publicacoes += 1
            referencia = self.__obter_dados_de_publicacao__(publicacao, posicao_da_pagina, publicacoes)
            lista_de_publicacoes.append(referencia)
            

        return lista_de_publicacoes
    


    def __compor_url_de_pesquisa__(self, termo_pesquisado: str, ano_inicial: int, ano_final: int, pagina: int):

        url_base = "https://scholar.google.com/scholar?q=[#1]&hl=pt-BR&lr=lang_pt&as_sdt=0%2C5&as_ylo=[#2]&as_yhi=[#3]"

        def converter_string_de_pesquisa(termo_original: str):
            resultado = termo_original.replace(" ", "+").lower()
            return resultado

        resultado = url_base.replace("[#1]", converter_string_de_pesquisa(termo_pesquisado)).replace("[#2]", str(ano_inicial)).replace("[#3]", str(ano_final))

        if pagina > 1:
            resultado += "&start=" + str((pagina -1)*10 )

        print('Pesquisando na URL: ', resultado)

        return resultado