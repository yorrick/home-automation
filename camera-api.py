
import requests
from bs4 import BeautifulSoup


def extract_readable_string(html):
    soup = BeautifulSoup(html)
    return list(soup.body.descendants)[-1].strip()

r = requests.get('http://localhost:8080/0/detection/status')
print extract_readable_string(r.content)

r = requests.get('http://localhost:8080/0/detection/start')
print extract_readable_string(r.content)

r = requests.get('http://localhost:8080/0/detection/pause')
print extract_readable_string(r.content)

