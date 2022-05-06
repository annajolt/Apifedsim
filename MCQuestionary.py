import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yfin
import questionary 
from re import L
from numpy.ma.core import shape
from matplotlib import style
from pandas_datareader import data as pdr



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


def stock_data():
    
    #Using questionary, give the user a list of cryptos to run the report on.
    stock = questionary.select("Which Crypto do you want to analyze?", choices=stockList, use_arrow_keys: bool=True).ask()

        print("Running report ...")

    #stocks in my portfolio
    stockList = ['BTC-USD','ETH-USD','LUNA1-USD','BNB-USD','ADA-USD']
    stocks = [stock for stock in stockList]

    endDate = dt.datetime.now()

    startDate = endDate - dt.timedelta(days=365)

    meanReturns, covMatrix = get_data(stocks, startDate, endDate)

    # Set weights if empty, otherwise make sure sum of weights equals one.
    if weights == "":
    questionary.text("What is the weight of the stock?").ask()
    num_stocks = len(stockData.columns.get_level_values(0).unique())
    weights = [1.0/num_stocks for s in range(0,num_stocks)]
    else:
    if round(sum(weights),2) < .99:
        raise AttributeError("Sum of portfolio weights must equal one.")


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

"""#Cholesky Decomposition (used to determine Lower Triangular Matrix)
# Z are the samples from a normal distribution
 for m in range(0, mc_sims):
  #mc loops
  Z = np.random.normal(size=(T, len(weights)))
  L = np.linalg.cholesky(covMatrix)
  #Assuming daily returns are distributed by a Multivariate Normal Distribution 
  dailyReturns = meanM + np.inner(L, Z)
  portfolio_sims[:,m] = np.cumprod(np.inner(weights, dailyReturns.T)+1)*initialPortfolio

"""
    def calc_cumulative_return(self):
        """
        Calculates the cumulative return of a stock over time using a Monte Carlo simulation (Brownian motion with drift).

        """
        
        # Get closing prices of each stock
        last_prices = self.stockData.xs('close',level=1,axis=1)[-1:].values.tolist()[0]
        
        # Calculate the mean and standard deviation of daily returns for each stock
        daily_returns = self.stockData.xs('daily_return',level=1,axis=1)
        mean_returns = daily_returns.mean().tolist()
        std_returns = daily_returns.std().tolist()
        
        # Initialize empty Dataframe to hold simulated prices
        portfolio_cumulative_returns = pd.DataFrame()
        
        # Run the simulation of projecting stock prices 'nSim' number of times
        for n in range(self.nSim):
        
            if n % 10 == 0:
                print(f"Running Monte Carlo simulation number {n}.")
        
            # Create a list of lists to contain the simulated values for each stock
            simvals = [[p] for p in last_prices]
    
            # For each stock in our data:
            for s in range(len(last_prices)):

                # Simulate the returns for each trading day
                for i in range(self.nTrading):
        
                    # Calculate the simulated price using the last price within the list
                    simvals[s].append(simvals[s][-1] * (1 + np.random.normal(mean_returns[s], std_returns[s])))
    
            # Calculate the daily returns of simulated prices
            sim_df = pd.DataFrame(simvals).T.pct_change()
    
            # Use the `dot` function with the weights to multiply weights with each column's simulated daily returns
            sim_df = sim_df.dot(self.weights)
    
            # Calculate the normalized, cumulative return series
            portfolio_cumulative_returns[n] = (1 + sim_df.fillna(0)).cumprod()
        
        # Set attribute to use in plotting
        self.simulated_return = portfolio_cumulative_returns
        
        # Calculate 95% confidence intervals for final cumulative returns
        self.confidence_interval = portfolio_cumulative_returns.iloc[-1, :].quantile(q=[0.025, 0.975])
        
        return portfolio_cumulative_returns

    def plot_simulation(self):
        """
        Visualizes the simulated stock trajectories using calc_cumulative_return method.

        """ 
        
        # Check to make sure that simulation has run previously. 
        if not isinstance(self.simulated_return,pd.DataFrame):
            self.calc_cumulative_return()
            
        # Use Pandas plot function to plot the return data
        plot_title = f"{self.nSim} Simulations of Cumulative Portfolio Return Trajectories Over the Next {self.nTrading} Trading Days."
        return self.simulated_return.plot(legend=None,title=plot_title)

""" #MCS graph
plt.plot(portfolio_sims)
plt.ylabel('Portfolio Value ($)')
plt.xlabel('Days')
plt.title('Monte Carlo Simulation of Personal Stock Portfolio')
plt.show()

  # An empty dictionary that will hold the daily pct change for each stock from the sector.
    symbol_pct_changes = {}

    # Calculate the daily percent change for each symbol in the sector.
    # Create a loop that selects each symbol in the symbols list.
    # Using the `sector_prices_df` DataFrame returned from the Alpaca API call,
    # call the `pct_change` function on the DataFrame's "close" column.
    for symbol in symbols:
        symbol_pct_changes[symbol] = stock_data['close'].pct_change()

    # Create a dataframe from the dictionary of daily pct changes.
    sector_pct_changes = pd.DataFrame.from_dict(symbol_pct_changes)

    # Calculate the average daily pct change for each day of the five stocks.
    sector_pct_changes['sector_pct_change'] = sector_pct_changes.mean(axis=1)

    # Sum the daily percent changes for the sector over the past year to find the sector yearly return.
    sector_yearly_rtn = sector_pct_changes['sector_pct_change'].sum()

    # Create a statement that displays the `results` of your sector_yearly_return calculation.
    # On a separate line (\n) ask the use if they would like to continue running the report.
    results = f"The cumulative return for the {sector} sector for the past year is {sector_yearly_rtn * 100}%.\nWould you like to choose another sector to analyze?"

    # Using the `results` statement created above,
    # prompt the user to run the report again (`y`) or exit the program (`n`).
    continue_running = questionary.select(results, choices=['y', 'n']).ask()

    # Return the `continue_running` variable from the `sector_report` function
    return continue_running
"""



# The `__main__` loop of the application.
# It is the entry point for the program.
if __name__ == "__main__":

    # Database connection string to the clean NYSE database
    database_connection_string = 'sqlite:///../Resources/nyse.db'

    # Create an engine to interact with the database
    engine = sql.create_engine(database_connection_string)

    # Read the NYSE table into a dataframe called `nyse_df`
    nyse_df = pd.read_sql_table('NYSE', engine)

    # Get a list of the sector names from the `nyse_df` DataFrame
    # Be sure to drop n/a values and capture only unique values.
    # You will use this list of `sector` names for the user options in the report.
    sectors = nyse_df['Sector']
    sectors = sectors.dropna()
    sectors = sectors.unique()

    # Create a variable named running and set it to True
    running = True

    # While running is `True` call the `sector_report` function.
    # Pass the `nyse_df` DataFrame `sectors` and the database `engine` as parameters.
    while running:
        continue_running = sector_report(sectors, engine)
        if continue_running == 'y':
            running = True
        else:
            running = False