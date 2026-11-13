def registra_impianto(impianti: list[ImpiantoSolare], impianto: ImpiantoSolare) -> None
    if(impianti is None) raise ValueError("Impianti null")
    if(impianto is None) raise ValueError("Impianto null")
    
def cerca_impianto(impianti: list[ImpiantoSolare], codice: str) -> ImpiantoSolare
    for imp in impianti:
            if imp.Codice == codice:
                return imp
    return None

def riepilogo_impianti(nome_azienda: str, impianti: list[ImpiantoSolare]) -> None
    for imp in impianti:
        if imp.modello = nome_azienda
            print(f"{imp.codice}, {imp.modello}, {imp.stato} {imp.potenza_kw}")