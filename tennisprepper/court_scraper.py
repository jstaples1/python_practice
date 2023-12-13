from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

import functions

# Create ChromeOptions object
chrome_options = Options()

# Emulate a mobile device
chrome_options.add_argument("--window-size=360,640")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36")

# Initialize WebDriver with Chrome and the configured options
browser = webdriver.Chrome(options=chrome_options)


browser.get(functions.getCourtURL('1','date')) 

# Wait for JS loading 
browser.implicitly_wait(10)

html = browser.page_source
browser.quit()

soup = BeautifulSoup(html, 'html.parser')



#functions.getCourtName(soup)
#functions.getDaysOfWeek(soup)

functions.getTimes(soup,"09:00 AM-10:00 AM")
functions.getTimes(soup,"10:00 AM-11:00 AM")
functions.getTimes(soup,"11:00 AM-12:00 PM")
functions.getTimes(soup,"12:00 PM-01:00 PM")
functions.getTimes(soup,"01:00 PM-02:00 PM")
# functions.getTimes(soup,"09:00 AM-10:00 AM")
# functions.getTimes(soup,"09:00 AM-10:00 AM")
# functions.getTimes(soup,"09:00 AM-10:00 AM")
# functions.getTimes(soup,"09:00 AM-10:00 AM")
# functions.getTimes(soup,"09:00 AM-10:00 AM")
# functions.getTimes(soup,"09:00 AM-10:00 AM")
#functions.getTimes(soup,"09:00 AM-10:00 AM")









