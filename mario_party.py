
# %%
import numpy as np
from numpy.random.mtrand import randint
import pandas as pd

# List all dice values for all the characters

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

# Make a list of lists with the dice values
dice_list = [dice1, mario, luigi, peach, daisy, wario, waluigi, yoshi, rosalina, donkey_kong, diddy_kong, goomba, shy_guy,
            koopa_troopa, monty_mole, bowser, bowser_junior, boo, hammer_bro, dry_bones, pom_pom]

# Make a list of the names of the characters in the same order as the previous list
dice_list_names= ["dice1", "mario", "luigi", "peach", "daisy", "wario", "waluigi", "yoshi", "rosalina", "donkey_kong", "diddy_kong", "goomba",
                "shy_guy", "koopa_troopa", "monty_mole", "bowser", "bowser_junior", "boo", "hammer_bro", "dry_bones", "pom_pom"]

# Zip both lists above and make it a list
comb_list = list(zip(dice_list_names, dice_list))

# Define the function to simulate x (boards) number of games of y (turns) number of turns
def comp_func(turns, boards):
    # Make variables global so they can be used outside the function
    global sorted_total_wins, total_wins

    # Initialize the total_wins dictionary which will contain the number of wins, the sum of the values of the die, and the list of die values
    total_wins = {}
    # Set all total_wins values to 0, 0, and an empty list for the list of die values
    for dice in dice_list_names:
        total_wins[dice] = [0, 0, []]
    # Simulate the games
    for rep in range(boards):
        total_steps = {}
        for dice in comb_list:
            for num in range(turns):
                if dice[0] in total_steps:
                    total_steps[dice[0]] += dice[1][randint(6)]
                else:
                    total_steps[dice[0]] = dice[1][randint(6)]
        # Sort list so that the first in the list (most steps) will add one to the total_wins counter
        sorted_list = sorted(total_steps.items(), key=lambda char:char[1], reverse=True)
        total_wins[sorted_list[0][0]][0] += 1
    # This sorting of total_wins has now become unnecessary
    sorted_total_wins = sorted(total_wins.items(), key=lambda char:char[1], reverse=True)

    # Add the sum of die values to the total_wins counter
    for die in comb_list:
        total_wins[die[0]][1] = np.array(die[1]).sum()

    # Add the list of dice values to total_wins
    for die in comb_list:
        total_wins[die[0]][2] = die[1]

    return sorted_total_wins, total_wins

comp_func(10, 2100)

df = pd.DataFrame.from_dict(total_wins, orient='index', columns=['Number of wins', 'Sum of die', 'Die']).sort_values(by='Number of wins', ascending=False)
print(df)
