import json
import csv


def carregar_json(path):
    """Carrega dados de um arquivo JSON"""
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)['exames']


def carregar_csv(path):
    """Carrega e transforma dados de um arquivo CSV"""
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return transformar_csv_para_json(reader)


def transformar_csv_para_json(reader):
    """Converte dados CSV para o formato JSON padronizado"""
    exames = []
    for linha in reader:
        exame = {
            "id_exame": linha["id_exame"],
            "paciente": {
                "nome": linha["nome"],
                "cpf": linha["cpf"],
                "idade": int(linha["idade"]),
                "sexo": linha["sexo"],
            },
            "exame": {
                "tipo": linha["tipo_exame"],
                "data": linha["data"],
                "resultados": {
                    linha["teste"]: {
                        "valor": float(linha["valor"]),
                        "unidade": linha["unidade"],
                        "referencia": linha["referencia"],
                    }
                },
            },
        }
        exames.append(exame)
    return exames


def carregar_dados(path, tipo_dados):
    """Carrega dados de arquivo JSON ou CSV"""
    if tipo_dados == 'csv':
        return carregar_csv(path)
    elif tipo_dados == 'json':
        return carregar_json(path)
    else:
        raise ValueError("Tipo de dados inválido. Use 'csv' ou 'json'.")


def obter_colunas(dados):
    """Retorna as colunas disponíveis nos dados"""
    return list(dados[-1].keys() if dados else [])


def tamanho_dados(dados):
    """Retorna a quantidade de exames"""
    return len(dados)


def fusionar_datasets(dadosA, dadosB):
    """Combina dois conjuntos de dados"""
    return dadosA + dadosB


def selection_sort_alfabetico(dados):
    """Ordena dados pelo nome do paciente usando Selection Sort"""
    dados_ordenados = dados.copy()
    n = len(dados_ordenados)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if dados_ordenados[j]['paciente']['nome'].lower() < dados_ordenados[min_idx]['paciente']['nome'].lower():
                min_idx = j
        if min_idx != i:
            dados_ordenados[i], dados_ordenados[min_idx] = dados_ordenados[min_idx], dados_ordenados[i]

    return dados_ordenados


def busca_binaria_paciente(lista_ordenada, nome_alvo):
    """Busca binária por todos os exames de um paciente em lista ordenada por nome
    Args:
        lista_ordenada: Lista de dicionários ordenados por nome do paciente
        nome_alvo: Nome completo do paciente a ser buscado
    Returns:
        Lista com todos os exames do paciente ou lista vazia se não encontrado
    """
    inicio = 0
    fim = len(lista_ordenada) - 1
    nome_alvo = nome_alvo.lower()
    exames_paciente = []

    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome_atual = lista_ordenada[meio]['paciente']['nome'].lower()

        if nome_atual == nome_alvo:
            # Encontrou um exame, agora busca todos adjacentes
            exames_paciente.append(lista_ordenada[meio])

            # Busca à esquerda
            i = meio - 1
            while i >= 0 and lista_ordenada[i]['paciente']['nome'].lower() == nome_alvo:
                exames_paciente.append(lista_ordenada[i])
                i -= 1

            # Busca à direita
            i = meio + 1
            while i < len(lista_ordenada) and lista_ordenada[i]['paciente']['nome'].lower() == nome_alvo:
                exames_paciente.append(lista_ordenada[i])
                i += 1

            return exames_paciente
        elif nome_alvo > nome_atual:
            inicio = meio + 1
        else:
            fim = meio - 1

    return exames_paciente  # Retorna lista vazia se não encontrar


def agrupar_por_paciente(dados):
    """Agrupa todos os exames de cada paciente em uma estrutura unificada

    Args:
        dados: Lista de dicionários contendo os exames

    Returns:
        Dicionário no formato {cpf: {dados_paciente, exames}}
    """
    pacientes = {}

    for exame in dados:
        cpf = exame['paciente']['cpf']

        if cpf not in pacientes:
            pacientes[cpf] = {
                'paciente': exame['paciente'].copy(),
                'exames': []
            }

        pacientes[cpf]['exames'].append({
            'id_exame': exame['id_exame'],
            'tipo': exame['exame']['tipo'],
            'data': exame['exame']['data'],
            'resultados': exame['exame']['resultados']
        })

    return pacientes


def salvar_dados_json(dados, caminho_arquivo):
    """Salva os dados em um arquivo JSON

    Args:
        dados: Dicionário ou lista com os dados a serem salvos
        caminho_arquivo: Caminho onde o arquivo será salvo
    """
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
