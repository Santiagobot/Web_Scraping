import requests
from lxml import html

res = requests.get('http://www.example.com/')
doc = html.fromstring(res.text)

tag = doc.cssselect('h1')[0].text_content()
print(tag.strip())
