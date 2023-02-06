import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy.stats import pearsonr


## homelessness rate data: https://www.statista.com/statistics/727847/homelessness-rate-in-the-us-by-state/


## score calculation weights: https://www.freedominthe50states.org/how-its-calculated
## map: https://www.freedominthe50states.org/land
## data: https://www.freedominthe50states.org/data

## median home value: https://www.experian.com/blogs/ask-experian/research/median-home-values-by-state/


total = 11.52

#weights
w1 = 5.3/total
w2 = 2.5/total
w3 = 2.5/total
w4 = 1/total

w5 = 0.1/total
w6 = 0.1/total
w7 = 0.01/total
w8 = 0.01/total


weights = [w1,w2,w3,w4,w5,w6,w7,w8]

# print(w1+w2+w3+w4+w5+w6+w7+w8)




states = []
land_freedom_scores = []
homeless_rates = []
home_vals = []

dem_states = []
dem_homeless_rates = []
dem_land_freedom_scores = []
dem_home_vals = []

rep_states = []
rep_homeless_rates = []
rep_land_freedom_scores = []
rep_home_vals = []



with open("data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    for row in reader:
        states.append(row[0])
        homeless_rates.append(float(row[1]))
        home_vals.append(float(row[11]))

        tmp = np.array(row[2:10]).astype(float)
        score = np.dot(tmp,weights)
        land_freedom_scores.append(score)

        if row[10]=="D":
            dem_states.append(row[0])
            dem_homeless_rates.append(float(row[1]))
            dem_land_freedom_scores.append(score)
            dem_home_vals.append(float(row[11]))

        else:
            rep_states.append(row[0])
            rep_homeless_rates.append(float(row[1]))
            rep_land_freedom_scores.append(score)
            rep_home_vals.append(float(row[11]))



alpha_to_use = 0.5

fig, ax = plt.subplots()


ax.scatter(dem_land_freedom_scores,dem_homeless_rates,color="blue",alpha=alpha_to_use)
ax.scatter(rep_land_freedom_scores,rep_homeless_rates,color="red",alpha=alpha_to_use)



z = np.polyfit(land_freedom_scores, homeless_rates, 1)
y_hat = np.poly1d(z)(land_freedom_scores)
ax.plot(land_freedom_scores, y_hat, "r-", lw=1,color="black")
ax.set_xlabel("Land Use Freedom Score",fontsize=14)
ax.set_ylabel("Homeless Rate per 10k",fontsize=14)


corr, _ = pearsonr(land_freedom_scores, homeless_rates)

corr = np.round(corr,decimals=3)

text = f"$R^2$ = {r2_score(homeless_rates,y_hat):0.4f}\nPearson correlation: " +str(corr)
plt.gca().text(0.5, 0.95, text,transform=plt.gca().transAxes,
     fontsize=13, verticalalignment='top')


for i, txt in enumerate(states):
    ax.annotate(txt, (land_freedom_scores[i], homeless_rates[i]),fontsize=6)


plt.savefig("plots/plot.png",dpi=1000)
plt.close()



fig, ax = plt.subplots()

ax.scatter(dem_land_freedom_scores,dem_homeless_rates,color="blue",alpha=alpha_to_use)



z = np.polyfit(dem_land_freedom_scores, dem_homeless_rates, 1)
y_hat = np.poly1d(z)(dem_land_freedom_scores)
ax.plot(dem_land_freedom_scores, y_hat, "r-", lw=1,color="black")
ax.set_xlabel("Land Use Freedom Score",fontsize=14)
ax.set_ylabel("Homeless Rate per 10k",fontsize=14)


corr, _ = pearsonr(dem_land_freedom_scores, dem_homeless_rates)

corr = np.round(corr,decimals=3)

text = f"$R^2$ = {r2_score(dem_homeless_rates,y_hat):0.4f}\nPearson correlation: " +str(corr)
plt.gca().text(0.5, 0.95, text,transform=plt.gca().transAxes,
     fontsize=13, verticalalignment='top')


for i, txt in enumerate(dem_states):
    ax.annotate(txt, (dem_land_freedom_scores[i], dem_homeless_rates[i]),fontsize=6)


plt.savefig("plots/dem_plot.png",dpi=1000)
plt.close()



fig, ax = plt.subplots()


ax.scatter(rep_land_freedom_scores,rep_homeless_rates,color="red",alpha=alpha_to_use)



z = np.polyfit(rep_land_freedom_scores, rep_homeless_rates, 1)
y_hat = np.poly1d(z)(rep_land_freedom_scores)
ax.plot(rep_land_freedom_scores, y_hat, "r-", lw=1,color="black")
ax.set_xlabel("Land Use Freedom Score",fontsize=14)
ax.set_ylabel("Homeless Rate per 10k",fontsize=14)


corr, _ = pearsonr(rep_land_freedom_scores, rep_homeless_rates)

corr = np.round(corr,decimals=3)

text = f"$R^2$ = {r2_score(rep_homeless_rates,y_hat):0.4f}\nPearson correlation: " +str(corr)
plt.gca().text(0.5, 0.95, text,transform=plt.gca().transAxes,
     fontsize=13, verticalalignment='top')


for i, txt in enumerate(rep_states):
    ax.annotate(txt, (rep_land_freedom_scores[i], rep_homeless_rates[i]),fontsize=6)


plt.savefig("plots/rep_plot.png",dpi=1000)
plt.close()

#######################################

fig, ax = plt.subplots()

ax.scatter(dem_land_freedom_scores,dem_home_vals,color="blue",alpha=alpha_to_use)
ax.scatter(rep_land_freedom_scores,rep_home_vals,color="red",alpha=alpha_to_use)



z = np.polyfit(land_freedom_scores, home_vals, 1)
y_hat = np.poly1d(z)(land_freedom_scores)
ax.plot(land_freedom_scores, y_hat, "r-", lw=1,color="black")
ax.set_xlabel("Land Use Freedom Score",fontsize=14)
ax.set_ylabel("Median Home Value ($)",fontsize=14)


corr, _ = pearsonr(land_freedom_scores, home_vals)

corr = np.round(corr,decimals=3)

text = f"$R^2$ = {r2_score(home_vals,y_hat):0.4f}\nPearson correlation: " +str(corr)
plt.gca().text(0.5, 0.95, text,transform=plt.gca().transAxes,
     fontsize=13, verticalalignment='top')


for i, txt in enumerate(states):
    ax.annotate(txt, (land_freedom_scores[i], home_vals[i]),fontsize=6)


plt.savefig("plots/home_vals_plot.png",dpi=1000,bbox_inches = "tight")
plt.close()





fig, ax = plt.subplots()

ax.scatter(dem_land_freedom_scores,dem_home_vals,color="blue",alpha=alpha_to_use)

z = np.polyfit(dem_land_freedom_scores, dem_home_vals, 1)
y_hat = np.poly1d(z)(dem_land_freedom_scores)
ax.plot(dem_land_freedom_scores, y_hat, "r-", lw=1,color="black")
ax.set_xlabel("Land Use Freedom Score",fontsize=14)
ax.set_ylabel("Median Home Value ($)",fontsize=14)


corr, _ = pearsonr(dem_land_freedom_scores, dem_home_vals)

corr = np.round(corr,decimals=3)

text = f"$R^2$ = {r2_score(dem_home_vals,y_hat):0.4f}\nPearson correlation: " +str(corr)
plt.gca().text(0.5, 0.95, text,transform=plt.gca().transAxes,
     fontsize=13, verticalalignment='top')


for i, txt in enumerate(dem_states):
    ax.annotate(txt, (dem_land_freedom_scores[i], dem_home_vals[i]),fontsize=6)


plt.savefig("plots/dem_home_vals_plot.png",dpi=1000,bbox_inches = "tight")
plt.close()







fig, ax = plt.subplots()

ax.scatter(rep_land_freedom_scores,rep_home_vals,color="red",alpha=alpha_to_use)



z = np.polyfit(rep_land_freedom_scores, rep_home_vals, 1)
y_hat = np.poly1d(z)(rep_land_freedom_scores)
ax.plot(rep_land_freedom_scores, y_hat, "r-", lw=1,color="black")
ax.set_xlabel("Land Use Freedom Score",fontsize=14)
ax.set_ylabel("Median Home Value ($)",fontsize=14)


corr, _ = pearsonr(rep_land_freedom_scores, rep_home_vals)

corr = np.round(corr,decimals=3)

text = f"$R^2$ = {r2_score(rep_home_vals,y_hat):0.4f}\nPearson correlation: " +str(corr)
plt.gca().text(0.5, 0.95, text,transform=plt.gca().transAxes,
     fontsize=13, verticalalignment='top')


for i, txt in enumerate(rep_states):
    ax.annotate(txt, (rep_land_freedom_scores[i], rep_home_vals[i]),fontsize=6)


plt.savefig("plots/rep_home_vals_plot.png",dpi=1000,bbox_inches = "tight")
plt.close()


