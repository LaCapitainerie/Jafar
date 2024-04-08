from collections import Counter;
from itertools import permutations;
import pandas as pd;

# Fonction principale
def predire(csv:str, col:list[str], *, prediction:list[int]) -> int:
    return result(*lecture_csv(csv=csv, col=col), prediction=prediction)

# Fonctions secondaires
def lecture_csv(csv:str, col:list[str]) -> tuple[Counter, int, int, int]:
    if not csv.endswith(".csv"):
        raise ValueError("Le fichier doit être un fichier CSV")
    if csv == "":
        raise ValueError("Le fichier ne doit pas être vide")

    df = pd.read_csv(csv, sep=';')

    # Comptage des boules
    boule = Counter()
    for each in col:
        # Counter of each column sorted
        boule += Counter(df[each].sort_values())

    return boule, boule.total(), len(boule.keys()), len(col)

# Fonctions de calcul
def moy_a_16(d:Counter, t:int, size:int) -> int:
    # Formule avec Carré plutôt que Absolue
    return sum([(r:=val*size - t)*r for val in d.values()])

# Fonction de calcul de l'écart type
def ecart_type(d:Counter, t:int, size:int, col_len:int) -> dict[tuple[int, ...], int]:
    # Dictionnaire des combinaisons et leur pourcentage
    percent:dict[int, int] = {}

    # Liste des combinaisons déjà vues
    values_already_seen:set = set()

    # Calcul des combinaisons
    for each in permutations(d, r=col_len):
        print(each, end="\r", )
        if (eachTuple := tuple(sorted(each))) not in values_already_seen:
            values_already_seen.add(each)
            percent[eachTuple] = moy_a_16(d + Counter(eachTuple), t+1, size)

    return percent

# Fonction de résultat
def result(d:Counter[int, int], t:int, size:int, tirage:int, *, prediction:list[int]) -> int:

    # Retourne la liste triée des écarts types
    s = sorted(ecart_type(d, t, size, tirage).items(), key=lambda x: x[1])
    prediction:tuple[int] = tuple(sorted(prediction))

    # Ecriture dans un fichier
    with open("result.txt", "w") as f:
        for each, _ in s:
            f.write(f"{each} : {'X' if each == prediction else ''}\n")

    # Print avec couleur
    for each, pred in s:
        print("\33[42m" if each == prediction else "\33[0m", each, pred)

    return 0