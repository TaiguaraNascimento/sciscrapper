from keyword_factory.keyword_factory import KeywordFactory
from keyword_factory.keyword_combination import KeywordCombination
from keyword_factory.keyword_composition import KeywordComposition
from base.referencia import Referencia
from exporter.research_exporter import ResearchExporter
from webscrappers.webscrapper import Webscrapper
from webscrappers.fontes_de_pesquisa import FontesDePesquisa
from webscrappers.google_scholar import GoogleScholar



class Orquestrador:

    

    def __init__(self, fontes_de_pesquisa: list, termos_fixos: list, termos_variaveis: list, composicao_da_lista: KeywordComposition, incluir_variacao_de_termos: KeywordCombination, endereco_de_exportacao: str, ano_inicial_de_pesquisa: int, ano_final_de_pesquisa: int):
        
        # Colecionar fontes de pesquisa
        self.fontes_de_pesquisa = fontes_de_pesquisa

        # Coleciona todas as palavras-chave do projeto de pesquisa
        keywords_factory = KeywordFactory(termos_fixos, termos_variaveis, composicao_da_lista, incluir_variacao_de_termos)
        self.keywords = keywords_factory.obter_lista_de_palavras()

        # Gerar objeto de gravação de arquivos
        self.exporter = ResearchExporter(endereco_de_exportacao)

        self.ano_inicial_de_pesquisa = ano_inicial_de_pesquisa
        self.ano_final_de_pesquisa = ano_final_de_pesquisa

            
    def processar_pesquisa_nas_fontes(self):
        
        # Gerar um webscrapper compartilhado
        self.webscrapper = Webscrapper()

        for rpa in self.fontes_de_pesquisa:
            if rpa == FontesDePesquisa.GOOGLE_SCHOLAR:
                google_scholar = GoogleScholar(self.webscrapper, self.exporter, self.keywords, self.ano_inicial_de_pesquisa, self.ano_final_de_pesquisa)
                google_scholar.processar_pesquisa_das_keywords()





    def concluir_processo(self):
        self.exporter.fechar_arquivo()

