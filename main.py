
"""
Metodologia do Searcher

Biblioteca / Facade / Webscrapper

Cada tipo de fonte recebe um  webscrapper / ele não herda-ele tem / recebe o manipulador de arquivos / recebe os parametros / recebe comiinação de keywords

Orquestrador / recebe um wescrapper / recebe um endereço de gravação / grava or arquivos / numeração automática do arquivo / registra tempo de execução

keywords são uma factory, com lista de palavras / recebe parametros


PROCESSO
criar orquestrador
definir quais fontes quero executar
definir quais palavras-chave pesquisar
definir parametros de pesquisa
definir local de armazenagem de arquivos / relatório de execução
definir se quero execuar análise no chatpdf
definir questões a serem respondidas
mandar executar


na execução, uma factory inicia a pesquisa na fonte de dados
acessa o log principal e vai incluindo os dados;
salva os arquivos na pasta selecionada
ao concluir a execução fecha o log
chama o proximo webscrapper
grava a conclusão final e o tempo de trabalho
"""

from base.orquestrador import Orquestrador
from exporter.research_exporter import ResearchExporter


from keyword_factory.keyword_composition import KeywordComposition
from keyword_factory.keyword_combination import KeywordCombination
from webscrappers.fontes_de_pesquisa import FontesDePesquisa



termos_fixos = ["Governo digital", "Governo eletrônico", "GovTech" ]
termos_variaveis = ["Capacitação e desenvolvimento", "Serviços Públicos", "Governo", "Gestão pública", "Combate à corrupção", "Acesso à informação", "Computação em nuvem", "Controle", "Digitalização", "Efetividade", "Eficácia", "Empreendedorismo", "Eficiência", "E-Gov", "Geointeligência", "Governança", "Inovação", "Inteligência Artificial", "Machine Learning (Aprendizagem de Máquina)", "Mineração de dados", "Políticas públicas", "Recursos", "Segregação de funções", "Sistema eletrônico", "Smart Cities", "Cidades Inteligentes", "Software", "Tecnologia da informação", "Terceirização", "Transformação digital", "Transparência"]


fontes_de_pesquisa = [FontesDePesquisa.GOOGLE_SCHOLAR]

endereco_de_exportacao = 'C:\\Users\\Taiguara Nascimento\\OneDrive - Fundação Instituto de Administração\\__backup\\Desktop\\resultado\\'

orquestrador = Orquestrador(fontes_de_pesquisa, termos_fixos, termos_variaveis, KeywordComposition.COMBINAR_TERMOS_FIXOS, KeywordCombination.INCLUIR_MAIUSCULAS_E_REMOVER_CARACTERES_ESPECIAIS, endereco_de_exportacao, 2019, 2024)

orquestrador.processar_pesquisa_nas_fontes()

