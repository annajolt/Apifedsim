'''
This code allows the user to choose one out of 5 different crypto currencies to run a Monte Carlo simulation. The user can choose the number of simulations, number of days the simulation runs and initial investment. The data the similation is based on is the most recent 365 days as downloaded from Yahoo Finance via API.

'''


# make sure the environment has yfinance, questionary and pandas
# if not make sure you do a pip install
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

# we will use one year worth of data to run the simulation
endDate = dt.datetime.now()

startDate = endDate - dt.timedelta(days=365)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)

# the user chooses a coin they want to simulate

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


# The user enters the number of simulations
mc_sims = questionary.text("How many simulations would you like to run (max 500)?").ask()
# While loop to make sure the number of simulation is under 500
while int(mc_sims) > 500:
    print("please enter a number lower than 500")
    mc_sims = questionary.text("How many simulations would you like to run (max 500)?").ask()
mc_sims = int(mc_sims)

# The user enters the number of days each simulation will run
T = questionary.text("How many days in the future would you like to run the Monte Carlo simulation for (max 1000)?").ask()
# While loop to make sure the number of days is under 1000
while int(T)> 1000:
    print("please enter a number lower than 1000")
    T = questionary.text("How many days in the future would you like to run the Monte Carlo simulation for (max 1000)?").ask()
T = int(T)

# The user enters the initial investment
initialPortfolio = questionary.text("What is your initial investment?").ask()

initialPortfolio = float(initialPortfolio)

#Monte Carlo Method

#empty arrays to fill with mean returns data based on number of days
meanM = np.full(shape=(T, len(weights)), fill_value= meanReturns)
meanM = meanM.T

#other array for portfolio returns data
portfolio_sims = np.full(shape=(T, mc_sims), fill_value=0.0)

#Cholesky Decomposition (used to determine Lower Triangular Matrix)
# Z are the samples from a normal distribution
for m in range(0, mc_sims):
  #mc loops
  Z = np.random.normal(size=(T, len(weights)))
  L = np.linalg.cholesky(covMatrix)
  #Assuming daily returns are distributed by a Multivariate Normal Distribution 
  dailyReturns = meanM + np.inner(L, Z)
  portfolio_sims[:,m] = np.cumprod(np.inner(weights, dailyReturns.T)+1)*initialPortfolio

# Summary statistics    
    
metrics = {}
metrics['max'] = portfolio_sims.max()
metrics['mean'] = portfolio_sims.mean()
metrics['min'] = portfolio_sims.min()
metrics['std'] = portfolio_sims.std()
metrics['25%'] = np.quantile(portfolio_sims, .25)
metrics['50%'] = np.quantile(portfolio_sims, .50)
metrics['75%'] = np.quantile(portfolio_sims, .75)
metrics['95% CI Lower'] = np.quantile(portfolio_sims, .025)
metrics['95% CI Upper'] = np.quantile(portfolio_sims, .975)
print(f"The summarization of your data {metrics}")

#MCS graph
plt.plot(portfolio_sims)
plt.ylabel('Portfolio Value ($)')
plt.xlabel('Days')
plt.title('Monte Carlo Simulation of Personal Crypto Portfolio')
plt.show()


# In[ ]:




