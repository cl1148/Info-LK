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

    def einfuegen(self,el):
        self.baum= self._einf(self.baum,el)
        
    def _einf(self, baum, el):
        if not baum:             return Knoten(el)
        elif baum.inhalt == el:  return baum
        elif baum.inhalt < el:   baum.rechts = self._einf(baum.rechts,el)
        else:                    baum.links  = self._einf(baum.links,el)
        return baum
        
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
   
