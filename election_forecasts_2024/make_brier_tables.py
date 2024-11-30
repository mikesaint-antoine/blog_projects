
import csv
from datetime import datetime
import sys
import matplotlib.pyplot as plt
from eval_functions import *


round_to = 4






outcomes = []
with open(f"forecasts/outcomes.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        outcomes.append(float(row[1]))

# outcomes where nate silver gave a forecast
outcomes_SUBSET = outcomes[:22]
del outcomes_SUBSET[1]
del outcomes_SUBSET[1]


######################################################################
# Manifold

probs = []
with open(f"forecasts/manifold_2024-10-22.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

manifold_2_weeks = round(brier_score(probs,outcomes),round_to)

probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

manifold_2_weeks_SUBSET = round(brier_score(probs_SUBSET,outcomes_SUBSET),round_to)



probs = []
with open(f"forecasts/manifold_2024-10-29.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

manifold_1_week = round(brier_score(probs,outcomes),round_to)

probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

manifold_1_week_SUBSET = round(brier_score(probs_SUBSET,outcomes_SUBSET),round_to)







probs = []
with open(f"forecasts/manifold_2024-11-04.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

manifold_day_before = round(brier_score(probs,outcomes),round_to)

probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

manifold_day_before_SUBSET = round(brier_score(probs_SUBSET,outcomes_SUBSET),round_to)








manifold_briers = [manifold_2_weeks, manifold_1_week, manifold_day_before]

manifold_briers_SUBSET = [manifold_2_weeks_SUBSET, manifold_1_week_SUBSET, manifold_day_before_SUBSET]


######################################################################
# Polymarket

probs = []
with open(f"forecasts/polymarket_2024-10-22.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

polymarket_2_weeks = round(brier_score(probs,outcomes),round_to)

probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

polymarket_2_weeks_SUBSET = round(brier_score(probs_SUBSET,outcomes_SUBSET),round_to)









probs = []
with open(f"forecasts/polymarket_2024-10-29.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

polymarket_1_week = round(brier_score(probs,outcomes),round_to)


probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

polymarket_1_week_SUBSET = round(brier_score(probs_SUBSET,outcomes_SUBSET),round_to)







probs = []
with open(f"forecasts/polymarket_2024-11-04.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

polymarket_day_before = round(brier_score(probs,outcomes),round_to)

probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

polymarket_day_before_SUBSET = round(brier_score(probs_SUBSET,outcomes_SUBSET),round_to)






polymarket_briers = [polymarket_2_weeks, polymarket_1_week, polymarket_day_before]

polymarket_briers_SUBSET = [polymarket_2_weeks_SUBSET, polymarket_1_week_SUBSET, polymarket_day_before_SUBSET]



######################################################################
# Crowdsourced

probs = []
with open(f"forecasts/crowdsourced_weighted_average.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

crowdsourced_day_before = round(brier_score(probs,outcomes),round_to)

probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

crowdsourced_day_before_SUBSET = round(brier_score(probs_SUBSET,outcomes_SUBSET),round_to)



######################################################################
# Mike Forecast

probs = []
with open(f"forecasts/mike_forecast.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

mike_forecast_day_before = round(brier_score(probs,outcomes),round_to)

probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

mike_forecast_day_before_SUBSET = round(brier_score(probs_SUBSET,outcomes_SUBSET),round_to)





######################################################################
# Nate Silver

probs = []
with open(f"forecasts/nate_silver_2024-10-21.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

nate_silver_2_weeks = round(brier_score(probs_SUBSET,outcomes_SUBSET),round_to)




probs = []
with open(f"forecasts/nate_silver_2024-10-28.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

nate_silver_1_week = round(brier_score(probs_SUBSET,outcomes_SUBSET),round_to)



probs = []
with open(f"forecasts/nate_silver_2024-11-03.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

nate_silver_day_before = round(brier_score(probs_SUBSET,outcomes_SUBSET),round_to)



nate_silver_briers = [nate_silver_2_weeks, nate_silver_1_week, nate_silver_day_before]



######################################################################
# writing output


filename = "results/brier_table.csv"
with open(filename, "w") as record_file:
    record_file.write(",2 Weeks Before, 1 Week Before, Day Before\n")
    record_file.write(f"Manifold Markets,{manifold_briers[0]},{manifold_briers[1]},{manifold_briers[2]}\n")
    record_file.write(f"Polymarket,{polymarket_briers[0]},{polymarket_briers[1]},{polymarket_briers[2]}\n")
    record_file.write(f"Crowdsourced Forecast,,,{crowdsourced_day_before}\n")
    record_file.write(f"Mike Forecast,,,{mike_forecast_day_before}\n")




filename = "results/brier_table_SUBSET.csv"
with open(filename, "w") as record_file:
    record_file.write(",2 Weeks Before, 1 Week Before, Day Before\n")
    record_file.write(f"Nate Silver,{nate_silver_briers[0]},{nate_silver_briers[1]},{nate_silver_briers[2]}\n")
    record_file.write(f"Manifold Markets,{manifold_briers_SUBSET[0]},{manifold_briers_SUBSET[1]},{manifold_briers_SUBSET[2]}\n")
    record_file.write(f"Polymarket,{polymarket_briers_SUBSET[0]},{polymarket_briers_SUBSET[1]},{polymarket_briers_SUBSET[2]}\n")
    record_file.write(f"Crowdsourced Forecast,,,{crowdsourced_day_before_SUBSET}\n")
    record_file.write(f"Mike Forecast,,,{mike_forecast_day_before_SUBSET}\n")

