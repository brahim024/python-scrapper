from urllib.request import urlopen
html=urlopen('https://github.com/brahim024/python-scrapper')
print(html.read())