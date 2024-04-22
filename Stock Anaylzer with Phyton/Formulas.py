import yfinance as yf
import Get_Stock_Datas as gsd

Time = input("Quarterly(Q) or Yearly(Y) ?").upper()

a = 0

# Net Income Margin         
if Time == "Y":
    def get_Net_Income_margin(stock):
        # Get the income statement for the stock
        income_statement = yf.Ticker(stock).income_stmt

        # Get the net income
        net_income_margin = income_statement.loc["Net Income"].iloc[0]/ income_statement.loc['Total Revenue'].iloc[0]

        return net_income_margin 
elif Time == "Q":
    def get_Net_Income(stock):
        # Get the income statement for the stock
        income_statement = yf.Ticker(stock).quarterly_income_stmt

        # Get the net income
        net_income_margin = income_statement.loc["Net Income"].iloc[0]/ income_statement.loc['Total Revenue'].iloc[0]

        return net_income_margin
   
# Gross Profit Margin
if Time == "Y":
    def get_Gross_Profit_margin(stock):
        
        income_statement = yf.Ticker(stock).income_stmt

        
        Gross_profit_margin = income_statement.loc["Gross Profit"].iloc[0]/ income_statement.loc['Total Revenue'].iloc[0]

        return Gross_profit_margin
elif Time == "Q":
    def get_Net_Income(stock):
        # Get the income statement for the stock
        income_statement = yf.Ticker(stock).quarterly_income_stmt

        # Get the net income
        Gross_profit_margin = income_statement.loc["Gross Profit"].iloc[0]/ income_statement.loc['Total Revenue'].iloc[0]

        return Gross_profit_margin
   
# Get ROA 
if Time == "Y":
    def get_ROA(stock):
        
        income_statement = yf.Ticker(stock).income_stmt
        balance_statement = yf.Ticker(stock).balance_sheet

        
        ROA = income_statement.loc["Net Income"].iloc[0]/ balance_statement.loc['Total Assets'].iloc[0]

        return ROA
elif Time == "Q":
    def get_Net_Income(stock):
        
        income_statement = yf.Ticker(stock).quarterly_income_stmt
        balance_statement = yf.Ticker(stock).quarterly_balance_sheet

        
        ROA = income_statement.loc["Net Income"].iloc[0]/ balance_statement.loc['Total Assets'].iloc[0]

        return ROA

#Get ROE 
if Time == "Y":
    def get_ROE(stock):
        
        income_statement = yf.Ticker(stock).income_stmt
        balance_statement = yf.Ticker(stock).balance_sheet

        
        ROE = income_statement.loc["Net Income"].iloc[0]/ balance_statement.loc["Stockholders Equity"].iloc[0]

        return ROE
elif Time == "Q":
    def get_Net_Income(stock):
        
        income_statement = yf.Ticker(stock).quarterly_income_stmt
        balance_statement = yf.Ticker(stock).quarterly_balance_sheet

        
        ROE = income_statement.loc["Net Income"].iloc[0]/ balance_statement.loc['Stockholders Equity'].iloc[0]

        return ROE
# Cash Flow Margin
if Time == "Y":
    def get_CFmargin(stock):
        
        income_statement = yf.Ticker(stock).income_stmt
        Cash_Flow_Statement = yf.Ticker(stock).cash_flow

        
        Cash_Flow_Margin =  Cash_Flow_Statement.loc['Operating Cash Flow'].iloc[0]/ income_statement.loc["Total Revenue"].iloc[0]

        return Cash_Flow_Margin
elif Time == "Q":
    def get_Net_Income(stock):
        
        income_statement = yf.Ticker(stock).quarterly_income_stmt
        Cash_Flow_Statement = yf.Ticker(stock).quarterly_cash_flow
        
        Cash_Flow_Margin =  Cash_Flow_Statement.loc['Operating Cash Flow'].iloc[0]/ income_statement.loc["Total Revenue"].iloc[0]


        return Cash_Flow_Margin