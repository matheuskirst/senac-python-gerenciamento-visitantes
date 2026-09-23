from datetime import date

def resolver_idade(aniversario: date):
    hoje = date.today()
    nascimento = aniversario
    idade = hoje.year - aniversario.year
    if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
        idade -= 1
    return idade
