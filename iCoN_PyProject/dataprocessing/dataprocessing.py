from iCoN_PyProject.citymodelling.dataset import *
from array import *

def processingMusei(city):

    replacement = {  # set di caratteri da sostituire nel dataframe
        "'": "",
        " ": "_",
        "-": "_",
        "à": "a",
        "é": "e",
        "ù": "u",
        "ò": "o"
    }

    df = get_dataset_musei(city)

    city_museum = df['Nome'].replace(replacement, regex=True)
    city_museum.replace("?", "")

    return city_museum

def processingAttrazioniTuristiche(city):

    replacement = {  # set di caratteri da sostituire nel dataframe
        "'": "",
        " ": "_",
        "-": "_",
        "à": "a",
        "é": "e",
        "ù": "u",
        "ò": "o"
    }

    df = get_dataset_attrazioni(city)

    city_attraction = df['Nome'].replace(replacement, regex=True)

    return city_attraction

def processingSport(city):
    replacement = {  # set di caratteri da sostituire nel dataframe
        "'": "",
        " ": "_",
        "-": "_",
        "à": "a",
        "é": "e",
        "ù": "u",
        "ò": "o"
    }

    df = get_dataset_sport(city)

    city_sports = df['Nome'].replace(replacement, regex=True)

    return city_sports

def processingCibo(city):
    replacement = {  # set di caratteri da sostituire nel dataframe
        "'": "",
        " ": "_",
        "-": "_",
        "à": "a",
        "é": "e",
        "ù": "u",
        "ò": "o"
    }

    df = get_dataset_cibi(city)

    city_cibi = df['Nome'].replace(replacement, regex=True)

    return city_cibi

def processingParchi(city):
    replacement = {  # set di caratteri da sostituire nel dataframe
        "'": "",
        " ": "_",
        "-": "_",
        "à": "a",
        "é": "e",
        "ù": "u",
        "ò": "o"
    }

    df = get_dataset_parchi(city)

    city_parchi = df['Nome'].replace(replacement, regex=True)

    return city_parchi

#restituisce le frequenze nel dataset di ogni categoria per ogni città
def getFrequencies(city):
    dataset_musei = get_dataset_musei(city)
    dataset_attrazioni = get_dataset_attrazioni(city)
    dataset_sport = get_dataset_sport(city)
    dataset_parchi = get_dataset_parchi(city)
    dataset_cibi = get_dataset_cibi(city)

    freq_musei = dataset_musei.groupby(["Comune"]).size()
    freq_attrazioni = dataset_attrazioni.groupby(["Comune"]).size()
    freq_sport = dataset_sport.groupby(["Comune"]).size()
    freq_parchi = dataset_parchi.groupby(["Comune"]).size()
    freq_cibi = dataset_cibi.groupby(["Comune"]).size()

    array_freq = array('i', [freq_musei, freq_attrazioni, freq_sport, freq_parchi, freq_cibi])
    print(array_freq)
    return array_freq


def createJoinofDataset():

    dataset_musei = get_dataset_musei("Bari")
    dataset_attrazioni = get_dataset_attrazioni("All")
    dataset_sport = get_dataset_sport("All")
    dataset_parchi = get_dataset_parchi("All")
    dataset_cibi = get_dataset_cibi("Bari")



    freq = dataset_musei.groupby(["Comune"]).size()
    freq2 = dataset_cibi.groupby(["Comune"]).size()

    print(freq, freq2)




