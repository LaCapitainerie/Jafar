from jafar import predire;

# Liste des nombres à trouver
prediction:list[int] = [3]
chances:list[str]   = ["numero_chance"]
normal:list[str]   = ["boule_1", "boule_2", "boule_3", "boule_4", "boule_5"]
csvFile:str          = "loto_201911.csv"

# Lecture et calcul des resultats
predire(csv=csvFile, col=normal, prediction=prediction)