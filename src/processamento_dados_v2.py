import json
import csv


class Dados:
    def __init__(self, dados):
        self.dados = dados
        self.nome_colunas = self.obter_colunas()
        self.tamanho_dados = len(dados)

    @staticmethod
    def leitura_json(path):
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
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')
            return Dados.transformar_csv_para_json(reader)

    @classmethod
    def leitura_dados(cls, path, tipo_dados):
        if tipo_dados == 'csv':
            dados = cls.leitura_csv(path)
        elif tipo_dados == 'json':
            dados = cls.leitura_json(path)
        else:
            raise ValueError("Use 'csv' ou 'json'")

        return cls(dados)

    def printar_dados(self):
        print(f'{self.dados}')

    def obter_colunas(self):
        return list(self.dados[-1].keys()) if self.dados else []

    @classmethod
    def join(cls, dadosA, dadosB):
        combined_list = dadosA.dados + dadosB.dados
        return cls(combined_list)

    def quick_sort(self):
        self.dados = self._quick_sort_recursivo(self.dados)

    def _quick_sort_recursivo(self, lista):
        if len(lista) <= 1:
            return lista
        
        pivo = lista[len(lista) // 2]['paciente']['nome'].lower()
        menores = [item for item in lista if item["paciente"]["nome"].lower() < pivo]
        iguais = [item for item in lista if item["paciente"]["nome"].lower() == pivo]
        maiores = [item for item in lista if item["paciente"]["nome"].lower() > pivo]

        return self._quick_sort_recursivo(menores) + iguais + self._quick_sort_recursivo(maiores)


    def buscar_sequencial(self, nome_alvo):
        nome_alvo = nome_alvo.lower()
        resultados = []

        for exame in self.dados:
            if exame['paciente']['nome'].lower() == nome_alvo:
                resultados.append(exame)

        return resultados
    
    def busca_binaria_paciente(self, nome_alvo):
        """Busca binária por todos os exames de um paciente em lista ordenada por nome
        Args:
            lista_ordenada: Lista de dicionários ordenados por nome do paciente
            nome_alvo: Nome completo do paciente a ser buscado
        Returns:
            Lista com todos os exames do paciente ou lista vazia se não encontrado
        """
        inicio = 0
        fim = len(self.dados) - 1
        nome_alvo = nome_alvo.lower()
        exames_paciente = []

        while inicio <= fim:
            meio = (inicio + fim) // 2
            nome_atual = self.dados[meio]['paciente']['nome'].lower()

            if nome_atual == nome_alvo:
                # Encontrou um exame, agora busca todos adjacentes
                exames_paciente.append(self.dados[meio])

                # Busca à esquerda
                i = meio - 1
                while i >= 0 and self.dados[i]['paciente']['nome'].lower() == nome_alvo:
                    exames_paciente.append(self.dados[i])
                    i -= 1

                # Busca à direita
                i = meio + 1
                while i < len(self.dados) and self.dados[i]['paciente']['nome'].lower() == nome_alvo:
                    exames_paciente.append(self.dados[i])
                    i += 1

                return exames_paciente
            elif nome_alvo > nome_atual:
                inicio = meio + 1
            else:
                fim = meio - 1

        return exames_paciente  # Retorna lista vazia se não encontrar

    def salvar_dados_json(self, path):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(self.dados, file, ensure_ascii=False, indent=2)
