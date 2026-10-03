import os
import json
from typing import Any
from dotenv import load_dotenv
from datetime import datetime
from dataclasses import asdict

from models import Visitante

class DbContext:
    def __init__(self) -> None:
        load_dotenv()
        self.visitantes_json: str = os.getenv('VISITANTES_JSON') or ""
        self.visitantes: list[Visitante] = self.__load() or []
        self.query = self.Query(self)

    def __load(self):
        try:
            with open(self.visitantes_json, "r", encoding="utf-8") as f:
                dados = json.load(f)
                for dado in dados:
                    dado["data_nascimento"] = datetime.strptime(dado["data_nascimento"], '%d/%m/%Y')
                    dado["data_visita"] = datetime.strptime(dado["data_visita"], '%d/%m/%Y')
                return [Visitante(**v) for v in dados]
        except:
            return []

    def create(self, visitante: Visitante):
        self.visitantes.append(visitante)

    def delete(self):
        pass

    def save_changes(self):
        with open(self.visitantes_json, "w", encoding="utf-8") as f:
            dados = [asdict(visitante) for visitante in self.visitantes]
            for dado in dados:
                dado["data_nascimento"] = datetime.strftime(dado["data_nascimento"], '%d/%m/%Y')
                dado["data_visita"] = datetime.strftime(dado["data_visita"], '%d/%m/%Y')
            json.dump(dados, f, indent=4)

    class Query:
        def __init__(self, parent: DbContext) -> None:
            self.parent = parent

        def __call__(self):
            self.result = []
            return self

        def where(self, function):
            self.result = list(filter(function, self.parent.visitantes))
            return self

        def order_by(self, field: str):
            self.result = sorted(self.parent.visitantes, key=lambda v: getattr(v, field))
            return self

        def to_list(self):
            return self.result

        def first(self):
            return self.result[0]

db = DbContext()
visitantes = db.query().where(lambda v: v.nome == "nome").order_by(Visitante.Campo.idade).first()
