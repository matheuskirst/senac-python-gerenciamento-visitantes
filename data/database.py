import json
from dataclasses import Field
from models import Visitante
from enums import Ordenar

class DbContext:
    def __init__(self):
        self.visitantes: list[Visitante] = []
    
    def adicionar(self, visitante: Visitante):
        self.visitantes.append(visitante)

    def remover(self, index: int):
        del self.visitantes[index]

    def remover_por_cpf(self, cpf):
        for visitante in self.visitantes:
            if visitante.cpf == cpf:
                self.visitantes.remove(visitante)

    def obter_item(self, campo:str, valor):
        for item in self.visitantes:
            if getattr(item, campo) == valor:
                return item
        return None

    def obter_items_lista(self, ordem=None, filtro=None):
        items = self.visitantes

        if ordem:
            if ordem == Ordenar.Nome:
                items += items.sort(key=lambda v: v.nome)
            elif ordem == Ordenar.Idade:
                items += items.sort(key=lambda v: v.idade)

        if filtro:
            items += filter(lambda v: v.ingresso_tipo == filtro, items)

        return items

    def obter_quantidade(self):
        return len(self.visitantes)

    def salvar(self):
        return
