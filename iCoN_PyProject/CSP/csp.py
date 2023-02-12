import datetime

from constraint import *
from datetime import datetime, timedelta

#stanze

A = "Stanza Doppia Matrimoniale"
B = "Stanza Tripla (matrimoniale e singolo)"
C = "Stanza Singola"
D = "Stanza Quadrupla (due letti singoli e uno matrimoniale"
E = "Suite Royal Excelsior"

H1 = "Hotel Excelsior"
H2 = "B&B Il Belvedere"
H3 = "Hotel La Rotonda"
H4 = "Hotel Principe Savoia"

#classe csp
class room_csp(Problem):
    def __init__(self, room: str, solver=None):
        super().__init__(solver=solver)
        self.room = room
        self.letto = self.addVariable("letto", ["singolo", "matrimoniale", "king size"])
        self.giorni = self.addVariable("giorni", [1, 2, 3, 4, 5, 6, 7])
        self.disponibilità = None

    def verifica_disponibilità(self):
        #print("Risoluzione del CSP con metodo: %s" %  (self.getSolver()))
        self.disponibilità = sorted(self.getSolutions(), key=lambda g: ['giorni'])

        if len(self.disponibilità) > 0:
            print("Ecco le stanze disponibili nell'Hotel scelto: ")
            i = 0
            while i < len(self.disponibilità):
                data_iniziale = datetime.strftime(datetime.today(), "%d/%m/%Y")
                data_finale = datetime.today() + timedelta(days=self.disponibilità[i]['giorni'])
                data_finale = datetime.strftime(data_finale, "%d/%m/%Y")
                print("Stanza[%d]: Da %d persone con Letto %s - Disponibile dal %s al %s " % (i, self.disponibilità[i]['persone'], self.disponibilità[i]['letto'], data_iniziale, data_finale))
                i = i+1
        else:
            print("Non ci sono stanze disponibili")

        return self.disponibilità

def genera_csp(num_persone):

    hotel_1 = room_csp(H1)
    hotel_1.addVariable("persone", [num_persone])
    hotel_1.addConstraint(lambda letto, persone, giorni: persone == 2 if letto == "matrimoniale" and giorni == 7 else persone == 1 if letto == "singolo" and giorni == 3 else None, ["letto", "persone", "giorni"])

    hotel_2 = room_csp(H2)
    hotel_2.addVariable("persone", [num_persone])
    hotel_2.addConstraint(lambda letto, persone, giorni: persone == 3 if letto == "matrimoniale + singolo" and giorni == 3 else persone == 4 if letto == "quattro singoli" and giorni == 5 else None,  ["letto", "persone", "giorni"])

    hotel_3 = room_csp(H3)
    hotel_3.addVariable("persone", [num_persone])
    hotel_3.addConstraint(lambda letto, persone,giorni: persone == 5 if letto == "matrimoniale" and giorni == 4 else persone == 1 if letto == "singolo" and giorni == 3 else None, ["letto", "persone", "giorni"])

    hotel_4 = room_csp(H4)
    hotel_4.addVariable("persone", [num_persone])
    hotel_4.addConstraint(lambda letto, persone, giorni: persone == 2 if letto == "king size" and giorni == 3 else persone == 1 if letto == "singolo" and giorni == 3 else None, ["letto", "persone", "giorni"])


    return [hotel_1, hotel_2, hotel_3, hotel_4]

def booking():


    print("Vuoi prenotare una stanza per la prossima settimana? [y/n]")
    risposta = str(input())



    if risposta == "y":
        print("Per quante persone vuoi prenotare?")
        num_persone = int(input())

        stanze = genera_csp(num_persone)

        print("Scegli una struttura fra quelle proposte: ")
        print("[1] %s\n[2] %s\n[3] %s\n[4] %s\n" % (H1, H2, H3, H4))
        scelta_hotel = int(input())

        while scelta_hotel <1 or scelta_hotel > 4:
            print("Selezione non valida. Scegli un una struttura da 1 a 4")
            scelta_hotel = int(input())

        hotel_selezionato = stanze[scelta_hotel-1]

        if len(hotel_selezionato.verifica_disponibilità()) > 0:

            print("\nScegli una stanza fra quelle disponibili:")
            prenotazione = int(input())

            if scelta_hotel == 1:
                print("Hai prenotato la stanza %d della struttura %s" % (prenotazione, H1))
            elif scelta_hotel == 2:
                print("Hai prenotato la stanza %d della struttura %s" % (prenotazione, H2))
            elif scelta_hotel == 3:
                print("Hai prenotato la stanza %d della struttura %s" % (prenotazione, H3))
            elif scelta_hotel == 4:
                print("Hai prenotato la stanza %d della struttura %s" % (prenotazione, H4))

    return

if __name__ == '__main__':
    booking()