import json
from datetime import datetime
from dataclasses import asdict
from models import Visitante
from enums import Ordenar, IngressoTipo

class DbContext:
    def __init__(self):
        self.visitantes_json = "visitantes.json"
        self.visitantes: list[Visitante] = self.carregar_dados()
    
    def adicionar(self, visitante: Visitante):
        self.visitantes.append(visitante)

    def remover(self, campo:str, valor):
        removeu_quantidade = 0
        for item in self.visitantes:
            if getattr(item, campo) == valor:
                self.visitantes.remove(item)
                removeu_quantidade += 1

        return removeu_quantidade

    def obter_visitante(self, campo:str, valor):
        for item in self.visitantes:
            if getattr(item, campo) == valor:
                return item
        return None

    def obter_visitantes_lista(self, ordem:Ordenar=None, filtro:IngressoTipo=None):
        items = self.visitantes

        if ordem:
            if ordem == Ordenar.Nome:
                items = sorted(items, key=lambda v: v.nome)
            elif ordem == Ordenar.Idade:
                items = sorted(items, key=lambda v: v.idade)

        if filtro:
            items = filter(lambda v: v.ingresso_tipo == filtro, items)

        return items

    def obter_quantidade_visitantes(self):
        return len(self.visitantes)

    def carregar_dados(self):
        try:
            with open(self.visitantes_json, "r") as f:
                dados = json.load(f)
                for dado in dados:
                    dado["data_nascimento"] = datetime.strptime(dado["data_nascimento"], '%d/%m/%Y')
                    dado["data_visita"] = datetime.strptime(dado["data_visita"], '%d/%m/%Y')
                return [Visitante(**v) for v in dados]
        except:
            return []

    def salvar_dados(self):
        with open(self.visitantes_json, "w") as f:
            dados = [asdict(visitante) for visitante in self.visitantes]
            for dado in dados:
                dado["data_nascimento"] = datetime.strftime(dado["data_nascimento"], '%d/%m/%Y')
                dado["data_visita"] = datetime.strftime(dado["data_visita"], '%d/%m/%Y')
            json.dump(dados, f, indent=4)
