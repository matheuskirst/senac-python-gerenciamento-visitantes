from enums import IngressoTipo

def resolver_ingresso_tipo(tipo):
    match tipo.ingresso_tipo:
        case IngressoTipo.Normal:
            ingresso_tipo = "Normal"
        case IngressoTipo.Vip:
            ingresso_tipo = "VIP"
        case IngressoTipo.Premium:
            ingresso_tipo = "Premium"
    return ingresso_tipo
