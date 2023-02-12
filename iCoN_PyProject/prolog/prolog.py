import os

from pyswip import Prolog
from swiplserver import PrologMQI
from iCoN_PyProject.dataprocessing.dataprocessing import *


#a partire dai dataset preprocessati, scrivo nel file kb.pl. (mode = 0 tutte le citta mode = 1 una sola citta) #da chiamare una sola volta
def setCityAttraction(city, mode):

    #Specifico i tipi di attrazioni disponibili
    arte_cultura: str = "arte e cultura"
    attrazioni: str = "attrazione"
    sport: str = "sport"
    arte: str = "arte"
    per_famiglie = "famiglie"
    parco_divertimenti = "parco_divertimenti"

    city_museum = processingMusei(city)
    city_attractions = processingAttrazioniTuristiche(city)
    city_sport = processingSport(city)
    city_cibi = processingCibo(city)
    city_parchi = processingParchi(city)


    #file_exists = os.path.exists('iCoN_PyProject/prolog/kb.pl') #controllo se il file già esiste
    if mode == 1:
        filename = "kb_"+city+".pl"
    else:
        filename = "kb_all.pl"

    path = "iCoN_PyProject/prolog/"+filename
    file = open(path, 'a', encoding="utf-8")


    for museum_name in city_museum:
        file.write("posto"+"("+museum_name+","+city+")."+"\n")

    for attraction_name in city_attractions:
        file.write("posto" + "(" + attraction_name + "," + city + ")." + "\n")

    for sport_name in city_sport:
        file.write("sport" + "(" + sport_name + "," + city + ")." + "\n")

    for cibo_name in city_cibi:
        file.write("cucina" + "(" + cibo_name + "," + city + ")." + "\n")

    for parco_name in city_parchi:
        file.write("parcodivertimenti" + "(" + parco_name + "," + city + ")." + "\n")

    file.close()

def prologSwiplServer():
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            result = prolog_thread.query("set_prolog_flag(encoding,utf8).")
            print(result)
            result = prolog_thread.query("consult(\"iCoN_PyProject/prolog/kb_all.pl\").")

    return result


def prolog_getCibi(city): #interroga la kb e restituisce tutte le specialità culinarie di una città

    lista_cibi = list()
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query("set_prolog_flag(encoding,utf8).")
            prolog_thread.query("consult(\"iCoN_PyProject/prolog/kb_all.pl\").")

            if city == "Milano":
                result = prolog_thread.query("cucina(Nome, milano).")
                for cibo in result:
                    lista_cibi.append(cibo["Nome"])
            elif city == "Torino":
                result = prolog_thread.query("cucina(Nome, torino).")
                for cibo in result:
                    lista_cibi.append(cibo["Nome"])
            elif city == "Roma":
                result = prolog_thread.query("cucina(Nome, roma).")
                for cibo in result:
                    lista_cibi.append(cibo["Nome"])
            elif city == "Napoli":
                result = prolog_thread.query("cucina(Nome, napoli).")
                for cibo in result:
                    lista_cibi.append(cibo["Nome"])
            elif city == "Bari":
                result = prolog_thread.query("cucina(Nome, bari).")
                for cibo in result:
                    lista_cibi.append(cibo["Nome"])
            elif city == "Palermo":
                result = prolog_thread.query("cucina(Nome, palermo).")
                for cibo in result:
                    lista_cibi.append(cibo["Nome"])

    return lista_cibi


def prolog_getSport(city):

    lista_sport = list()
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query("set_prolog_flag(encoding,utf8).")
            prolog_thread.query("consult(\"iCoN_PyProject/prolog/kb_all.pl\").")

            result = prolog_thread.query("sport(Nome, "+city+")")

            for sport in result:
                lista_sport.append(sport["Nome"])

    return lista_sport

def prolog_getParchi(city):

    lista_parchi = list()
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query("set_prolog_flag(encoding,utf8).")
            prolog_thread.query("consult(\"iCoN_PyProject/prolog/kb_all.pl\").")

            result = prolog_thread.query("parcodivertimenti(Nome, " + city + ")")

            for parco in result:
                lista_parchi.append(parco["Nome"])

    return lista_parchi

def prolog_getSpiagge(city):

    lista_spiagge = list()
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query("set_prolog_flag(encoding,utf8).")
            prolog_thread.query("consult(\"iCoN_PyProject/prolog/kb_all.pl\").")

            result = prolog_thread.query("spiaggia(Nome, " + city + ")")

            for spiaggia in result:
                lista_spiagge.append(spiaggia["Nome"])

    return lista_spiagge

def prolog_hasMare(city): #interroga la kb e dice se la città ha o non ha il mare
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query("set_prolog_flag(encoding,utf8).")
            prolog_thread.query("consult(\"iCoN_PyProject/prolog/kb_all.pl\").")
            result = prolog_thread.query("hamare("+city+")")

    return result



if __name__ == '__main__':

    prolog_getParchi("Roma")