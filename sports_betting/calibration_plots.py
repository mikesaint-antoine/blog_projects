import numpy as np 
import csv
import matplotlib.pyplot as plt
# from eval_functions import *
import sys





def calibration(y_true,y_score,bin_bounds=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]):
    assert len(y_true) == len(y_score)

    error = 0

    bin_means = []
    outcome_means = []
    outcome_stds = []
    pred_means = []
    bin_counts = []


    for i in range(len(bin_bounds)-1):

        total = 0
        happened = 0

        outcomes = []
        preds = []

        for j in range(len(y_score)):

            score = y_score[j]

            if score >= bin_bounds[i] and score < bin_bounds[i+1]:


                total += 1

                happened += y_true[j]
                outcomes.append(y_true[j])
                preds.append(score)


        if total > 0:
            bin_means.append(np.mean([bin_bounds[i],bin_bounds[i+1]]))
            outcome_means.append(np.mean(outcomes))
            outcome_stds.append(np.std(outcomes))
            pred_means.append(np.mean(preds))
            bin_counts.append(total)



    return([bin_means, outcome_means, pred_means, bin_counts])













# sport = "nhl"
# sport = "mlb"
# sport = "nfl"
# sport = "nba"
sport = "ncaa_football"


# sports = ["nhl","mlb","nfl","nba","ncaa_football"]


y_true = []
y_pred = []

with open(f"processed_data/{sport}.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        # print(row)

        y_true.append(float(row[0]))
        y_pred.append(float(row[1]))




[bin_means, outcome_means, pred_means, bin_counts] = calibration(y_true,y_pred)


for i in range(len(bin_means)):
    print(f"bin mean: {round(bin_means[i],3)}")
    print(f"outcome mean: {round(outcome_means[i],3)}")
    print(f"pred mean: {round(pred_means[i],3)}")
    print(f"bincounts: {round(bin_counts[i],3)}")
    print()





fig, axs = plt.subplots(1, 1, sharex=True, sharey=True)

scaling_factor = 0.1

sizes = [count * scaling_factor for count in bin_counts]


axs.scatter(bin_means,outcome_means,s=sizes)
axs.set(autoscale_on=False, aspect='equal')
perfect, = axs.plot([0,1],[0,1],color="black",label="perfect")
axs.legend(handles=[perfect],fontsize=12,loc=4)
axs.set_title(f"{sport.upper()}",fontsize=16)
axs.set_xlabel("Prediction Probability",fontsize=12)
axs.set_ylabel("Outcome Fraction",fontsize=12)


plt.savefig(f"calibration_plots/{sport}.png",dpi=1000)


