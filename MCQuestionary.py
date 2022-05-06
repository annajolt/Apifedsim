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



# function to run the Monte Carlo Simulationn
def stock_data():
    
    #Using questionary, give the user a list of cryptos to run the report on.
    stock = questionary.select("Which Crypto do you want to analyze?",
                               choices=stockList).ask()
        #print("Running report ...")

    #avaiable stocks to work with
    stockList = ['BTC-USD','ETH-USD','LUNA1-USD','BNB-USD','ADA-USD']
    stocks = [stock for stock in stockList]

    endDate = dt.datetime.now()

    startDate = endDate - dt.timedelta(days=365)

    meanReturns, covMatrix = get_data(stocks, startDate, endDate)

    # Set weights if empty, otherwise make sure sum of weights equals one.
    if weights == "":
        weight = questionary.text("What is the weight of the stock?").ask()
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

    #Cholesky Decomposition (used to determine Lower Triangular Matrix)
    # Z are the samples from a normal distribution
    for m in range(0, mc_sims):
        #mc loops
        Z = np.random.normal(size=(T, len(weights)))
        L = np.linalg.cholesky(covMatrix)
        #Assuming daily returns are distributed by a Multivariate Normal Distribution 
        dailyReturns = meanM + np.inner(L, Z)
        portfolio_sims[:,m] = np.cumprod(np.inner(weights, dailyReturns.T)+1)*initialPortfolio
   
"""

    # plot the simulation (line plot)
    def plot_simulation(self):
    
        # Visualizes the simulated stock trajectories using calc_cumulative_return method.
 
        
        # Check to make sure that simulation has run previously. 
        if not isinstance(self.simulated_return,pd.DataFrame):
            self.calc_cumulative_return()
            
        # Use Pandas plot function to plot the return data
        plot_title = f"{self.nSim} Simulations of Cumulative Portfolio Return Trajectories Over the Next {self.nTrading} Trading Days."
        return self.simulated_return.plot(legend=None,title=plot_title)
    
    # plot the simuluation (distribution/bar graph)
    def plot_distribution(self):
    
       # Visualizes the distribution of cumulative returns simulated using calc_cumulative_return method.

    
        
        # Check to make sure that simulation has run previously. 
        if not isinstance(self.simulated_return,pd.DataFrame):
            self.calc_cumulative_return()
        
        # Use the `plot` function to create a probability distribution histogram of simulated ending prices
        # with markings for a 95% confidence interval
        plot_title = f"Distribution of Final Cumuluative Returns Across All {self.nSim} Simulations"
        plt = self.simulated_return.iloc[-1, :].plot(kind='hist', bins=10,density=True,title=plot_title)
        plt.axvline(self.confidence_interval.iloc[0], color='r')
        plt.axvline(self.confidence_interval.iloc[1], color='r')
        return plt 
        """
#MCS graph
plt.plot(portfolio_sims)
plt.ylabel('Portfolio Value ($)')
plt.xlabel('Days')
plt.title('Monte Carlo Simulation of Personal Stock Portfolio')
plt.show()


# An empty dictionary that will hold the daily pct change for each stock.
stock_pct_changes = {}

    # Calculate the daily percent change for each symbol in the sector.
    # Create a loop that selects each symbol in the symbols list.
    # Using the `sector_prices_df` DataFrame returned from the Alpaca API call,
    # call the `pct_change` function on the DataFrame's "close" column.
for stock in stocks:
    stock_pct_changes[stock] = stockData['Close'].pct_change()

    # Create a dataframe from the dictionary of daily pct changes.
    stock_pct_changes = pd.DataFrame.from_dict(stock_pct_changes)

    # Calculate the average daily pct change for each day of the five stocks.
    stock_pct_changes['sector_pct_change'] = sector_pct_changes.mean(axis=1)

    # Sum the daily percent changes for the sector over the past year to find the sector yearly return.
    sector_yearly_rtn = sector_pct_changes['sector_pct_change'].sum()

    # Create a statement that displays the `results` of your sector_yearly_return calculation.
    # On a separate line (\n) ask the use if they would like to continue running the report.
    results = f"The cumulative return for the {sector} sector for the past year is {sector_yearly_rtn * 100}%.\nWould you like to choose another sector to analyze?"

    # Using the `results` statement created above,
    # prompt the user to run the report again (`y`) or exit the program (`n`).
    continue_running = questionary.select(results, choices=['y', 'n']).ask()

    # Return the `continue_running` variable from the `sector_report` function
    # return continue_running




    # The `__main__` loop of the application.
# It is the entry point for the program.
if __name__ == "__main__":

    # connection to the clean data
    

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