def bissextoSep(string):
    partes = string.split("/")
    if len(partes) != 3:
        return {}
    return {
        "dia": partes[0],
        "mes": partes[1],
        "mês": partes[1],  
        "ano": partes[2]
    }
