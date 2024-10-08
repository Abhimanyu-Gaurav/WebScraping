import requests # Here requets module used access HTML code of the website.
from bs4 import BeautifulSoup 

url = "https://timesofindia.indiatimes.com/city/delhi"

r = requests.get(url) # it is used to get url of website.

print(r.status_code)
print(r.text)
print(r.url)
 
soup = BeautifulSoup(r.text , "html.parser")

print(soup.prettify()) # To see data in beautifull manner along with tree.
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.a)
print(soup.h1)
        
        # Objects in BeautifulSoup
# 1 # TAG
tag = soup.html
print(tag)
print(type(tag))

tag = soup.p
print(tag)
tag = soup.h1
print(tag)
tag = soup.h2
print(tag)

# 2 # Navigable string

tag = soup.p.string
print(tag)

tag = soup.a.string
print(tag)

tag = soup.h1.string
print(tag)

# 3 # BeautifulSoup
print(soup.body)
print(soup.find("p"))   # This will help in finding 1st items i.e here Paragraph. 
print(soup.find_all("p"))  # This will help in finding all items of choice.
print(soup.find_all("h1"))

# 4 # Comments
com = soup.p.string
print(com)

com = soup.p.prettify
print(com)

# Finding elements
class_data = soup.find("div", class_="contentwrapper") # by class we fetch data.
print(class_data)
print(class_data.find_all('p')) # to find pargraph tag in particular class.

id_data = soup.find("div", id_="contentwrapper") # by id we fetch data.
print(id_data)
print(id_data.find_all('p')) # to find pargraph tag in particular id.

# Extracting Text from the tags in web page
lines = soup.find_all("p")
print(lines)

for l in lines:
    print(l.text) # to extract only text from paragraph

s = soup.find("div",class_ = "") # This is to extract data from class.
#or
s = soup.find("p",class_ = "") # This is to extract data from particular class.
print(s) 

# Extracting links in web page
links = soup.find_all("a")
print(links)

for i in links:
    print(i)     # To get data of all anchor tags .
    print(i.get("href")) # To get data of all links, which is kept in href attribute of anchor.

#  
img = soup.find_all("img")   # To extract image url of data.
print(img)      # To get all data of images

for i in img:
    print(i.get("src")) # To get url of image, which in  src attribute.
    print(i.get("alt")) # To get name of image.

    