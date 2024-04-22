
import yfinance as yf
import random as rd
import numpy as np
from scipy.stats import gmean



list = []

number = int(input("How many stock do you want to compare ? \n "  ))

i = 0
ticker_list=[]
while int(i) < number:
    stock = input ("Please enter stock ticker \n ")
    ticker_list.append(stock)
    i = i + 1
    
data = yf.download(ticker_list, '2000-1-1')['Adj Close']


correlation = data.dropna().corr()
coveriance = data.dropna().cov() 

#Get the daily return & Geo mean 
Daily_return = (data.pct_change(1)) + 1 
Geo_mean_portfolio = gmean(Daily_return.dropna())-1



# Below, it will generate random weights
weights = []
for stock in ticker_list:
    weights.append(rd.random())

weights = weights/np.sum(weights)

Initial_investment = int(input("How much do you want to invest ?"))
investment = Daily_return * weights * Initial_investment

