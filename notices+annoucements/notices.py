from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set path to chromedriver.exe
webdriver_path = 'path_to_chromedriver/chromedriver'  # Replace with your chromedriver path

# Create a new Chrome instance
driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

# Load the webpage
url = 'https://dps.psx.com.pk/announcements/psx'
driver.get(url)

# Wait for the page to fully render
driver.implicitly_wait(10)

# Get the page source after rendering
page_source = driver.page_source

# Create a BeautifulSoup object using the rendered page source
soup = BeautifulSoup(page_source, 'html.parser')

# Find all announcement rows
announcement_rows = soup.find_all('tr')

# Iterate over the rows and extract the announcement details
for row in announcement_rows:
    # Find the columns within the row
    columns = row.find_all('td')
    if len(columns) == 4:  # Ensure it's a valid announcement row
        # Extract the required information from the columns
        date = columns[0].text.strip()
        time = columns[1].text.strip()
        announcement = columns[2].text.strip()
        pdf_link = columns[3].find('a')['href']

        # Print or process the extracted information as needed
        print("Date:", date)
        print("Time:", time)
        print("Announcement:", announcement)
        print("PDF Link:", pdf_link)
        print("------")

# Quit the browser
driver.quit()
