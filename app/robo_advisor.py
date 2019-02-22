from dotenv import load_dotenv
import json
import os
import requests
import pandas as pd 
from datetime import datetime

load_dotenv() 

apikey = os.environ.get("ALPHAVANTAGE_API_KEY")
