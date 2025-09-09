from processamento_dados_v2 import Dados

# Caminhos de entrada (dados brutos)
path_json = 'data/raw/dados_laboratorioA.json'
path_csv = 'data/raw/dados_laboratorioB.csv'

# -------------------------------
# EXTRACT
# -------------------------------
dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(f'Nomes colunas (Empresa A | JSON): {dados_empresaA.nome_colunas}')
print(f'Quantidade de exames (Empresa A | JSON): {dados_empresaA.tamanho_dados}')

print('-'*150)

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(f'Nomes colunas (Empresa B | CSV): {dados_empresaB.nome_colunas}')
print(f'Quantidade de exames (Empresa B | CSV): {dados_empresaB.tamanho_dados}')

print('-'*150)

# -------------------------------
# TRANSFORM
# -------------------------------

# Fusão dos dados
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f'Total de exames após fusão: {dados_fusao.tamanho_dados}')

# QUICK SORT
print("Antes de ordenar:")
for d in dados_fusao.dados[:5]:  # acessando o atributo .dados
    print(d["paciente"]["nome"])

# aplicar o quick sort
dados_fusao.quick_sort()

print("\nDepois de ordenar:")
for d in dados_fusao.dados[:5]:
    print(d["paciente"]["nome"])

# Busca sequencial
paciente_alvo = 'João Silva'
exames_paciente = dados_fusao.buscar_sequencial(paciente_alvo)
print(f'Exames encontrados para {paciente_alvo}: {len(exames_paciente)}')
for exame in exames_paciente:
    print(f"- {exame['exame']['tipo']} em {exame['exame']['data']}")

# Busca Binária
paciente_alvo = 'Ana Souza'
exames_paciente = dados_fusao.busca_binaria_paciente(paciente_alvo)
print(f'Exames encontrados para {paciente_alvo}: {len(exames_paciente)}')
for exame in exames_paciente:
    print(f"- {exame['exame']['tipo']} em {exame['exame']['data']}")

# -------------------------------
# LOAD
# -------------------------------
path_dados_combinados = 'data/processed/dados_laboratorios.json'
dados_fusao.salvar_dados_json(path_dados_combinados)
print(f'Caminho dos dados de fusão: {path_dados_combinados}')
