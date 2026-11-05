from tkinter import *
from dlisten_dummy import *
l = Listen()
def vorwaerts():
    """
    diese Methode sorgt dafuer, dass die Anzeige nach der Rechnung
    aktualisiert wird
    """
    l.weiter()
    ergebnis['text']=l.akt.gib_inhalt()  

def zurueck():
    """
    diese Methode sorgt dafuer, dass die Anzeige nach der Rechnung
    aktualisiert wird
    """
    l.zurueck()
    ergebnis['text']=l.akt.gib_inhalt()
    
def rein():
    """
    diese Methode sorgt dafuer, dass die Anzeige nach der Rechnung
    aktualisiert wird
    """
    text= wert1.get()
    l.einordnen(text)
    ergebnis['text']=l.akt.gib_inhalt()
    
def raus():
    el= wert1.get()
    l.loeschen(el)
#dieser ganze Kram ist fuer die Anzeige notwendig   
schrift = 'arial 12  bold'
hauptfenster  = Tk ()
hauptfenster.title ("Adressverwalter")

fenster1     = Frame (hauptfenster)#ein Rahmen fuer graph. Elemente
fenster1.pack ()
fenster2     = Frame (hauptfenster)
fenster2.pack ()
fenster3     = Frame (hauptfenster)
fenster3.pack ()
#Wert 1
text1 = Label(fenster1, text = 'neuer Eintrag',font = schrift)  #ein Textfeld
wert1 = Entry (fenster1 )                #ein Eingabefeld
wert1.insert(0,'')                         #der Defaultwert beim Programmstart
text1.pack (side="left")
wert1.pack (side="left")
# das Ergebnis
text3 = Label(fenster3, text = 'aktuelles: ',font= schrift)
ergebnis  = Label (fenster3, font= schrift,text=l.akt.gib_inhalt())
text3.pack (side="left")
ergebnis.pack (side="left")
Knopf1 = Button (hauptfenster, text="->",font= schrift,width='12',
                      command = vorwaerts,bg="red")
Knopf1.pack (side="left")
Knopf2 = Button (hauptfenster, text="<-",font= schrift,width='12',
                      command = zurueck, bg="yellow")
Knopf2.pack (side="left")
Knopf3 = Button (hauptfenster, text="übernehmen",font= schrift,width='12',
                      command = rein, bg="green")
Knopf3.pack (side="left")
Knopf4 = Button (hauptfenster, text="löschen",font= schrift,width='12',
                      command = raus, bg="blue")
Knopf4.pack (side="left")
endeknopf = Button(hauptfenster, text = 'ENDE', font= schrift,bg="black",
                   command=hauptfenster.destroy, fg="white")
endeknopf.pack(side="right")
hauptfenster.mainloop ()
