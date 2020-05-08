from bs4 import BeautifulSoup
import requests

url = 'https://www.lemonde.fr/'
page = requests.get(url)

searched_word = 'virus'

soup = BeautifulSoup(page, 'html.parser')
results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)


print('Found the word "{0}" {1} times\n'.format(searched_word, len(results)))
