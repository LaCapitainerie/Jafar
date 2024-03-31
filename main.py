from jafar import predire;

# Liste des nombres à trouver
prediction:list[int] = [3]
colonnes:list[str]   = ["numero_chance"]
csvFile:str          = "loto_201911.csv"

# Lecture et calcul des resultats
predire(csv=csvFile, col=colonnes, prediction=prediction)