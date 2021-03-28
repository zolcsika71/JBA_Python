import requests

from bs4 import BeautifulSoup

number_of_article = int(input())
url = input()

r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
soup = BeautifulSoup(r.content, 'html.parser')
headings = soup.find_all('h2')

print(headings[number_of_article].text)
