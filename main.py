import requests

url = "https://timesofindia.indiatimes.com/city/delhi"

r = requests.get(url)
print(r.text)