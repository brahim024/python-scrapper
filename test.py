import requests
from bs4 import BeautifulSoup
from csv import writer
response=requests.get('https://deals.souq.com/eg-en/cameras-and-accessories/t/9191?q=eyJzIjoic3IiLCJmIjpbXX0%3D&ref=nav')
soup=BeautifulSoup(response.text,'html.parser')
products=soup.findAll(class_='columns small-8 medium-12')
with open('product.cvs','w') as csv_file:
	csv_writer=writer(csv_file)
	headers=['Product','Price']
	csv_writer.writerow(headers)
	for product in products:
		title=product.find(class_='itemTitle').get_text().replace('\n','')
		price=product.find(class_='is block sk-clr1')
		print('Product',product.text)
		print('Price:',price.text)

		csv_writer.writerow([title,price.text])
	