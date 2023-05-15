import requests

# response = requests.get("https://www.google.com")
# print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": 'harry',
    "body": 'bhai',
    "userId": 1,
}
headers = {
    'Content-type': 'application/json; charset=UTF-8',
}
response = requests.post(url, headers=headers, json=data)
print(response.text)


url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)
