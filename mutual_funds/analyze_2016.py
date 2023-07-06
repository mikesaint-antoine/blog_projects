import yfinance as yf
import numpy as np
import sys
import matplotlib.pyplot as plt

# data source:
# https://www.nasdaq.com/articles/best-mutual-funds-2016-2016-12-30



# removed: JHSVX, WTSVX, ACRTX
# they gave an error for yfinance


tickers = ["AVALX",
"TDVFX",
"HDPMX",
"QISCX",
"BOTSX",
"BOSVX",
"TASVX",
"SMVAX",
"HCMZX",
"CSMIX",
"RYSEX",
"GSITX",
"ICSCX",
"FSCCX",
"WSCVX",
"DEVLX",
"LMVYX",
"PSOPX",
"DASCX",
"RYPNX",
"VCSVX",
"SCYVX",
"LSVQX",
"VSSVX",
"BERWX",
"PMDIX",
"KSDIX",
"FRVLX",
"MMEYX",
"GOGFX",
"ARTLX",
"SCETX",
"DRSVX",
"FRMCX",
"ESPAX",
"PRSVX",
"CWSIX",
"DFSVX",
"IYSAX",
"WHGSX",
"NPRTX",
"AASCX",
"CSCVX",
"TVOAX",
"NOSGX",
"CIPSX",
"IPSIX",
"SCVIX",
"MSCFX",
"DFFVX",
"AVFIX",
"ARSVX",
"HRVIX",
"SEVAX",
"NWUIX",
"MXXVX",
"CDOFX",
"SPY"]



article_date = "2016-12-30"
before_date = "2015-12-30"
after_date = "2017-12-30"
# 1 year before and 1 year after article publication




pre_rois = []
post_rois = []
for ticker in tickers:

    # calculating percent return, year BEFORE article
    data = yf.download(ticker, start=before_date, end=article_date)
    start_price = data['Adj Close'].iloc[0]
    end_price = data['Adj Close'].iloc[-1]
    roi = round((end_price/start_price - 1)*100,3)
    pre_rois.append(roi)

    # calculating percent return, year AFTER article
    data = yf.download(ticker, start=article_date, end=after_date)
    start_price = data['Adj Close'].iloc[0]
    end_price = data['Adj Close'].iloc[-1]
    roi = round((end_price/start_price - 1)*100,3)
    post_rois.append(roi)


## last element in tickers, pre_rois, post_rois is SPY
assert(tickers[-1]=="SPY")
pre_spy = pre_rois[-1]
post_spy = post_rois[-1]


# calculating fund/spy return ratios
pre_ratios = []
post_ratios = []
for i in range(len(tickers)-1):
    # len - 1 because last element is SPY, so that is excluded

    print(f"{tickers[i]}\tpre ratio: {round(pre_rois[i]/pre_spy,3)}\tpost ratio: {round(post_rois[i]/post_spy,3)}")

    pre_ratios.append(round(pre_rois[i]/pre_spy,3))
    post_ratios.append(round(post_rois[i]/post_spy,3))


pre_ratios = np.array(pre_ratios)
post_ratios = np.array(post_ratios)


## yfinance puts a limit on queries per hour, 
## so if you're going to be running a lot and debugging the plots
## it might be better to just run once and save these ratios in np objects, then load to plot
# np.save('pre_ratios.npy', pre_ratios)
# np.save('post_ratios.npy', post_ratios)



## plot ratio distributions
fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=False)


alpha_to_use= 0.5
color_to_use = "blue"
ax1.hist(pre_ratios,bins=20,alpha=alpha_to_use,color=color_to_use)
ax1.axvline(x = 1,linestyle="dashed",color="black")
ax2.hist(post_ratios,bins=20,alpha=alpha_to_use,color=color_to_use)
ax2.axvline(x = 1,linestyle="dashed",color="black")

ax1.set_title("1 Year Pre-Article",fontsize=14)
ax2.set_title("1 Year Post-Article",fontsize=14)

ax2.set_xlabel("Fund / SPY Return Ratio",fontsize=14)
ax2.set_ylabel("Occurences",fontsize=14)

ax2.set_xticks(list(range(-1,9)))


plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
# plt.show()
plt.savefig("hist_2016.png",dpi=1000)

