from pyswip import Prolog
from iCoN_PyProject.dataprocessing.dataprocessing import *

#a partire dai dataset preprocessati, scrivo nel file kb.pl
def setCityAttraction(city):

    #Specifico i tipi di attrazioni disponibili
    arte_cultura: str = "arte e cultura"
    attrazioni: str = "attrazione"
    sport: str = "sport"
    arte: str = "arte"
    per_famiglie = "famiglie"
    parco_divertimenti = "parco_divertimenti"

    city_museum = processingMusei(city)
    city_attractions = processingAttrazioniTuristiche(city)

    #file_exists = os.path.exists('iCoN_PyProject/prolog/kb.pl') #controllo se il file già esiste

    filename = "kb_"+city+".pl"
    path = "iCoN_PyProject/prolog/"+filename
    file = open(path, 'a', encoding="utf-8")

    for museum_name in city_museum:
        #prolog_engine.assertz("museo(museum_name,city)")
        file.write("posto"+"("+museum_name+","+city+","+arte_cultura+")."+"\n")

    for attraction_name in city_attractions:
        file.write("posto" + "(" + attraction_name + "," + city + "," +attrazioni+ ")." + "\n")

    file.close()



