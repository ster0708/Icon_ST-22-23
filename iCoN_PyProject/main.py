import pandas as pd
import os
import csv
from iCoN_PyProject.dataset import *
from iCoN_PyProject.prolog.prolog import *




if __name__ == '__main__':

    print("Start... \n")
    print("Vediamo cosa cerchi dal tuo prossimo viaggio! \n")

    print("Vuoi visitare musei e luoghi rilevanza artistica/culturale?")

    arte_cultura:str = input()

    print("Ti interessano eventi sportivi e sei un appassionato di sport/calcio?")

    sport: str = input()

    print("Vuoi viaggiare con la famiglia e cerchi divertimento per grandi e piccoli?")

    parchi: str = input()

    print("Hai interesse nel degustare cibo tipico della cucina locale?")

    cibo: str = input()

    print("\n")

    print("Calcoliamo la tua prossima meta...")

    print(import_dataset_cibo("Bari"))

