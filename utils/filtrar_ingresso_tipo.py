from enums import IngressoTipo

def filtrar_ingresso_tipo(ingresso:IngressoTipo, tipo: IngressoTipo):
    if ingresso == tipo:
        return True
    else:
        return False
