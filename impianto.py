class ImpiantoSolare:
    def __init__(self, codice: str, modello: str, localita: str, potenza_masssima_kw: float, stato: str) -> None
        if(codice is None) raise ValueError("Codice null")
        self.codice = codice
        if(modello is None) raise ValueError("Modello null")
        self.modello = modello
        if(localita is None) raise ValueError("Località null")
        self.localita = localita
        if(potenza_massima_kw <= 0) raise ValueError("Potenza massima deve essere positiva")
        self.potenza_massima_kw = potenza_massima_kw
        if(stato is None) raise ValueError("Stato null")
        self.stato = stato
        self.pannelli = []
        
    def aggiungi_pannello(pannello: PannelloFotovoltaico) -> None
        int sum = 0
        for pnl in self.pannelli
            if(cerca_pannello(pannello.codice) == pnl)
                raise ValueError("Codici duplicati")sum = sum + pnl.potenza_kw
        if(potenza_pannelli() + pannello.potenza_kw > self.potenza_massima_kw)
            raise ValueError("Potenza massiam superata")
        self.pannelli.append(pannello)
    
    def potenza_pannelli() -> float
        for pnl in self.pannelli
            sum = sum + pnl.potenza_kw
        return sum
    
    def cerca_pannello(codice: str) -> PannelloFotovoltaico
        for pnl in self.pannelli
            if(pnl.codice == codice)
                return pnl
        return None
            
    def rimuovi_pannello(codice :str) -> PannelloFotovoltaico
        for pnl in self.pannelli
            if(pnl.codice == codice)
                self.pannelli.remove(pnl)
                return pnl
            
    def pannelli_sotto_potenza(potenza_massima: float) -> list[PannelloFotovoltaico]
        list[PannelloFotovoltaico] panels = []
        for pnl in self.pannelli
            if(pnl is not PannelloFotovoltaico)
                raise ValueError("No pannello")
            if(potenza_massima <= 0) raise ValueError("Potenza negativa")
            if(pnl.potenza_kw <= potenza_massima)
                panels.append(pnl)
        return panels
        
    
        
        