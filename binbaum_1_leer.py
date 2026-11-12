class Knoten:
    def __init__(self, inhalt):
        self.inhalt = inhalt
        self.rechts = None
        self.links = None
        
class Binbaum:
    """
    Binaerbaum
    """
    def __init__(self):
        self.baum = None

    def istleer(self):
        return self.baum == None

    def istInnerer(self):
        return self.baum != None and (self.baum.links != None or self.baum.rechts != None)

    def istBlatt(self):
        return self.baum != None and self.baum.links == None and self.baum.rechts == None

    def anzKnoten(self):
        return self._anzKnoten(self.baum)
    
    def _anzKnoten(self, baum):
        if not baum:
            return 0    
        return 1 + self._anzKnoten(baum.links) + self._anzKnoten(baum.rechts)

    def anzInnere(self):
        return self._anzInnere(self.baum)

    def _anzInnere(self, baum):
        if not baum:
            return 0
        if baum.links or baum.rechts:
            return 1 + self._anzInnere(baum.links) + self._anzInnere(baum.rechts)
        return 0

    def anzBlaetter(self):
        return self._anzBl(self.baum)

    def _anzBl(self, baum):
        if not baum:
            return 0
        elif self.istBlatt(baum):
            return 1
        else:
            return self._anzBl(baum.links) + self._anzBl(baum.rechts)

    def einfuegen(self,el):
        self.baum= self._einf(self.baum,el)
        
    def _einf(self, baum, el):
        if not baum:             return Knoten(el)
        elif baum.inhalt == el:  return baum
        elif baum.inhalt < el:   baum.rechts = self._einf(baum.rechts,el)
        else:                    baum.links  = self._einf(baum.links,el)
        return baum

    def hoehe(self):
        return self._hoehe(self.baum)

    def _hoehe(self, baum):
        if not baum:
            return 0
        else:
            return 1 + max(self._hoehe(baum.links), self._hoehe(baum.rechts))
    
    def show (self):
        if self.baum :            
            self._showtree (self.baum, 0)
        else         : print("-Leer")

    def _showtree (self, baum, h):
        if baum:
           self._showtree (baum.rechts,h+1)
           for i in range (h) : print("\t", end=' ')
           print(str (baum.inhalt) + " --< ")
           self._showtree (baum.links,h+1)
        else :
           for i in range (h) : print("\t", end=' ')
           print("-Leer")

if __name__=="__main__":
    b= Binbaum()
    b.show()
    for val in [7,6,1,4,2,5,3,11]:    
        b.einfuegen(val)
        print("einfuegen ",val,"\n\n")
        b.show()
        print("\n\n")
        
    b.show()
   
