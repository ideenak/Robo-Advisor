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

