import json
import csv
import os
from typing import List, Dict, Any, Optional

"""
processamento_dados_v2.py
Refatorado: separa responsabilidades em classes
- Dados: carregamento, fusão, persistência
- Ordenacao: algoritmos de ordenação (quick sort)
- Busca: busca sequencial e binária (opera sobre listas)
- EstruturasLineares: fila e pilha (simples, sem deque)
- ProgramacaoDinamica: versões recursiva, memoization e bottom-up de um problema tipo knapsack
"""

class Dados:
    """Classe responsável por carregar, agregar e salvar dados de exames."""

    def __init__(self, dados: List[Dict[str, Any]]):
        self.dados = dados
        self.nome_colunas = self.obter_colunas()
        self.tamanho_dados = len(dados)

    # --------------------------
    # Leitura
    # --------------------------
    @staticmethod
    def leitura_json(path: str) -> List[Dict[str, Any]]:
        """Lê exames de um arquivo JSON (espera chave 'exames')."""
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)['exames']

    @staticmethod
    def transformar_csv_para_json(reader) -> List[Dict[str, Any]]:
        """Converte dados CSV para o formato JSON padronizado."""
        exames = []
        for linha in reader:
            exame = {
                "id_exame": linha["id_exame"],
                "paciente": {
                    "nome": linha["nome"],
                    "cpf": linha["cpf"],
                    "idade": int(linha["idade"]) if linha.get("idade") else None,
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

    @staticmethod
    def leitura_csv(path: str) -> List[Dict[str, Any]]:
        """Lê exames de um arquivo CSV e retorna lista de exames no formato padronizado."""
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')
            return Dados.transformar_csv_para_json(reader)

    @classmethod
    def leitura_dados(cls, path: str, tipo_dados: str) -> 'Dados':
        """Factory: lê CSV ou JSON e retorna instância de Dados."""
        if tipo_dados == 'csv':
            dados = cls.leitura_csv(path)
        elif tipo_dados == 'json':
            dados = cls.leitura_json(path)
        else:
            raise ValueError("Use 'csv' ou 'json'")
        return cls(dados)

    # --------------------------
    # Operações básicas
    # --------------------------
    def printar_dados(self) -> None:
        """Imprime uma prévia dos dados (use com cautela para grandes volumes)."""
        print(self.dados)

    def obter_colunas(self) -> List[str]:
        """Retorna as chaves do último exame (representando colunas)."""
        return list(self.dados[-1].keys()) if self.dados else []

    @classmethod
    def join(cls, dadosA: 'Dados', dadosB: 'Dados') -> 'Dados':
        """Fusão: concatena as listas de exames e retorna nova instância."""
        combined_list = dadosA.dados + dadosB.dados
        return cls(combined_list)

    def salvar_dados_json(self, path: str) -> None:
        """Salva os dados atuais em arquivo JSON."""
        # garante que diretório exista
        dirpath = os_path_dir(path)
        if dirpath:
            try:
                os.makedirs(dirpath, exist_ok=True)
            except Exception:
                pass
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(self.dados, file, ensure_ascii=False, indent=2)


def os_path_dir(path: str) -> Optional[str]:
    dirpath = os.path.dirname(path)
    return dirpath if dirpath else None


class Ordenacao:
    """Classe contendo algoritmos de ordenação."""

    @staticmethod
    def quick_sort(lista: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """QuickSort funcional (retorna nova lista ordenada pelo nome do paciente)."""
        if len(lista) <= 1:
            return lista[:]
        pivo = lista[len(lista) // 2]['paciente']['nome'].lower()
        menores = [item for item in lista if item['paciente']['nome'].lower() < pivo]
        iguais = [item for item in lista if item['paciente']['nome'].lower() == pivo]
        maiores = [item for item in lista if item['paciente']['nome'].lower() > pivo]
        return Ordenacao.quick_sort(menores) + iguais + Ordenacao.quick_sort(maiores)


class Busca:
    """Classe contendo métodos de busca (sequencial e binária)."""

    @staticmethod
    def buscar_sequencial(lista: List[Dict[str, Any]], nome_alvo: str) -> List[Dict[str, Any]]:
        nome_alvo = nome_alvo.lower()
        return [exame for exame in lista if exame['paciente']['nome'].lower() == nome_alvo]

    @staticmethod
    def busca_binaria(lista: List[Dict[str, Any]], nome_alvo: str) -> List[Dict[str, Any]]:
        """
        Busca binária que retorna todos os exames de um paciente.
        REQUISITO: `lista` deve estar previamente ordenada por nome do paciente.
        """
        inicio, fim = 0, len(lista) - 1
        nome_alvo = nome_alvo.lower()
        resultados = []
        while inicio <= fim:
            meio = (inicio + fim) // 2
            nome_atual = lista[meio]['paciente']['nome'].lower()
            if nome_atual == nome_alvo:
                resultados.append(lista[meio])
                # explora adjacentes iguais
                i = meio - 1
                while i >= 0 and lista[i]['paciente']['nome'].lower() == nome_alvo:
                    resultados.append(lista[i])
                    i -= 1
                i = meio + 1
                while i < len(lista) and lista[i]['paciente']['nome'].lower() == nome_alvo:
                    resultados.append(lista[i])
                    i += 1
                return resultados
            elif nome_alvo > nome_atual:
                inicio = meio + 1
            else:
                fim = meio - 1
        return resultados


class EstruturasLineares:
    """Fila e pilha implementadas de forma simples (manual)."""

    @staticmethod
    def criar_fila(lista: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Retorna uma cópia da lista representando a fila (ordem cronológica)."""
        return [exame for exame in lista]

    @staticmethod
    def desenfileirar(fila: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Remove e retorna o primeiro elemento (O(n) aqui)."""
        return fila.pop(0) if fila else None

    @staticmethod
    def criar_pilha(lista: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Retorna uma cópia da lista representando a pilha (last-in first-out)."""
        return [exame for exame in lista]

    @staticmethod
    def desempilhar(pilha: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Remove e retorna o último elemento (O(1))."""
        return pilha.pop() if pilha else None


class ProgramacaoDinamica:
    """
    Implementações de exemplo para a Sprint 4.
    O problema modelado aqui é análogo ao '0/1 Knapsack' (mochila):
    - insumos: lista de consumos/custos/valores por item
    - capacidade: limite por dia (ou outro recurso)
    As três versões (recursiva, memoization e bottom-up) estão implementadas.
    """

    @staticmethod
    def consumo_recursivo(insumos: List[int], capacidade: int, n: int) -> int:
        """Versão recursiva simples (exponencial)."""
        if n == 0 or capacidade == 0:
            return 0
        if insumos[n - 1] > capacidade:
            return ProgramacaoDinamica.consumo_recursivo(insumos, capacidade, n - 1)
        else:
            incluir = insumos[n - 1] + ProgramacaoDinamica.consumo_recursivo(insumos, capacidade - insumos[n - 1], n - 1)
            excluir = ProgramacaoDinamica.consumo_recursivo(insumos, capacidade, n - 1)
            return max(incluir, excluir)

    @staticmethod
    def consumo_memoization(insumos: List[int], capacidade: int, n: int, memo: dict) -> int:
        """Versão top-down com memoization (dicionário)."""
        if n == 0 or capacidade == 0:
            return 0
        key = (n, capacidade)
        if key in memo:
            return memo[key]
        if insumos[n - 1] > capacidade:
            memo[key] = ProgramacaoDinamica.consumo_memoization(insumos, capacidade, n - 1, memo)
        else:
            incluir = insumos[n - 1] + ProgramacaoDinamica.consumo_memoization(insumos, capacidade - insumos[n - 1], n - 1, memo)
            excluir = ProgramacaoDinamica.consumo_memoization(insumos, capacidade, n - 1, memo)
            memo[key] = max(incluir, excluir)
        return memo[key]

    @staticmethod
    def consumo_bottom_up(insumos: List[int], capacidade: int) -> int:
        """Versão iterativa bottom-up (programação dinâmica clássica)."""
        n = len(insumos)
        dp = [[0] * (capacidade + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for c in range(1, capacidade + 1):
                if insumos[i - 1] <= c:
                    dp[i][c] = max(insumos[i - 1] + dp[i - 1][c - insumos[i - 1]], dp[i - 1][c])
                else:
                    dp[i][c] = dp[i - 1][c]
        return dp[n][capacidade]
