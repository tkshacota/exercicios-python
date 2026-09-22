import pandas as pd

exemplo1 =[10,20,30,40,50]
series1 = pd.Series(exemplo1)
print(series1)

exemplo2 = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}
series2 = pd.Series(exemplo2)
print(series2)

print("media: ", series2.mean())
print("soma: ", series2.sum())
print("maximo: ", series2.max())
print("min: ", series2.min())

url = 'https://www.fdic.gov/bank-failures/failed-bank-list'
dfs = pd.read_html(url)
df_bancos = dfs [0]
print("dimensoes(linhas,colunas): ", df_bancos.shape)
print("\nTIpos de cada coluna: ", df_bancos.dtypes)
print("\nPrimeiras 5 linhas: ", df_bancos.head())