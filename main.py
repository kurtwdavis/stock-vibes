import requests 
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
endpoint_url = 'https://newsapi.org/v2/top-headlines'

params = {'country':"us"}

response = requests.get(endpoint_url, params=params, headers={"Authorization": api_key})



if response.status_code == 200:
    articles = response.json()['articles']
    headlines = [article['title'] for article in articles]
    for headline in headlines:
        print(headline)
else:
    print('ERROR getting headlines.. (line 18)')