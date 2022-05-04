# Apifedsim

Possible User stories:
1)	As a portfolio manager I need to see the trend of a cryptocurrency to determine if it will be beneficial to add to an individual’s portfolio
Acceptance Criteria: Given that I need to know the trend when a certain cryptocurrency is selected then a simulation needs to be produced.
2)	As a crypto trader I need a visualization of volatility of cryptocurrencies to determine the best & worse possible returns of that cryptocurrency
Acceptance Criteria:  Given that I need to know the volatility when choosing a cryptocurrency to determine best & worse possible returns then I need to have a simulation producing the returns
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
