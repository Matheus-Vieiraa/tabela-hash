# tabela-hash
 #script Python realiza o processamento de um arquivo CSV, removendo colunas desnecessárias e aplicando hash SHA-256 em colunas específicas para anonimização ou proteção de dados sensíveis.
Como usar:
-Substitua 'Caminho do arquivo' pelo caminho do seu arquivo CSV de entrada
-Substitua 'coluna1','coluna2','coluna3' pelas colunas que deseja remover
-Substitua ['colunaA', 'colunaB'] pelas colunas que deseja anonimizar com hash
-Substitua 'caminho do arquivo/nome do arquivo.csv' pelo caminho de saída desejado
-Execute o script

# Observações:
-O hashing é irreversível, garanta que não precisa dos dados originais após o processamento

-Recomenda-se fazer backup do arquivo original antes de executar o script

-Para dados muito grandes, pode ser necessário otimizar o processo de hashing


# Funcionalidades:
-Leitura de dados: Lê um arquivo CSV com delimitador ';'

-Inspeção inicial: Mostra as primeiras linhas e nome de todas as colunas

-Limpeza de dados: Remove colunas especificadas (coluna1, coluna2, coluna3)

-Anonimização: Aplica hash SHA-256 nas colunas especificadas (colunaA, colunaB)

-Exportação: Salva o resultado em um novo arquivo CSV com o mesmo delimitador
