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
    
if __name__ = __main__:
    impianti = list[ImpiantoSolare]
    impianti.registra_impianto(impianti, ImpiantoSolare("3232","Pascal","Sassari",300.00,"Attivo"))
    impianti.registra_impianto(impianti, ImpiantoSolare("2234","Pascal","Santa",300.00,"In collaudo"))
    impianti.registra_impianto(impianti, ImpiantoSolare("1123","Comadnini","Asss",300.00,"In collaudo"))
    impianti.registra_impianto(impianti, ImpiantoSolare("6666","Comadnini","Santa",300.00,"In installazione"))
    
    
    