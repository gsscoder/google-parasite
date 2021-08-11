import urllib.parse
from requests_html import HTMLSession

def query(subject):
    session = HTMLSession()
    request = session.get(f'https://www.google.com/search?q={urllib.parse.quote(subject)}')
    return request.html

def do_math(expression):
    html = query(expression)
    return float(html.find('#cwos')[0].text)