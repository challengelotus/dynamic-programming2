import processamento_dados

path_json = 'data/raw/dados_laboratorioA.json'
path_csv = 'data/raw/dados_laboratorioB.csv'

# Extract
dados_laboratorioA = processamento_dados.carregar_json(path_json)
print(f'Dados do Laboratório A (primeiros 2 registros): \n{dados_laboratorioA[:2]}')
print(f'Nomes colunas (Laboratório A | JSON): {processamento_dados.obter_colunas(dados_laboratorioA)}')
print(f'Quantidade de exames (Laboratório A | JSON): {processamento_dados.tamanho_dados(dados_laboratorioA)}\n')

dados_laboratorioB = processamento_dados.carregar_csv(path_csv)
print(f'Dados do Laboratório B (primeiros 2 registros): \n{dados_laboratorioB[:2]}\n')
print(f'Nomes colunas (Laboratório B | CSV): {processamento_dados.obter_colunas(dados_laboratorioB)}')
print(f'Quantidade de exames (Laboratório B | CSV): {processamento_dados.tamanho_dados(dados_laboratorioB)}\n')


# Transform
dados_fusao = processamento_dados.fusionar_datasets(dados_laboratorioA, dados_laboratorioB)
print(f'Total de exames após fusão: {processamento_dados.tamanho_dados(dados_fusao)}')
print(f'Nomes colunas (Fusão): {processamento_dados.obter_colunas(dados_fusao)}\n')

dados_ordenados = processamento_dados.selection_sort_alfabetico(dados_fusao)
print(f'Primeiro exame após ordenação: {dados_ordenados[0]["paciente"]["nome"]}')
print(f'Último exame após ordenação: {dados_ordenados[-1]["paciente"]["nome"]}\n')

paciente_alvo = 'João Silva'
exames_paciente = processamento_dados.busca_binaria_paciente(
    dados_ordenados, paciente_alvo)
print(f'Exames encontrados para {paciente_alvo}: {len(exames_paciente)}')
for exame in exames_paciente:
    print(f"- {exame['exame']['tipo']} em {exame['exame']['data']}")

dados_agrupados = processamento_dados.agrupar_por_paciente(dados_ordenados)
print("\n=== DADOS AGRUPADOS POR PACIENTE ===")
for cpf in list(dados_agrupados.keys())[:2]:
    paciente = dados_agrupados[cpf]
    print(f"\nPaciente: {paciente['paciente']['nome']} (CPF: {cpf})")
    print(f"Total de exames: {len(paciente['exames'])}")
    print("Exames realizados:")
    for exame in paciente['exames'][:3]:  # Mostra até 3 exames
        print(f"- {exame['tipo']} ({exame['data']}) | ID: {exame['id_exame']}")
print("\n=== RESUMO ===")
print(f"Pacientes únicos: {len(dados_agrupados)}")
print(f"Total de exames: {processamento_dados.tamanho_dados(dados_ordenados)}")


# Load
path_dados_agrupados = 'data\processed\dados_laboratorios_agrupados.json'
processamento_dados.salvar_dados_json(dados_agrupados, path_dados_agrupados)
print(f'Caminho dos dados de fusão: {path_dados_agrupados}')
