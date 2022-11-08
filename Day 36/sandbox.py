import os
import requests

apikey = os.environ["ALPHAVANTAGE_ACCESS_KEY"]

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={apikey}'
r = requests.get(url)
data = r.json()

print(data)
