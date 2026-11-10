#Beispielprogramm fuer einfach verkettete Listen

class Knoten:
    def __init__(self,inhalt):
        self.inhalt = inhalt
        self.next = None
    
class Stapel:    
    def __init__(self):        
        self.kopf = None #Zeiger auf den ersten Knoten
        
    def istLeer(self):        
        return self.kopf == None
   
    def auflegen(self, el):        
        neu=Knoten(el)
        neu.next=self.kopf
        self.kopf=neu
        
    def oben(self):
        if not self.istLeer():
            return self.kopf.inhalt
        else:
            return None
            
    def entnehmen(self):
        if not self.istLeer():
            self.kopf = self.kopf.next

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
    
# if __name__ == "__main__":
#    st = Stapel()
#    st.auflegen(5)
#    st.auflegen(3)
#    st.auflegen(1)
#    st.erstes()
#    st.zeigen()

if __name__ == "__main__":
    rechnung = input("Geben Sie eine Zeichenkette ein: ")
    st = Stapel()
    rechnungArray = rechnung.split(" ")
    for el in rechnungArray:
        if el == "+" or el == "-" or el == "*" or el == "/":
            operand1 = st.oben()
            st.entnehmen()
            operand2 = st.oben()
            st.entnehmen()
            if el == "+":
                st.auflegen(operand2 + operand1)
            elif el == "-":
                st.auflegen(operand2 - operand1)
            elif el == "*":
                st.auflegen(operand2 * operand1)
            elif el == "/":
                st.auflegen(operand2 / operand1)
        else:
            st.auflegen(float(el))
    ergebnis = st.oben()
    st.entnehmen()
    if not st.istLeer(): 
        print("Fehlender Operator am Ende!")
    else:
        print(ergebnis)
