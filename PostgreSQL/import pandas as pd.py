import pandas as pd

# Substitua 'caminho/para/seu/arquivo.csv' pelo caminho real para o arquivo CSV
df = pd.read_csv('https://github.com/Andrehlb/desenvolve2023.github.io/blob/24411e6831516b30642102d6b32f0de3e8cb1f15/PostgreSQL/netflix_export.csv')

# Exibe as primeiras 5 linhas do DataFrame
print(df.head())
