import numpy as np 
import csv
from eval_functions import *


games = []
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
            games.append(row[0])

            # normalize betting odds (have to do this because raw odds include profit for bookie)
            prob_yes = odds_to_prob(float(row[1]))
            prob_no = odds_to_prob(float(row[2]))
            betting_pred.append(prob_yes/(prob_yes+prob_no))

            fte_pred.append(float(row[3])/100)

            outcomes.append(int(row[5]))
            control.append(0.5)


## write CSV / TSV
with open("processed_data.csv", "w") as record_file:
    record_file.write("event,betting_prob,fivethirtyeight_prob,noskill_control_prob,outcome\n")

    for i in range(len(games)):
        record_file.write(f"{games[i]},{betting_pred[i]},{fte_pred[i]},{control[i]},{outcomes[i]}\n")
