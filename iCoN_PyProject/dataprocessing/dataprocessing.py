from iCoN_PyProject.citymodelling.dataset import *

def processingMusei(city):

    replacement = {  # set di caratteri da sostituire nel dataframe
        "'": "",
        " ": "_",
        "-": "_",
        "à": "a",
        "é": "e",
        "ù": "u",
        "ò": "o",
        "?": ""
    }

    df = get_dataset_musei(city)

    city_museum = df['Nome'].replace(replacement, regex=True)

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

