
# -*- coding: cp1252 -*-
class Knoten:
    def __init__(self,inhalt=None):
        self.inhalt = inhalt
        self.next = None
        self.prev = None
    def gib_inhalt(self):
        return self.inhalt

class Listen:

    def __init__(self):     
        self.liste = Knoten('nix drin')
        self.anz = 0
        self.akt = self.liste
        self.liste.next = self.liste
        self.liste.prev = self.liste

    def einordnen(self, el):
        akt = self.liste
        neu = Knoten(el)
        while akt != self.liste.prev and akt.next.inhalt < neu.inhalt:
            akt = akt.next
        if akt != self.liste.prev:
            neu.next = akt.next
            neu.prev = akt
            akt.next = neu
            akt.next.prev = neu
        
meineListe = Listen()
meineListe.einordnen(Knoten("e"))
