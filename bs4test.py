from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('https://github.com/brahim024')
bs=BeautifulSoup(html.read())
print(bs.h1)