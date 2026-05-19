import pandas as pd

print('Carregando base de dados...')

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

df = pd.read_csv(url, sep=';')

print('\nPrimeiras 5 linhas:')
print(df.head())

print('\nDimensões da base:')
print(df.shape)

print('\nInformações gerais:')
df.info()

print('\nValores nulos:')
print(df.isnull().sum())

print('\nIniciando limpeza dos dados...')

df['Condominio'] = df['Condominio'].fillna(0)
df['IPTU'] = df['IPTU'].fillna(0)

df = df.dropna(subset=['Valor'])

df = df.drop_duplicates()

df = df[df['Valor'] > 0]
df = df[df['Area'] > 0]

print('\nDados após limpeza:')
print(df.shape)

print('\nTipos de imóveis:')
print(df['Tipo'].value_counts())

media_bairro = (
    df.groupby('Bairro')['Valor']
    .mean()
    .sort_values(ascending=False)
)

print('\nTop 10 bairros com maior média de aluguel:')
print(media_bairro.head(10))

df.to_csv('aluguel_tratado.csv', sep=';', index=False)

print('\nArquivo aluguel_tratado.csv gerado com sucesso.')
