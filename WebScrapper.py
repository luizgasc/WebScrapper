from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError
import pandas as pd

url = 'https://www.nfl.com/stats/team-stats/'
headers = {}
l = []
header = []


def decode_html(input):
    return " ".join(input.split()).replace('> <', '><')


try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    html = html.decode('utf-8')
    html = decode_html(html)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    table_rows = table.find_all('tr')
    table_headers = soup.findAll('th')
    for th in table_headers:
        tcolumn = th.text
        header.append(tcolumn)

    for tr in table_rows:
        td = tr.findAll('td')
        row = [tr.text for tr in td]
        l.append(row)
    df = pd.DataFrame(l)


    df.columns = header
    print(df)

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)
