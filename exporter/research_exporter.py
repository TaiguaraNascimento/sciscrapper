import xlsxwriter
from datetime import datetime
from base.referencia import Referencia




class ResearchExporter:

    numeracao = 0

    def __init__(self, endereco_de_exportacao: str) -> None:
        self.endereco_de_exportacao = endereco_de_exportacao
        self.arquivo_para_exportacao = xlsxwriter.Workbook(self.__gerar_nome_de_arquivo__(endereco_de_exportacao))
        self.sheet_de_saida = self.arquivo_para_exportacao.add_worksheet('relatorio')
        self.__adicionar_titulos__()
    

    def __gerar_nome_de_arquivo__(self, endereco_de_exportacao: str):
        nome_base = 'relatorio_webscrapper_'
        nome_base += datetime.now().strftime('%d%m%Y_%H%M%S')
        return endereco_de_exportacao + nome_base + '.xlsx'
    
    def __adicionar_titulos__(self):
        self.numeracao += 1
        self.sheet_de_saida.write('A' + str(self.numeracao), 'Linha')
        self.sheet_de_saida.write('B' + str(self.numeracao), 'Ano_de_publicacao')
        self.sheet_de_saida.write('C' + str(self.numeracao), 'Titulo_do_conteudo')
        self.sheet_de_saida.write('D' + str(self.numeracao), 'Data_hora_da_consulta')
        self.sheet_de_saida.write('E' + str(self.numeracao), 'Pagina_consultada')
        self.sheet_de_saida.write('F' + str(self.numeracao), 'Posicao_na_pagina')
        self.sheet_de_saida.write('G' + str(self.numeracao), 'Referencia')
        self.sheet_de_saida.write('H' + str(self.numeracao), 'Resumo')
        self.sheet_de_saida.write('I' + str(self.numeracao), 'Link_de_acesso')
        self.sheet_de_saida.write('J' + str(self.numeracao), 'Tipo_de_conteudo')
        self.sheet_de_saida.write('K' + str(self.numeracao), 'Nome_original_do_arquivo')
        self.sheet_de_saida.write('L' + str(self.numeracao), 'Nome_editado_do_arquivo')
        self.sheet_de_saida.write('M' + str(self.numeracao), 'Endereco_de_arquivo')

    def adicionar_referencia(self, referencia: Referencia):
        self.numeracao += 1
        self.sheet_de_saida.write('A' + str(self.numeracao), self.numeracao)
        self.sheet_de_saida.write('B' + str(self.numeracao), referencia.ano_de_publicacao)
        self.sheet_de_saida.write('C' + str(self.numeracao), referencia.titulo_do_conteudo)
        self.sheet_de_saida.write('D' + str(self.numeracao), referencia.data_hora_da_consulta)
        self.sheet_de_saida.write('E' + str(self.numeracao), referencia.pagina_consultada)
        self.sheet_de_saida.write('F' + str(self.numeracao), referencia.posicao_na_pagina)
        self.sheet_de_saida.write('G' + str(self.numeracao), referencia.referencia)
        self.sheet_de_saida.write('H' + str(self.numeracao), referencia.resumo)
        self.sheet_de_saida.write('I' + str(self.numeracao), referencia.link_de_acesso)
        self.sheet_de_saida.write('J' + str(self.numeracao), referencia.tipo_de_conteudo)
        self.sheet_de_saida.write('K' + str(self.numeracao), referencia.nome_original_do_arquivo)
        self.sheet_de_saida.write('L' + str(self.numeracao), referencia.nome_editado_do_arquivo)
        self.sheet_de_saida.write('M' + str(self.numeracao), referencia.endereco_de_arquivo)

    def fechar_arquivo(self):
        self.arquivo_para_exportacao.close()