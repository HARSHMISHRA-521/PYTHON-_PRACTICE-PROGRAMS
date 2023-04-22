import requests
from bs4 import BeautifulSoup

# the below code is used to parse and scrap data from a website
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)


# the down code is to post a json form data

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": 'harsh',
    "body": 'bhai',
    "userId": 12,
  }
headers =  {
    'Content-type': 'application/json; charset=UTF-8',
  }
response = requests.post(url, headers=headers, json=data)

print(response.text)