import json
import csv

class Dados:
    def __init__(self, dados):
        self.dados = dados
        self.nome_colunas = self.obter_colunas()
        self.qtd_linhas = self.data_size()
    
    @staticmethod
    def leitura_json(path):
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)['exames']
        
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
    
    def data_size(self):
        return len(self.dados)
