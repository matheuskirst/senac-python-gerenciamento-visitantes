import uuid
from data import DbContext
from datetime import date
from models import Visitante
from enums import IngressoTipo
from utils import resolver_idade, resolver_ingresso_tipo

class VisitanteService:
    def __init__(self, db: DbContext):
        self.db = db

    def cadastrar_visitante(self, dados: dict):
        cpfExiste = self.db.obter_por_cpf(dados["cpf"])

        if cpfExiste != None:
            return {"Erro": "Já existe um visitante cadastrado com esse CPF.\n\nO cadastro não foi realizado."}

        numero_ingresso = str(uuid.uuid4())
        
        visitante = Visitante(
            nome=dados["nome"],
            data_nascimento=dados["dataNascimento"],
            cpf=dados["cpf"],
            ingresso_tipo=dados["ingressoTipo"],
            data_visita=dados["dataVisita"],
            numero_ingresso=numero_ingresso
        )
        self.db.adicionar(visitante)

        return {"Sucesso": "Visitante cadastrado com sucesso!"}

    def remover_visitante(self, cpf: str):
        self.db.remover(cpf)

    def listar_todos(self):
        try:
            visitantes = self.db.obter_todos()

            if visitantes == None or len(visitantes) <= 0:
                return {"Erro": "Não ha visitantes cadastrados"}

            lista_visitantes_dados = []

            for visitante in visitantes:
                visitante_dados = {
                    "Nome": visitante.nome,
                    "Idade": f"{resolver_idade(visitante.data_nascimento)} anos",
                    "Ingresso": resolver_ingresso_tipo(visitante.ingresso_tipo),
                }
                lista_visitantes_dados.append(visitante_dados)

            return lista_visitantes_dados

        except Exception as e:
            return {"Erro": f"Ocorreu um erro interno{e}"}


    def consultar_por_cpf(self, cpf: str):
        try:
            visitante = self.db.obter_por_cpf(cpf)

            if visitante == None:
                return {"Erro": "Visitante não encontrado"}

            visitante_dados = {
                "Nome": visitante.nome,
                "Idade": f"{resolver_idade(visitante.data_nascimento)} anos",
                "CPF": visitante.cpf,
                "Data de Nascimento": visitante.data_nascimento,
                "Ingresso": resolver_ingresso_tipo(visitante.ingresso_tipo),
                "Data da visita": visitante.data_visita.strftime('%d/%m/%Y'),
                "Número do ingresso": visitante.numero_ingresso
            }
            return visitante_dados

        except:
            return {"Erro": "Ocorreu um erro interno"}
