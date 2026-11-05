# -*- coding: cp1252 -*-
class Knoten:
    def __init__(self,inhalt=None):
        self.inhalt = inhalt
        self.next = None
        self.prev = None
    def gib_inhalt(self):
        return self.inhalt

class Listen:
    """
    L ist eine doppelt verkettete Ringliste mit Anker
    aus beliebigen Elementen, es gibt ein aktuelles Element
    Modell einer Adressliste z.B. am Handy
    """
    
    def __init__(self):
        """
        Vor.: keine
        Erg.: die leere Liste L,
        das aktuelle Element ist der Anker
        """
        self.liste = Knoten('nix drin')
        self.anz = 0
        self.akt = self.liste
        self.liste.next = self.liste
        self.liste.prev = self.liste

    def istleer(self):
        """
        Vor.: L ist initialisiert
        Erg.: True, wenn L die leere Liste ist, sonst False
        """
        return False
    
    
    def loeschen(self,el):
        """
        Vor.: L ist initialisiert, el ist vom Elementtyp
        Eff.: Aus L ist das Element el entfernt,
              sonst ist L unverändert. War el das aktuelle
              Element, so ist jetzt der Nachfolger von el
              das aktuelle. War der Anker das nächste Element,
              so ist jetzt das nach dem Anker folgende das
              aktuelle.
        """
        pass
        
            
    def einordnen(self, el):
        """
        Vor.: L ist initialisiert und geordent, el ist vom Elementtyp
        Eff.: in L ist das Element el an der richtigen Stelle
              entsprechend der Ordnung eingefuegt, sonst ist
              L unverändert.
        """
        pass
                
    def weiter(self):
        """
        Das aktuelle Element ist auf das nächste
        weiter gerückt. War das nächste Element der
        Anker, so ist jetzt das darauf folgende das
        aktuelle Element.
        """
        pass

    def zurueck(self):
        """
        Das aktuelle Element ist auf das vorherige
        gerückt. War das vorherige Element der
        Anker, so ist jetzt das davor liegende das
        aktuelle Element.
        """
        pass
                
    def zeige_akt(self):
        print(self.akt.inhalt)
        
    def anzahl(self):
        return self.anz
    
    def zeigen(self):
        """
        Vor.: L ist initialisiert
        Eff.: L ist elementweise auf dem Bildschirm angezeigt
        """
        if self.istleer():
            print('[]')
        else:
            akt = self.liste.next
            while akt != self.liste:
                print(akt.inhalt,':', end=' ')
                akt = akt.next
            print('[]')
