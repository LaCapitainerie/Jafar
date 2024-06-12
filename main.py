"""
Importation de la fonction predire du module jafar
"""
from jafar import predire

# Fichier CSV
csvFile:str = "loto_201911.csv"

# Liste des nombres à trouver
prediction:list[int] = [3]
values:list[str] = ["numero_chance"]

# Lecture et calcul des resultats
predire(csv=csvFile, col=values, prediction=prediction)

# Liste des boules normales
prediction:list[int] = [8, 28, 40, 41, 42]
values:list[str] = ["boule_1", "boule_2", "boule_3", "boule_4", "boule_5"]


# Lecture et calcul des resultats
predire(csv=csvFile, col=values, prediction=prediction)
