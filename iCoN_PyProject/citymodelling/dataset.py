import pandas as pd
import os



def import_dataset_musei(city):

    """

     dataframe_musei = pd.read_csv(directory + "\musei_italia.csv", sep=';',
                                names=["Comune", "Provincia", "Regione","Nome","Anno inserimento", "Data e ora inserimento",
                                       "Identificatore in OpenStreetMap", "Longitudine","Latitudine"])
    """
    directory = os.getcwd() + "\iCoN_PyProject\dataset"
    dataframe_musei = pd.read_csv(directory + "\musei_italia.csv", sep=';')
    dataframe_musei.dropna() #pulisce il dataset dalle celle vuote

    if city == "Milano":
        dataframe_musei_milano = dataframe_musei.loc[dataframe_musei["Comune"] == 15146]
        return dataframe_musei_milano
    elif city == "Torino":
        dataframe_musei_torino = dataframe_musei.loc[dataframe_musei["Comune"] == 1272]
        return dataframe_musei_torino
    elif city == "Roma":
        dataframe_musei_roma = dataframe_musei.loc[dataframe_musei["Comune"] == 58091]
        return dataframe_musei_roma
    elif city == "Napoli":
        dataframe_musei_napoli = dataframe_musei.loc[dataframe_musei["Comune"] == 63049]
        return dataframe_musei_napoli
    elif city == "Bari":
        dataframe_musei_bari = dataframe_musei.loc[dataframe_musei["Comune"] == 72006]
        return dataframe_musei_bari
    elif city == "Palermo":
        dataframe_musei_palermo = dataframe_musei.loc[dataframe_musei["Comune"] == 82053]
        return dataframe_musei_palermo


def import_dataset_attrazioni_turistiche(city):
    directory = os.getcwd() + "\iCoN_PyProject\dataset"
    dataframe_attrazioni_turistiche = pd.read_csv(directory + "\\attrazioni_turistiche_italia.csv", encoding='ISO-8859-1',
                                                   on_bad_lines='skip', sep = ';')


    dataframe_attrazioni_turistiche_clean = dataframe_attrazioni_turistiche[['Comune', 'Nome']] #seleziona solo le colonne Comune e Nome

    #dataframe_attrazioni_turistiche_clean = dataframe_attrazioni_turistiche_clean[dataframe_attrazioni_turistiche_clean.Comune != "ALTRO"]

    dataframe_attrazioni_turistiche_clean = dataframe_attrazioni_turistiche_clean.dropna(subset=["Nome"])

    dataframe_attrazioni_turistiche_clean = dataframe_attrazioni_turistiche_clean.drop_duplicates(subset=["Nome"])

    if city == "Milano":
        dataframe_attrazioni_turistiche_milano = dataframe_attrazioni_turistiche_clean.loc[dataframe_attrazioni_turistiche_clean["Comune"] == "MILANO"]
        return dataframe_attrazioni_turistiche_milano
    elif city == "Torino":
        dataframe_attrazioni_turistiche_torino = dataframe_attrazioni_turistiche_clean.loc[dataframe_attrazioni_turistiche_clean["Comune"] == "TORINO"]
        return dataframe_attrazioni_turistiche_torino
    elif city == "Roma":
        dataframe_attrazioni_turistiche_roma = dataframe_attrazioni_turistiche_clean.loc[dataframe_attrazioni_turistiche_clean["Comune"] == "ROMA"]
        return dataframe_attrazioni_turistiche_roma
    elif city == "Napoli":
        dataframe_attrazioni_turistiche_napoli = dataframe_attrazioni_turistiche_clean.loc[dataframe_attrazioni_turistiche_clean["Comune"] == "NAPOLI"]
        return dataframe_attrazioni_turistiche_napoli
    elif city == "Bari":
        dataframe_attrazioni_turistiche_bari = dataframe_attrazioni_turistiche_clean.loc[dataframe_attrazioni_turistiche_clean["Comune"] == "BARI"]
        return dataframe_attrazioni_turistiche_bari
    elif city == "Palermo":
        dataframe_attrazioni_turistiche_palermo = dataframe_attrazioni_turistiche_clean.loc[dataframe_attrazioni_turistiche_clean["Comune"] == "PALERMO"]
        return dataframe_attrazioni_turistiche_palermo

#importiamo il dataset sport
def import_dataset_sport(city):
    directory = os.getcwd() + "\iCoN_PyProject\dataset"
    dataframe_sport = pd.read_csv(directory + "\\stadi_italia.csv",
                                   encoding='utf-8',
                                   on_bad_lines='skip', sep=';')

    if city == "Milano":
        dataframe_sport_milano = dataframe_sport.loc[dataframe_sport["Comune"] == "MILANO"]
        return dataframe_sport_milano
    elif city == "Torino":
        dataframe_sport_torino = dataframe_sport.loc[dataframe_sport["Comune"] == "TORINO"]
        return dataframe_sport_torino
    elif city == "Roma":
        dataframe_sport_roma = dataframe_sport.loc[dataframe_sport["Comune"] == "ROMA"]
        return dataframe_sport_roma
    elif city == "Napoli":
        dataframe_sport_napoli = dataframe_sport.loc[dataframe_sport["Comune"] == "NAPOLI"]
        return dataframe_sport_napoli
    elif city == "Bari":
        dataframe_sport_bari = dataframe_sport.loc[dataframe_sport["Comune"] == "BARI"]
        return dataframe_sport_bari
    elif city == "Palermo":
        dataframe_sport_palermo = dataframe_sport.loc[dataframe_sport["Comune"] == "PALERMO"]
        return dataframe_sport_palermo



#importiamo il dataset parchi divertimento
def import_dataset_parchi_divertimento(city):
    directory = os.getcwd() + "\iCoN_PyProject\dataset"
    dataframe_parchi = pd.read_csv(directory + "\\parchi_divertimento_italia.csv",
                                                  encoding='utf-8',
                                                  on_bad_lines='skip', sep=';')

    dataframe_parchi = dataframe_parchi[["Comune", "Nome", "Rating"]]

    if city == "Milano":
        dataframe_parchi_milano = dataframe_parchi.loc[dataframe_parchi["Comune"] == "MILANO"]
        return dataframe_parchi_milano
    elif city == "Torino":
        dataframe_parchi_torino = dataframe_parchi.loc[dataframe_parchi["Comune"] == "TORINO"]
        return dataframe_parchi_torino
    elif city == "Roma":
        dataframe_parchi_roma = dataframe_parchi.loc[dataframe_parchi["Comune"] == "ROMA"]
        return dataframe_parchi_roma
    elif city == "Napoli":
        dataframe_parchi_napoli = dataframe_parchi.loc[dataframe_parchi["Comune"] == "NAPOLI"]
        return dataframe_parchi_napoli
    elif city == "Bari":
        dataframe_parchi_bari = dataframe_parchi.loc[dataframe_parchi["Comune"] == "BARI"]
        return dataframe_parchi_bari
    elif city == "Palermo":
        dataframe_parchi_palermo = dataframe_parchi.loc[dataframe_parchi["Comune"] == "PALERMO"]
        return dataframe_parchi_palermo

def import_dataset_cibo(city):
    directory = os.getcwd() + "\iCoN_PyProject\dataset"
    dataframe_cibo = pd.read_csv(directory + "\\cucina_italia.csv",
                                   encoding='utf-8',
                                   on_bad_lines='skip', sep=';')

    dataframe_cibo = dataframe_cibo[["Comune", "Nome"]]

    if city == "Milano":
        dataframe_cibo_milano = dataframe_cibo.loc[dataframe_cibo["Comune"] == "MILANO"]
        return dataframe_cibo_milano
    elif city == "Torino":
        dataframe_cibo_torino = dataframe_cibo.loc[dataframe_cibo["Comune"] == "TORINO"]
        return dataframe_cibo_torino
    elif city == "Roma":
        dataframe_cibo_roma = dataframe_cibo.loc[dataframe_cibo["Comune"] == "ROMA"]
        return dataframe_cibo_roma
    elif city == "Napoli":
        dataframe_cibo_napoli = dataframe_cibo.loc[dataframe_cibo["Comune"] == "NAPOLI"]
        return dataframe_cibo_napoli
    elif city == "Bari":
        dataframe_cibo_bari = dataframe_cibo.loc[dataframe_cibo["Comune"] == "BARI"]
        return dataframe_cibo_bari
    elif city == "Palermo":
        dataframe_cibo_palermo = dataframe_cibo.loc[dataframe_cibo["Comune"] == "PALERMO"]
        return dataframe_cibo_palermo


def get_dataset_musei(city):
    dataframe_musei_ = import_dataset_musei(city)
    return dataframe_musei_ #ritorna un dataframe pandas

def get_dataset_attrazioni(city):
    dataframe_attrazioni_ = import_dataset_attrazioni_turistiche(city)
    return dataframe_attrazioni_ #ritorna un dataframe pandas

def get_dataset_parchi(city):
    dataframe_parchi_ = import_dataset_parchi_divertimento(city)
    return dataframe_parchi_ #ritorna un dataframe pandas
