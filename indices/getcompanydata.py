from bs4 import BeautifulSoup
import requests
company='ASC'
def companydata(company):
 url = f'https://dps.psx.com.pk/company/{company}'

# Send a GET request to the website and get the HTML content
 response = requests.get(url)


 soup = BeautifulSoup(response.content, 'html.parser')
 QuotePrice = soup.select_one('.quote__close').get_text(strip=True)

 Openlabel = soup.find('div', class_='stats_label', text='Open')
 OpenValue = Openlabel.find_next_sibling('div', class_='stats_value').get_text(strip=True)

 highlabel = soup.find('div', class_='stats_label', text='High')
 highValue = highlabel.find_next_sibling('div', class_='stats_value').get_text(strip=True)

 lowlabel = soup.find('div', class_='stats_label', text='Low')
 lowValue = lowlabel.find_next_sibling('div', class_='stats_value').get_text(strip=True)

 Volumelabel = soup.find('div', class_='stats_label', text='Volume')
 VolumeValue = Volumelabel.find_next_sibling('div', class_='stats_value').get_text(strip=True)

 return VolumeValue

def getcompanyprofile(company):
 url = f'https://dps.psx.com.pk/company/{company}'

 # Send a GET request to the website and get the HTML content
 response = requests.get(url)

 soup = BeautifulSoup(response.content, 'html.parser')
 QuotePrice = soup.select_one('.quote__close').get_text(strip=True)
 description_div = soup.find('div', class_='profile__item--decription')

 # Extract the description textasambjhbjh
 description = description_div.find('p').get_text(strip=True)

 # Print the extracted descripion of data
 return description


#get equity valeus
def equityprofile(company):
 url = f'https://dps.psx.com.pk/company/{company}'

 # Send a GET request to the website and get the HTML content
 response = requests.get(url)

 soup = BeautifulSoup(response.content, 'html.parser')
 shares = soup.find('div', class_='stats_label', text='Shares')
 sharesValue = shares.find_next_sibling('div', class_='stats_value').get_text(strip=True)

 freefloat = soup.find('div', class_='stats_label', text='Free Float')
 freefloatValue = freefloat.find_next_sibling('div', class_='stats_value').get_text(strip=True)

 return freefloatValue
print(equityprofile(company))