import numpy as np
from sklearn import metrics


def calibration(y_true,y_score,bin_bounds=[0,0.2,0.4,0.6,0.8,1]):
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






def brier_score(y_true,y_score):


    assert len(y_true) == len(y_score)


    N = len(y_score)

    total = 0

    for i in range(N):
        total += (y_score[i] - y_true[i])**2

    total = total/N



    return total


