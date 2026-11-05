#Beispielprogramm fuer einfach verkettete Listen

class Knoten:
    def __init__(self,inhalt):
        self.inhalt = inhalt
        self.next = None
    
class Listen:    
    def __init__(self):        
        self.liste = None #Zeiger auf den ersten Knoten
        
    def istLeer(self):        
        return self.liste == None
    
    def laenge(self):
        #ToDo
        return 0
   
    def vornAnhaengen(self, el):        
        """
        Vor.: die Liste ist initialisiert
        Erg.: das neue Element ist der neue Kopf der Liste, der
              Rest ist unveraendert
        """
        neu=Knoten(el)
        neu.next=self.liste
        self.liste=neu
        
    def istEnthalten(self,el):
        """
        Vor.: die Liste ist initialisiert
        Erg.: geliefert ist True, falls el in der Liste ist,
              sonst False
        """      
        return False #todo
        
    def hintenAnhaengen(self,el):
        """
        Vor.: die Liste ist initialisiert
        Erg.: das neue Element ist das letzte Element der Liste, der
              Rest ist unveraendert
        """        
        neu=Knoten(el)
        if self.istLeer():
            self.liste =neu
        else:
            akt=self.liste
            while akt.next:
                akt=akt.next
            akt.next =neu
            
            
    def einordnen(self,el):
        """
        Vor.: die Liste ist initialisiert und geordnet
        Erg.: das neue Element ist eingeordnet
        """
        neu=Knoten(el)
        if not self.liste: #liste leer
            self.liste=neu            
        elif self.liste.inhalt > el: #nur ein Element
            neu.next = self.liste
            self.liste = neu            
        else:
            akt= self.liste
            while akt.next and akt.next.inhalt<neu.inhalt: #suche richtige Stelle
                akt=akt.next
            neu.next=akt.next
            akt.next= neu
        
        
        
        
        
        
        
        
        
    def loescheElement(self,el):
        """
        Vor.: die Liste ist initialisiert
        Erg.: das uebergebene Element ist in der Liste nicht mehr vorhanden
              sonst ist nichts veraendert
        """
        pass
    
    def zeigen(self):
        if self.istLeer():print('[]')
        else:
            print('[',end='')
            akt=self.liste
            while akt.next:
                print(akt.inhalt,end=', ')
                akt=akt.next
            print(akt.inhalt,end=']\n')
            
 
              
if __name__ == "__main__":
    li = Listen()    
    for el in [5,3,1,1,4,9]:
        li.einordnen(el)    
        li.zeigen()
    
    
