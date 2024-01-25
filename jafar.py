#numero_chance = {1: 62, 2: 67, 3: 57, 4: 67, 5: 61, 6: 61, 7: 65, 8: 59, 9: 81, 10: 78}
#boule = {1: 52, 2: 42, 3: 54, 4: 54, 5: 60, 6: 59, 7: 62, 8: 49, 9: 52, 10: 44, 11: 51, 12: 68, 13: 60, 14: 45, 15: 63, 16: 48, 17: 52, 18: 47, 19: 50, 20: 51, 21: 48, 22: 65, 23: 52, 24: 56, 25: 47, 26: 61, 27: 50, 28: 61, 29: 48, 30: 55, 31: 65, 32: 55, 33: 51, 34: 49, 35: 63, 36: 50, 37: 50, 38: 59, 39: 45, 40: 48, 41: 55, 42: 53, 43: 46, 44: 68, 45: 47, 46: 54, 47: 49, 48: 65, 49: 54}


def lecture_csv(col:str=""):
    import pandas as pd;
    df = pd.read_csv("loto.csv", sep=';')

    numero_chance = {i: 0 for i in range(1, 10+1)}
    for each in df["numero_chance"]:
        numero_chance[each] += 1

    boule = {i: 0 for i in range(1, 49+1)}
    for i in range(1, 5):
        for each in df[f"boule_{i}"]:
            boule[each] += 1
    d = (numero_chance if col == "chance" else boule)
    return (d, sum(d.values()))


def show(d:dict[int,int], t:int) -> dict[int,float]:
    return {key: val/t for key, val in d.items()}

def moy_a_16(d:dict[int, int]) -> int:
    normal = 1/49
    return sum([abs(_ - normal) for _ in d.values()])

def ecart_type_min(d:dict[int, int], t:int) -> list[tuple[int, float]]:
    percent = {i: 0 for i in range(1, 49+1)}
    t += 1
    for i in range(1, 49+1):
        d[i] += 1
        percent[i] = moy_a_16(show(d, t))
    return percent

def result(d:dict[int, int], t:int):
    s = sorted(ecart_type_min(d, t).items(), key=lambda x: x[1])
    [print(each) for each in s]
    return s

data, times = lecture_csv()
result(data, times)