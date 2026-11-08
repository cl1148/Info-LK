class Knoten:
    def __init__(self,inhalt):
        self.inhalt = inhalt
        self.next = None
    
class Stapel:    
    def __init__(self):        
        self.kopf = None #Zeiger auf den ersten Knoten
        
    def istLeer(self):        
        return self.kopf == None
   
    def auflegen_el(self, el):        
        neu=Knoten(el)
        neu.next=self.kopf
        self.kopf=neu
        
    def erstes_El(self):
        if not self.istLeer():
            return print(self.kopf.inhalt)
        else:
            return None
            
    def abnehemen(self):
        if not self.istLeer():
            self.kopf = self.kopf.next 
        else: 
            return None

    def zeigen(self):
        if self.istLeer():
            print('[]')
        else:
            print('[',end='')
            knoten=self.kopf 
            while knoten != None:
                print(knoten.inhalt,end='')
                knoten=knoten.next
                if knoten != None: print(',',end='')
            print(']')
            
 
              
if __name__ == "__main__":
    st = Stapel()
    st.auflegen_el(5)
    st.auflegen_el(3)
    st.auflegen_el(1)
    st.erstes_El()
    st.zeigen()
