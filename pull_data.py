#!/usr/bin/env python
# coding: utf-8

# In[4]:


import yfinance as yf
from pandas_datareader import data as pdr
from datetime import date, timedelta, datetime
import pandas as pd
import threading
import bisect


# In[5]:


dfStocks=pd.read_csv('tickers.csv')  
tickers=dfStocks.ticker.tolist()


# In[6]:


today = date.today()
day_delta=90

#today = today - timedelta(day_delta)

start = today - timedelta(day_delta)
start= start.strftime("%Y-%m-%d")

end = today + timedelta(1)
end = end.strftime("%Y-%m-%d")


# In[7]:


#     ticker='SE'
#     today = datetime.today()
#     days45 = today + timedelta(45)

#     optTicker = yf.Ticker(ticker)
#     last_price=optTicker.history().tail(1)['Close'].iloc[0]

#     date_list=optTicker.options
#     date_df = pd.to_datetime(date_list)
#     date_diffs = abs(days45 - date_df)
#     closest_date = date_list[date_diffs.argmin()]


#     opt = optTicker.option_chain(closest_date)

#     optCalls=opt[0]
#     optPuts=opt[1]

#     strikes=optPuts['strike'].tolist()
#     strikes.sort()
    
#     index = bisect.bisect(strikes, last_price)
#     sellPut=strikes[index-1]
#     if sellPut-5 in strikes:
#         buyPut=sellPut-5
#     else:
#         index = bisect.bisect(strikes, sellPut-1.5)
#         buyPut=strikes[index-1]

#     sellDF=optPuts[optPuts['strike']==sellPut]
#     buyDF=optPuts[optPuts['strike']==buyPut]

#     width=sellDF.strike.iloc[0]-buyDF.strike.iloc[0]
#     premium=sellDF.bid.iloc[0]-buyDF.ask.iloc[0]
#     if premium<0:
#         premium=(sellDF.bid.iloc[0]+sellDF.ask.iloc[0])/2-(buyDF.bid.iloc[0]+buyDF.ask.iloc[0])/2
#     if premium>width:
#         premium=0
#         IV=0
#     else:
#         IV=sellDF.impliedVolatility.iloc[0]
# #     index = bisect.bisect(strikes, last_price)
# #     sellPut=strikes[index-1]
# #     if sellPut-5 in strikes:
# #         buyPut=sellPut-5
# #     else:
# #         index = bisect.bisect(strikes, sellPut-1.5)
# #         buyPut=strikes[index-1]

# #     sellDF=optPuts[optPuts['strike']==sellPut]
# #     buyDF=optPuts[optPuts['strike']==buyPut]

# #     width=sellDF.strike.iloc[0]-buyDF.strike.iloc[0]
# #     premium=sellDF.bid.iloc[0]-buyDF.ask.iloc[0]
# #     IV=sellDF.impliedVolatility.iloc[0]
#     #print(sellPut,buyPut)
#     #optPuts.head()
#     #print([width,premium,IV])
#     #optPuts[(optPuts['strike'] ==67.5) | (optPuts['strike']==62.5) ].head()
#     #optPuts.head()


# In[8]:


# ticker='MSFT'
# ahTicker = yf.Ticker(ticker)
# ahTicker.history()


# In[9]:


def getPutSpread(last_price,ticker):
    today = datetime.today()
    days45 = today + timedelta(45)

    optTicker = yf.Ticker(ticker)
    #last_price=optTicker.history().tail(1)['Close'].iloc[0]

    date_list=optTicker.options
    date_df = pd.to_datetime(date_list)
    date_diffs = abs(days45 - date_df)
    closest_date = date_list[date_diffs.argmin()]


    opt = optTicker.option_chain(closest_date)

    optCalls=opt[0]
    optPuts=opt[1]

    strikes=optPuts['strike'].tolist()
    strikes.sort()

    index = bisect.bisect(strikes, last_price)
    sellPut=strikes[index-1]
    if sellPut-5 in strikes:
        buyPut=sellPut-5
    else:
        index = bisect.bisect(strikes, sellPut-1.5)
        buyPut=strikes[index-1]

    sellDF=optPuts[optPuts['strike']==sellPut]
    buyDF=optPuts[optPuts['strike']==buyPut]

    width=sellDF.strike.iloc[0]-buyDF.strike.iloc[0]
    premium=sellDF.bid.iloc[0]-buyDF.ask.iloc[0]
    if premium<0:
        premium=(sellDF.bid.iloc[0]+sellDF.ask.iloc[0])/2-(buyDF.bid.iloc[0]+buyDF.ask.iloc[0])/2
    if premium>width:
        premium=0
        IV=0
    else:
        IV=sellDF.impliedVolatility.iloc[0]
    outputArr=[width,premium,IV]
    return outputArr
    #print(optPuts.columns)
    #print (width,premium,IV)



# In[10]:


def stok_data_pull():
        dfOutput=pd.DataFrame()

        for t in tickers:
            df = yf.download(t.replace('.', '-').replace('^', '-'), 
                                  start=start, 
                                  end=end,
                                  prepost=True,
                                  progress=False)

            df['Stock']=t
            dfTemp=df.reset_index()
            last_price=dfTemp[dfTemp['Date']==dfTemp['Date'].max()].Close.iloc[0]
            try:
                putSpread=getPutSpread(last_price,t)
            except:
                putSpread=[0,0,0]
            df['putWidth']=putSpread[0]
            df['putPremium']=putSpread[1]
            df['putIV']=putSpread[2]
            try:
                dfOutput=pd.concat([dfOutput, df])
            except:
                print('error '+t)

        dfOutput.drop_duplicates()
        dfOutput['dt']=''
        dfOutput['dt'].iloc[0] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dfOutput.to_csv('static/data.csv')
        return "done"


# In[11]:


#one time

stok_data_pull()


# In[24]:


# def get_stock_data():
#     threading.Timer(300.0, get_stock_data).start() # called every 5 minute
#     try:
#         stok_data_pull()
#     except:
#         pass

#get_stock_data()


# In[ ]:




