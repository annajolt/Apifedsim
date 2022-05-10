#!/usr/bin/env python
# coding: utf-8

# In[1]:


import questionary


# In[6]:


# Select prompt for 'T' or time
time_response = questionary.select(
    "How long would you like to run your simulation for?",
    choices=[
        "10 days",
        "50 days",
        "100 days",
        "200 days",
        "500 days"
    ]).ask()

# Assign to 'T = 100 ' replace 100 with time_response


# In[ ]:


# Select prompt for sims
sim_response = questionary.select(
    "How many simulations would you like to run per-day?",
    choices=[
        "50 simulations",
        "100 simulations",
        "200 simulations",
        "350 simulations",
        "500 simulations"
    ]).ask()

# Assing to 'mc_sims = 100' replace 100 with sim_response


# In[ ]:


#Monte Carlo Method

#number of simulations
mc_sims = sim_response
T = time_response #timeframe in days


# In[ ]:




