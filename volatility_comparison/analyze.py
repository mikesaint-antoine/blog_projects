import csv
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

times = []
polymarket = []
manifold = []


format_string = '%m/%d/%y %H:%M'

## read CSV / TSV
with open("superconductor.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        time = datetime.strptime(row[0], format_string)

        times.append(time)
        polymarket.append(float(row[1])/100)
        manifold.append(float(row[2])/100)



plot1, = plt.plot(times,polymarket,color='red',label="Polymarket")
plot2, = plt.plot(times,manifold,color='blue',label="Manifold")

plt.legend(handles=[plot1, plot2],fontsize=14)
plt.xticks(fontsize=6) 
plt.ylabel("Price / Probability",fontsize=16)
plt.xlabel("Time (one datapoint per hour)",fontsize=16)
# plt.show()

plt.savefig('timeseries.png',dpi = 1000)
plt.close()





poly_CV = []
man_CV = []

for i in range(len(polymarket)):

    low_ind = max(0,i-5)
    high_ind = min(len(polymarket),i+6)

    poly_CV.append(np.std(polymarket[low_ind:high_ind]) / np.mean(polymarket[low_ind:high_ind]))
    man_CV.append(np.std(manifold[low_ind:high_ind]) / np.mean(manifold[low_ind:high_ind]))


plot1, = plt.plot(times,poly_CV,color='red',label="Polymarket")
plot2, = plt.plot(times,man_CV,color='blue',label="Manifold")

plt.legend(handles=[plot1, plot2],fontsize=14)
plt.xticks(fontsize=6) 
plt.ylabel("Rolling CV",fontsize=16)
plt.xlabel("Time (one datapoint per hour)",fontsize=16)
# plt.show()

plt.savefig('rolling_cv.png',dpi = 1000)
plt.close()



poly_pct_change = []
man_pct_change = []

for i in range(len(polymarket)-1):
    poly_pct_change.append((polymarket[i+1]/polymarket[i] - 1)*100)

    man_pct_change.append((manifold[i+1]/manifold[i] - 1)*100)




print(f"Polymarket std of pct changes: {round(np.std(poly_pct_change),3)}")
print(f"Manifold std of pct changes: {round(np.std(man_pct_change),3)}")
print()

print(f"Polymarket CV of pct changes: {round(np.std(poly_pct_change) / np.mean(poly_pct_change),3)}")
print(f"Manifold CV of pct changes: {round(np.std(man_pct_change) / np.mean(man_pct_change),3)}")

