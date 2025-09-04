import json
import csv

class Dados:
    def __init__(self, dados):
        self.dados = dados
    
    @staticmethod
    def leitura_json(path):
        with open(path, 'r') as file:
            return json.load(file)

    @staticmethod
    def leitura_csv(path):
        dados_csv = []
        with open(path, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                dados_csv.append(row)
        return dados_csv
    
    @classmethod
    def leitura_dados(cls, path, tipo_dados):
        if tipo_dados == 'csv':
            dados = cls.leitura_csv(path)
        elif tipo_dados == 'json':
            dados = cls.leitura_json(path)
        else:
            raise ValueError("Use 'csv' ou 'json'")
        
        return dados
