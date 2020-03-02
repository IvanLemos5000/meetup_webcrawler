from bs4 import BeautifulSoup
import requests

url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'

open_url = requests.get(url)
soup = BeautifulSoup(open_url.content, 'html.parser')

with open('html_test.txt','w') as test:
	test.write(soup.prettify())

print(soup.find('a'))
print(soup.title)
