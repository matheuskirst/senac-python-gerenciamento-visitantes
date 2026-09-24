from datetime import datetime
from services import VisitanteService
from utils import clear_screen, title_divider, divider, print_title, solicitar_texto, mensagem_voltar
from enums import IngressoTipo, Ordenar

class SistemaView:
    def __init__(self, visitantes_service: VisitanteService):
        self.visitantes_service = visitantes_service

    def run(self):
        self.menu_principal()

    def menu_principal(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("1. Cadastrar Visitante")
            print("2. Remover Visitante")
            print("3. Listar Visitantes")
            print("4. Ordenar Visitantes")
            print("5. Filtrar Visitantes")
            print("6. Consultar Visitante por CPF")
            print("7. Encerrar Programa")
            print(divider)
            escolha = input("\nSelecione uma opção: ")

            match escolha:
                case "1":
                    self.tela_cadastrar_visitante()
                case "2":
                    self.tela_remover_visitante()
                case "3":
                    self.tela_listar_visitantes()
                case "4":
                    self.tela_ordenar_visitantes()
                case "5":
                    return
                case "6":
                    self.tela_consultar_por_cpf()
                case "7":
                    break

    def tela_cadastrar_visitante(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("Cadastrar visitante:")
            print(divider)

            nome = solicitar_texto("Nome: ")

            while True:
                data_nascimento = solicitar_texto("Data de Nascimento (DD-MM-YYYY): ")
                try:
                    data_nascimento = datetime.strptime(data_nascimento, '%d-%m-%Y').date()
                    break
                except:
                    input("Erro: Valor inválido!")

            while True:
                try:
                    cpf = solicitar_texto("CPF: ")
                    if len(cpf) != 11:

                        print()
                        input("Erro: CPF inválido, deve conter 11 caracteres!")
                    else:
                        break
                except:
                    input("Erro: Valor inválido!")

            while True:
                print("Tipo de ingresso:")
                print("1. Normal:")
                print("2. VIP:")
                print("3. Premium:")

                ingresso_tipo_escolha = input("Ingresso: ")
                match ingresso_tipo_escolha:
                    case "1":
                        ingresso_tipo = IngressoTipo.Normal
                        break
                    case "2":
                        ingresso_tipo = IngressoTipo.Vip
                        break
                    case "3":
                        ingresso_tipo = IngressoTipo.Premium
                        break
                    case _:
                        input("Erro: Valor inválido!")

            while True:
                data_visita = solicitar_texto("Data de Visita (DD-MM-YYYY): ")
                try:
                    data_visita = datetime.strptime(data_visita, '%d-%m-%Y').date()
                    break
                except:
                    input("Erro: Valor inválido!")

            novo_visitante = {
                "nome": nome,
                "dataNascimento": data_nascimento,
                "cpf": cpf,
                "ingressoTipo": ingresso_tipo,
                "dataVisita": data_visita
            }

            resultado = self.visitantes_service.cadastrar_visitante(novo_visitante)

            print()
            print(resultado)
            print()
            print(divider)
            mensagem_voltar()
            return

    def tela_remover_visitante(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("Remover por CPF:")
            print(divider)
            while True:
                try:
                    cpf = solicitar_texto("CPF: ")
                    if len(cpf) != 11:

                        print()
                        input("Erro: CPF inválido, deve conter 11 caracteres!")
                    else:
                        break
                except:
                    input("Erro: Valor inválido!")

            resultado = self.visitantes_service.consultar_por_cpf(cpf)

            for chave, valor in resultado.items():
                print(f"{chave}: {valor}")

            print()
            print(divider)
            mensagem_voltar()
            return

    def tela_listar_visitantes(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("Lista de visitantes:")
            print(divider)

            resultado = self.visitantes_service.listar_todos()

            for chave, valor in resultado.items():
                print(f"{chave}: {valor}")

            print()
            print(divider)
            mensagem_voltar()
            return

    def tela_ordenar_visitantes(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("Ordenar visitantes:")
            print(divider)

            print("1. Ordernar por nome")
            print("2. Ordernar por idade")
            print("3. Voltar")

            escolha = input("Opção: ")
            match escolha:
                case "1":
                    resultado = self.visitantes_service.listar_todos(ordem=Ordenar.Nome)
                case "2":
                    resultado = self.visitantes_service.listar_todos(ordem=Ordenar.Idade)
                case "3":
                    break
                case _:
                    continue

            for chave, valor in resultado.items():
                print(f"{chave}: {valor}")

            print()
            print(divider)
            mensagem_voltar()
            return

    def tela_filtrar_visitantes(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("Ordenar visitantes:")
            print(divider)

            print("1. Filtrar por Ingresso Normal")
            print("2. Filtrar por Ingresso VIP")
            print("3. Filtrar por Ingresso Premium")
            print("4. Voltar")

            escolha = input("Opção: ")
            match escolha:
                case "1":
                    resultado = self.visitantes_service.listar_todos(filtro=IngressoTipo.Normal)
                case "2":
                    resultado = self.visitantes_service.listar_todos(filtro=IngressoTipo.Vip)
                case "3":
                    resultado = self.visitantes_service.listar_todos(filtro=IngressoTipo.Premium)
                case "4":
                    break
                case _:
                    continue

            for chave, valor in resultado.items():
                print(f"{chave}: {valor}")

            print()
            print(divider)
            mensagem_voltar()
            return

    def tela_consultar_por_cpf(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("Consulta por CPF:")
            print(divider)
            while True:
                try:
                    cpf = solicitar_texto("CPF: ")
                    if len(cpf) != 11:

                        print()
                        input("Erro: CPF inválido, deve conter 11 caracteres!")
                    else:
                        break
                except:
                    input("Erro: Valor inválido!")

            resultado = self.visitantes_service.consultar_por_cpf(cpf)
            print(divider)
            for chave, valor in resultado.items():
                print(f"{chave}: {valor}")

            print(divider)
            mensagem_voltar()
            return
