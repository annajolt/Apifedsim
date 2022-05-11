#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yfin
from re import L
from numpy.ma.core import shape
from matplotlib import style
from pandas_datareader import data as pdr
import questionary


# In[2]:


#getting data

#needed to bypass yahoo 
yfin.pdr_override()

#function to collect the mean returns and covalance matrix
def get_data(stocks, start, end):
  stockData = pdr.get_data_yahoo(stocks, start, end)
  stockData = stockData['Close']
  returns = stockData.pct_change()
  meanReturns = returns.mean()
  covMatrix = returns.cov()
  return meanReturns, covMatrix


#stocks in my portfolio
stockList = ['BTC-USD','ETH-USD','LUNA1-USD','BNB-USD','ADA-USD']
stocks = [stock for stock in stockList]

endDate = dt.datetime.now()

startDate = endDate - dt.timedelta(days=365)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)

#weights for portfolio

# the original code gave random weights
#weights = np.random.random(len(meanReturns))
#weights = np.random.random(5)
import questionary

coin = questionary.select(
    "What crypto currency would you like analyse?",
    choices=[
        "BTC",
        "ETH",
        "LUNA1",
        "BNB",
        "ADA"
    ]).ask()

if coin == "BTC":
    weights = [1,0,0,0,0]
elif coin == "ETH":
    weights = [0,1,0,0,0]
elif coin == "LUNA1":
    weights = [0,0,1,0,0]
elif coin == "BNB":
    weights = [0,0,0,1,0]
elif coin == "ADA":
    weights = [0,0,0,0,1]

print(weights)

# Giving the same weight to each cryto currency
#weights = [0.2,0.2,0.2,0.2,0.2]
#weights /= np.sum(weights)
#weights


# In[ ]:


#Monte Carlo Method

#number of simulations
mc_sims = 100
T = 100 #timeframe in days

#empty arrays to fill with mean returns data based on number of days
meanM = np.full(shape=(T, len(weights)), fill_value= meanReturns)
meanM = meanM.T

#other array for portfolio returns data
portfolio_sims = np.full(shape=(T, mc_sims), fill_value=0.0)

initialPortfolio = 10000
# portfolio_cumulative_returns = pd.Dataframe()
#Cholesky Decomposition (used to determine Lower Triangular Matrix)
# Z are the samples from a normal distribution
for m in range(0, mc_sims):
  #mc loops
  Z = np.random.normal(size=(T, len(weights)))
  L = np.linalg.cholesky(covMatrix)
  #Assuming daily returns are distributed by a Multivariate Normal Distribution 
  dailyReturns = meanM + np.inner(L, Z)
  portfolio_sims[:,m] = np.cumprod(np.inner(weights, dailyReturns.T)+1)*initialPortfolio

# summary/describe function of the data

#self.confidence_interval = portfolio_sims.quantile(q=[0.025, 0.975])
# def summarize_cumulative_return():
"""
Calculate final summary statistics for Monte Carlo simulated stock data.
"""
metrics = {}
metrics['max'] = portfolio_sims.max()
metrics['mean'] = portfolio_sims.mean()
metrics['min'] = portfolio_sims.min()
metrics['std'] = portfolio_sims.std()
metrics['25%'] = np.quantile(portfolio_sims, .25)
metrics['50%'] = np.quantile(portfolio_sims, .50)
metrics['75%'] = np.quantile(portfolio_sims, .75)
metrics['95% CI Lower'] = np.quantile(portfolio_sims, .025)
metrics['95% CI Upper'] = np.quantile(portfolio_sims, .0975)
# ci_series.index = ["95% CI Lower","95% CI Upper"]
# metrics.append(ci_series)

print(f"The summarization of your data {metrics}")
#MCS graph
plt.plot(portfolio_sims)
plt.ylabel('Portfolio Value ($)')
plt.xlabel('Days')
plt.title('Monte Carlo Simulation of Personal Crypto Portfolio')
plt.show()


