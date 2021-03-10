import requests


def get_content_type(url):
    r = requests.get(url)
    return r.headers['content-type']
