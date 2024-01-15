import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import time
from threading import Lock
import json
import psutil


#The functions in this file are used to scrape content from the UBC court booking website

def processRunning(processName):
    '''
    Checks if a process is running by name
    '''
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                print("processRunning found" + proc.name())
                
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def chromeBrowserRunning():
    '''
    Checks if a process is running by name
    '''
    for proc in psutil.process_iter():
        try:
            if "chrome_crashpad_handler" in proc.name().lower():
                continue

            if "chrome" in proc.name().lower():
                print("processRunning found: " + proc.name() + "---" + proc.status())

            if "chrome" in proc.name().lower() and proc.status() != "zombie":
                print("processRunning found: " + proc.name() + "---" + proc.status())
                
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def killXvfbDisplays():

    for p in psutil.process_iter():
        if "chrome" in str(p.name):
            print("chrome found")
            print(p.name)
            
            if "chrome_crashpad_handler" in str(p.name):
                continue
            else:
                print("chrome is still running")
                #p.terminate()
                print(p.name)

    if "Xvfb" in str(p.name):  
        print("Xfbd found")
        #print(p.name)
        p.terminate()

    #   if p.name == 'chrome':
#     print(p.pid)
#     print(p.info)
#     print(p.username)
#     print(p.cwd())
#     print(p.exe())
#     print(p.status())
#     print(p.nice())
#     print(p.cpu_percent())
#     print(p.memory_percent())
#     print(p.memory_info())
#     print(p.memory_info_ex())
#     print(p.create_time())
#     print(p.num_threads())
#     print(p.threads())
#     print(p.cpu_times())
#     print(p.cpu_affinity())
#     print(p.cpu_num())
#     print(p.io_counters())
#     print(p.ionice())
#     print(p.rlimit())
#     print(p.environ())
#     print(p.terminal())
#     print(p.is_running())
#     print(p.is_suspended())
#     print(p.is_stopped())
#     print(p.as_dict())
#     print(p.name)
#     print("Process is running")    


def getHTMLSoup(date,courtNumber,browser):

    courtURL = getCourtURL(date,courtNumber)
    
    browser.get(courtURL)
    
    #allow some time for client side javascript to make its changes to the page
    browser.implicitly_wait(2)

    soup = BeautifulSoup(browser.page_source,'html.parser')
    return soup

def getChromeDriver(xvfb):

    # if (processRunning("Xvfb")):
    #     print("Xvfb is running in getChromeDriver")
    # else:
    #     print("Xvfb is not running in getChromeDriver")

    # set xvfb display since there is no GUI in docker container.

    

    # Create ChromeOptions object
    chrome_options = Options()

    # run the browser headless without gui since it will execute on the server
    chrome_options.add_argument("--headless")

    # Emulate a mobile device so that the ubc court interface only displays 2 courts (today and tmrw)
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=360,640")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36")
 
    # Initialize WebDriver with Chrome and the configured options
    browser = webdriver.Chrome(options=chrome_options)

    return browser



def getCourtName(soup):
    match = soup.find(name='h1',class_='facility-name')
    return match.text

def getDaysOfWeek(soup):
    matches = soup.find_all(name='strong',class_='bm-booking-block-header-day')
    daysOfWeek = ""
    for m in matches: 
        if daysOfWeek == "":
            daysOfWeek = m.text[3:]
            continue
        daysOfWeek = daysOfWeek + " and " + (m.text[3:])

    return daysOfWeek  

     
def getTimes(soup,time):
    matches = soup.find_all(name='span',attrs={'title':time})  
    if len(matches) > 0:
        return str(len(matches)) + " courts available at " + time 
    #print("There are ",len(matches), " courts available at " , time)
    

def getDataUIDs(soup):
    matches = soup.find_all(name='div',attrs={'data-uid':True})
    for m in matches: 
        print(m['data-uid'],end="\n")   

def getCourtURL(date,courtNumber):

    facilities = {}
    facilities['1'] = 'c0668c1c-1fd6-4432-a20e-4c50aaad5baa'
    facilities['2'] = 'e2d99dda-cdc4-4af4-8df6-6c8061ffd56f'
    facilities['3'] = 'c117a102-0ba0-4aa8-b8cf-eb8a1480be55'
    facilities['4'] = '47f78e62-2ac0-4d39-8ffa-5d331f60e14e'
    facilities['5'] = 'e5432c07-c2a6-46d1-a5d7-25c58567046c'
    facilities['6'] = 'f7000b6c-0d93-472b-97af-e0f22915439f'
    facilities['7'] = '5dac0879-1fbb-4dfe-ac67-5dcaa925d2f5'
    facilities['8'] = 'ccbf3aa0-f263-44eb-b394-a603115f587a'
    facilities['10'] = 'd5894b7a-2b61-4345-a1a8-ea8a50c921ae'
    facilities['11'] = 'd3a55644-6681-42a7-b8f5-09d796d35c07'
    facilities['12'] = '00dc0e70-6536-4a5a-b60b-9f6b0d0ba050'
    facilities['13'] = '308fd9d5-0de2-442e-8bd7-3fa6b607d170'

    facilityId = facilities[courtNumber]
    
    date = date + 'T00:44:05.314Z'

    url='https://ubc.perfectmind.com/24063/Clients/BookMe4LandingPages/Facility?facilityId='+ facilityId+ '&widgetId=c7c36ee3-2494-4de2-b2cb-d50a86487656&calendarId=e65c1527-c4f8-4316-b6d6-3b174041f00e&arrivalDate='+ date +'&landingPageBackUrl=https://ubc.perfectmind.com/24063/Clients/BookMe4FacilityList/List?calendarId=e65c1527-c4f8-4316-b6d6-3b174041f00e&widgetId=c7c36ee3-2494-4de2-b2cb-d50a86487656&embed=False&singleCalendarWidget=true://ubc.perfectmind.com/24063/Clients/BookMe4FacilityList/List?widgetId=c7c36ee3-2494-4de2-b2cb-d50a86487656&calendarId=e65c1527-c4f8-4316-b6d6-3b174041f00e'
    
    return url   


def getCourtTimes():
    courtTimes = []
    courtTimes.append('08:00 AM-09:00 AM')
    courtTimes.append('09:00 AM-10:00 AM')
    courtTimes.append('10:00 AM-11:00 AM')
    courtTimes.append('11:00 AM-12:00 PM')
    courtTimes.append('12:00 PM-01:00 PM')
    courtTimes.append('01:00 PM-02:00 PM')
    courtTimes.append('02:00 PM-03:00 PM')
    courtTimes.append('03:00 PM-04:00 PM')
    courtTimes.append('04:00 PM-05:00 PM')
    courtTimes.append('05:00 PM-06:00 PM')
    courtTimes.append('06:00 PM-07:00 PM')
    courtTimes.append('07:00 PM-08:00 PM')
    courtTimes.append('08:00 PM-09:00 PM')
    courtTimes.append('09:00 PM-10:00 PM')
    courtTimes.append('10:00 PM-11:00 PM')

    return courtTimes

def getCompleteResponseBody(date,courtNumber,soup):

    #body = "<html><body>"
    #body = "The Courts available for " + getDaysOfWeek(soup) + "<br><br>"
    body = ""
    body = body + "<b>------" + getCourtName(soup) + "------</b><br>"

    
    for courtTime in getCourtTimes():   
        times = getTimes(soup,courtTime)
        if times != None:
            body = body + "<a href = '" + getCourtURL(date,courtNumber) + "' target='_blank'>"+ times +"</a><br><br>"

            #body = body + times + " -> <a href = '" + getCourtURL(date,courtNumber) + "' target='_blank'>Book Now</a><br><br>"
  
    #body = body + "</body></html>"
    return body    

   
def getResponseBodies(date):

    if date == None:
        return "Please submit a date in the format YYYY-MM-DD"
    
    if (chromeBrowserRunning()):
        return "Chromebot is busy scraping for another user (thinks chrome is running), please try in a minute or two"

    if (processRunning("Xvfb")):
        return "Chromebot is busy scraping for another user (thinks Xvfb is running), please try again in a minute or two"

    start = time.time()

    display = Display(visible=0, size=(800, 600))
    display.start()

    #create one chrome(driver) instance and use it to get all court urls
    browser = getChromeDriver(display)

    response = " "
    #for i in range(8):
    for i in range(8):    
        soup = getHTMLSoup(date,str(i+1),browser)
        response = response + getCompleteResponseBody(date,str(i+1),soup)
        
        print(getCourtName(soup))
        

    end = time.time()
    print("Time taken to execute getResponseBodies:", end - start)

    #close chrome(driver)
    browser.quit
    time.sleep(1)

    #should clean up any Xvfb display sessions created to use chrome
    display.stop()
    time.sleep(2)
    killXvfbDisplays()

    return response

    
def getResponseBody(date,courtNumber):
    #exit
    start = time.time()

    if date == None:
        return "Please enter a date in the format YYYY-MM-DD"
    soup = BeautifulSoup(getHTMLSourceUsingChromeWebdriver(date,courtNumber),'html.parser')
    
    #body = "<html><body>"
    body = "The Courts available for " + getDaysOfWeek(soup) + "<br>"

    #soup = BeautifulSoup(getHTMLSourceUsingChromeWebdriver(date,courtNumber),'html.parser')
    
    body = body + "------<b>" + getCourtName(soup) + "</b>------<br>"

    for courtTime in getCourtTimes():   
        times = getTimes(soup,courtTime)
        if times != None:
            body = body + times + " -> <a href = '" + getCourtURL(date,courtNumber) + "' target='_blank'>Book Now</a><br>"
  
    #body = body + "</body></html>"
            
    end = time.time()
    #print("Time taken to execute getResponseBody:", end - start)
        
    
    return body




def getHTMLSourceUsingChromeWebdriver(date, courtNumber):

    start = time.time()

    lock = Lock()

    lock.acquire()

    # set xvfb display since there is no GUI in docker container.
    display = Display(visible=0, size=(800, 600))
    display.start()
    

    # Create ChromeOptions object
    chrome_options = Options()

    # run the browser headless without gui since it will execute on the server
    chrome_options.add_argument("--headless")

    # Emulate a mobile device so that the ubc court interface only displays 2 courts (today and tmrw)
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=360,640")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36")
 
    # Initialize WebDriver with Chrome and the configured options
    browser = webdriver.Chrome(options=chrome_options)

    courtURL = getCourtURL(date,courtNumber)
    
    browser.get(courtURL)
    
    browser.implicitly_wait(2)

    html = browser.page_source

    #time.sleep(5)
    browser.quit()

    lock.release()

    soup = BeautifulSoup(html, 'html.parser')  

    end = time.time()
    #print("Time to execute getHTMLSourceUsingChromeWebdriver:", end - start)
     
    return soup.prettify()


###########UNUSED Method, keeping if need to switch back to REST call to browserless.io, browserless.io is not free...
def getHTMLSource(date, courtNumber):
    courtURL = getCourtURL(date,courtNumber)
    
    url = "https://chrome.browserless.io/content?token=7367bf98-e83f-4fd9-9234-1ec1eddfba68"
    
    #Note that the viewport is set to 360x640 for the browserless.io call to force the UBC website to return only 2 days of values in the ui (forces mobile display)
    data = {
            "url": courtURL,
            "viewport": {
                "width": 360,
                "height": 640
                }
            }
    response = requests.post(url, json=data)
    return response.text
