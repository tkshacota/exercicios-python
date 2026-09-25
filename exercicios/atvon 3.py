# Importa o módulo sqlite3 para criar e manipular bancos de dados relacionais em arquivo local
import sqlite3
# Importa o pandas para carregar, estruturar, tratar e analisar os dados através de DataFrames
import pandas as pd
# Importa o pyplot do matplotlib para configurar janelas, eixos, títulos e renderizar gráficos
import matplotlib.pyplot as plt
# Importa o seaborn para criar gráficos estatísticos com visual moderno e paletas de cores prontas
import seaborn as sns

# Estabelece a conexão com o banco SQLite 'dados_vendas.db' (cria o arquivo se ele não existir)
conexao = sqlite3.connect('dados_vendas.db')
# Cria o cursor, que é o objeto executor responsável por enviar e rodar instruções SQL no banco
cursor = conexao.cursor()

# Apaga a tabela caso já exista, permitindo reexecutar o script sem duplicar registros ou acusar erro
cursor.execute('DROP TABLE IF EXISTS vendas1')

# Cria a estrutura da tabela com tipos de dados adequados:
# - id_venda: chave primária com incremento automático a cada nova linha
# - Data_venda: campo no formato de data (AAAA-MM-DD)
# - Produto e Categoria: campos de texto
# - Valor_venda: tipo real para números com casas decimais (ponto flutuante)
cursor.execute('''
CREATE TABLE vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    Data_venda DATE,
    Produto TEXT,
    Categoria TEXT,
    Valor_venda REAL
)
''')

# Insere 14 registros de vendas distribuídos ao longo dos meses de 2023 para compor a base de teste
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''')
# Confirma e salva permanentemente as inserções realizadas no arquivo do banco de dados
conexao.commit()

# Executa uma consulta SQL buscando todas as colunas da tabela e carrega o resultado num DataFrame do Pandas
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

# Converte os textos da coluna 'Data_venda' para o tipo datetime, permitindo ordenação cronológica correta
df_vendas['Data_venda'] = pd.to_datetime(df_vendas['Data_venda'])

# Imprime o resumo estrutural do DataFrame: total de linhas, nomes das colunas, tipos e valores ausentes
print(df_vendas.info())

# Exibe as 5 primeiras linhas da tabela para conferência dos dados carregados
print("\nPrimeiras linhas:")
print(df_vendas.head())

# Calcula o faturamento total somando todos os valores da coluna 'Valor_venda'
faturamento_total = df_vendas['Valor_venda'].sum()

# Calcula o tíquete médio dividindo o total vendido pela quantidade de vendas realizadas
ticket_medio = df_vendas['Valor_venda'].mean()

# Imprime o faturamento formatado em reais com separador de milhar e duas casas decimais
print(f"\nfaturamento_total: R$ {faturamento_total:,.2f}")
print(f"ticket médio por venda: R$ {ticket_medio:,.2f}\n")

# Agrupa as vendas por categoria e calcula simultaneamente: contagem de vendas, soma e valor médio
# O reset_index() transforma a coluna 'Categoria' (que era o índice do agrupamento) em coluna comum do DataFrame
analise_categorias = df_vendas.groupby('Categoria')['Valor_venda'].agg(['count', 'sum', 'mean']).reset_index()

# Renomeia as colunas resultantes para títulos claros e intuitivos
analise_categorias.columns = ['Categoria', 'Qtd_vendas', 'Total_vendido', 'Media_venda']

# Exibe a tabela com o resumo estatístico por categoria no terminal
print("desempenho por categoria:")
print(analise_categorias)

# Define o tamanho da tela do gráfico de barras (8 polegadas de largura por 5 de altura)
plt.figure(figsize=(8, 5))

# Cria o gráfico de barras com Seaborn:
# - x='Categoria': categorias no eixo horizontal
# - y='Total_vendido': valores faturados no eixo vertical
# - hue='Categoria' e legend=False: atribui uma cor diferente por barra sem exibir legenda duplicada
# - palette='viridis': paleta de cores moderna com bom contraste
sns.barplot(data=analise_categorias, x='Categoria', y='Total_vendido', hue='Categoria', palette='viridis', legend=False)

# Adiciona título principal e rótulos aos eixos horizontal e vertical
plt.title('Total de vendas por categoria', fontsize=14, pad=10)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Valor total (R$)', fontsize=12)

# Adiciona linhas de grade horizontais tracejadas para facilitar a leitura visual dos valores monetários
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibe a janela com o gráfico de barras
plt.show()

# Define o tamanho da janela para o gráfico de linhas (10 de largura por 5 de altura)
plt.figure(figsize=(10, 5))

# Cria o gráfico de linhas temporal com Seaborn:
# - sort_values('Data_venda'): garante que os pontos sigam a ordem temporal cronológica dos meses
# - x='Data_venda' e y='Valor_venda': eixos de tempo e de valor da venda
# - marker='o': desenha círculos em cada ponto de venda
# - color='b': define a cor azul para a linha
sns.lineplot(data=df_vendas.sort_values('Data_venda'), x='Data_venda', y='Valor_venda', marker='o', color='b')

# Define o título e os nomes dos eixos do gráfico temporal
plt.title('Evolucao de vendas ao longo de 2023', fontsize=14, pad=10)
plt.xlabel('Data da venda', fontsize=12)
plt.ylabel('Valor da venda (R$)', fontsize=12)

# Inclina os rótulos de data em 45 graus para evitar sobreposição de textos no eixo horizontal
plt.xticks(rotation=45)

# Adiciona linhas de grade quadriculadas suaves com 50% de opacidade
plt.grid(True, linestyle='--', alpha=0.5)

# Ajusta as margens da janela para não cortar os textos das datas e legendas
plt.tight_layout()

# Exibe a janela com o gráfico de linhas
plt.show()

# Fecha a conexão com o banco SQLite liberando o arquivo e a memória do sistema operacional
conexao.close()