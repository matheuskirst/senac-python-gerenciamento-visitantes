from data import DbContext
from services import VisitanteService
from view import SistemaView

def main():
    db = DbContext()
    visitante_service = VisitanteService(db=db)
    sistema_view = SistemaView(visitantes_service=visitante_service)

    sistema_view.run()

if __name__ == "__main__":
    main()
