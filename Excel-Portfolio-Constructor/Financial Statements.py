import Get_Stock_Datas as gsd
import yfinance as yf


for i in gsd.data:
    x = yf.Ticker(gsd.stock)
    

for stocks in gsd.ticker_list :
 a = yf.Ticker(stocks)