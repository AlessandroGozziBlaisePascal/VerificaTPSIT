class PannelloFotovoltaico:
    def __init__(self, codice:str, modello:str, potenza_kw: float) -> None
        if(codice is None) raise new ValueError("Null codice")
        self.codice = codice
        if(modello is None) raise new ValueError("Null modello")
        self.modello = modello
        if(potenza_kw <= 0) raise new ValueError("Must positive potenza")
        self.potenza_kw = potenza_kw
        
        