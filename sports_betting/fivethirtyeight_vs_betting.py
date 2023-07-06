import sys
import numpy as np 
import csv
import matplotlib.pyplot as plt
from eval_functions import *



sports = ["fivethirtyeight_mlb","fivethirtyeight_nfl","fivethirtyeight_nba","mlb","nfl","nba"]
years = ["2016","2017","2018","2019","2020"]

means = []
stds = []

for sport in sports:


    scores = []
    for year in years:

        if sport in ["mlb","nfl","nba"]:
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

                    elif sport=="nba":
                        if row[0]!="" :
                            data.append([row[0], row[2], row[3], float(row[8]),float(row[11]) ])
      
                    else:
                        if row[0]!="" and row[11] != "NL":
                            data.append([row[0], row[2], row[3], float(row[8]),float(row[11]) ])
                            # Date, VH, Team, Final score, ML odds, 




            y_true = []
            # did home team win? (or the second listed team if neither was the home team)

            y_score = []

            for i in range(0,len(data), 2):

                assert(data[i][0] == data[i+1][0])
                assert(data[i][1] != data[i+1][1] or data[i][1]=="N")
                assert(data[i+1][1]=="H" or data[i+1][1]=="N")

                v_score = data[i][3]
                h_score = data[i+1][3]

                oddsV = data[i][4]
                oddsH = data[i+1][4]

                probV = odds_to_prob(oddsV) / (odds_to_prob(oddsV)+odds_to_prob(oddsH))
                probH = odds_to_prob(oddsH) / (odds_to_prob(oddsV)+odds_to_prob(oddsH))



                if h_score>v_score:
                    y_true.append(1)
                    y_score.append(probH)

                elif h_score<v_score:
                    y_true.append(0)
                    y_score.append(probH)

                ## if neither of these is true, it was a tie so we skip     


            assert len(y_true) == len(y_score)



            betting_brier = brier_score(y_true,y_score)

            scores.append(betting_brier)

            rounded = np.round(betting_brier,decimals=4)

            print()
            print()
            print(f"sport: {sport}")
            print(f"year: {year}")
            print(f"brier score: {rounded}")
        
        else:
            fte_data = []
            ## read CSV / TSV

            fte_y_true = []
            fte_y_score = []


            with open(f"data/{sport}.csv") as csvfile:
                reader = csv.reader(csvfile, delimiter=',')

                next(reader)
                for row in reader:
                    if row[0]==year:


                        if sport=="fivethirtyeight_mlb":
                            if float(row[6]) in [0,1]:
                                # prediction and outcome of Team1 winning
                                fte_y_true.append(int(row[6]))
                                fte_y_score.append(float(row[5]))
                                fte_data.append(row)  

                        else:
                             if float(row[5]) in [0,1]:
                                # prediction and outcome of Team1 winning
                                fte_y_true.append(int(row[5]))
                                fte_y_score.append(float(row[4]))
                                fte_data.append(row)                             


            fte_brier = brier_score(fte_y_true,fte_y_score)
            scores.append(fte_brier)


            rounded = np.round(fte_brier,decimals=4)

            print()
            print()
            print(f"sport: {sport}")
            print(f"year: {year}")
            print(f"brier score: {rounded}")
    

    means.append(np.mean(scores))
    stds.append(np.std(scores))


fte_means = means[0:3]
fte_stds = stds[0:3]


betting_means = means[3:]
betting_stds = stds[3:]

N = 3
fteMeans = (means[0], means[1], means[2])
fteStd =   (stds[0], stds[1], stds[2])

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, fteMeans, width, color='royalblue',alpha=0.5, yerr=fteStd,capsize=10)

bettingMeans = (means[3], means[4], means[5])
bettingStd =   (stds[3], stds[4], stds[5])
rects2 = ax.bar(ind+width, bettingMeans, width, color='seagreen', alpha=0.5,yerr=bettingStd,capsize=10)

# add some
ax.set_ylabel('Brier Scores',size=16)
ax.set_title('Brier Scores, 2016-2020 Seasons',size=16)
ax.set_xticks(ind + width / 2)
ax.set_xticklabels( (sports[3], sports[4], sports[5]) )

ax.legend( (rects1[0], rects2[0]), ('FiveThirtyEight', 'Betting Odds'),fontsize=9 )

# plt.show()


plt.savefig("figs/fivethirtyeight_vs_betting.png",dpi=1000)


