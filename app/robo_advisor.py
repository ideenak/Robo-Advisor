from dotenv import load_dotenv
import json
import os
import requests
import pandas as pnd 
from datetime import datetime

load_dotenv() 

apikey = os.environ.get("ALPHAVANTAGE_API_KEY")

while True:
    ticker = input("Please enter the ticker of your stock of choice: ") 
    if ticker.isdigit:
        print("Invalid entry: a stock ticker only uses characters - integers or symbols are not permitted")
    else:
        pull = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&apikey" + apikey)
        
