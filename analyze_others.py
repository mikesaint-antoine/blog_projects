import yfinance as yf
import numpy as np
import sys


year = "2015"



## 2014
# https://www.nasdaq.com/articles/zacks-1-ranked-growth-mutual-funds-best-of-funds-2014-02-06
# criteria: 1 year
if year=="2014":

    tickers = ["BIAOX","IALAX","FBGRX","THCGX","RSMOX", "SPY" ]

    article_date = "2014-02-06"
    before_date = "2013-02-06"
    after_date = "2015-02-06"


## 2015
# https://www.nasdaq.com/articles/top-mutual-funds-best-returns-10-years-2015-10-05
# criteria: 10 years
if year=="2015":
    tickers = ["PRHSX","JAGLX","FBIOX","FBSOX","USSCX","FSRPX","FDLSX","FSHCX","HIAHX","FSPHX", "SPY" ]
    
    # # criteria: 10 years 
    # after date is to present (at least it was the present when I first did the analysis)
    article_date = "2015-09-30"
    before_date = "2005-09-30"
    after_date = "2023-01-20"




pre_rois = []
post_rois = []
for ticker in tickers:

    # calculating percent return, BEFORE article
    data = yf.download(ticker, start=before_date, end=article_date)
    start_price = data['Adj Close'].iloc[0]
    end_price = data['Adj Close'].iloc[-1]
    roi = round((end_price/start_price - 1)*100,3)
    pre_rois.append(roi)

    # calculating percent return, AFTER article
    data = yf.download(ticker, start=article_date, end=after_date)
    start_price = data['Adj Close'].iloc[0]
    end_price = data['Adj Close'].iloc[-1]
    roi = round((end_price/start_price - 1)*100,3)
    post_rois.append(roi)


## last element in tickers, pre_rois, post_rois is SPY
assert(tickers[-1]=="SPY")
pre_spy = pre_rois[-1]
post_spy = post_rois[-1]


## just printing results here so I can copy and paste into excel table
for i in range(len(tickers)):

    print(f"{tickers[i]}\tpre ratio: {round(pre_rois[i]/pre_spy,3)}\tpost ratio: {round(post_rois[i]/post_spy,3)}")

