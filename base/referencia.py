import datetime

class Referencia:

    def __init__(self):
        self.data_hora_da_consulta = str(datetime.datetime.now())
        self.pagina_consultada = ""
        self.posicao_na_pagina = ""
        self.titulo_do_conteudo = ""
        self.referencia = ""
        self.resumo = ""
        self.ano_de_publicacao = ""
        self.link_de_acesso = ""
        self.tipo_de_conteudo = ""
        self.nome_original_do_arquivo = ""
        self.nome_editado_do_arquivo = ""
        self.endereco_de_arquivo = ""

    def exibir_dados_da_publicacao(self):
        print('Ano_de_publicacao: ', self.ano_de_publicacao)
        print('Titulo_do_conteudo: ', self.titulo_do_conteudo)
        print('Data_hora_da_consulta: ', self.data_hora_da_consulta)
        print('Pagina_consultada: ', self.pagina_consultada)
        print('Posicao_na_pagina: ', self.posicao_na_pagina)
        print('Referencia: ', self.referencia)
        print('Resumo: ', self.resumo)
        print('Link_de_acesso: ', self.link_de_acesso)
        print('Tipo_de_conteudo: ', self.tipo_de_conteudo)
        print('Nome_original_do_arquivo: ', self.nome_original_do_arquivo)
        print('Nome_editado_do_arquivo: ', self.nome_editado_do_arquivo)
        print('Endereco_de_arquivo: ', self.endereco_de_arquivo)



