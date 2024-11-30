import csv
from datetime import datetime
import sys
import matplotlib.pyplot as plt
from eval_functions import *


scaling_factor_to_use = 10


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


make_calibration_plot(outcomes, probs, title="Manifold - 2 Weeks Out", plot_file="plots/manifold_2_weeks.png", scaling_factor=scaling_factor_to_use)


probs = []
with open(f"forecasts/manifold_2024-10-29.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

make_calibration_plot(outcomes, probs, title="Manifold - 1 Week Out", plot_file="plots/manifold_1_week.png", scaling_factor=scaling_factor_to_use)


probs = []
with open(f"forecasts/manifold_2024-11-04.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

make_calibration_plot(outcomes, probs, title="Manifold - Day Before", plot_file="plots/manifold_day_before.png", scaling_factor=scaling_factor_to_use)


######################################################################
# Polymarket

probs = []
with open(f"forecasts/polymarket_2024-10-22.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))


make_calibration_plot(outcomes, probs, title="Polymarket - 2 Weeks Out", plot_file="plots/polymarket_2_weeks.png", scaling_factor=scaling_factor_to_use)


probs = []
with open(f"forecasts/polymarket_2024-10-29.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

make_calibration_plot(outcomes, probs, title="Polymarket - 1 Week Out", plot_file="plots/polymarket_1_week.png", scaling_factor=scaling_factor_to_use)


probs = []
with open(f"forecasts/polymarket_2024-11-04.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

make_calibration_plot(outcomes, probs, title="Polymarket - Day Before", plot_file="plots/polymarket_day_before.png", scaling_factor=scaling_factor_to_use)



######################################################################
# Crowdsourced

probs = []
with open(f"forecasts/crowdsourced_weighted_average.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

make_calibration_plot(outcomes, probs, title="Crowdsourced - Day Before", plot_file="plots/crowdsourced_day_before.png", scaling_factor=scaling_factor_to_use)


######################################################################
# Mike Forecast

probs = []
with open(f"forecasts/mike_forecast.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

make_calibration_plot(outcomes, probs, title="Mike Forecast - Day Before", plot_file="plots/mike_forecast_day_before.png", scaling_factor=scaling_factor_to_use)




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

make_calibration_plot(outcomes_SUBSET, probs_SUBSET, title="Nate Silver SUBSET - 2 Weeks Out", plot_file="plots/nate_silver_2_weeks.png", scaling_factor=scaling_factor_to_use)


probs = []
with open(f"forecasts/nate_silver_2024-10-28.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

make_calibration_plot(outcomes_SUBSET, probs_SUBSET, title="Nate Silver SUBSET - 1 Week Out", plot_file="plots/nate_silver_1_week.png", scaling_factor=scaling_factor_to_use)


probs = []
with open(f"forecasts/nate_silver_2024-11-03.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        probs.append(float(row[1]))

probs_SUBSET = probs[:22]
del probs_SUBSET[1]
del probs_SUBSET[1]

make_calibration_plot(outcomes_SUBSET, probs_SUBSET, title="Nate Silver SUBSET - Day Before", plot_file="plots/nate_silver_day_before.png", scaling_factor=scaling_factor_to_use)
