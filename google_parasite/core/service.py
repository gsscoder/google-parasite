import urllib.parse
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def query(subject):
    session = HTMLSession()
    request = session.get(f'https://www.google.com/search?q={urllib.parse.quote(subject)}')
    request.html.render(timeout=2)
    return BeautifulSoup(request.html.raw_html, 'html.parser')

def do_math(expression):
    soup = query(expression)
    return float(soup.find_all('span', id='cwos')[0].text)