import Get_Stock_Datas as gsd
import yfinance as yf

i = 0 
for i in gsd.data:
    x = yf.Ticker(gsd.stock)
    