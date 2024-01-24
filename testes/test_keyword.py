import pytest
from keyword_factory.keyword_factory import KeywordFactory
from keyword_factory.keyword_composition import KeywordComposition
from keyword_factory.keyword_combination import KeywordCombination


def test_instanciacao_de_objeto():
    termos_fixos = ['fixo']
    termos_variaveis = ['variaveis']
    keyword_factory = KeywordFactory(termos_fixos, termos_variaveis, KeywordComposition.NAO_COMBINAR_TERMOS_FIXOS, KeywordCombination.MANTER_ORIGINAL)
    assert isinstance(keyword_factory, KeywordFactory)


def test_remover_acentuacao():
    termos_fixos = ['fixo']
    termos_variaveis = ['variaveis']
    keyword_factory = KeywordFactory(termos_fixos, termos_variaveis, KeywordComposition.NAO_COMBINAR_TERMOS_FIXOS, KeywordCombination.MANTER_ORIGINAL)
    texto_puro = keyword_factory.__remover_caracteres_especiais__("óbvio Avião Lâmpada Óxidos Pulmões Ênfase Ética Ático à Moça")
    assert texto_puro == "obvio Aviao Lampada Oxidos Pulmoes Enfase Etica Atico a Moca"

def test_avaliar_atribuicoes_de_configuracoes():
    termos_fixos = ['fixo']
    termos_variaveis = ['variaveis']
    keyword_factory = KeywordFactory(termos_fixos, termos_variaveis, KeywordComposition.NAO_COMBINAR_TERMOS_FIXOS, KeywordCombination.MANTER_ORIGINAL)
    assert keyword_factory.composicao_da_lista == KeywordComposition.NAO_COMBINAR_TERMOS_FIXOS


def test_testar_lista_de_variacoes_possiveis_por_termo_sem_combinar_lista():
    termos_fixos = ['fixo']
    termos_variaveis = ['variáveis', 'ótimo', 'ávido']
    keyword_factory = KeywordFactory(termos_fixos, termos_variaveis, KeywordComposition.NAO_COMBINAR_TERMOS_FIXOS, KeywordCombination.MANTER_ORIGINAL)

    palavras = keyword_factory.obter_lista_de_palavras()

    resultado_esperado = ['variáveis', 'ótimo', 'ávido']

    assert palavras == resultado_esperado


def test_testar_lista_de_variacoes_possiveis_por_termo_combinando_lista():
    termos_fixos = ['termo fixo']
    termos_variaveis = ['variáveis', 'ótimo', 'ávido', 'marcação', 'ênfase']
    keyword_factory = KeywordFactory(termos_fixos, termos_variaveis, KeywordComposition.COMBINAR_TERMOS_FIXOS, KeywordCombination.MANTER_ORIGINAL)

    palavras = keyword_factory.obter_lista_de_palavras()

    resultado_esperado = ['termo fixo variáveis', 'termo fixo ótimo', 'termo fixo ávido',  'termo fixo marcação', 'termo fixo ênfase']

    assert palavras == resultado_esperado


def test_testar_lista_de_variacoes_possiveis_por_termo_combinando_lista_e_com_variacoes():
    termos_fixos = ['termo fixo']
    termos_variaveis = ['variáveis', 'ótimo', 'ávido', 'marcação', 'ênfase']
    keyword_factory = KeywordFactory(termos_fixos, termos_variaveis, KeywordComposition.COMBINAR_TERMOS_FIXOS, KeywordCombination.INCLUIR_MAIUSCULAS_E_REMOVER_CARACTERES_ESPECIAIS)

    palavras = keyword_factory.obter_lista_de_palavras()

    resultado_esperado = ['termo fixo variáveis', 
                          'termo fixo variaveis', 
                          'TERMO FIXO VARIÁVEIS', 
                          'TERMO FIXO VARIAVEIS', 
                          'termo fixo ótimo', 
                          'termo fixo otimo', 
                          'TERMO FIXO ÓTIMO', 
                          'TERMO FIXO OTIMO', 
                          'termo fixo ávido',  
                          'termo fixo avido',  
                          'TERMO FIXO ÁVIDO', 
                          'TERMO FIXO AVIDO', 
                          'termo fixo marcação', 
                          'termo fixo marcacao', 
                          'TERMO FIXO MARCAÇÃO', 
                          'TERMO FIXO MARCACAO', 
                          'termo fixo ênfase',
                          'termo fixo enfase',
                          'TERMO FIXO ÊNFASE',
                          'TERMO FIXO ENFASE']

    assert palavras == resultado_esperado


def test_testar_lista_de_variacoes_possiveis_por_termo_sem_combinar_lista_mas_com_variacoes():
    termos_fixos = ['termo fixo']
    termos_variaveis = ['variáveis', 'ótimo', 'ávido', 'marcação', 'ênfase']
    keyword_factory = KeywordFactory(termos_fixos, termos_variaveis, KeywordComposition.NAO_COMBINAR_TERMOS_FIXOS, KeywordCombination.INCLUIR_MAIUSCULAS_E_REMOVER_CARACTERES_ESPECIAIS)

    palavras = keyword_factory.obter_lista_de_palavras()

    resultado_esperado = ['variáveis', 
                          'variaveis', 
                          'VARIÁVEIS', 
                          'VARIAVEIS', 
                          'ótimo', 
                          'otimo', 
                          'ÓTIMO', 
                          'OTIMO', 
                          'ávido',  
                          'avido',  
                          'ÁVIDO', 
                          'AVIDO', 
                          'marcação', 
                          'marcacao', 
                          'MARCAÇÃO', 
                          'MARCACAO', 
                          'ênfase',
                          'enfase',
                          'ÊNFASE',
                          'ENFASE']

    assert palavras == resultado_esperado


def test_testar_multiplas_combinacoes():
    termos_fixos = ['termo1', 'termo2', 'termo3']
    termos_variaveis = ['variavel1', 'variavel2', 'variavel3']
    keyword_factory = KeywordFactory(termos_fixos, termos_variaveis, KeywordComposition.COMBINAR_TERMOS_FIXOS, KeywordCombination.MANTER_ORIGINAL)

    palavras = keyword_factory.obter_lista_de_palavras()

    resultado_esperado = ['termo1 variavel1', 
                          'termo1 variavel2', 
                          'termo1 variavel3', 
                          'termo2 variavel1', 
                          'termo2 variavel2', 
                          'termo2 variavel3', 
                          'termo3 variavel1', 
                          'termo3 variavel2', 
                          'termo3 variavel3']

    assert palavras == resultado_esperado


def test_testar_multiplas_combinacoes_com_variacoes():
    termos_fixos = ['termo1', 'termo2', 'termo3']
    termos_variaveis = ['variável1', 'carniça', 'ênclise3']
    keyword_factory = KeywordFactory(termos_fixos, termos_variaveis, KeywordComposition.COMBINAR_TERMOS_FIXOS, KeywordCombination.INCLUIR_MAIUSCULAS_E_REMOVER_CARACTERES_ESPECIAIS)

    palavras = keyword_factory.obter_lista_de_palavras()

    resultado_esperado = [

        'termo1 variável1',
        'termo1 variavel1',
        'TERMO1 VARIÁVEL1',
        'TERMO1 VARIAVEL1',
        'termo1 carniça',
        'termo1 carnica',
        'TERMO1 CARNIÇA',
        'TERMO1 CARNICA',
        'termo1 ênclise3',
        'termo1 enclise3',
        'TERMO1 ÊNCLISE3',
        'TERMO1 ENCLISE3',
        'termo2 variável1',
        'termo2 variavel1',
        'TERMO2 VARIÁVEL1',
        'TERMO2 VARIAVEL1',
        'termo2 carniça',
        'termo2 carnica',
        'TERMO2 CARNIÇA',
        'TERMO2 CARNICA',
        'termo2 ênclise3',
        'termo2 enclise3',
        'TERMO2 ÊNCLISE3',
        'TERMO2 ENCLISE3',
        'termo3 variável1',
        'termo3 variavel1',
        'TERMO3 VARIÁVEL1',
        'TERMO3 VARIAVEL1',
        'termo3 carniça',
        'termo3 carnica',
        'TERMO3 CARNIÇA',
        'TERMO3 CARNICA',
        'termo3 ênclise3',
        'termo3 enclise3',
        'TERMO3 ÊNCLISE3',
        'TERMO3 ENCLISE3'
    ]

    assert palavras == resultado_esperado

