from datetime import datetime
from services import VisitantesService
from utils import clear_screen, title_divider, divider, print_title, solicitar_texto, mensagem_voltar, print_resultado
from enums import IngressoTipo, Ordenar

class SistemaView:
    def __init__(self, visitantes_service: VisitantesService):
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
            print("6. Consultar por CPF")
            print("7. Consultar por data da visita")
            print("8. Estatísticas")
            print("0. Encerrar Programa")
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
                    self.tela_filtrar_visitantes()
                case "6":
                    self.tela_consultar_por_cpf()
                case "7":
                    self.tela_consultar_por_data()
                case "8":
                    self.tela_estatisticas()
                case "0":
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
                data_nascimento = solicitar_texto("Data de Nascimento (DD/MM/YYYY): ")
                try:
                    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    if data_nascimento > datetime.now().date():
                        print("Erro: Data de nascimento inválida! (O visitante não pode nascer no futuro)")
                        input()
                    elif data_nascimento.year > datetime.now().date().year - 18:
                        print("Erro: Data de nascimento inválida! (O cadastro deve ser realizado por um adulto)")
                        input()
                    else:
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
                data_visita = solicitar_texto("Data de Visita (DD/MM/YYYY): ")
                try:
                    data_visita = datetime.strptime(data_visita, '%d/%m/%Y').date()
                    if data_visita < datetime.now().date():
                        print("Erro: Data de visita inválida! (Informe uma data igual ou posterior à data atual)")
                        input()
                    else:
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

            print(divider)
            print_resultado(resultado)
            print(divider)
            mensagem_voltar()
            return

    def tela_remover_visitante(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("Remover por CPF:")
            print("Digite '1' para voltar")
            print(divider)
            try:
                cpf = input("CPF: ")
                if cpf == '1':
                    return
                if len(cpf) != 11:
                    print("Erro: CPF inválido, deve conter 11 caracteres!")
                    input()
                    continue
            except:
                input("Erro: Valor inválido!")
                continue

            print("Tem certeza que deseja remover o visitante? (S/n)")
            confirmar = input("Opção: ").lower()
            if confirmar != "s":
                return

            resultado = self.visitantes_service.remover_visitante_por_cpf(cpf)

            print(divider)
            print_resultado(resultado)
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
            for visitante in resultado:
                for chave, valor in visitante.items():
                    print(f"{chave}: {valor}")
                print(divider)

            print()
            mensagem_voltar()
            return

    def tela_ordenar_visitantes(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("Digite '0' para voltar")
            print("Ordenar visitantes:")
            print(divider)

            print("1. Ordernar por nome")
            print("2. Ordernar por idade")
            print("3. Voltar")
            print()

            escolha = input("Opção: ")
            match escolha:
                case "1":
                    resultado = ordem = Ordenar.Nome
                case "2":
                    resultado = ordem = Ordenar.Idade
                case "3":
                    break
                case _:
                    continue

            print(divider)
            print("Visitantes:")
            print(divider)
            resultado = self.visitantes_service.listar_por_ordem(ordem)
            for visitante in resultado:
                for chave, valor in visitante.items():
                    print(f"{chave}: {valor}")
                print(divider)

            print()
            mensagem_voltar()

    def tela_filtrar_visitantes(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("Digite '0' para voltar")
            print("Ordenar visitantes:")
            print(divider)

            print("1. Filtrar por Ingresso Normal")
            print("2. Filtrar por Ingresso VIP")
            print("3. Filtrar por Ingresso Premium")
            print()

            escolha = input("Opção: ")
            match escolha:
                case "1":
                    resultado = filtro = IngressoTipo.Normal
                case "2":
                    resultado = filtro = IngressoTipo.Vip
                case "3":
                    resultado = filtro = IngressoTipo.Premium
                case _:
                    continue

            print(divider)
            print(f"Visitantes {filtro}:")
            print(divider)
            resultado = self.visitantes_service.listar_por_ingresso(filtro)
            for visitante in resultado:
                print(f"{visitante["Nome"]} - {visitante["Idade"]} anos")
                print(divider)

            print()
            mensagem_voltar()

    def tela_consultar_por_cpf(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("Digite '0' para voltar")
            print("Consulta por CPF:")
            print(divider)
            try:
                cpf = input("CPF: ")
                if cpf == '0':
                    return
                if len(cpf) != 11:
                    print("Erro: CPF inválido, deve conter 11 caracteres!")
                    input()
                    continue
            except:
                input("Erro: Valor inválido!")
                continue

            resultado = self.visitantes_service.consultar_por_cpf(cpf)
            print(divider)
            print_resultado(resultado)
            print(divider)
            mensagem_voltar()

    def tela_consultar_por_data(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("Digite '0' para voltar")
            print("Consulta por data da visita (DD/MM/AAAA):")
            print(divider)
            try:
                data = input("Data: ")
                if data == '0':
                    return
                data = datetime.strptime(data, '%d/%m/%Y')
            except:
                input("Erro: Valor inválido!")
                continue

            print()
            print(divider)
            print(f"Visitantes para {data.strftime('%d/%m/%Y')}:")
            print(divider)
            resultado = self.visitantes_service.consultar_por_data(data)
            for visitante in resultado:
                for chave, valor in visitante.items():
                    print(f"{chave}: {valor}")
                print(divider)

            print()
            mensagem_voltar()

    def tela_estatisticas(self):
        while True:
            clear_screen()
            print_title()

            print()
            print("Estatísticas do parque:")
            print(divider)

            resultado = self.visitantes_service.obter_estatisticas()
            
            print(resultado)
            print()
            mensagem_voltar()
