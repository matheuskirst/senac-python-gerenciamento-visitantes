from datetime import date
from dataclasses import dataclass
from enums import IngressoTipo

@dataclass
class Visitante:
    nome: str
    data_nascimento: str
    idade: int
    cpf: str
    ingresso_tipo: IngressoTipo
    data_visita: str
    numero_ingresso: str

    class Campo:
        nome = 'nome'
        data_nascimento = 'data_nascimento'
        idade = 'idade'
        cpf = 'cpf'
        ingresso_tipo = 'ingresso_tipo'
        data_visita = 'data_visita'
        numero_ingresso = 'numero_ingresso'
