import pandas as pd

# Importar o dataset 'Amazonas.csv'
arquivo = r'c:\Users\valter.mascarenhas\Downloads\Amazonas.csv'
df = pd.read_csv(arquivo)

# Exibir as primeiras e as últimas 5 linhas do dataset
# Primeiras linhas
print("=" * 50)
print("PRIMEIRAS 5 LINHAS")
print("=" * 50)
print(df.head())

# Últimas linhas
print("\n" + "=" * 50)
print("ÚLTIMAS 5 LINHAS")
print("=" * 50)
print(df.tail())

# Outra forma de exibir as primeiras e as últimas 5 linhas do dataset.
#df.head(5)
#df.tail(5)
#print(df.head())
#print(df.tail())

# Valor mínimo e máximo da coluna 'year'
ano_min = df['year'].min()
ano_max = df['year'].max()

print(f"Ano mínimo: {ano_min}")
print(f"Ano máximo: {ano_max}")

# Alternativa para obter o valor mínimo e máximo da coluna 'year'.
#print(df['year'].agg(['min', 'max']))

# Determinar o número total de incêndios por estado.
df.groupby('state')['number'].sum()
print("\nNúmero total de incêndios por estado:")
print(df.groupby('state')['number'].sum())

# Guardar o resultado anterior num novo DataFrame. Ordene-o de forma decrescente com base no número de incêndios.
df_inc_por_estado = df.groupby('state')['number'].sum().reset_index()
df_inc_por_estado = df_inc_por_estado.sort_values('number', ascending=False)
print("\nNúmero total de incêndios por estado (ordenado de forma decrescente):")
print(df_inc_por_estado)

#df_inc_por_estado.columns = ['Estado', 'Total_Incendios']
#print(df_inc_por_estado)

# Calcular o número total de incêndios, por ano, no estado do Acre.
df_acre = df[df['state'] == 'Acre']
df_inc_acre_por_ano = df_acre.groupby('year')['number'].sum()
print("\nNúmero total de incêndios por ano no estado do Acre:")
print(df_inc_acre_por_ano)

# Calcular a média de incêndios e imprimir com duas casas decimais.
media_incendios = df['number'].mean()
print(f"Média de incêndios: {media_incendios:.2f}")

# Selecionar as últimas 5 linhas do DataFrame e filtrar apenas as duas últimas colunas.
ultimas_linhas = df.tail(5)
ultimas_colunas = ultimas_linhas.iloc[:, -2:]
print("\nÚltimas 5 linhas e duas últimas colunas:")
print(ultimas_colunas)
#print(df.columns) #Exibir o nome das colunas para identificar as duas últimas colunas(Se quiser ver as colunas antes para confirmar)

# Identifique o estado que, em dezembro, registou mais de 950 incêndios. Considere utilizar uma mask para filtrar os dados.
mask = (df['month'] == 'Dezembro') & (df['number'] > 950)
estados_dezembro = df[mask]['state'].unique()
print("\nEstados que registaram mais de 950 incêndios em dezembro:")
print(estados_dezembro)

# Descubra todos os estados onde ocorreram incêndios no mês de dezembro. Utilizar uma estrutura de repetição e, na lista final, ordene os estados por ordem alfabética.
"""mask_dezembro = df['month'] == 'Dec'
df_dezembro = df[mask_dezembro]
estados = []
for estado in df_dezembro['state']:
    if estado not in estados:
        estados.append(estado)
estados.sort()
print("Estados com incêndios em dezembro:")
print(estados)
"""
estados_todos_dezembro = df[df['month'] == 'Dezembro']['state'].unique()
estados_todos_dezembro = sorted(estados_todos_dezembro)
print("\nEstados onde ocorreram incêndios em dezembro (ordenados alfabeticamente):")
print(estados_todos_dezembro)

#Uma forma mais simples usando pandas:
#estados = sorted(df[df['month'] == 'Dezembro']['state'].unique())
#print(estados)
