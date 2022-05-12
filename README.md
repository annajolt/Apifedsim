# *Crypto Query Lite - Crypto Analysis Tool* 
   <p align='center'> <img src='images/icons-390.jpg'></p>

---
### *Necessary Library imports*
- import pandas as pd
- import datetime as dt
- import numpy as np
- import matplotlib.pyplot as plt
- import yfinance as yfin
- from re import L
- from numpy.ma.core import shape
- from matplotlib import style
- from pandas_datareader import data as pdr
- import questionary

### *User Story*

As a crypto trader you need a visualization of volatility of a cryptocurrency based on your initial investment to determine the best and worse possible returns of the cryptocurrency you select.

### *Our Solution - Crypto Query Lite*

Our team created a cryptocurrency analyzing tool, *Crypto Query Lite*, which will allow the user to view the possible outcomes in regards to the cryptocurrency they invest in and the amount of the initial investment.

The user will be prompted to select the cryptocurrency they wish to analyze and view stats for. After the selection, they will continue on to the amount of simulations they want to produce, how far ahead they want the simulation to run and the initial amount they wish to invest in the selected cryptocurrency. *Crypto Query Lite* uses a Monte Carlo Simulation to produce the analysis of the crypto.

The user will be able to view the cryptocurrencies: 
- Minimum
- Maximum
- STD (Standard Deviation)
- Mean
- 25% Quantile
- 50% Quantile
- 75% Quantile
- 95% CI Lower
- 95% CI Upper

As well as a graph of the simulation, as sampled by the picture below:
<p align='center'> <img src='images/MC_simulation_graph.png'></p>


