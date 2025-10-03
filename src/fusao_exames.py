from processamento_dados import Dados, Ordenacao, Busca, EstruturasLineares, ProgramacaoDinamica

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

# QUICK SORT (usando classe Ordenacao)
print("Antes de ordenar:")
for d in dados_fusao.dados[:5]:
    print(d["paciente"]["nome"])

# aplicar o quick sort (retorna nova lista ordenada)
dados_fusao.dados = Ordenacao.quick_sort(dados_fusao.dados)

print("\nDepois de ordenar:")
for d in dados_fusao.dados[:5]:
    print(d["paciente"]["nome"])

# Busca sequencial (classe Busca)
paciente_alvo = 'João Silva'
exames_paciente = Busca.buscar_sequencial(dados_fusao.dados, paciente_alvo)
print(f'Exames encontrados para {paciente_alvo}: {len(exames_paciente)}')
for exame in exames_paciente:
    print(f"- {exame['exame']['tipo']} em {exame['exame']['data']}")

# Busca Binária (requer dados ordenados)
paciente_alvo = 'Ana Souza'
exames_paciente = Busca.busca_binaria(dados_fusao.dados, paciente_alvo)
print(f'Exames encontrados para {paciente_alvo}: {len(exames_paciente)}')
for exame in exames_paciente:
    print(f"- {exame['exame']['tipo']} em {exame['exame']['data']}")

# -------------------------------
# FILA / PILHA (EstruturasLineares)
# -------------------------------
fila_exames = EstruturasLineares.criar_fila(dados_fusao.dados)
print("\nFila de exames (ordem cronológica):")
for e in fila_exames[:5]:
    print(f"{e['paciente']['nome']} - {e['exame']['tipo']}")

print("\nDesenfileirando (FIFO):")
while fila_exames:
    exame = EstruturasLineares.desenfileirar(fila_exames)
    print(f"Saiu da fila: {exame['paciente']['nome']} - {exame['exame']['tipo']}")

pilha_exames = EstruturasLineares.criar_pilha(dados_fusao.dados)
print("\nPilha de exames (últimos primeiro):")
for e in pilha_exames[:5]:
    print(f"{e['paciente']['nome']} - {e['exame']['tipo']}")

print("\nDesempilhando (LIFO):")
while pilha_exames:
    exame = EstruturasLineares.desempilhar(pilha_exames)
    print(f"Saiu da pilha: {exame['paciente']['nome']} - {exame['exame']['tipo']}")

# -------------------------------
# PROGRAMACAO DINAMICA (Sprint 4)
# -------------------------------
# exemplo didático: consumos (unidades) por exame e capacidade diária
insumos = [2, 3, 4, 5]  # consumo por exame (exemplo)
capacidade = 5
n = len(insumos)

print("\n--- Programação Dinâmica (exemplo Knapsack) ---")
print("Versão Recursiva:", ProgramacaoDinamica.consumo_recursivo(insumos, capacidade, n))
print("Versão Memoization:", ProgramacaoDinamica.consumo_memoization(insumos, capacidade, n, {}))
print("Versão Bottom-Up:", ProgramacaoDinamica.consumo_bottom_up(insumos, capacidade))

# -------------------------------
# LOAD
# -------------------------------
path_dados_combinados = 'data/processed/dados_laboratorios.json'
dados_fusao.salvar_dados_json(path_dados_combinados)
print(f'\nCaminho dos dados de fusão: {path_dados_combinados}')
