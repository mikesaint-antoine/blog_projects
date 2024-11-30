import csv
from datetime import datetime
import sys
import numpy as np

election_date = datetime.strptime("11/5/2024", "%m/%d/%Y").date()


days_before = []
names = []
data = []

# NOTE -- this file isn't actually included in the git repo because many of the entries were anonymous
with open("contest/contest_entries.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:


        # how many days before election (for time-weighted brier)
        entry_date = datetime.strptime(row[0], "%m/%d/%Y %H:%M:%S").date() # this .date() is to ignore hours
        days_before.append((election_date - entry_date).days)

        # name
        names.append(row[1])


        # get probs
        tmp = []
        for item in row[4:]:
            prob = float(item)

            if prob > 1:
                prob = prob/100 # needed because a bunch of people didn't read the instructions :(
            tmp.append(prob)
        data.append(tmp)

data = np.array(data)



questions = []
outcomes = []
with open(f"forecasts/outcomes.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        questions.append(row[0])
        outcomes.append(float(row[1]))



raw_briers = []
weighted_briers = []

for i in range(data.shape[0]):

    # calculate raw brier
    brier_score = 0
    for j in range(data.shape[1]):

        brier_score += (data[i,j] - outcomes[j])**2
    
    brier_score = brier_score / data.shape[1]

    raw_briers.append(brier_score)

    weighted_score = brier_score * np.exp(-0.002 * days_before[i])

    weighted_briers.append(weighted_score)




weighted_briers = np.array(weighted_briers)

inds_of_winners = list(np.argsort(weighted_briers)[:3])


print()
print()
print(f"First place\t{names[inds_of_winners[0]]}\t{round(raw_briers[inds_of_winners[0]],3)}\t{days_before[inds_of_winners[0]]}\t{round(weighted_briers[inds_of_winners[0]],3)}")
print(f"Second place\t{names[inds_of_winners[1]]}\t{round(raw_briers[inds_of_winners[1]],3)}\t{days_before[inds_of_winners[1]]}\t{round(weighted_briers[inds_of_winners[1]],3)}")
print(f"Third place\t{names[inds_of_winners[2]]}\t{round(raw_briers[inds_of_winners[2]],3)}\t{days_before[inds_of_winners[2]]}\t{round(weighted_briers[inds_of_winners[2]],3)}")

# print(min(weighted_briers))




early_names = names[:28]
early_raw_briers = raw_briers[:28]
early_weighted_briers = weighted_briers[:28]
early_days_before = days_before[:28]



early_winner_ind = np.argsort(early_weighted_briers)[0]


print(f"Early winner\t{early_names[early_winner_ind]}\t{round(early_raw_briers[early_winner_ind],3)}\t{early_days_before[early_winner_ind]}\t{round(early_weighted_briers[early_winner_ind],3)}")

# print(min(early_weighted_briers))



################################################################################################################

## this is the code that was used to generate the time-weighted crowdsourced forecast average

# ## weighted forecast average

# # weights - most recent forecasts considered more important
# # similar formula to time-weighted brier score, but different parameter and different reason for doing
# weights = np.exp(-0.025 * np.array(days_before))
# normalized_weights = weights / np.sum(weights)

# time_weighted_avg_forecast = np.average(data, axis=0, weights=normalized_weights)

# time_weighted_avg_forecast = np.round(time_weighted_avg_forecast, decimals=3)

# print(time_weighted_avg_forecast.shape)

# filename = f"forecasts/crowdsourced_weighted_average.csv"

# with open(filename, "w") as record_file:
#     record_file.write("question,prob\n")

#     for i in range(len(questions)):
#         record_file.write(f"{questions[i]},{time_weighted_avg_forecast[i]}\n")