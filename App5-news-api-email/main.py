import requests


api_key = "df8f6e675f67487fbe78f62e673e47ed"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-12-15&sortBy=publishedAt&apiKey=df8f6e675f67487fbe78f62e673e47ed"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()


print(content["articles"])

body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + "none" if article["description"] is None else article["description"] + 2*"\n"
        print(body)