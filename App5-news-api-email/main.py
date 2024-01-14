import requests


api_key = "df8f6e675f67487fbe78f62e673e47ed"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-12-14&sortBy=publishedAt&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

print(content["articles"])

for article in content["articles"]:
    print(article["title"])