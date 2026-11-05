class Listen: 
    def __init__(self):
        self.liste = None
    def istleer(self):
        return self.liste == None

    def loescheEl(self, el):
            if self.liste != None:
                akt = self.liste
                akt1 = self.liste
                while akt != None:
                    if akt.inhalt == el:            
                        if akt == self.liste:       
                            self.liste = akt.next
                        else:
                            akt1.next = akt.next
                    akt1 = akt

class Knoten:
    def __init__(self, inhalt):
        self.inhalt = inhalt
        self.next = None

    def einordnen(self, el):
        neu = Knoten(el)
        akt = self.liste
        if self.istleer():
            self.liste = neu
        else: 
            while akt.next != None and neu.inhalt > akt.next.inhalt:
                akt = akt.next

    def einordnen2(self,el):
        neu = Knoten(el)
        if self.liste == None:
            self.liste = neu
            return
        elif self.liste.inhalt > el:
            neu.next = self.liste
            self.liste = neu
        akt = self.liste
        while akt.next != None and akt.next.inhalt < neu.inhalt:    # suche richtige Stelle
            akt = akt.next
        neu.next = akt.next
        akt.next = neu