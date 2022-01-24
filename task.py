import pandas as pd
import requests
from bs4 import BeautifulSoup

import io


c=pd.read_csv("D:\Downloads\Input.xlsx - Sheet1.csv")
print(c.head())
url= c[c["URL"]]
for url in url:
    URL = url
    r = requests.get(URL)
    print(r.content)
