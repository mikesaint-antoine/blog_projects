import numpy as np 
import csv
from sklearn import metrics
import matplotlib.pyplot as plt
from eval_functions import *



##################################################################################################
## global plot style vars
axis_label_size = 14
legend_size = 10
title_size = 14

dpi=300
## resolution for figs


color_scheme = ["blue", "red", "orange","green","gray","black"]
##################################################################################################





## trying to read in data

prob_mat = []
outcomes = []
incumbents = []
ns_control = []

with open("midterm_data.csv") as tsvfile:

    reader = csv.reader(tsvfile, delimiter=',')

    next(reader)
    for row in reader:

        # if row[15] != "UNRESOLVED" and (np.mean(np.array(row[2:11]).astype(float)) <=0.9 and np.mean(np.array(row[2:11]).astype(float)) >=0.1):
        if row[15] != "UNRESOLVED" :

            # check to see if there are values for manifold (subset of total questions)
            if len(row[11])>0:
                prob_mat.append(row[2:14])
                incumbents.append(row[14])
                outcomes.append(row[15])
                ns_control.append(0.5)





prob_mat = np.array(prob_mat).astype(float)
outcomes = np.array(outcomes).astype(float)
incumbents = np.array(incumbents).astype(float)




assert prob_mat.shape[0] == outcomes.shape[0]
assert prob_mat.shape[0] == incumbents.shape[0]


## prob_mat columns
## predictit_2_weeks_out,predictit_1_week_out,predictit_day_before,538_2_weeks_out,538_1_week_out,538_day_before,ebo_2_weeks_out,ebo_1_week_out,ebo_day_before,manifold_2_weeks_out,manifold_1_week_out,manifold_day_before


##########################################################################################
## print stats


## Remember this is a subset of all predictit questions
#predictit_2_weeks_out
print("PredictIt (subset) 2 Weeks:")
print_stats(outcomes,prob_mat[:,0],round=1)

#predictit_1_week_out
print("PredictIt (subset) 1 Week:")
print_stats(outcomes,prob_mat[:,1],round=1)

#predictit_day_before
print("PredictIt (subset) Day Before:")
print_stats(outcomes,prob_mat[:,2],round=1)

# #538_2_weeks_out
# print_stats(outcomes,prob_mat[:,3],round=1)

# #538_1_week_out
# print_stats(outcomes,prob_mat[:,4],round=1)

# #538_day_before
# print_stats(outcomes,prob_mat[:,5],round=1)

# #ebo_2_weeks_out
# print_stats(outcomes,prob_mat[:,6],round=1)

# #ebo_1_week_out
# print_stats(outcomes,prob_mat[:,7],round=1)

# #ebo_day_before
# print_stats(outcomes,prob_mat[:,8],round=1)


#manifold_2_weeks_out
print("Manifold 2 Weeks:")
print_stats(outcomes,prob_mat[:,9],round=1)

#manifold_1_week_out
print("Manifold 1 Week:")
print_stats(outcomes,prob_mat[:,10],round=1)

#manifold_day_before
print("Manifold Day Before:")
print_stats(outcomes,prob_mat[:,11],round=1)



# #incumbent control
print("Incumbent Control:")
print_stats(outcomes,incumbents,round=1)




# #no skill control
print("No Skill Control:")
print_stats(outcomes,ns_control,round=1)

##########################################################################################



## ROC Curve, 2 weeks out -- ALL

#no skill
if sum(outcomes)/len(outcomes) >=0.5:
    y_ns = [1 for _ in range(len(outcomes))]
else:
    y_ns = [0 for _ in range(len(outcomes))]

# #predictit_2_weeks_out
fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,prob_mat[:,0], pos_label=1)
predictit, = plt.plot(fpr,tpr,label="PredictIt",color=color_scheme[0])

# # #538_2_weeks_out
# fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,prob_mat[:,3], pos_label=1)
# fte, = plt.plot(fpr,tpr,label="FiveThirtyEight",color=color_scheme[1])


# # #ebo_2_weeks_out
# fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,prob_mat[:,6], pos_label=1)
# ebo, = plt.plot(fpr,tpr,label="Election Betting Odds",color=color_scheme[2])

# #manifold_2_weeks_out
fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,prob_mat[:,9], pos_label=1)
manifold, = plt.plot(fpr,tpr,label="Manifold",color=color_scheme[3])


# #incumbent control
fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,incumbents, pos_label=1)
incumbent_control, = plt.plot(fpr,tpr,label="Incumbent Control",color=color_scheme[4])



# #ns control
fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,y_ns, pos_label=1)
ns_control, = plt.plot(fpr,tpr,label="NS Control",color=color_scheme[5])



plt.legend(handles=[predictit,manifold,incumbent_control,ns_control],fontsize=legend_size,loc="lower right")
plt.xlabel("False Positive Rate",fontsize=axis_label_size)
plt.ylabel("True Positive Rate",fontsize=axis_label_size)
plt.ylim(0,1)
plt.xlim(0,1)
plt.title("ROC Curve -- 2 Weeks Out",fontsize=title_size)

# plt.show()
plt.savefig("figs/roc_curve_2_weeks_MANIFOLD.png",dpi=dpi)
plt.close()



##########################################################################################
##########################################################################################
## ROC Curve, 1 week out -- ALL

#no skill
if sum(outcomes)/len(outcomes) >=0.5:
    y_ns = [1 for _ in range(len(outcomes))]
else:
    y_ns = [0 for _ in range(len(outcomes))]

# #predictit_1_weeks_out
fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,prob_mat[:,1], pos_label=1)
predictit, = plt.plot(fpr,tpr,label="PredictIt",color=color_scheme[0])

# # #538_1_week_out
# fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,prob_mat[:,4], pos_label=1)
# fte, = plt.plot(fpr,tpr,label="FiveThirtyEight",color=color_scheme[1])


# # #ebo_1_week_out
# fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,prob_mat[:,7], pos_label=1)
# ebo, = plt.plot(fpr,tpr,label="Election Betting Odds",color=color_scheme[2])





# #manifold_1_week_out
fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,prob_mat[:,10], pos_label=1)
manifold, = plt.plot(fpr,tpr,label="Manifold",color=color_scheme[3])


# #incumbent control
fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,incumbents, pos_label=1)
incumbent_control, = plt.plot(fpr,tpr,label="Incumbent Control",color=color_scheme[4])



# #ns control
fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,y_ns, pos_label=1)
ns_control, = plt.plot(fpr,tpr,label="NS Control",color=color_scheme[5])



plt.legend(handles=[predictit,manifold,incumbent_control,ns_control],fontsize=legend_size,loc="lower right")
plt.xlabel("False Positive Rate",fontsize=axis_label_size)
plt.ylabel("True Positive Rate",fontsize=axis_label_size)
plt.ylim(0,1)
plt.xlim(0,1)
plt.title("ROC Curve -- 1 Week Out",fontsize=title_size)

# plt.show()
plt.savefig("figs/roc_curve_1_week_MANIFOLD.png",dpi=dpi)
plt.close()








##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
## ROC Curve, Day Before -- ALL

#no skill
if sum(outcomes)/len(outcomes) >=0.5:
    y_ns = [1 for _ in range(len(outcomes))]
else:
    y_ns = [0 for _ in range(len(outcomes))]

# #predictit_1_weeks_out
fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,prob_mat[:,2], pos_label=1)
predictit, = plt.plot(fpr,tpr,label="PredictIt",color=color_scheme[0])


# # #538_day_before
# fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,prob_mat[:,5], pos_label=1)
# fte, = plt.plot(fpr,tpr,label="FiveThirtyEight",color=color_scheme[1])


# # #ebo_day_before
# fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,prob_mat[:,8], pos_label=1)
# ebo, = plt.plot(fpr,tpr,label="Election Betting Odds",color=color_scheme[2])




# #manifold_1_week_out
fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,prob_mat[:,11], pos_label=1)
manifold, = plt.plot(fpr,tpr,label="Manifold",color=color_scheme[3])


# #incumbent control
fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,incumbents, pos_label=1)
incumbent_control, = plt.plot(fpr,tpr,label="Incumbent Control",color=color_scheme[4])



# #ns control
fpr, tpr, roc_thresholds = metrics.roc_curve(outcomes,y_ns, pos_label=1)
ns_control, = plt.plot(fpr,tpr,label="NS Control",color=color_scheme[5])



plt.legend(handles=[predictit,manifold,incumbent_control,ns_control],fontsize=legend_size,loc="lower right")
plt.xlabel("False Positive Rate",fontsize=axis_label_size)
plt.ylabel("True Positive Rate",fontsize=axis_label_size)
plt.ylim(0,1)
plt.xlim(0,1)
plt.title("ROC Curve -- Day Before",fontsize=title_size)

# plt.show()
plt.savefig("figs/roc_curve_day_before_MANIFOLD.png",dpi=dpi)
plt.close()




##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################

## Calibration plots -- 2 weeks out

cal_legend = 8
cal_title = 10
cal_ax = 10

fig, axs = plt.subplots(1, 2, sharex=True, sharey=True)

fig.suptitle('Calibration Plots -- 2 Weeks Out', fontsize=16)



# PredictIt
[bin_means, outcome_means] = calibration(outcomes,prob_mat[:,0])
axs[0].scatter(bin_means,outcome_means)
# ax1.set(adjustable='box',autoscale_on=False, aspect='equal')
axs[0].set(autoscale_on=False, aspect='equal')
perfect, = axs[0].plot([0,1],[0,1],color="black",label="perfect")
axs[0].legend(handles=[perfect],fontsize=cal_legend,)
axs[0].set_title("PredictIt",fontsize=cal_title)
axs[0].set_xlabel("Prediction Probability",fontsize=cal_ax)
axs[0].set_ylabel("Outcome Fraction",fontsize=cal_ax)

# Manifold
[bin_means, outcome_means] = calibration(outcomes,prob_mat[:,9])
axs[1].scatter(bin_means,outcome_means)
axs[1].set(autoscale_on=False, aspect='equal')
perfect, = axs[1].plot([0,1],[0,1],color="black",label="perfect")
axs[1].legend(handles=[perfect],fontsize=cal_legend,)
axs[1].set_title("Manifold Markets",fontsize=cal_title)





fig = plt.gcf()
fig.set_size_inches(6, 3)


# plt.show()
plt.savefig("figs/calibration_2_weeks_MANIFOLD.png",dpi=dpi)
plt.close()

##########################################################################################


## Calibration plots -- 1 week out

fig, axs = plt.subplots(1, 2, sharex=True, sharey=True)

fig.suptitle('Calibration Plots -- 1 Week Out', fontsize=16)



# PredictIt
[bin_means, outcome_means] = calibration(outcomes,prob_mat[:,1])
axs[0].scatter(bin_means,outcome_means)
# ax1.set(adjustable='box',autoscale_on=False, aspect='equal')
axs[0].set(autoscale_on=False, aspect='equal')
perfect, = axs[0].plot([0,1],[0,1],color="black",label="perfect")
axs[0].legend(handles=[perfect],fontsize=cal_legend,)
axs[0].set_title("PredictIt",fontsize=cal_title)
axs[0].set_xlabel("Prediction Probability",fontsize=cal_ax)
axs[0].set_ylabel("Outcome Fraction",fontsize=cal_ax)

#Manifold
[bin_means, outcome_means] = calibration(outcomes,prob_mat[:,10])
axs[1].scatter(bin_means,outcome_means)
axs[1].set(autoscale_on=False, aspect='equal')
perfect, = axs[1].plot([0,1],[0,1],color="black",label="perfect")
axs[1].legend(handles=[perfect],fontsize=cal_legend,)
axs[1].set_title("Manifold Markets",fontsize=cal_title)



fig = plt.gcf()
fig.set_size_inches(6, 3)

# plt.show()
plt.savefig("figs/calibration_1_week_MANIFOLD.png",dpi=dpi)
plt.close()


##########################################################################################


## Calibration plots -- Day before

fig, axs = plt.subplots(1, 2, sharex=True, sharey=True)

fig.suptitle('Calibration Plots -- Day Before', fontsize=16)



# PredictIt
[bin_means, outcome_means] = calibration(outcomes,prob_mat[:,2])
axs[0].scatter(bin_means,outcome_means)
# ax1.set(adjustable='box',autoscale_on=False, aspect='equal')
axs[0].set(autoscale_on=False, aspect='equal')
perfect, = axs[0].plot([0,1],[0,1],color="black",label="perfect")
axs[0].legend(handles=[perfect],fontsize=cal_legend,)
axs[0].set_title("PredictIt",fontsize=cal_title)
axs[0].set_xlabel("Prediction Probability",fontsize=cal_ax)
axs[0].set_ylabel("Outcome Fraction",fontsize=cal_ax)

# Manifold
[bin_means, outcome_means] = calibration(outcomes,prob_mat[:,11])
axs[1].scatter(bin_means,outcome_means)
axs[1].set(autoscale_on=False, aspect='equal')
perfect, = axs[1].plot([0,1],[0,1],color="black",label="perfect")
axs[1].legend(handles=[perfect],fontsize=cal_legend,)
axs[1].set_title("Manifold Markets",fontsize=cal_title)





fig = plt.gcf()
fig.set_size_inches(6, 3)


# plt.show()
plt.savefig("figs/calibration_day_before_MANIFOLD.png",dpi=dpi)
plt.close()









