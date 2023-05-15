import requests
import json

API_key = "fe063f3b2ead4a3bafaeb533e96dece7"
query = input("What type of news are you interested in? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2023-04-15&sortBy=publishedAt&apiKey={API_key}"
r = requests.get(url)
news = json.loads(r.text)
# print(news)
for article in news['articles']:
    print(article['title'])
    print(article['description'])
    print("================================")
