import uuid
from data import DbContext
from datetime import date
from models import Visitante
from enums import IngressoTipo, Ordenar
from utils import resolver_idade, resolver_ingresso_tipo

class VisitantesService:
    def __init__(self, db: DbContext):
        self.db = db

    def cadastrar_visitante(self, dados: dict):
        cpfExiste = self.db.obter_visitante(campo=Visitante.Campo.cpf, valor=dados["cpf"])

        if cpfExiste != None:
            return {"Erro": "Já existe um visitante cadastrado com esse CPF.\n\nO cadastro não foi realizado."}

        numero_ingresso = str(uuid.uuid4())
        
        visitante = Visitante(
            nome = dados["nome"],
            data_nascimento = dados["dataNascimento"],
            idade = resolver_idade(dados["dataNascimento"]),
            cpf = dados["cpf"],
            ingresso_tipo = dados["ingressoTipo"],
            data_visita = dados["dataVisita"],
            numero_ingresso = numero_ingresso
        )
        self.db.adicionar(visitante)
        self.db.salvar_dados()

        return {"Sucesso": "Visitante cadastrado com sucesso!"}

    def remover_visitante_por_cpf(self, cpf: str):
        try:
            visitante = self.db.obter_visitante(campo=Visitante.Campo.cpf, valor=cpf)

            if visitante == None:
                return {"Erro": "Visitante não encontrado"}

            self.db.remover(campo=Visitante.Campo.cpf, valor=cpf)
            self.db.salvar_dados()
            return {"Sucesso": f"Visitante: {visitante.nome}, CPF: '{visitante.cpf}' removido com sucesso!"}
        except:
            return {"Erro": "Ocorreu um erro interno."}

    def listar_todos(self):
        try:
            visitantes = self.db.obter_visitantes_lista()

            if not visitantes:
                return {"Erro": "Não ha visitantes cadastrados."}

            lista_visitantes_dados = []

            for visitante in visitantes:
                visitante_dados = {
                    "Nome": visitante.nome,
                    "Idade": f"{visitante.idade} anos",
                    "Ingresso": resolver_ingresso_tipo(visitante.ingresso_tipo),
                }
                lista_visitantes_dados.append(visitante_dados)

            return lista_visitantes_dados

        except:
            return [{"Erro": "Ocorreu um erro interno"}]

    def listar_por_ingresso(self, ingresso:IngressoTipo):
        try:
            filtros = {"filtro_campo": Visitante.Campo.ingresso_tipo, "filtro_valor": ingresso}

            visitantes = self.db.obter_visitantes_lista(filtro=filtros)

            if not visitantes:
                return {"Erro": "Não ha visitantes cadastrados."}

            lista_visitantes_dados = []

            for visitante in visitantes:
                visitante_dados = {
                    "Nome": visitante.nome,
                    "Idade": f"{visitante.idade} anos"
                }
                lista_visitantes_dados.append(visitante_dados)

            return lista_visitantes_dados

        except:
            return [{"Erro": f"Ocorreu um erro interno"}]

    def listar_por_ordem(self, ordem:Ordenar):
        try:
            ordenar = ""
            match ordem:
                case Ordenar.Nome:
                    ordenar = Visitante.Campo.nome
                case Ordenar.Idade:
                    ordenar = Visitante.Campo.idade

            visitantes = self.db.obter_visitantes_lista(ordernar_campo = ordenar)

            if not visitantes:
                return {"Erro": "Não ha visitantes cadastrados."}

            lista_visitantes_dados = []

            for visitante in visitantes:
                visitante_dados = {
                    "Nome": visitante.nome,
                    "Idade": f"{visitante.idade} anos",
                    "Ingresso": resolver_ingresso_tipo(visitante.ingresso_tipo),
                }
                lista_visitantes_dados.append(visitante_dados)

            return lista_visitantes_dados

        except:
            return [{"Erro": f"Ocorreu um erro interno"}]

    def consultar_por_cpf(self, cpf: str):
        try:
            visitante = self.db.obter_visitante(campo=Visitante.Campo.cpf, valor=cpf)

            if visitante == None:
                return {"Erro": "Visitante não encontrado"}

            visitante_dados = {
                "Nome": visitante.nome,
                "Idade": f"{visitante.idade} anos",
                "CPF": visitante.cpf,
                "Data de Nascimento": visitante.data_nascimento.strftime('%d/%m/%Y'),
                "Ingresso": resolver_ingresso_tipo(visitante.ingresso_tipo),
                "Data da visita": visitante.data_visita.strftime('%d/%m/%Y'),
                "Número do ingresso": visitante.numero_ingresso
            }
            return visitante_dados

        except:
            return {"Erro": "Ocorreu um erro interno."}

    def consultar_por_data(self, data: date):
        try:
            visitantes = self.db.obter_visitantes_lista(campo=Visitante.Campo.data_visita, valor=data)

            if visitantes == None:
                return {"Erro": "Nenhum visitante encontrado"}

            visitantes_dados = []

            for visitante in visitantes:
                dados = {
                    "Nome": visitante.nome,
                    "Idade": f"{visitante.idade} anos",
                    "CPF": visitante.cpf,
                    "Data de Nascimento": visitante.data_nascimento.strftime('%d/%m/%Y'),
                    "Ingresso": resolver_ingresso_tipo(visitante.ingresso_tipo),
                    "Data da visita": visitante.data_visita.strftime('%d/%m/%Y'),
                    "Número do ingresso": visitante.numero_ingresso
                }
                visitantes_dados.append(dados)
            return visitantes_dados

        except:
            return {"Erro": "Ocorreu um erro interno."}

    def obter_estatisticas(self):
        visitantes = self.db.obter_visitantes_lista()

        if visitantes == None or len(visitantes) == 0:
            return {"Erro": "Não existem visitantes cadastrados para gerar estatísticas"}



        quantidade = self.db.obter_quantidade_visitantes()

        ingresso = IngressoTipo.Normal
        ingressos_normal = len(self.db.obter_quantidade_visitantes(filtro=ingresso))
        ingresso = IngressoTipo.Vip
        ingressos_vip = len(self.db.obter_quantidade_visitantes(filtro=ingresso))
        ingresso = IngressoTipo.Premium
        ingressos_premium = len(self.db.obter_quantidade_visitantes(filtro=ingresso))

        lista_idades = self.db.obter_campo_lista(campo=Visitante.Campo.idade)

        idade_media = sum(lista_idades) / len(lista_idades)

        estatisticas = {
            "Total de visitantes": quantidade,
            "Ingressos Normal": ingressos_normal,
            "Ingressos VIP": ingressos_vip,
            "Ingressos Premium": ingressos_premium,
            "Média de idade": idade_media
        }
        
        return estatisticas
