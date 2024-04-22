import yfinance as yf
import xlwings as xl
import pandas as pd 

wb = xl.Book()
ws = wb.sheets.active


name = input("What stock?")

ticker = yf.Ticker(name)


             
IS = wb.sheets[0]
IS.name = "Income Statement"
IS.range("A1").value =  ticker.income_stmt
IS.autofit()


BS = wb.sheets.add("Balance_Sheet")

BS.range("A1").value = ticker.balance_sheet
BS.autofit()

CF = wb.sheets.add("Cash Flow")
CF.range("A1").value = ticker.cash_flow
CF.autofit()
