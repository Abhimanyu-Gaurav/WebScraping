import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/city/delhi"

r = requests.get(url)

print(r.status_code)
print(r.text)
print(r.url)
print(r.status_code)

soup = BeautifulSoup(r.text , "html.parser")
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.a)
print(soup.h1)