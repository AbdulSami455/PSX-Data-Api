import requests
from bs4 import BeautifulSoup

url = 'https://dps.psx.com.pk/announcements/psx'

response = requests.get(url)

# Create a BeautifulSoup object by passing the HTML content and specify the parser
soup = BeautifulSoup(response.content, 'html.parser')

def notice():
 h2_tags = soup.find_all('h2')
 for h2 in h2_tags:
    print(h2.get_text())

