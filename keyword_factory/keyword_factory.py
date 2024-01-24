
import re
from unidecode import unidecode
from keyword_factory.keyword_combination import KeywordCombination
from keyword_factory.keyword_composition import KeywordComposition


class KeywordFactory:

    def __init__(self, termos_fixos: list, termos_variaveis: list, composicao_da_lista: KeywordComposition, incluir_variacao_de_termos: KeywordCombination):

        self.composicao_da_lista = composicao_da_lista
        self.incluir_variacao_de_termos = incluir_variacao_de_termos

        self.lista_variavel = termos_variaveis
        self.termos_fixos = termos_fixos

        self.__colocar_todos_os_termos_em_minusculas__()
        
    def __remover_caracteres_especiais__(self, texto_original):
        try:
            padrao = r'[^a-zA-Z0-9\s]'
            retorno = unidecode(texto_original)
            retorno = re.sub(padrao, ' ', retorno)
            return retorno
        except:
            return ""

    def __colocar_todos_os_termos_em_minusculas__(self):
        novos_termos_fixos = [item.lower() for item in self.termos_fixos] 
        self.termos_fixos = novos_termos_fixos

        novos_termos_variaveis = [item.lower() for item in self.lista_variavel] 
        self.lista_variavel = novos_termos_variaveis

    def obter_lista_de_palavras(self):

        lista_final_de_saida = []

        if self.composicao_da_lista == KeywordComposition.NAO_COMBINAR_TERMOS_FIXOS:
            for termos_variaveis in self.lista_variavel:
                termo_de_pesquisa = termos_variaveis
                lista_final_de_saida.extend(self.__obter_lista_de_variacoes_possiveis_por_termo__(termo_de_pesquisa))

        elif self.composicao_da_lista == KeywordComposition.COMBINAR_TERMOS_FIXOS:
            for termo_fixo in self.termos_fixos:
                for termos_variaveis in self.lista_variavel:
                    termo_de_pesquisa = termo_fixo + " " + termos_variaveis
                    lista_final_de_saida.extend(self.__obter_lista_de_variacoes_possiveis_por_termo__(termo_de_pesquisa))

        return lista_final_de_saida

    def __obter_lista_de_variacoes_possiveis_por_termo__(self, termo: str):

        lista_completa_de_retorno = []

        # MANTER ORIGINAL
        lista_completa_de_retorno.append(termo)

        # INCLUIR MAIUSCULAS
        if self.incluir_variacao_de_termos == KeywordCombination.INCLUIR_MAIUSCULAS:
            lista_completa_de_retorno.append(termo.upper())

        # INCLUIR MAIUSCULAS E REMOVER ESPECIAIS
        if self.incluir_variacao_de_termos == KeywordCombination.INCLUIR_MAIUSCULAS_E_REMOVER_CARACTERES_ESPECIAIS:
            lista_completa_de_retorno.append(self.__remover_caracteres_especiais__(termo))
            lista_completa_de_retorno.append(termo.upper())
            lista_completa_de_retorno.append(self.__remover_caracteres_especiais__(termo.upper()))

        # INCLUIR REMOVER ESPECIAIS
        if self.incluir_variacao_de_termos == KeywordCombination.REMOVER_CARACTERES_ESPECIAIS:
            lista_completa_de_retorno.append(self.__remover_caracteres_especiais__(termo))

        return lista_completa_de_retorno


