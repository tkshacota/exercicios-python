import pandas as pd

data = {

'nome': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto E'],

'quantidade de itens comprados': [3, 1, 4, 3, 2],

'tipo de item': ['Eletrônico', 'Vestuário', 'Alimento', 'Eletrônico', 'Alimento'],

'receita total': [120, 80, 60, 120, 90]
}
df=pd.DataFrame(data)
df_banco = pd.DataFrame(data)
df.drop_duplicates(inplace=True, keep='last')

df['preco do item'] = df['receita total']/df['quantidade de itens comprados']

itens_acima_de_50 = df[df['preco do item'] > 50]
print("itens acima de 50 reais: ", itens_acima_de_50)

