import json
import csv


class Dados:
    def __init__(self, dados):
        # Instância guarda a lista de exames
        self.dados = dados
        self.nome_colunas = self.obter_colunas()
        self.tamanho_dados = len(dados)

    # --------------------------
    # LEITURA DE ARQUIVOS
    # --------------------------
    @staticmethod
    def leitura_json(path):
        """Lê exames de um arquivo JSON"""
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)['exames']

    @staticmethod
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

    @staticmethod
    def leitura_csv(path):
        """Lê exames de um arquivo CSV"""
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')
            return Dados.transformar_csv_para_json(reader)

    @classmethod
    def leitura_dados(cls, path, tipo_dados):
        """Carrega dados (CSV ou JSON) e retorna uma instância de Dados"""
        if tipo_dados == 'csv':
            dados = cls.leitura_csv(path)
        elif tipo_dados == 'json':
            dados = cls.leitura_json(path)
        else:
            raise ValueError("Use 'csv' ou 'json'")
        return cls(dados)

    # --------------------------
    # OPERAÇÕES BÁSICAS
    # --------------------------
    def printar_dados(self):
        """Exibe todos os exames da instância (pouco prático para bases grandes)"""
        print(f'{self.dados}')

    def obter_colunas(self):
        """Retorna as chaves de um exame (colunas da base)"""
        return list(self.dados[-1].keys()) if self.dados else []

    @classmethod
    def join(cls, dadosA, dadosB):
        """Faz a fusão de duas instâncias de Dados"""
        combined_list = dadosA.dados + dadosB.dados
        return cls(combined_list)

    def salvar_dados_json(self, path):
        """Salva os dados atuais em arquivo JSON"""
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(self.dados, file, ensure_ascii=False, indent=2)

    # --------------------------
    # ORDENAÇÃO (QUICK SORT)
    # --------------------------
    def quick_sort(self):
        """Ordena exames pelo nome do paciente"""
        self.dados = self._quick_sort_recursivo(self.dados)

    def _quick_sort_recursivo(self, lista):  # privado (auxiliar do quick_sort)
        """Implementação recursiva do QuickSort (uso interno)"""
        if len(lista) <= 1:
            return lista

        pivo = lista[len(lista) // 2]['paciente']['nome'].lower()
        menores = [item for item in lista if item["paciente"]["nome"].lower() < pivo]
        iguais = [item for item in lista if item["paciente"]["nome"].lower() == pivo]
        maiores = [item for item in lista if item["paciente"]["nome"].lower() > pivo]

        return self._quick_sort_recursivo(menores) + iguais + self._quick_sort_recursivo(maiores)

    # --------------------------
    # BUSCAS
    # --------------------------
    def buscar_sequencial(self, nome_alvo):
        """Busca sequencial de exames por nome do paciente"""
        nome_alvo = nome_alvo.lower()
        return [exame for exame in self.dados if exame['paciente']['nome'].lower() == nome_alvo]

    def busca_binaria_paciente(self, nome_alvo):
        """Busca binária de exames por paciente (requer lista ordenada)"""
        inicio, fim = 0, len(self.dados) - 1
        nome_alvo = nome_alvo.lower()
        exames_paciente = []

        while inicio <= fim:
            meio = (inicio + fim) // 2
            nome_atual = self.dados[meio]['paciente']['nome'].lower()

            if nome_atual == nome_alvo:
                exames_paciente.append(self.dados[meio])
                # varre esquerda
                i = meio - 1
                while i >= 0 and self.dados[i]['paciente']['nome'].lower() == nome_alvo:
                    exames_paciente.append(self.dados[i])
                    i -= 1
                # varre direita
                i = meio + 1
                while i < len(self.dados) and self.dados[i]['paciente']['nome'].lower() == nome_alvo:
                    exames_paciente.append(self.dados[i])
                    i += 1
                return exames_paciente
            elif nome_alvo > nome_atual:
                inicio = meio + 1
            else:
                fim = meio - 1

        return exames_paciente  # lista vazia se não encontrar

    # --------------------------
    # FILA (FIFO)
    # --------------------------
    def criar_fila_exames(self):
        """Cria uma fila (FIFO) em ordem cronológica"""
        return [exame for exame in self.dados]

    def desenfileirar(self, fila):
        """Remove e retorna o exame mais antigo da fila"""
        return fila.pop(0) if fila else None

    # --------------------------
    # PILHA (LIFO)
    # --------------------------
    def criar_pilha_exames(self):
        """Cria uma pilha (LIFO) em ordem inversa"""
        return [exame for exame in self.dados]

    def desempilhar(self, pilha):
        """Remove e retorna o último exame da pilha"""
        return pilha.pop() if pilha else None
