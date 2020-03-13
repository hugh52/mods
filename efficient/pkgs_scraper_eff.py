#!/home/william/anaconda3/bin/python


import requests
from bs4 import BeautifulSoup


url = 'https://docs.anaconda.com/anaconda/packages/py3.7_linux-64/'
req = requests.get(url)
print(req)

soup = BeautifulSoup(req.content, 'html.parser')

trs = soup.select('table tr')

trs = [list(trs) for trs in trs]

trs = [trs[i][j] for i in range(len(trs))
       if("conda" not in str(trs[i]).lower()
          and "name" not in str(trs[i]).lower())
       for j in range(len(trs[i])) if j == 1]

tr = [trs[i].text.strip() for i in range(len(trs))
      if not str(trs[i]).startswith('_')]

pth = '/home/william/Desktop/'

with open(pth + 'requirements.txt', 'w+') as file:
    [file.write(str(item).replace("'", "") + "\n") for item in tr]
