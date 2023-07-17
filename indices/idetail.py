from bs4 import BeautifulSoup
import requests

url = 'https://www.psx.com.pk/market-summary/'

# Send a GET request to the website and get the HTML content
response = requests.get(url)

# Create a BeautifulSoup object by passing the HTML content and specify the parser
soup = BeautifulSoup(response.content, 'html.parser')


#getvalueofanyindex
def getindices(indexname):
 h3_element = soup.find('h3', text=indexname)
 h4_element = h3_element.find_next_sibling('h4')
 h4_text = h4_element.get_text().strip()
 return h4_text
#print(getindices('KSE100'))
#valuesofcompanies
def listofcompanieswithprofit():

 green_text_trs = soup.find_all('tr', class_='green-text-td')
 for tr in green_text_trs:
    list=[]
    td1 = tr.find('td')
    text = td1.get_text(strip=True)
    list.append(text)

 return list

#list of all indices

def listofindices():

    list=['KSE100','ALLSHR','KSE30','KMI30','BKTI','OGTI','KMIALLSHR','PSXDIV20','UPP9','NITPGI','ACI','JSMFI']
    return list
print(listofindices())

