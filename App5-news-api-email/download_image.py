
import requests


url = "https://savetibet.org/wp-content/uploads/2019/06/uyghur-flag-1200-768x403.jpg"
response = requests.get(url)

with open("Uyghur-flag.jpg","wb") as file:
    file.write(response.content)