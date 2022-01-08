
# %%
import numpy as np
from numpy.random.mtrand import randint, random_integers
import pandas as pd

dice1 = [1, 2, 3, 4, 5, 6]
mario = [1, 3, 3, 3, 5, 6]
luigi = [1, 1, 1, 5, 6, 7]
peach = [0, 2, 4, 4, 4, 6]
daisy = [3, 3, 3, 3, 4, 4]
wario = [0, 0, 6, 6, 6, 6]
waluigi = [0, 1, 3, 5, 5, 7]
yoshi = [0, 1, 3, 5, 5, 7]
rosalina = [0, 0, 2, 3, 4, 8]
donkey_kong = [0, 0, 0, 0, 10, 10]
diddy_kong = [0, 0, 0, 7, 7, 7]
goomba = [0, 0, 3, 4, 5, 6]
shy_guy = [0, 4, 4, 4, 4, 4]
koopa_troopa = [1, 1, 2, 3, 3, 10]
monty_mole = [0, 2, 3, 4, 5, 6]
bowser = [0, 0, 1, 8, 9, 10]
bowser_junior = [1, 1, 1, 4, 4, 9]
boo = [0, 0, 5, 5, 7, 7]
hammer_bro = [0, 1, 1, 1, 5, 5]
dry_bones = [1, 1, 1, 6, 6, 6]
pom_pom = [0, 3, 3, 3, 3, 8]

dice_list = [dice1, mario, luigi, peach, daisy, wario, waluigi, yoshi, rosalina, donkey_kong, diddy_kong, goomba, shy_guy,
            koopa_troopa, monty_mole, bowser, bowser_junior, boo, hammer_bro, dry_bones, pom_pom]

dice_list_names= ["dice1", "mario", "luigi", "peach", "daisy", "wario", "waluigi", "yoshi", "rosalina", "donkey_kong", "diddy_kong", "goomba",
                "shy_guy", "koopa_troopa", "monty_mole", "bowser", "bowser_junior", "boo", "hammer_bro", "dry_bones", "pom_pom"]

comb_list = list(zip(dice_list_names, dice_list))

def comp_func(turns, reps):
    global sorted_total_wins, total_wins

    total_wins = {}
    for dice in dice_list_names:
        total_wins[dice] = [0, 0]
    for rep in range(reps):
        total_steps = {}
        for dice in comb_list:
            for num in range(turns):
                if dice[0] in total_steps:
                    total_steps[dice[0]] += dice[1][randint(6)]
                else:
                    total_steps[dice[0]] = dice[1][randint(6)]
        sorted_list = sorted(total_steps.items(), key=lambda char:char[1], reverse=True)
        total_wins[sorted_list[0][0]][0] += 1
    sorted_total_wins = sorted(total_wins.items(), key=lambda char:char[1], reverse=True)

    for die in comb_list:
        total_wins[die[0]][1] = np.array(die[1]).sum()
    sorted_total_sum = sorted(total_wins.items(), key=lambda char:char[1], reverse=True)

    return sorted_total_wins, total_wins

comp_func(10, 2100)

df = pd.DataFrame.from_dict(total_wins, orient='index', columns=['Number of wins', 'Sum of die']).sort_values(by='Number of wins', ascending=False)
print(df)
