import matplotlib.pyplot as plt
import random
from typing import Literal

wining_choice_type = Literal['green', 'red', 'black', 'low', 'high', 'even', 'odd', '1st 12', '2nd 12', '3rd 12', '1 to 18', '19 to 36', '1st column', '2nd column', '3rd column', 'street', '2 to 1 1', '2 to 1 2', '2 to 1 3', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

def roulette():

    wining_choice = []

    number = random.randint(0, 36)

    # Green Red Black
    if number == 0:
        return ['green']
    elif number % 2 == 0:
        wining_choice.append('red')
    else:
        wining_choice.append('black')

    # Low High
    if number < 19:
        wining_choice.append('low')
    else:
        wining_choice.append('high')

    # Even Odd
    if number % 2 == 0:
        wining_choice.append('even')
    else:
        wining_choice.append('odd')

    # Dozen
    if number in range(1, 13):
        wining_choice.append('1st 12')
    elif number in range(13, 25):
        wining_choice.append('2nd 12')
    else:
        wining_choice.append('3rd 12')

    # Column
    if number in range(1, 19):
        wining_choice.append('1 to 18')
    else:
        wining_choice.append('19 to 36')

    # Street
    wining_choice.append(number)


    # 2 to 1
    wining_choice.append('2 to 1 ' + str(number % 3 + 1))
    
    return wining_choice

def show_stat(data:list[int], nb_tirages:int, début:int) -> None:
    median = sorted(data)[len(data)//2]

    plt.scatter(range(len(data)), data, color='blue', label='Gain Finaux')

    plt.axhline(y=median, color='red', linestyle='--', label=f'Gain Median: {median:.2f}')
    
    plt.axhline(y=début, color='red', linestyle='--', label=f'Départ: {début:.2f}')

    plt.title('Gain Finaux Estimées en {} Tours'.format(nb_tirages))
    plt.xlabel('Parties')
    plt.ylabel('Gain Finaux')

    plt.legend()

    plt.show()

def main(tirages = 50):

    stats = {
        'green': 0,
        'red': 0,
        'black': 0,
        'low': 0,
        'high': 0,
        'even': 0,
        'odd': 0,
        '1st 12': 0,
        '2nd 12': 0,
        '3rd 12': 0,
        '1 to 18': 0,
        '19 to 36': 0,
        '1st column': 0,
        '2nd column': 0,
        '3rd column': 0,
        'street': 0,
        '2 to 1 1': 0,
        '2 to 1 2': 0,
        '2 to 1 3': 0,
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
        21: 0,
        22: 0,
        23: 0,
        24: 0,
        25: 0,
        26: 0,
        27: 0,
        28: 0,
        29: 0,
        30: 0,
        31: 0,
        32: 0,
        33: 0,
        34: 0,
        35: 0,
        36: 0
    }

    money = 100
    bet_percent = 1/6
    bet_win_percent = 3

    bet:list[wining_choice_type] = '1st 12', '2nd 12'

    fois = 15

    values = []
    for _ in range(tirages):
        money = 100
        for _ in range(fois):

            if money <= 5:
                print("Vous n'avez plus d'argent, arrêt du jeu au tour", _)
                break

            choices = roulette()
            for choice in choices:
                stats[choice] += 1

            if any(_ in choices for _ in bet):
                money -= round(bet_percent * money)
                money += round(bet_percent * money * bet_win_percent)
            else:
                money -= round(bet_percent * money)

            # Random
            # bet = [random.choice(["1st 12", '2nd 12', "3rd 12"]) for _ in range(2)]

            # Non Sortis
            # bet = list({'1st 12', '2nd 12', '3rd 12'} ^ ({'1st 12', '2nd 12', '3rd 12'} & set(choices)))

        values.append(money)

    show_stat(values, fois, 100)

if __name__ == '__main__':
    main(1000)