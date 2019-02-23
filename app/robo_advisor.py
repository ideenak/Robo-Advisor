from dotenv import load_dotenv
import json
import os
import requests
import pandas as pnd 
from datetime import datetime
import datetime

load_dotenv() 

apikey = str(os.environ.get("ALPHAVANTAGE_API_KEY"))
#Shoutout to @Chenmi1997 for the help here on the "str(...)" part"
print("--------------------------------------------------- ")
print(" ")
print("WELCOME TO THE BLUECHIP STOCK PICKER ")
print(" ")
print("This application helps volatility traders choose stocks that have low volatility")
print("in order to assist in decisionmaking with regards to determining which equities") 
print("to write calls and puts for.")
print(" ")

print("Disclaimer: this is not professional investment advice")
print(" ")

print("--------------------------------------------------- ")

print(" ")


while True:
    ticker = input("Please enter the ticker of your stock of choice: ") 
    #Shoutout to @hiepnguyen for helping me realize a while loop is optimal for this
    
    if ticker.isdigit():
        print("Invalid entry: a stock ticker only uses characters - integers or symbols are not permitted")
    else:
        pull = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&apikey=" + apikey)
        
        if "Error" in pull.text:
            print("Error: stock either cannot be found or is not listed on Alpha Vantage - please enter another stock ticker")
        else:
            break  

j=pull.json()

time = datetime.datetime.now()
a = time.strftime("%Y")
b = time.strftime("%m")
c = time.strftime("%d")    
d = time.strftime("%I")
e = time.strftime("%M")
f = time.strftime("%p")

t,opn,h,l,close,vol = [],[],[],[],[],[]

for lx, value in j["Time Series (Daily)"].items():
    t.append(lx)
    
    opn.append(float(value["1. open"]))

    h.append(float(value["2. high"]))
    
    l.append(float(value["3. low"]))
    
    close.append(float(value["4. close"]))
    
    vol.append(float(value["5. volume"]))
#Shoutout to THE @Chenmi1997
print(" ")
print("--------------------------------------------------- ")
print(" ")
print("Stock Ticker: " + ticker)
print(" ")
print("Program Run On: " + a + "-" + b + "-" + c + " " + d + ":" + e + " " + f)
print(" ")
print("...")
print(" ")
print("Now saving the requested information")
print(" ")
print("...")
print(" ")
