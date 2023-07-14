import requests
from bs4 import BeautifulSoup

url = 'https://www.psx.com.pk/market-summary/'

response = requests.get(url)

# Create a BeautifulSoup object by passing the HTML content and specify the parser
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)

#Function to get Status of Stock Exchange
def status():
 text=soup.find('span',text='Status:')
 span_text = text.next_sibling.strip()
 return span_text


#get Number of Stocks
def trades():
    text = soup.find('span', text='Trades:')
    span_text = text.next_sibling.strip()
    return span_text


#function to get Volume of Stock Market
def volume():
  text = soup.find('span', text='Volume:')
  span_text=text.next_sibling.strip()
  return span_text


#get total Companies
def totalcompanies():
    text = soup.find('span', text='Total:')
    span_text = text.next_sibling.strip()
    return span_text


#total Companies in Profit
def companiesinprofit():
    text = soup.find('span', text='Advanced:')
    span_text = text.next_sibling.strip()
    return span_text


#companies in Loss
def companiesinloss():
    text = soup.find('span', text='Declined:')
    span_text = text.next_sibling.strip()
    return span_text

#
print(companiesinloss())