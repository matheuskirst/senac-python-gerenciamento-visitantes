from datetime import date
from dataclasses import dataclass
from enums import IngressoTipo

@dataclass
class Visitante:
    nome: str
    data_nascimento: date
    cpf: str
    ingresso_tipo: IngressoTipo
    data_visita: date
    numero_ingresso: str
