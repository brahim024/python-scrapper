from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("https://github.com/brahim024?tab=repositories")
bsObj=BeautifulSoup(html)
nameList=bsObj.findAll('h3',{'class':'wb-break-all'})
for name in nameList:
    print(name.get_text())