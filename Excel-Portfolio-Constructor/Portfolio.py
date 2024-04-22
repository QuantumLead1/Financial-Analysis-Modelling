import yfinance as yf
import xlwings as xw
import datetime as date
import pandas as pd
import Get_Stock_Datas as gsd 
import Formulas
import Financial_Statements 


from dateutil.relativedelta import relativedelta

# Open Excel File and name the first page 
Book = xw.Book(0)
Pg1 = Book.sheets.active
Pg1.name = "Daily Stock Prices"


Pg1.range("A1").value = gsd.data
Pg1.autofit()

# In correlation table page, print a correlation table 
Book.sheets.add("Correlation Table")
P2 = Book.sheets.active
P2.range("A1").value = gsd.correlation

#Cor and Cov, deletes the na values, the correlation and covs will not show 100% data

gsd.coveriance

Book.sheets.add("Portfolio")
P3 = Book.sheets.active
P3.range("A1").value = "Stock Tickers"
P3.range("B1").value = gsd.ticker_list
P3.range("A2").value = "Stock Weights"
P3.range("B2").value =gsd.weights



P3.autofit()


P4 = Book.sheets.add("Competitor Analysis") 

# Get Net income Margin
P4.range("B1").value = "Net Income Margin"

a = 0
for i in gsd.ticker_list:
    P4.range("A2").offset(a,0).value = i
    P4.range("B2").offset(a,0).value = Formulas.get_Net_Income_margin(i)
    a = a + 1 

# Get Gross Margin
P4.range("C1").value = "Gross Profit Margin"
a = 0
for i in gsd.ticker_list:
    P4.range("B2").offset(a,1).value = Formulas.get_Gross_Profit_margin(i)
    a = a + 1 

#Get ROA 

P4.range("D1").value = "Return on Assets"
a = 0
for i in gsd.ticker_list:
    P4.range("B2").offset(a,2).value = Formulas.get_ROA(i)
    a = a + 1 

#Get ROE

P4.range("E1").value = "Return on Equity"
a = 0
for i in gsd.ticker_list:
    P4.range("B2").offset(a,3).value = Formulas.get_ROE(i)
    a = a + 1 

#Get Cash Flow margin
P4.range("F1").value = "Cash Flow Margin"
a = 0
for i in gsd.ticker_list:
    P4.range("B2").offset(a,4).value = Formulas.get_CFmargin(i)
    a = a + 1 

P4.autofit()
