from models import Visitante

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

    def obter_todos(self):
        return self.visitantes

    def obter_por_index(self, index: int):
        return self.visitantes[index]
    
    def obter_por_nome(self, nome: str):
        filtro = []
        for visitante in self.visitantes:
            if visitante.nome == nome:
                filtro.append(visitante)
        return filtro
        
    def obter_por_cpf(self, cpf: str):
        for visitante in self.visitantes:
            if visitante.cpf == cpf:
                return visitante
        return None
    
    def obter_quantidade(self):
        return len(self.visitantes)
