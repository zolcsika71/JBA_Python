import requests

from bs4 import BeautifulSoup

link_index = int(input()) - 1
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a')
print(f'{links[link_index].get("href")}')
