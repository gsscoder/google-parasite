import urllib.parse
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def query(text):
    session = HTMLSession()
    request = session.get(f'https://www.google.com/search?q={urllib.parse.quote(text)}')
    request.html.render(timeout=5)
    return BeautifulSoup(request.html.raw_html, 'html.parser')

def do_math(expression):
    soup = query(expression)
    return float(soup.find_all('span', id='cwos')[0].text)

def get_summary(subject):
    items = []
    soup = query(subject)
    for li in soup.find_all('ol')[1]:
       items.append(li.text.strip())
    return items