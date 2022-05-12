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

As a crypto trader you need a visualization of volatility of a cryptocurrency based on your initial investment to determine the best & worse possible returns of the cryptocurrency you select.

### *Our Solution - Crypto Query Lite*



Steps: 
1. I will need an option to choose cryptocurrencies (established by using questionary through .ask() function; 
2. After cryptocurrency is chosen will need the app to know how far back we are reviewing the cryptocurrency (1 yr, 2 yr, 5 yr?); 
3. Singular tokens or multiple tokens at a time can be chosen
4. This data for the cryptocurrency will be retrieved by/from Yfinance; 
5. Might need an initial investment amount that is planned to be invested;
6. Run the data through the Monte Carlo simulation;
a. for the simulation will need to establish how far ahead we will be looking -, 1 yr, 5 yr.
7. Retrieve the mean, median, min & max returns from the monte carlo simulations;
8. Plot the returned data;
9. Print the 95% CI lower & 95% CI higher (the least & most that can be earned);
