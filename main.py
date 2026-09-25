from data import DbContext
from services import VisitantesService
from view import SistemaView

def main():
    db = DbContext()
    visitantes_service = VisitantesService(db=db)
    sistema_view = SistemaView(visitantes_service=visitantes_service)

    sistema_view.run()

if __name__ == "__main__":
    main()
