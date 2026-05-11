# Análise de Imóveis com Python e Pandas

Projeto desenvolvido para praticar manipulação, limpeza e análise de dados utilizando Python e Pandas a partir de uma base de imóveis para aluguel.

## Objetivo

O objetivo deste projeto é aplicar técnicas de análise de dados em um cenário real, realizando:

- Importação de dados
- Identificação de inconsistências
- Tratamento de valores nulos
- Remoção de dados duplicados
- Filtragem de registros inválidos
- Análise exploratória dos dados

## Dataset

A base utilizada contém informações sobre imóveis para aluguel, incluindo:

- Tipo do imóvel
- Bairro
- Número de quartos
- Vagas de garagem
- Suítes
- Área em m²
- Valor do aluguel
- Condomínio
- IPTU

## Tecnologias utilizadas

- Python
- Pandas
- Google Colab
- Git
- GitHub
  
## Estrutura do projeto

```bash
analise-imoveis-python-pandas/
│
├── data/
│   ├── aluguel.csv
│   └── aluguel_tratado.csv
│
├── src/
│   └── analise.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Etapas realizadas

### 1. Coleta dos dados
Os dados foram importados a partir de uma base pública em formato CSV.

### 2. Limpeza dos dados
Foram realizados os seguintes tratamentos:

- Preenchimento de valores nulos em condomínio e IPTU
- Remoção de registros duplicados
- Remoção de imóveis com valores inválidos
- Remoção de imóveis com área inválida

### 3. Análise exploratória
Foram extraídos insights como:

- Tipos de imóveis mais frequentes
- Bairros com maior média de aluguel
- Distribuição dos preços de aluguel

## Resultado

Ao final do processo, foi gerada uma nova base de dados tratada:

`aluguel_tratado.csv`

## Aprendizados

Com este projeto, foi possível desenvolver habilidades em:

- Manipulação de dados com Python
- Limpeza e tratamento de datasets
- Análise exploratória com Pandas
- Organização de projetos para portfólio
