import numpy as np 
import csv
import matplotlib.pyplot as plt
from eval_functions import *
import sys


##################################################################################################

# reading in FULL DATA

full_data = []

with open("data.csv") as tsvfile:
    reader = csv.reader(tsvfile, delimiter=',')

    next(reader)
    # skipping first row (heading names)

    for row in reader:
        full_data.append(row)



##################################################################################################
##################################################################################################
##################################################################################################



## write CSV / TSV
with open("output.txt", "w") as record_file:
    record_file.write("\n\n\n")




# selection - ALL 4 OVERLAP


manifold_probs = []
kalshi_probs = []
polymarket_probs = []
draftkings_probs = []
outcomes = []
awards = []

for row in full_data:


    if len(row[2])>0 and len(row[3])>0 and len(row[4])>0 and len(row[6])>0:
        awards.append(row[0])
        manifold_probs.append(float(row[2]))
        kalshi_probs.append(float(row[3]))
        polymarket_probs.append(float(row[4]))
        draftkings_probs.append(float(row[6]))
        outcomes.append(float(row[7]))

awards = list(set(awards))


manifold_brier = round(brier_score(outcomes,manifold_probs),3)
kalshi_brier = round(brier_score(outcomes,kalshi_probs),3)
polymarket_brier = round(brier_score(outcomes,polymarket_probs),3)
draftkings_brier = round(brier_score(outcomes,draftkings_probs),3)

with open("output.txt", "a") as record_file:
    record_file.write("#################################################################\n")
    record_file.write("All 4 Overlap\n")
    record_file.write("\n")
    record_file.write(f"Number of awards: {len(awards)}\n")
    record_file.write(f"Number of events: {len(outcomes)}\n")
    record_file.write("\n")
    record_file.write(f"Manifold Brier Score: {manifold_brier}\n")
    record_file.write(f"Kalshi Brier Score: {kalshi_brier}\n")
    record_file.write(f"Polymarket Brier Score: {polymarket_brier}\n")
    record_file.write(f"DraftKings Brier Score: {draftkings_brier}\n")
    record_file.write("\n")
    record_file.write("\n")
    record_file.write("\n")



##################################################################################################
##################################################################################################
##################################################################################################

# selection - Manifold, Kalshi, Draftkings OVERLAP


manifold_probs = []
kalshi_probs = []
draftkings_probs = []
outcomes = []
awards = []

for row in full_data:


    if len(row[2])>0 and len(row[3])>0 and len(row[6])>0:
        awards.append(row[0])
        manifold_probs.append(float(row[2]))
        kalshi_probs.append(float(row[3]))
        draftkings_probs.append(float(row[6]))
        outcomes.append(float(row[7]))

awards = list(set(awards))


manifold_brier = round(brier_score(outcomes,manifold_probs),3)
kalshi_brier = round(brier_score(outcomes,kalshi_probs),3)
draftkings_brier = round(brier_score(outcomes,draftkings_probs),3)

with open("output.txt", "a") as record_file:
    record_file.write("#################################################################\n")
    record_file.write("Manifold, Kalshi, Draftkings Overlap\n")
    record_file.write("\n")
    record_file.write(f"Number of awards: {len(awards)}\n")
    record_file.write(f"Number of events: {len(outcomes)}\n")
    record_file.write("\n")
    record_file.write(f"Manifold Brier Score: {manifold_brier}\n")
    record_file.write(f"Kalshi Brier Score: {kalshi_brier}\n")
    record_file.write(f"DraftKings Brier Score: {draftkings_brier}\n")
    record_file.write("\n")
    record_file.write("\n")
    record_file.write("\n")



##################################################################################################
##################################################################################################
##################################################################################################

# selection - Manifold, Polymarket, DraftKings OVERLAP


manifold_probs = []
polymarket_probs = []
draftkings_probs = []
outcomes = []
awards = []

for row in full_data:


    if len(row[2])>0 and len(row[4])>0 and len(row[6])>0:
        awards.append(row[0])
        manifold_probs.append(float(row[2]))
        polymarket_probs.append(float(row[4]))
        draftkings_probs.append(float(row[6]))
        outcomes.append(float(row[7]))

awards = list(set(awards))


manifold_brier = round(brier_score(outcomes,manifold_probs),3)
polymarket_brier = round(brier_score(outcomes,polymarket_probs),3)
draftkings_brier = round(brier_score(outcomes,draftkings_probs),3)

with open("output.txt", "a") as record_file:
    record_file.write("#################################################################\n")
    record_file.write("Manifold, Polymarket, DraftKings Overlap\n")
    record_file.write("\n")
    record_file.write(f"Number of awards: {len(awards)}\n")
    record_file.write(f"Number of events: {len(outcomes)}\n")
    record_file.write("\n")
    record_file.write(f"Manifold Brier Score: {manifold_brier}\n")
    record_file.write(f"Polymarket Brier Score: {polymarket_brier}\n")
    record_file.write(f"DraftKings Brier Score: {draftkings_brier}\n")
    record_file.write("\n")
    record_file.write("\n")
    record_file.write("\n")
    record_file.write("##########################################################################################################\n")
    record_file.write("##########################################################################################################\n")
    record_file.write("##########################################################################################################\n")



##################################################################################################
##################################################################################################
##################################################################################################

# Manifold Calibration


probs = []
outcomes = []
awards = []

for row in full_data:


    if len(row[2])>0:
        awards.append(row[0])
        probs.append(float(row[2]))
        outcomes.append(float(row[7]))

awards = list(set(awards))





[bin_means, outcome_means, pred_means, bin_counts] = calibration(outcomes,probs)

with open("output.txt", "a") as record_file:
    record_file.write("Manifold Calibration\n")
    record_file.write("\n")
    record_file.write(f"Number of awards: {len(awards)}\n")
    record_file.write(f"Number of events: {len(outcomes)}\n")
    record_file.write("\n")

    for i in range(len(bin_means)):
        record_file.write(f"bin mean: {round(bin_means[i],3)}\n")
        record_file.write(f"outcome mean: {round(outcome_means[i],3)}\n")
        record_file.write(f"pred mean: {round(pred_means[i],3)}\n")
        record_file.write(f"bincounts: {round(bin_counts[i],3)}\n")
        record_file.write("\n")
        record_file.write("\n")


##########################
# plot

fig, axs = plt.subplots(1, 1, sharex=True, sharey=True)

scaling_factor = 10

sizes = [count * scaling_factor for count in bin_counts]



# plot bin center as x
# axs.scatter(bin_means,outcome_means,s=sizes)

# plot prob mean as x
axs.scatter(pred_means,outcome_means,s=sizes)



axs.set(autoscale_on=False, aspect='equal')
perfect, = axs.plot([0,1],[0,1],color="black",label="perfect")
axs.legend(handles=[perfect],fontsize=12,loc=4)
axs.set_title(f"Manifold Calibration",fontsize=16)
axs.set_xlabel("Prediction Probability",fontsize=12)
axs.set_ylabel("Outcome Fraction",fontsize=12)
axs.set_xlim(-0.05,1.05)
axs.set_ylim(-0.05,1.05)

plt.savefig(f"calibration_plots/manifold.png",dpi=1000)





##################################################################################################
##################################################################################################
##################################################################################################

# Kalshi Calibration


probs = []
outcomes = []
awards = []

for row in full_data:


    if len(row[3])>0:
        awards.append(row[0])
        probs.append(float(row[3]))
        outcomes.append(float(row[7]))

awards = list(set(awards))




[bin_means, outcome_means, pred_means, bin_counts] = calibration(outcomes,probs)

with open("output.txt", "a") as record_file:
    record_file.write("#################################################################\n")
    record_file.write("Kalshi Calibration\n")
    record_file.write("\n")
    record_file.write(f"Number of awards: {len(awards)}\n")
    record_file.write(f"Number of events: {len(outcomes)}\n")
    record_file.write("\n")

    for i in range(len(bin_means)):
        record_file.write(f"bin mean: {round(bin_means[i],3)}\n")
        record_file.write(f"outcome mean: {round(outcome_means[i],3)}\n")
        record_file.write(f"pred mean: {round(pred_means[i],3)}\n")
        record_file.write(f"bincounts: {round(bin_counts[i],3)}\n")
        record_file.write("\n")
        record_file.write("\n")


##########################
# plot

fig, axs = plt.subplots(1, 1, sharex=True, sharey=True)

scaling_factor = 10

sizes = [count * scaling_factor for count in bin_counts]



# plot bin center as x
# axs.scatter(bin_means,outcome_means,s=sizes)

# plot prob mean as x
axs.scatter(pred_means,outcome_means,s=sizes)



axs.set(autoscale_on=False, aspect='equal')
perfect, = axs.plot([0,1],[0,1],color="black",label="perfect")
axs.legend(handles=[perfect],fontsize=12,loc=4)
axs.set_title(f"Kalshi Calibration",fontsize=16)
axs.set_xlabel("Prediction Probability",fontsize=12)
axs.set_ylabel("Outcome Fraction",fontsize=12)
axs.set_xlim(-0.05,1.05)
axs.set_ylim(-0.05,1.05)

plt.savefig(f"calibration_plots/kalshi.png",dpi=1000)





##################################################################################################
##################################################################################################
##################################################################################################

# Polymarket Calibration


probs = []
outcomes = []
awards = []

for row in full_data:


    if len(row[4])>0:
        awards.append(row[0])
        probs.append(float(row[4]))
        outcomes.append(float(row[7]))

awards = list(set(awards))




[bin_means, outcome_means, pred_means, bin_counts] = calibration(outcomes,probs)

with open("output.txt", "a") as record_file:
    record_file.write("#################################################################\n")
    record_file.write("Polymarket Calibration\n")
    record_file.write("\n")
    record_file.write(f"Number of awards: {len(awards)}\n")
    record_file.write(f"Number of events: {len(outcomes)}\n")
    record_file.write("\n")

    for i in range(len(bin_means)):
        record_file.write(f"bin mean: {round(bin_means[i],3)}\n")
        record_file.write(f"outcome mean: {round(outcome_means[i],3)}\n")
        record_file.write(f"pred mean: {round(pred_means[i],3)}\n")
        record_file.write(f"bincounts: {round(bin_counts[i],3)}\n")
        record_file.write("\n")
        record_file.write("\n")


##########################
# plot

fig, axs = plt.subplots(1, 1, sharex=True, sharey=True)

scaling_factor = 10

sizes = [count * scaling_factor for count in bin_counts]



# plot bin center as x
# axs.scatter(bin_means,outcome_means,s=sizes)

# plot prob mean as x
axs.scatter(pred_means,outcome_means,s=sizes)



axs.set(autoscale_on=False, aspect='equal')
perfect, = axs.plot([0,1],[0,1],color="black",label="perfect")
axs.legend(handles=[perfect],fontsize=12,loc=4)
axs.set_title(f"Polymarket Calibration",fontsize=16)
axs.set_xlabel("Prediction Probability",fontsize=12)
axs.set_ylabel("Outcome Fraction",fontsize=12)
axs.set_xlim(-0.05,1.05)
axs.set_ylim(-0.05,1.05)

plt.savefig(f"calibration_plots/polymarket.png",dpi=1000)




##################################################################################################
##################################################################################################
##################################################################################################

# DraftKings Calibration


probs = []
outcomes = []
awards = []

for row in full_data:


    if len(row[6])>0:
        awards.append(row[0])
        probs.append(float(row[6]))
        outcomes.append(float(row[7]))

awards = list(set(awards))




[bin_means, outcome_means, pred_means, bin_counts] = calibration(outcomes,probs)

with open("output.txt", "a") as record_file:
    record_file.write("#################################################################\n")
    record_file.write("DraftKings Calibration\n")
    record_file.write("\n")
    record_file.write(f"Number of awards: {len(awards)}\n")
    record_file.write(f"Number of events: {len(outcomes)}\n")
    record_file.write("\n")

    for i in range(len(bin_means)):
        record_file.write(f"bin mean: {round(bin_means[i],3)}\n")
        record_file.write(f"outcome mean: {round(outcome_means[i],3)}\n")
        record_file.write(f"pred mean: {round(pred_means[i],3)}\n")
        record_file.write(f"bincounts: {round(bin_counts[i],3)}\n")
        record_file.write("\n")
        record_file.write("\n")


##########################
# plot

fig, axs = plt.subplots(1, 1, sharex=True, sharey=True)

scaling_factor = 10

sizes = [count * scaling_factor for count in bin_counts]



# plot bin center as x
# axs.scatter(bin_means,outcome_means,s=sizes)

# plot prob mean as x
axs.scatter(pred_means,outcome_means,s=sizes)



axs.set(autoscale_on=False, aspect='equal')
perfect, = axs.plot([0,1],[0,1],color="black",label="perfect")
axs.legend(handles=[perfect],fontsize=12,loc=4)
axs.set_title(f"DraftKings Calibration",fontsize=16)
axs.set_xlabel("Prediction Probability",fontsize=12)
axs.set_ylabel("Outcome Fraction",fontsize=12)
axs.set_xlim(-0.05,1.05)
axs.set_ylim(-0.05,1.05)

plt.savefig(f"calibration_plots/draftkings.png",dpi=1000)