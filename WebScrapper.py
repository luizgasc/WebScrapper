from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


url = 'https://www.nfl.com/stats/team-stats'
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
    
    df = pd.DataFrame(l,columns=header)
    df = df.drop([0,1])
    df = df.set_index('Team')

    print(df)

    
 

    df["TD"]=df["TD"].astype(float)
    df.plot.bar(y="TD",rot=0)
    plt.show()
    





except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)
