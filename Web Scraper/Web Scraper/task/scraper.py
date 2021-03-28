import requests
from bs4 import BeautifulSoup
import string
import os


def get_input():
    pages = {
        'number_of_pages': int(input()),
        'type': input()
    }

    return pages


def get_soup(url_):
    parser = 'html.parser'
    req = requests.get(url_, headers={'Accept-Language': 'en-US,en;q=0.5'})

    if req:
        return BeautifulSoup(req.text, parser)
    else:
        print(f'error_code: {req.status_code}')
        exit()


def transform_to_file_name(name_):
    return name_.translate(str.maketrans(' ', '_', string.punctuation)) + '.txt'


def get_articles(soup_):
    return soup_.find_all('article')


def get_article_type(soup_, article_type_):
    return soup_.find('span', class_='c-meta__type').text.strip() == article_type_


def article_title(soup_):
    return soup_.find('a').text.strip()


def get_link(soup_):
    return 'https://www.nature.com' + soup_.find('a')['href']


def get_article(soup_):
    try:
        return soup_.find('div', class_='article__body').text.strip()
    except AttributeError:
        try:
            return soup_.find('div', class_='article-item__body').text.strip()
        except AttributeError:
            try:
                return soup_.find('div', class_='c-article-section__content').text.strip()
            except AttributeError:
                return None


def make_directory(root_, page_n):
    make_dir = root_ + '\\Page_' + page_n

    if not os.access(make_dir, os.F_OK):
        os.mkdir(make_dir)
        os.chdir(make_dir)
        print(f'make dir: {make_dir}')
    else:
        os.chdir(make_dir)


def write_file(root_, file_name, content):
    with open(file_name, 'wb') as file:
        file.write(content.encode())

    print('saving')


base_url = 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page='
user_input = get_input()
number_of_pages = user_input['number_of_pages']
type_of_articles = user_input["type"]
root = os.getcwd()

for i in range(1, number_of_pages + 1):
    url = base_url + str(i)
    soup = get_soup(url)
    articles = get_articles(soup)
    make_directory(root, str(i))
    for article in articles:
        if get_article_type(article, type_of_articles):
            name = transform_to_file_name(article_title(article))
            link = get_link(article)
            article_soup = get_soup(link)
            if get_article(article_soup) is not None:
                write_file(root, name, get_article(article_soup))

os.chdir(root)
print('Saved all articles.')
