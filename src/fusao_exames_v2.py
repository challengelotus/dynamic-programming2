from processamento_dados_v2 import Dados

path_json = 'data/raw/dados_laboratorioA.json'
path_csv = 'data/raw/dados_laboratorioB.csv'


# Extract
dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(f'Dados da Empresa A: {dados_empresaA}')

print('')

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(f'Dados da Empresa B: {dados_empresaB}')