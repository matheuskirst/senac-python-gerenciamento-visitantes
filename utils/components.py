title_divider = "=" * 40
divider = "-" * 30

def print_title():
    print(title_divider)
    print("     PARQUE AVENTURA     ")
    print(title_divider)

def solicitar_texto(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor != "":
            return valor

    print("Este campo não pode ficar vazio!")

def mensagem_voltar():
    input("Pressione Enter para voltar")
