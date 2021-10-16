from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.nfl.com/stats/player-stats/'

response = urlopen(url)

html = response.read()
soup = BeautifulSoup(html, 'html.parser')

print(soup.find('table'))

