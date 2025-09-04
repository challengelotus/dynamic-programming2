from processamento_dados_v2 import Dados

path_json = 'data/raw/dados_laboratorioA.json'
path_csv = 'data/raw/dados_laboratorioB.csv'

# Extract
dados_empresaA = Dados.leitura_dados(path_json, 'json')
dados_empresaA.printar_dados()
print(f'Nomes colunas (Empresa A | JSON): {dados_empresaA.nome_colunas}')
print(f'Quantidade de colunas (Empresa A | JSON): {dados_empresaA.qtd_linhas}')

print('-'*118)

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
dados_empresaB.printar_dados()
print(f'Nomes colunas (Empresa B | CSV): {dados_empresaB.nome_colunas}')
print(f'Quantidade de colunas (Empresa B | CSV): {dados_empresaB.qtd_linhas}')