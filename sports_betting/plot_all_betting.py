import sys
import numpy as np 
import csv
import matplotlib.pyplot as plt
from eval_functions import *



sports = ["nhl","mlb","nfl","nba","ncaa_football"]
years = ["2016","2017","2018","2019","2020"]

means = []
stds = []

for sport in sports:

    scores = []
    for year in years:

        # reading betting odds

        data = []
        ## read CSV / TSV
        with open(f"data/{sport}_{year}.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            next(reader)
            for row in reader:
                if sport=="mlb":
                    if row[15] != "NL" and row[14] != "NL" and row[0]!="":
                        data.append([row[0],row[2], row[3], float(row[14]), float(row[15]),float(row[16])])
                
                elif sport=="nhl":
                    data.append([row[0], row[2], row[3], float(row[7]),float(row[8]) ])
                
                else:
        
                    if row[0]!="" and row[11] != "NL":
                        data.append([row[0], row[2], row[3], float(row[8]),float(row[11]) ])
                        # Date, VH, Team, Final score, ML odds, 
                        # input()



        y_true = []
        # did home team win?

        y_score = []

        for i in range(0,len(data), 2):

            # avoiding neutral games, only looking at ones where one team is home and other is away
            

            assert(data[i][0] == data[i+1][0])
            assert(data[i][1] != data[i+1][1] or data[i][1]=="N")
            assert(data[i+1][1]=="H" or data[i+1][1]=="N" or sport=="nhl")

            v_score = data[i][3]
            h_score = data[i+1][3]

            oddsV = data[i][4]
            oddsH = data[i+1][4]

            probV = odds_to_prob(oddsV) / (odds_to_prob(oddsV)+odds_to_prob(oddsH))
            probH = odds_to_prob(oddsH) / (odds_to_prob(oddsV)+odds_to_prob(oddsH))


            # print(probV+probH)


            if h_score>v_score:
                y_true.append(1)
                y_score.append(probH)

            elif h_score<v_score:
                y_true.append(0)
                y_score.append(probH)

            ## if neither of these is true, it was a tie so we skip    


        assert len(y_true) == len(y_score)



        betting_brier = brier_score(y_true,y_score)

        # print(f"Year: {year}")
        # print(f"Betting Brier: {betting_brier}")
        scores.append(betting_brier)




    means.append(np.mean(scores))
    stds.append(np.std(scores))





x_pos = np.arange(len(sports))


fig, ax = plt.subplots()
ax.bar(x_pos, means, yerr=stds, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Brier Scores',size=16)
ax.set_xticks(x_pos)
ax.set_xticklabels(sports)
ax.set_title('Betting Market Brier Scores, 2016-2020',size=16)
ax.yaxis.grid(True)

# plt.show()

plt.savefig("figs/all_betting_bar_graph.png",dpi=1000)


sys.exit("")

