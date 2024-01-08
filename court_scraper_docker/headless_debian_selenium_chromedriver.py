# import external libraries.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

# set xvfb display since there is no GUI in docker container.
display = Display(visible=0, size=(800, 600))
display.start()

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=360,640")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36")


browser = webdriver.Chrome(options=chrome_options)

 
#browser.get('http://www.example.com')
browser.get("https://ubc.perfectmind.com/24063/Clients/BookMe4LandingPages/Facility?facilityId=c0668c1c-1fd6-4432-a20e-4c50aaad5baa&widgetId=c7c36ee3-2494-4de2-b2cb-d50a86487656&calendarId=e65c1527-c4f8-4316-b6d6-3b174041f00e&arrivalDate=2023-12-30T06:12:52.061Z&landingPageBackUrl=https://ubc.perfectmind.com/24063/Clients/BookMe4FacilityList/List?calendarId=e65c1527-c4f8-4316-b6d6-3b174041f00e&widgetId=c7c36ee3-2494-4de2-b2cb-d50a86487656&embed=False&singleCalendarWidget=true://ubc.perfectmind.com/24063/Clients/BookMe4FacilityList/List?widgetId=c7c36ee3-2494-4de2-b2cb-d50a86487656&calendarId=e65c1527-c4f8-4316-b6d6-3b174041f00e")

# Wait for JS loading 
browser.implicitly_wait(10)

html = browser.page_source
print(html)

# close chromedriver and display
browser.quit()
display.stop()
