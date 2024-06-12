"""
Importation des modules nécessaires
"""
from collections import Counter
from itertools import combinations
import pandas as pd

def predire(csv:str, col:list[str], *, prediction:list[int]) -> int:
    """
    Fonction principale de prédiction
    :param csv: Fichier CSV
    :param col: Liste des colonnes à lire
    :param prediction: Liste des nombres à trouver
    :return: 0
    """
    return result(*lecture_csv(csv=csv, col=col), prediction=prediction)

# Fonctions secondaires
def lecture_csv(csv:str, col:list[str]) -> tuple[Counter, int, int, int]:
    """
    Fonction de lecture du fichier CSV
    :param csv: Fichier CSV
    :param col: Liste des colonnes à lire
    :return: Counter, int, int, int
    """
    if not csv.endswith(".csv"):
        raise ValueError("Le fichier doit être un fichier CSV")
    if csv == "":
        raise ValueError("Le fichier ne doit pas être vide")

    df = pd.read_csv(csv, sep=';')

    # Comptage des boules
    boule = Counter()
    for each in col:
        # Counter of each column sorted
        boule += Counter(df[each])

    return boule, boule.total(), len(boule.keys()), len(col)

# Fonctions de calcul
def moy_a_16(d:Counter, t:int, size:int) -> int:
    """
    Fonction de calcul de la moyenne à 16
    :param d: Counter
    :param t: int
    :param size: int
    :return: int
    """
    # Formule avec Carré plutôt que Absolue
    return sum((r:=val*size - t)*r for val in d.values())

# Fonction de calcul de l'écart type
def ecart_type(d:Counter, t:int, size:int, col_len:int) -> dict[tuple[int, ...], int]:
    """
    Fonction de calcul de l'écart type
    :param d: Counter
    :param t: int
    :param size: int
    :param col_len: int
    :return: dict[tuple[int, ...], int]
    """
    # Dictionnaire des combinaisons et leur pourcentage
    percent:dict[int, int] = {}

    # Calcul des combinaisons
    for each in combinations(d, r=col_len):
        percent[each] = moy_a_16(d + Counter(each), t+1, size)

    return percent

# Fonction de résultat
def result(d:Counter[int, int], t:int, size:int, tirage:int, *, prediction:list[int]) -> int:
    """
    Fonction de résultat
    :param d: Counter
    :param t: int
    :param size: int
    :param tirage: int
    :param prediction: list[int]
    :return: int
    """

    # Retourne la liste triée des écarts types
    s = sorted(ecart_type(d, t, size, tirage).items(), key=lambda x: x[1])
    prediction:tuple[int] = tuple(sorted(prediction))

    # Ecriture dans un fichier
    with open("result.txt", "w", encoding="utf8") as f:
        for each, pred in s[:10]:
            f.write(f"{each} : {'X' if each == prediction else ''}\n")
            print("\33[42m" if each == prediction else "\33[0m", each, pred)
        

    return 0
