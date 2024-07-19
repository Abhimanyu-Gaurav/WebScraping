import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/city/delhi"

r = requests.get(url)

# print(r.status_code)
# print(r.text)
# print(r.url)
# print(r.status_code)

soup = BeautifulSoup(r.text , "html.parser")

# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.a)
# print(soup.h1)

# TAG
tag = soup.html
# print(tag)
# print(type(tag))

# tag = soup.p
# print(tag)
# tag = soup.h1
# print(tag)
# tag = soup.h2
# print(tag)

## Navigable string

# tag = soup.p.string
# print(tag)

# tag = soup.a.string
# print(tag)

# tag = soup.h1.string
# print(tag)

## BeautifulSoup
print(soup.body)
# print(soup.find("p"))
# print(soup.find_all("p"))
# print(soup.find_all("h1"))

