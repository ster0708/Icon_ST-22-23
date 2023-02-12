from operator import attrgetter
from iCoN_PyProject.citymodelling.city import *
from iCoN_PyProject.learning.bayesian_network_3 import *
from iCoN_PyProject.CSP.csp import *
from iCoN_PyProject.prolog.prolog import *


def startProlog(citta):

    esci = False

    while not esci:
        print("\nVuoi saperne di più su %s? Scegli una delle seguenti opzioni:" % (citta))

        print("[1] - E' una città di mare?")
        print("[2] - Quali sono le specialità culinarie?")
        print("[3] - Quali sono gli eventi sportivi?")
        print("[4] - Quali sono i parchi divertimento nei dintorni?")
        print("[0] - Esci \n")

        scelta = int(input())

        if scelta == 1:
            if prolog_hasMare(citta.lower()):
                print("%s è una città di mare" % citta) #aggiungi controllo sul mese per la balneazione
                print("Vuoi sapere se ci sonospiagge in città? [y / n]")
                risposta = str(input())
                if risposta == "y":
                    listaspiagge = prolog_getSpiagge(citta.lower())
                    print("Le spiagge di %s sono:" % citta)
                    i = 1
                    for spiag in listaspiagge:
                        print("%d - %s" % (i, spiag))
                        i = i + 1
            else:
                print("%s non è una città di mare" % citta)
        if scelta == 2: #specialità culinarie
            lista_cibi = prolog_getCibi(citta)
            print("Le specialità culinarie di %s sono:" % citta)
            i = 1
            for cib in lista_cibi:
                print("%d - %s" % (i, cib))
                i = i + 1
        if scelta == 3: #eventi sportivi
            lista_sport = prolog_getSport(citta.lower())
            print("Gli stadi famosi vicino %s sono:" % citta)
            i = 1
            for sp in lista_sport:
                print("%d - %s" % (i , sp))
                i = i+1

        if scelta == 4:
            lista_parchi = prolog_getParchi(citta.lower())
            print("I parchi divertimento vicino %s sono:" % citta)
            print("1 - %s" % (lista_parchi[0]))
            print("2 - %s\n" % (lista_parchi[1]))
        if scelta == 0:
            esci = True

    return


if __name__ == '__main__':

    print("Start... \n")
    print("Vediamo cosa cerchi nel tuo prossimo viaggio! \n")

    print("Vuoi visitare musei e luoghi di rilevanza artistica/culturale? [y/n]")

    arte_cultura: str = input()

    print("Ti interessano eventi sportivi e sei un appassionato di calcio? [y/n]")

    sport: str = input()

    print("Vuoi viaggiare con la famiglia e cerchi divertimento per grandi e piccoli? [y/n]")

    parchi: str = input()

    print("Hai interesse nel degustare cibo tipico della cucina locale? [y/n]")

    cibo: str = input()

    print("\n")

    print("Calcoliamo la tua prossima meta...")

    cultura, divertimento, famiglia = init(arte_cultura, sport, parchi, cibo)

    lista_proba = predict_bayesian(build_network(), cultura, divertimento, famiglia)

    lista_citta = list()

    Milano = City("Milano", lista_proba[0])
    lista_citta.append(Milano)

    Torino = City("Torino", lista_proba[1])
    lista_citta.append(Torino)

    Roma = City("Roma", lista_proba[2])
    lista_citta.append(Roma)

    Napoli = City("Napoli", lista_proba[3])
    lista_citta.append(Napoli)

    Palermo = City("Palermo", lista_proba[4])
    lista_citta.append(Palermo)

    Bari = City("Palermo", lista_proba[5])
    lista_citta.append(Bari)

    lista_citta = sorted(lista_citta, key=attrgetter('prob'), reverse=True)
    print("\nLe città più compatibili con te sono:")
    i = 1
    while i <= 3:
        print("[%d] - %s, con una probabilità di %.2f " % (i, lista_citta[i].getNome(), lista_citta[i].getProb() * 100))
        i = i + 1

    print("\nQuale città scegli?")
    i_cit = int(input())
    print("\nHai scelto %s" % lista_citta[i_cit].getNome())

    booking()

    startProlog(lista_citta[i_cit].getNome())





