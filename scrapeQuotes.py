from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


urls = ["http://quotes.toscrape.com","http://quotes.toscrape.com/page/2/","http://quotes.toscrape.com/page/3/"]

quotes = []
with open('quotes.txt','w') as f:
	for my_url in urls:
		#open web client
		uClient = uReq(my_url)

		#read the html page
		html = uClient.read()

		#close the client
		uClient.close()

		#use the bs4 to parse the html page
		page_soup = soup(html,"html.parser")

		#traverse the hmtl

		#example
		#print(page_soup.h1)

		container = page_soup.findAll('div',{'class':'quote'})
		
		
		for i in range(len(container)):
			#text is stored in the span tag
			span = container[i].find('span',{'class':'text'})
			#remove the noise in the text.
			sentence = span.text[1:len(span.text)-1]
			#print(sentence)
			#write text to the text file
			f.write(sentence + '\n')
f.close()




