import numpy as np 
import csv
from eval_functions import *



betting_pred = []
fte_pred = []
outcomes = []
control = []

## read CSV / TSV
with open("data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)

    for row in reader:

        # games that haven't happened yet are excluded
        if row[5] in ["0","1"]:

            # normalize betting odds (have to do this because raw odds include profit for bookie)
            prob_yes = odds_to_prob(float(row[1]))
            prob_no = odds_to_prob(float(row[2]))
            betting_pred.append(prob_yes/(prob_yes+prob_no))

            fte_pred.append(float(row[3])/100)

            outcomes.append(int(row[5]))
            control.append(0.5)


print()
print()

print("Betting Odds Brier Score:")
print(brier_score(outcomes,betting_pred))

print()
print("FiveThirtyEight Brier Score:")
print(brier_score(outcomes,fte_pred))
print()
print("No Skill Controll Brier Score:")
print(brier_score(outcomes,control))
