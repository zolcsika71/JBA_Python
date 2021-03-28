import requests

from bs4 import BeautifulSoup


url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
heading = soup.find('h1')
print(heading.text)
