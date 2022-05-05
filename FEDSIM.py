#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports

import numpy as np
import pandas as pd
import os
import yfinance as yf
import datetime as dt
import questionary


# In[ ]:


# prompts users to select token for simulation
questionary.select(
    "hello, what token would you like to look into?",
    choices=[
        'btc',
        'eth',
        'ada',
        'luna1',
        'bnb'
    ]).ask() 


# In[ ]:


# prompts simulation length
questionary.select(
    "how long would you like to run your forecast?"
    choices=[
        '1 year',
        '3 years',
        '5 years'
    ]).ask()


# Not sure how to integrate questionary into the actual application


# In[ ]:


# import token history from API Download here



limit_rows=1000


# In[ ]:


#We can also incorporate a weighting system to evaluate 2 coins at once; not sure how to format questionary to suit this


# In[ ]:


# MC simulations (1, 3, or 5 years based off user selection) 'prices_df' = API download dataframe
# link questionary ask results with selecting simulation length
MC_1 = MCSimulation(portfolio_data = prices_df['btc'], num_simulation = 500, num_trading_days = 252) # 1 year simualtion
MC_3 = MCSimulation(portfolio_data = prices_df['btc'], num_simulation = 500, num_trading_days = 252 * 3) # 3 year sim
MC_5 = MCSimulation(portfolio_data = prices_df['btc'], num_simulation = 500, num_trading_days = 252 * 5) # 5 year sim

# view input data
MC_1.potfolio_data.head()


# In[ ]:


# run sim
MC_1.calc_cumulative_return()


# In[ ]:


# print a line plot
sim_line_plot = MC_1.plot_simulation()


# In[ ]:


# print a probablility distribution
sim_dist_plot = MC_1.plot_distribution()


# In[ ]:


# print a summary of simulation statistic results
summary_stats = MC_1.summarize_cumulative_return()


# In[ ]:


# prompts users to either add a coin to the portfolio & re-run sim as a weighted sim
questionary.select(
    "Would you like to add a coin to your simulated portfolio?"
    choices=[
        'yes',
        'no'
    ]).ask()
    
    if 'yes':
        


# In[ ]:


# prompts user to select new coin (is there a way to remove the option aready selected?)
questionary.select(
    "What coin would you like to add to your portfolio?"
    choices=[
        'btc',
        'eth',
        'ada',
        'luna1',
        'bnb'
    ]).ask()


# In[ ]:


# prompts users to select a new timeframe
questionary.select(
    "How long would you like to run your new weighted simulation?"
    choices=[
        '1 year',
        '3 years',
        '5 years'
    ]).ask()


# In[ ]:


# runs new weighted sim legths
MC_weighted_1 = MCSimulation(portfolio_data = prices_df['btc', 'eth'], weights = [.60,.40], num_simulation = 500, num_trading_days = 252)
MC_weighted_3 = MCSimulation(portfolio_data = prices_df['btc', 'eth'], weights = [.60,.40], num_simulation = 500, num_trading_days = 252 * 3)
MC_weighted_5 = MCSimulation(portfolio_data = prices_df['btc', 'eth'], weights = [.60,.40], num_simulation = 500, num_trading_days = 252 * 5)

# view input data
MC_weighted_1.potfolio_data.head()


# In[ ]:


# run sim
MC_weighted_1.calc_cumulative_return()


# In[ ]:


# print a line plot
weighted_sim_line_plot = MC_1.plot_simulation()


# In[ ]:


# print a probablility distribution
weigthed_sim_dist_plot = MC_1.plot_distribution()


# In[ ]:


# print a summary of simulation statistic results
weighted_summary_stats = MC_1.summarize_cumulative_return()


# In[ ]:




