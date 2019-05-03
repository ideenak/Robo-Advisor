from robo_advisor import to_usd, get_response
from dotenv import load_dotenv
import json
import os
import requests
import pandas as pnd 
from datetime import datetime


def test_to_usd():
    result = to_usd(10)
    result1 = to_usd(1000)
    result2 = to_usd(57.3333)
    result3 = to_usd(.011111111)
    assert result == "$ 10.00"
    assert result1 == "$ 1000.00"
    assert result2 == "$ 57.33"
    assert result3 == "$ 0.01"


def test_getresponse():
    ticker = "AAPL"
    apikey = str(os.environ.get("ALPHAVANTAGE_API_KEY"))
    #pull1 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&apikey=" + apikey)

    answer = get_response("AAPL", apikey)

    parsed_answer = json.loads(answer.text)
    result = list(parsed_answer)

    assert result == ['Meta Data', 'Time Series (Daily)']
