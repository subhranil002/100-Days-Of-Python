import requests
import json

query = input("What type of news are you interested in? ")

# Construct the URL with the query and API key
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-06-15&sortBy=publishedAt&apiKey=9b26984f12a94bbdbd2a1a73132ed3e5"

# Send a GET request to the News API
r = requests.get(url)

# Parse the response as JSON
news = json.loads(r.text)

# Iterate over the articles and print their titles and descriptions
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")